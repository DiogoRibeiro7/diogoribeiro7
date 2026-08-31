"""Generate evidence-based flagship metrics for the profile Statistics page."""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final
from xml.sax.saxutils import escape

OWNER: Final[str] = "DiogoRibeiro7"
FEATURED_PATH: Final[Path] = Path("FEATURED.md")
MANIFEST_PATH: Final[Path] = Path("data/portfolio.json")
STATISTICS_PATH: Final[Path] = Path("STATISTICS.md")
OUTPUT_PATH: Final[Path] = Path("assets/portfolio-evidence.svg")
API_ROOT: Final[str] = "https://api.github.com"
CONTROLS_START: Final[str] = "<!-- statistics:controls:start -->"
CONTROLS_END: Final[str] = "<!-- statistics:controls:end -->"


@dataclass(frozen=True)
class RepoEvidence:
    """Mechanical quality signals found in one flagship repository."""

    name: str
    has_ci: bool
    has_tests: bool
    has_docs: bool
    has_citation: bool
    has_reproducibility_assets: bool


@dataclass(frozen=True)
class AuditResult:
    """Complete flagship audit used by both Markdown and SVG outputs."""

    repositories: tuple[str, ...]
    evidence: tuple[RepoEvidence, ...]
    real_data_count: int
    research_software_count: int

    @property
    def total(self) -> int:
        return len(self.repositories)


