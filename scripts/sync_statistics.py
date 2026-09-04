"""Synchronise human-readable statistics tables with canonical portfolio data."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from generate_topic_statistics import count_topics

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "data" / "portfolio.json"
PROJECTS_PATH = ROOT / "PROJECTS.md"
FEATURED_PATH = ROOT / "FEATURED.md"
STATISTICS_PATH = ROOT / "STATISTICS.md"
FEATURED_REPO_PATTERN = re.compile(r"https://github\.com/DiogoRibeiro7/([^/)#]+)")

SNAPSHOT_START = "<!-- statistics:snapshot:start -->"
SNAPSHOT_END = "<!-- statistics:snapshot:end -->"
DEPTH_START = "<!-- statistics:depth:start -->"
DEPTH_END = "<!-- statistics:depth:end -->"
OUTPUTS_START = "<!-- statistics:outputs:start -->"
OUTPUTS_END = "<!-- statistics:outputs:end -->"
BOUNDARIES_START = "<!-- statistics:boundaries:start -->"
BOUNDARIES_END = "<!-- statistics:boundaries:end -->"
DENOMINATOR_START = "<!-- statistics:denominator:start -->"
DENOMINATOR_END = "<!-- statistics:denominator:end -->"
OUTPUTS_INTRO_START = "<!-- statistics:outputs-intro:start -->"
OUTPUTS_INTRO_END = "<!-- statistics:outputs-intro:end -->"


def load_manifest() -> dict[str, Any]:
    """Load and minimally validate the canonical portfolio manifest."""
    payload: object = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError("Portfolio manifest must be a JSON object.")
    for key in ("projects", "outputs", "case_studies"):
        if key not in payload or not isinstance(payload[key], list):
            raise TypeError(f"Manifest field {key!r} must be a list.")
    return payload


def catalogue_total() -> int:
    """Count curated catalogue entries using the same parser as the topic widget."""
    markdown = PROJECTS_PATH.read_text(encoding="utf-8")
    return sum(count_topics(markdown).values())


def featured_total() -> int:
    """Count the human-curated repositories listed in FEATURED.md."""
    text = FEATURED_PATH.read_text(encoding="utf-8")
    matches = FEATURED_REPO_PATTERN.findall(text)
    repos = list(dict.fromkeys(repo for repo in matches if repo != "diogoribeiro7"))
    if len(repos) != 12:
        raise ValueError(f"Expected 12 curated Featured repositories, found {len(repos)}: {repos}")
    return len(repos)


def metrics(manifest: dict[str, Any]) -> dict[str, Any]:
    """Derive all Statistics-page counts from their canonical sources."""
    projects = manifest["projects"]
    outputs = manifest["outputs"]
    cases = manifest["case_studies"]

    total = len(projects)
    if total == 0:
        raise ValueError("Portfolio manifest contains no projects.")

    real_data = sum(bool(project.get("real_data")) for project in projects)
    research_software = sum(bool(project.get("research_software")) for project in projects)
    pypi = sum(bool(project.get("pypi")) for project in projects)
    domains = len({case["domain"] for case in cases})
    output_types = Counter(str(item["type"]) for item in outputs)

    return {
        "projects": total,
        "outputs": len(outputs),
        "cases": len(cases),
        "domains": domains,
        "pypi": pypi,
        "real_data": real_data,
        "research_software": research_software,
        "featured": featured_total(),
        "catalogue": catalogue_total(),
        "output_types": output_types,
    }


def render_snapshot(values: dict[str, Any]) -> str:
    """Render the compact portfolio snapshot table."""
    total = int(values["projects"])
    real_data = int(values["real_data"])
    research_software = int(values["research_software"])
    return "\n".join([
        SNAPSHOT_START,
        "| Portfolio signal | Current value |",
        "| :-- | --: |",
        f'| Manifest-backed public projects | **{total}** |',
        f'| Substantial outputs | **{values["outputs"]}** |',
        f'| Case studies | **{values["cases"]} across {values["domains"]} domains** |',
        f'| Published PyPI packages | **{values["pypi"]}** |',
        f'| Real-data / empirical projects | **{real_data} / {total} ({100 * real_data / total:.0f}%)** |',
        f'| Research software / methods | **{research_software} / {total} ({100 * research_software / total:.0f}%)** |',
        f'| Curated flagship repositories | **{values["featured"]}** |',
        f'| Curated catalogue entries | **{values["catalogue"]}** |',
        SNAPSHOT_END,
    ])


def render_depth(values: dict[str, Any]) -> str:
    """Render the portfolio-wide research/output depth table."""
    total = int(values["projects"])
    real_data = int(values["real_data"])
    research_software = int(values["research_software"])
    return "\n".join([
        DEPTH_START,
        "| Measure | Current scope | What it means |",
        "| :-- | --: | :-- |",
        f'| Manifest-backed public projects | **{total}** | Projects with explicit category, maturity and evidence metadata |',
        f'| Substantial outputs | **{values["outputs"]}** | Published software, research programmes, empirical/replication studies, and decision/engineering artifacts |',
        f'| Published PyPI packages | **{values["pypi"]}** | Verified package releases, not merely package-ready repositories |',
        f'| Real-data / empirical projects | **{real_data} / {total} ({100 * real_data / total:.0f}%)** | Explicitly classified in the manifest |',
        f'| Research software / methods | **{research_software} / {total} ({100 * research_software / total:.0f}%)** | Explicitly classified libraries, methods and research tooling |',
        f'| Case studies | **{values["cases"]} across {values["domains"]} domains** | End-to-end problem → constraints → method → outcome narratives |',
        f'| Curated flagship projects | **{values["featured"]}** | Reviewer-oriented subset; deliberately not used as the portfolio denominator |',
        DEPTH_END,
    ])


def render_outputs(values: dict[str, Any]) -> str:
    """Render output-class counts from manifest output types."""
    output_types: Counter[str] = values["output_types"]
    ordered_types = (
        "Published research software",
        "Research and paper programmes",
        "Empirical and replication studies",
        "Decision and engineering artifacts",
    )
    rows = [OUTPUTS_START, "| Output class | Count |", "| :-- | --: |"]
    rows.extend(f"| {label} | **{output_types.get(label, 0)}** |" for label in ordered_types)
    rows.append(OUTPUTS_END)
    return "\n".join(rows)


def render_denominator(values: dict[str, Any]) -> str:
    """Render the primary-denominator sentence.

    The counts in this sentence and the outputs sentence below used to be prose
    the generators did not own, so a manifest change left them silently wrong
    while every generated table around them was correct.
    """
    return "\n".join([
        DENOMINATOR_START,
        f'**Primary denominator:** the **{values["projects"]} public projects represented in the canonical '
        f'[`data/portfolio.json`](data/portfolio.json) manifest**. This is broader than the '
        f'{values["featured"]}-project Featured subset and narrower than every repository ever created on the account.',
        DENOMINATOR_END,
    ])


def render_outputs_intro(values: dict[str, Any]) -> str:
    """Render the sentence introducing the output-composition table."""
    return "\n".join([
        OUTPUTS_INTRO_START,
        f'The **{values["outputs"]} outputs** currently break down into:',
        OUTPUTS_INTRO_END,
    ])


def render_boundaries(values: dict[str, Any]) -> str:
    """Render the denominator reference table."""
    return "\n".join([
        BOUNDARIES_START,
        "| Question | Denominator |",
        "| :-- | :-- |",
        f'| What does the serious public portfolio contain? | **{values["projects"]} manifest-backed public projects** |',
        f'| What inspectable artifacts has it produced? | **{values["outputs"]} output records** |',
        f'| What can a reviewer inspect end-to-end? | **{values["cases"]} case studies across {values["domains"]} domains** |',
        f'| How strong are repository controls on the curated front page? | **{values["featured"]} flagship repositories** |',
        f'| Where is the broad catalogue concentrated? | **{values["catalogue"]} PROJECTS.md entries** |',
        BOUNDARIES_END,
    ])


def replace_block(text: str, start: str, end: str, replacement: str) -> str:
    """Replace exactly one generated marker block."""
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one block between {start} and {end}; found {len(matches)}.")
    return pattern.sub(replacement, text, count=1)


def render_statistics(text: str, values: dict[str, Any]) -> str:
    """Return Statistics Markdown with all generated tables refreshed."""
    updated = replace_block(text, SNAPSHOT_START, SNAPSHOT_END, render_snapshot(values))
    updated = replace_block(updated, DEPTH_START, DEPTH_END, render_depth(values))
    updated = replace_block(updated, OUTPUTS_START, OUTPUTS_END, render_outputs(values))
    updated = replace_block(updated, DENOMINATOR_START, DENOMINATOR_END, render_denominator(values))
    updated = replace_block(updated, OUTPUTS_INTRO_START, OUTPUTS_INTRO_END, render_outputs_intro(values))
    return replace_block(updated, BOUNDARIES_START, BOUNDARIES_END, render_boundaries(values))


def main() -> int:
    """Generate the canonical tables, or fail if the committed page is stale."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("generate", "check"))
    args = parser.parse_args()

    values = metrics(load_manifest())
    current = STATISTICS_PATH.read_text(encoding="utf-8")
    expected = render_statistics(current, values)

    if args.command == "generate":
        STATISTICS_PATH.write_text(expected, encoding="utf-8")
        return 0

    if current != expected:
        print("ERROR: STATISTICS.md generated tables are stale.")
        return 1

    print("Statistics tables are consistent with canonical portfolio data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
