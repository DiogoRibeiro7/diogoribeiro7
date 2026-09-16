"""Synchronise the reviewer-facing public portfolio index in PROJECTS.md."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "data" / "portfolio.json"
PROJECTS_PATH = ROOT / "PROJECTS.md"

INDEX_START = "<!-- projects:public-index:start -->"
INDEX_END = "<!-- projects:public-index:end -->"
TITLE_PATTERN = re.compile(r"^# Selected Work\s*$", re.MULTILINE)

# The routes aggregate canonical maturity labels; they do not create a second
# project taxonomy. Every manifest project must resolve to exactly one route.
PUBLIC_ROUTES: tuple[tuple[str, tuple[str, ...], str, str], ...] = (
    (
        "Released software",
        ("published software",),
        "Installable public software with release evidence.",
        "[PyPI](PYPI.md) · [Outputs](OUTPUTS.md)",
    ),
    (
        "Production systems",
        ("production-style system",),
        "Serving, observability, data contracts, streaming or operational monitoring.",
        "[Featured](FEATURED.md) · [Case Studies](CASE_STUDIES.md)",
    ),
    (
        "Empirical & replication evidence",
        ("empirical study", "replication study"),
        "Real-data experiments, replications and falsifiable comparative studies.",
        "[Outputs](OUTPUTS.md) · [Case Studies](CASE_STUDIES.md)",
    ),
    (
        "Decision systems",
        ("decision system", "decision study"),
        "Optimisation, policy simulation and cost-sensitive operating decisions.",
        "[Case Studies](CASE_STUDIES.md)",
    ),
    (
        "Research programmes",
        ("research programme", "research portfolio"),
        "Active multi-stage research with explicit questions, provenance and validation.",
        "[Research](RESEARCH.md)",
    ),
    (
        "Research software & methods",
        ("research software",),
        "Reusable algorithms or methods whose evidence is broader than a package release.",
        "[Methods](METHODS.md) · [Outputs](OUTPUTS.md)",
    ),
)


def load_manifest() -> dict[str, Any]:
    """Load and minimally validate the canonical portfolio manifest."""
    payload: object = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError("Portfolio manifest must be a JSON object.")
    projects = payload.get("projects")
    if not isinstance(projects, list) or not projects:
        raise TypeError("Manifest field 'projects' must be a non-empty list.")
    return payload


def route_counts(manifest: dict[str, Any]) -> list[tuple[str, int, str, str]]:
    """Aggregate project maturities into reviewer-facing evidence routes."""
    projects = manifest["projects"]
    maturities = Counter(str(project.get("maturity", "")) for project in projects)

    configured_labels = [label for _, labels, _, _ in PUBLIC_ROUTES for label in labels]
    if len(configured_labels) != len(set(configured_labels)):
        raise ValueError("Public portfolio routes contain duplicate maturity labels.")

    unknown = sorted(set(maturities) - set(configured_labels))
    if unknown:
        raise ValueError(f"Project maturities missing public portfolio routes: {unknown}")

    rows: list[tuple[str, int, str, str]] = []
    assigned = 0
    for route, labels, evidence, destination in PUBLIC_ROUTES:
        count = sum(maturities[label] for label in labels)
        rows.append((route, count, evidence, destination))
        assigned += count

    if assigned != len(projects):
        raise ValueError(
            f"Public portfolio routes assign {assigned} projects, expected {len(projects)}."
        )
    return rows


def render_index(manifest: dict[str, Any]) -> str:
    """Render the generated reviewer-facing public portfolio index."""
    rows = route_counts(manifest)
    total = len(manifest["projects"])
    lines = [
        INDEX_START,
        "## Public portfolio index",
        "",
        f"The canonical manifest currently contains **{total} public projects**. This index groups them by evidence state rather than subject area, so a reviewer can choose the right depth quickly. The broader catalogue below also includes additional historical, exploratory and private work.",
        "",
        "| Reviewer path | Public projects | What that evidence means | Inspect next |",
        "| :-- | --: | :-- | :-- |",
    ]
    for route, count, evidence, destination in rows:
        lines.append(f"| **{route}** | **{count}** | {evidence} | {destination} |")
    lines.extend(
        [
            "",
            "Topic and application area remain separate from maturity. Use the detailed catalogue below when the question is *what domain does this project address?*; use this index when the question is *what kind of evidence does this project provide?*",
            INDEX_END,
        ]
    )
    return "\n".join(lines)


def replace_or_insert(text: str, replacement: str) -> str:
    """Replace the index block, or insert it directly below the page title."""
    pattern = re.compile(re.escape(INDEX_START) + r".*?" + re.escape(INDEX_END), re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) > 1:
        raise ValueError(f"Expected at most one PROJECTS index block; found {len(matches)}.")
    if matches:
        return pattern.sub(replacement, text, count=1)

    title_match = TITLE_PATTERN.search(text)
    if not title_match:
        raise ValueError("PROJECTS.md title '# Selected Work' was not found.")
    insert_at = title_match.end()
    return text[:insert_at] + "\n\n" + replacement + text[insert_at:]


def render_projects(text: str, manifest: dict[str, Any]) -> str:
    """Return PROJECTS.md with the public index synchronised."""
    return replace_or_insert(text, render_index(manifest))


def main() -> int:
    """Generate the public index, or fail if the committed page is stale."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("generate", "check"))
    args = parser.parse_args()

    manifest = load_manifest()
    current = PROJECTS_PATH.read_text(encoding="utf-8")
    expected = render_projects(current, manifest)

    if args.command == "generate":
        PROJECTS_PATH.write_text(expected, encoding="utf-8")
        return 0

    if current != expected:
        print("ERROR: PROJECTS.md public portfolio index is stale.")
        return 1

    print("PROJECTS.md public portfolio index is consistent with canonical portfolio data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