def _headers() -> dict[str, str]:
    """Return GitHub API request headers, using the Actions token when present."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "diogoribeiro7-profile-metrics",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _get_json(url: str) -> object:
    """Fetch and decode a GitHub API JSON response."""
    request = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return []
        raise RuntimeError(f"GitHub API request failed: {url} ({exc.code})") from exc


def _contents(repo: str, path: str = "") -> list[dict[str, object]]:
    """Return directory entries from one repository path."""
    suffix = f"/{path}" if path else ""
    payload = _get_json(f"{API_ROOT}/repos/{OWNER}/{repo}/contents{suffix}")
    if not isinstance(payload, list):
        return []
    return [item for item in payload if isinstance(item, dict)]


def _names(entries: list[dict[str, object]]) -> set[str]:
    """Return entry names with runtime type validation."""
    result: set[str] = set()
    for item in entries:
        name = item.get("name")
        if isinstance(name, str):
            result.add(name)
    return result


def _featured_repos() -> list[str]:
    """Parse the twelve curated repositories from FEATURED.md."""
    text = FEATURED_PATH.read_text(encoding="utf-8")
    matches = re.findall(r"https://github\.com/DiogoRibeiro7/([^/)#]+)", text)
    repos = list(dict.fromkeys(repo for repo in matches if repo != "diogoribeiro7"))
    if len(repos) != 12:
        raise ValueError(f"Expected 12 flagship repositories, found {len(repos)}: {repos}")
    return repos


def _project_metadata() -> dict[str, dict[str, Any]]:
    """Load semantic project classifications from the canonical manifest."""
    payload: object = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("projects"), list):
        raise TypeError("Portfolio manifest must contain a projects list.")

    metadata: dict[str, dict[str, Any]] = {}
    for project in payload["projects"]:
        if not isinstance(project, dict) or not isinstance(project.get("repo"), str):
            raise TypeError("Every manifest project must be an object with a string repo field.")
        metadata[project["repo"]] = project
    return metadata


def _audit_repo(repo: str) -> RepoEvidence:
    """Audit mechanically verifiable repository-level evidence."""
    root = _names(_contents(repo))
    github = _names(_contents(repo, ".github")) if ".github" in root else set()
    workflows = _contents(repo, ".github/workflows") if "workflows" in github else []

    docs_markers = {"docs", "mkdocs.yml", "mkdocs.yaml", "docs.yml", "docs.yaml"}
    test_markers = {"tests", "test", "pytest.ini", "tox.ini"}
    citation_markers = {"CITATION.cff", ".zenodo.json"}
    reproducibility_markers = {
        "experiments",
        "artifacts",
        "results",
        "reports",
        "notebooks",
        "data",
        "data_sources",
        "config",
        "configs",
    }

    return RepoEvidence(
        name=repo,
        has_ci=bool(workflows),
        has_tests=bool(root & test_markers),
        has_docs=bool(root & docs_markers),
        has_citation=bool(root & citation_markers),
        has_reproducibility_assets=bool(root & reproducibility_markers),
    )


def audit() -> AuditResult:
    """Run the full structural and semantic audit over the curated flagship set."""
    repos = _featured_repos()
    metadata = _project_metadata()
    missing = [repo for repo in repos if repo not in metadata]
    if missing:
        raise ValueError(f"Featured repositories missing from canonical manifest: {missing}")

    evidence = tuple(_audit_repo(repo) for repo in repos)
    real_data_count = sum(bool(metadata[repo].get("real_data")) for repo in repos)
    research_software_count = sum(bool(metadata[repo].get("research_software")) for repo in repos)
    return AuditResult(tuple(repos), evidence, real_data_count, research_software_count)


def _coverage(count: int, total: int) -> str:
    """Format a count and percentage for Markdown."""
    return f"{count} / {total} ({100 * count / total:.0f}%)"


def _metric(label: str, count: int, total: int, note: str) -> tuple[str, str, str]:
    """Format one metric tuple for SVG rendering."""
    return label, f"{count}/{total} · {100 * count / total:.0f}%", note


def _metrics(result: AuditResult) -> list[tuple[str, int, str]]:
    """Return all dashboard metrics from one audit result."""
    evidence = result.evidence
    return [
        ("CI-backed", sum(item.has_ci for item in evidence), "GitHub Actions workflow present"),
        ("Automated tests", sum(item.has_tests for item in evidence), "tests/test/pytest/tox marker present"),
        ("Dedicated documentation", sum(item.has_docs for item in evidence), "docs directory or docs config present"),
        ("Citable / archived", sum(item.has_citation for item in evidence), "CITATION.cff or Zenodo metadata present"),
        (
            "Reproducibility assets",
            sum(item.has_reproducibility_assets for item in evidence),
            "experiments/results/data/config-style artifacts present",
        ),
        (
            "Real-data / empirical",
            result.real_data_count,
            "canonical manifest classification for the curated flagship set",
        ),
        (
            "Research software / methods",
            result.research_software_count,
            "canonical manifest classification for the curated flagship set",
        ),
    ]


def _render_svg(result: AuditResult) -> str:
    """Render the dark/light-compatible flagship evidence dashboard."""
    metrics = [_metric(label, count, result.total, note) for label, count, note in _metrics(result)]
    width = 900
    card_w = 420
    card_h = 104
    gap = 20
    rows = (len(metrics) + 1) // 2
    height = 90 + rows * (card_h + gap) + 42

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Flagship portfolio evidence metrics</title>',
        f'<desc id="desc">Evidence metrics computed across {result.total} flagship repositories.</desc>',
        '<style>',
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#c9d1d9}',
        '.title{font-size:24px;font-weight:700}.sub{font-size:13px;fill:#8b949e}',
        '.card{fill:#161b22;stroke:#30363d;stroke-width:1}.label{font-size:14px;font-weight:600}',
        '.value{font-size:24px;font-weight:700;fill:#58a6ff}.note{font-size:11px;fill:#8b949e}',
        '</style>',
        '<rect width="100%" height="100%" rx="12" fill="#0d1117"/>',
        '<text x="24" y="34" class="title">Flagship portfolio evidence</text>',
        f'<text x="24" y="58" class="sub">Audited across {result.total} featured repositories · structural signals, not popularity metrics</text>',
    ]

    for index, (label, value, note) in enumerate(metrics):
        col = index % 2
        row = index // 2
        x = 24 + col * (card_w + gap)
        y = 78 + row * (card_h + gap)
        parts.extend(
            [
                f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="10" class="card"/>',
                f'<text x="{x + 18}" y="{y + 27}" class="label">{escape(label)}</text>',
                f'<text x="{x + 18}" y="{y + 59}" class="value">{escape(value)}</text>',
                f'<text x="{x + 18}" y="{y + 82}" class="note">{escape(note)}</text>',
            ]
        )

    parts.append(
        f'<text x="24" y="{height - 18}" class="sub">Generated from FEATURED.md + GitHub repository structure + canonical manifest classifications.</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def _render_controls_table(result: AuditResult) -> str:
    """Render the Statistics-page engineering-control table from the same audit."""
    evidence = result.evidence
    rows = [
        CONTROLS_START,
        "| Control | Coverage |",
        "| :-- | --: |",
        f'| CI workflow present | **{_coverage(sum(item.has_ci for item in evidence), result.total)}** |',
        f'| Automated-test marker present | **{_coverage(sum(item.has_tests for item in evidence), result.total)}** |',
        f'| Dedicated documentation | **{_coverage(sum(item.has_docs for item in evidence), result.total)}** |',
        f'| Citation / archive metadata | **{_coverage(sum(item.has_citation for item in evidence), result.total)}** |',
        f'| Reproducibility-style assets | **{_coverage(sum(item.has_reproducibility_assets for item in evidence), result.total)}** |',
        CONTROLS_END,
    ]
    return "\n".join(rows)


def _replace_controls(text: str, replacement: str) -> str:
    """Replace exactly one generated engineering-control block."""
    pattern = re.compile(re.escape(CONTROLS_START) + r".*?" + re.escape(CONTROLS_END), re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one engineering-control block; found {len(matches)}.")
    return pattern.sub(replacement, text, count=1)


def _expected_statistics(result: AuditResult) -> str:
    """Return Statistics Markdown with the flagship control table refreshed."""
    current = STATISTICS_PATH.read_text(encoding="utf-8")
    return _replace_controls(current, _render_controls_table(result))


def generate(result: AuditResult) -> None:
    """Write both audit-derived outputs."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(_render_svg(result), encoding="utf-8")
    STATISTICS_PATH.write_text(_expected_statistics(result), encoding="utf-8")


def check(result: AuditResult) -> int:
    """Fail when either committed audit-derived output is stale."""
    errors: list[str] = []
    if OUTPUT_PATH.read_text(encoding="utf-8") != _render_svg(result):
        errors.append("assets/portfolio-evidence.svg is stale")
    if STATISTICS_PATH.read_text(encoding="utf-8") != _expected_statistics(result):
        errors.append("STATISTICS.md flagship engineering-control table is stale")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Flagship engineering controls are synchronized with the current audit.")
    return 0


def main() -> int:
    """Generate audit outputs or verify their committed state."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("generate", "check"), nargs="?", default="generate")
    args = parser.parse_args()
    result = audit()
    if args.command == "generate":
        generate(result)
        return 0
    return check(result)


if __name__ == "__main__":
    raise SystemExit(main())
