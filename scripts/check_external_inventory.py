from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "portfolio.json"
USER_AGENT = "diogoribeiro7-profile-integrity/1.0"


def get(url: str, attempts: int = 3) -> tuple[int, bytes]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
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


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors: list[str] = []

    for project in manifest["projects"]:
        repo = project["repo"]
        url = f"https://api.github.com/repos/DiogoRibeiro7/{repo}"
        try:
            status, payload = get(url)
            if status != 200:
                errors.append(f"GitHub repository unavailable ({status}): {repo}")
                continue
            metadata = json.loads(payload)
            if metadata.get("private"):
                errors.append(f"manifest exposes a private repository: {repo}")
        except Exception as exc:  # network errors should be visible, not silently ignored
            errors.append(str(exc))

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

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("All manifest repositories and PyPI packages resolve publicly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
