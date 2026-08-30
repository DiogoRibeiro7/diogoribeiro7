"""Generate the GitHub profile topic-statistics SVG from PROJECTS.md.

The script counts curated project entries under selected second-level headings and
renders a dependency-free SVG suitable for embedding directly in Markdown.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_PATH = ROOT / "PROJECTS.md"
OUTPUT_PATH = ROOT / "assets" / "topic-statistics.svg"

TOPIC_LABELS: dict[str, str] = {
    "Production AI & LLM Systems": "AI & LLM systems",
    "ML Engineering & MLOps": "ML engineering & MLOps",
    "Deep Learning & Scientific Computing": "Scientific ML & deep learning",
    "Data Engineering & Streaming": "Data engineering & streaming",
    "Statistical & Applied Data Science": "Statistics & applied DS",
    "Optimisation & Decision Systems": "Optimisation & decisions",
    "Economics, Finance & Policy Research": "Economics, finance & policy",
    "Mathematical Methods & Algorithms": "Mathematics & algorithms",
    "Developer Tooling": "Developer tooling",
}

HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
PROJECT_RE = re.compile(r"^-\s+")


def count_topics(markdown: str) -> dict[str, int]:
    """Count project bullets beneath the configured second-level headings."""
    counts = {heading: 0 for heading in TOPIC_LABELS}
    active_heading: str | None = None

    for raw_line in markdown.splitlines():
        heading_match = HEADING_RE.match(raw_line)
        if heading_match:
            heading = heading_match.group(1).strip()
            active_heading = heading if heading in counts else None
            continue

        if active_heading is not None and PROJECT_RE.match(raw_line):
            counts[active_heading] += 1

    if not any(counts.values()):
        raise ValueError("No project entries were found under configured topic headings.")

    return counts


def render_svg(counts: dict[str, int]) -> str:
    """Render a responsive horizontal-bar SVG from topic counts."""
    rows = [(TOPIC_LABELS[key], counts[key]) for key in TOPIC_LABELS]
    total = sum(value for _, value in rows)
    maximum = max(value for _, value in rows)

    width = 820
    left = 255
    right = 70
    top = 74
    row_height = 38
    bar_height = 18
    chart_width = width - left - right
    height = top + len(rows) * row_height + 48

    elements: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Project topics</title>',
        f'<desc id="desc">Distribution of {total} curated project entries across technical and research topics.</desc>',
        '<style>',
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#c9d1d9}',
        '.muted{fill:#8b949e}.label{font-size:14px}.value{font-size:13px;font-weight:600}.title{font-size:20px;font-weight:700}.subtitle{font-size:13px}',
        '.track{fill:#21262d}.bar{fill:#58a6ff}',
        '@media (prefers-color-scheme: light){text{fill:#24292f}.muted{fill:#57606a}.track{fill:#d8dee4}.bar{fill:#0969da}}',
        '</style>',
        '<text x="24" y="30" class="title">Topics I work on</text>',
        f'<text x="24" y="52" class="subtitle muted">{total} curated project entries · generated from PROJECTS.md</text>',
    ]

    for index, (label, value) in enumerate(rows):
        y = top + index * row_height
        bar_width = 0 if maximum == 0 else chart_width * value / maximum
        percentage = 0 if total == 0 else 100 * value / total
        escaped_label = html.escape(label)
        elements.extend(
            [
                f'<text x="24" y="{y + 14}" class="label">{escaped_label}</text>',
                f'<rect x="{left}" y="{y}" width="{chart_width}" height="{bar_height}" rx="9" class="track"/>',
                f'<rect x="{left}" y="{y}" width="{bar_width:.1f}" height="{bar_height}" rx="9" class="bar"/>',
                f'<text x="{width - 18}" y="{y + 14}" text-anchor="end" class="value">{value} · {percentage:.0f}%</text>',
            ]
        )

    elements.append('</svg>')
    return "\n".join(elements) + "\n"


def main() -> None:
    """Read the catalogue, compute counts, and write the SVG widget."""
    markdown = PROJECTS_PATH.read_text(encoding="utf-8")
    counts = count_topics(markdown)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_svg(counts), encoding="utf-8")


if __name__ == "__main__":
    main()
