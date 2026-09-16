from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "portfolio.json"
USER_AGENT = "diogoribeiro7-profile-integrity/1.0"
GITHUB_API_PREFIX = "https://api.github.com/"
OWNER = "DiogoRibeiro7"
PUBLIC_PAGES = (
    "README.md",
    "FEATURED.md",
    "PROJECTS.md",
    "METHODS.md",
    "RESEARCH.md",
    "OUTPUTS.md",
    "CASE_STUDIES.md",
    "TEACHING.md",
    "PYPI.md",
    "STATISTICS.md",
)
REPOSITORY_LINK_PATTERN = re.compile(
    rf"https://github\.com/{re.escape(OWNER)}/([A-Za-z0-9_.-]+)"
)


def request_headers(url: str) -> dict[str, str]:
    """Build request headers, authenticating GitHub API calls when possible."""
    headers = {"User-Agent": USER_AGENT}
    token = os.environ.get("GITHUB_TOKEN")

    if url.startswith(GITHUB_API_PREFIX):
        headers.update(
            {
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )
        if token:
            headers["Authorization"] = f"Bearer {token}"

    return headers


def get(url: str, attempts: int = 3) -> tuple[int, bytes]:
    """Fetch a public metadata endpoint with bounded retries."""
    request = urllib.request.Request(url, headers=request_headers(url))
    last_error: Exception | None = None

    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.status, response.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(1.5 * (attempt + 1))

    raise RuntimeError(f"request failed after {attempts} attempts: {url}: {last_error}")


def linked_repositories() -> dict[str, tuple[str, ...]]:
    """Return same-owner repositories linked from reviewer-facing Markdown pages."""
    pages_by_repo: dict[str, list[str]] = {}

    for relative_path in PUBLIC_PAGES:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for repo in REPOSITORY_LINK_PATTERN.findall(text):
            pages_by_repo.setdefault(repo, []).append(relative_path)

    return {
        repo: tuple(dict.fromkeys(pages))
        for repo, pages in sorted(pages_by_repo.items())
    }


def manifest_deep_links(manifest: dict) -> list[tuple[str, str, str, tuple[str, ...]]]:
    """Return unique repository ref/path links used by generated public pages."""
    labels_by_link: dict[tuple[str, str, str], list[str]] = {}

    for collection in ("outputs", "case_studies"):
        for item in manifest.get(collection, []):
            path = item.get("path")
            if not path:
                continue
            repo = item["repo"]
            ref = item.get("ref", "main")
            key = (repo, ref, path)
            label = f'{collection}:{item.get("title", repo)}'
            labels_by_link.setdefault(key, []).append(label)

    return [
        (repo, ref, path, tuple(labels))
        for (repo, ref, path), labels in labels_by_link.items()
    ]


def check_repository_public(repo: str, contexts: tuple[str, ...]) -> str | None:
    """Verify that a referenced repository exists and is publicly inspectable."""
    url = f"https://api.github.com/repos/{OWNER}/{repo}"
    context = ", ".join(contexts)

    try:
        status, payload = get(url)
    except Exception as exc:
        return f"GitHub repository unavailable: {repo} ({context}): {exc}"

    if status != 200:
        return f"GitHub repository unavailable ({status}): {repo} ({context})"

    metadata = json.loads(payload)
    if metadata.get("private"):
        return f"public profile exposes a private repository: {repo} ({context})"
    return None


def check_deep_link(
    repo: str,
    ref: str,
    path: str,
    labels: tuple[str, ...],
) -> str | None:
    """Verify that a manifest-backed GitHub ref/path resolves publicly."""
    encoded_path = quote(path, safe="/")
    encoded_ref = quote(ref, safe="")
    url = (
        f"https://api.github.com/repos/{OWNER}/{repo}/contents/"
        f"{encoded_path}?ref={encoded_ref}"
    )
    context = ", ".join(labels)

    try:
        status, _ = get(url)
    except Exception as exc:
        return (
            f"manifest deep link unavailable: {repo}@{ref}/{path} "
            f"({context}): {exc}"
        )

    if status != 200:
        return (
            f"manifest deep link unavailable ({status}): "
            f"{repo}@{ref}/{path} ({context})"
        )
    return None


def main() -> int:
    """Verify public repositories, packages, and manifest-backed deep links."""
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors: list[str] = []
    contexts_by_repo: dict[str, list[str]] = {}

    for project in manifest["projects"]:
        repo = project["repo"]
        contexts_by_repo.setdefault(repo, []).append("manifest:projects")
        if "featured" in project:
            errors.append(
                f"legacy featured field is not allowed in project metadata: {repo}; "
                "FEATURED.md is the sole Featured source of truth"
            )

        package = project.get("pypi")
        if package:
            pypi_url = f"https://pypi.org/pypi/{package}/json"
            try:
                status, payload = get(pypi_url)
                if status != 200:
                    errors.append(f"PyPI package unavailable ({status}): {package}")
                    continue
                metadata = json.loads(payload)
                canonical = metadata.get("info", {}).get("name")
                if not canonical:
                    errors.append(f"PyPI package has no canonical name: {package}")
            except Exception as exc:
                errors.append(str(exc))

    for repo, pages in linked_repositories().items():
        contexts_by_repo.setdefault(repo, []).extend(f"page:{page}" for page in pages)

    for repo, contexts in sorted(contexts_by_repo.items()):
        deduplicated = tuple(dict.fromkeys(contexts))
        error = check_repository_public(repo, deduplicated)
        if error:
            errors.append(error)

    for repo, ref, path, labels in manifest_deep_links(manifest):
        error = check_deep_link(repo, ref, path, labels)
        if error:
            errors.append(error)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        "All referenced repositories, manifest PyPI packages, and deep links "
        "resolve publicly."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
