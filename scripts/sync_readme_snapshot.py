"""Synchronise the README portfolio snapshot with canonical portfolio data."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
MANIFEST_PATH = ROOT / "data" / "portfolio.json"
FEATURED_PATH = ROOT / "FEATURED.md"

START = "<!-- readme:portfolio-snapshot:start -->"
END = "<!-- readme:portfolio-snapshot:end -->"
FEATURED_REPO_PATTERN = re.compile(r"https://github\.com/DiogoRibeiro7/([^/)#]+)")


def load_manifest() -> dict[str, Any]:
    """Load the canonical portfolio manifest with minimal type validation."""
    payload: object = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError("Portfolio manifest must be a JSON object.")
    for key in ("projects", "outputs", "case_studies"):
        if key not in payload or not isinstance(payload[key], list):
            raise TypeError(f"Manifest field {key!r} must be a list.")
    return payload


def featured_total() -> int:
    """Count the human-curated repositories listed in FEATURED.md."""
    text = FEATURED_PATH.read_text(encoding="utf-8")
    matches = FEATURED_REPO_PATTERN.findall(text)
    repos = list(dict.fromkeys(repo for repo in matches if repo != "diogoribeiro7"))
    if len(repos) != 12:
        raise ValueError(f"Expected 12 curated Featured repositories, found {len(repos)}: {repos}")
    return len(repos)


def metrics(manifest: dict[str, Any]) -> dict[str, int]:
    """Derive the compact README evidence counts from canonical sources."""
    projects = manifest["projects"]
    outputs = manifest["outputs"]
    cases = manifest["case_studies"]

    total = len(projects)
    if total == 0:
        raise ValueError("Portfolio manifest contains no projects.")

    return {
        "projects": total,
        "outputs": len(outputs),
        "pypi": sum(bool(project.get("pypi")) for project in projects),
        "cases": len(cases),
        "domains": len({str(case["domain"]) for case in cases}),
        "real_data": sum(bool(project.get("real_data")) for project in projects),
        "featured": featured_total(),
    }


def render(values: dict[str, int]) -> str:
    """Render the generated README evidence table."""
    total = values["projects"]
    empirical = values["real_data"]
    return "\n".join(
        [
            START,
            "| Evidence | Current scope |",
            "| :-- | --: |",
            f'| Manifest-backed public projects | **{total}** |',
            f'| Substantial outputs | **{values["outputs"]}** |',
            f'| Published PyPI packages | **{values["pypi"]}** |',
            f'| Case studies | **{values["cases"]} across {values["domains"]} domains** |',
            f'| Real-data / empirical projects | **{empirical} / {total} ({100 * empirical / total:.0f}%)** |',
            f'| Curated flagship repositories | **{values["featured"]}** |',
            END,
        ]
    )


def replace_snapshot(text: str, replacement: str) -> str:
    """Replace exactly one generated README snapshot block."""
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one README snapshot block; found {len(matches)}.")
    return pattern.sub(replacement, text, count=1)


def main() -> int:
    """Generate the README snapshot, or fail when the committed block is stale."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("generate", "check"))
    args = parser.parse_args()

    current = README_PATH.read_text(encoding="utf-8")
    expected = replace_snapshot(current, render(metrics(load_manifest())))

    if args.command == "generate":
        README_PATH.write_text(expected, encoding="utf-8")
        return 0

    if current != expected:
        print("ERROR: README.md portfolio snapshot is stale.")
        return 1

    print("README portfolio snapshot is consistent with canonical portfolio data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
