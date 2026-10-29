"""Render six evidence-volume dimensions from the curated project catalogue.

The radius is relative project-entry volume, not a proficiency or quality score.
Each configured PROJECTS.md section contributes to exactly one dimension.
"""

from __future__ import annotations

import html
import math
from pathlib import Path

from generate_topic_statistics import PROJECTS_PATH, TOPIC_LABELS, count_topics

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "assets" / "evidence-radar.svg"

DIMENSIONS: dict[str, tuple[str, ...]] = {
    "AI & ML systems": ("Production AI & LLM Systems", "ML Engineering & MLOps"),
    "Scientific & maths": ("Deep Learning & Scientific Computing", "Mathematical Methods & Algorithms"),
    "Data & tooling": ("Data Engineering & Streaming", "Developer Tooling"),
    "Statistics": ("Statistical & Applied Data Science",),
    "Decision systems": ("Optimisation & Decision Systems",),
    "Economics & policy": ("Economics, Finance & Policy Research",),
}


def aggregate_topics(counts: dict[str, int]) -> dict[str, int]:
    """Group all curated headings once, rejecting missing or duplicate mappings."""
    mapped = [heading for headings in DIMENSIONS.values() for heading in headings]
    if len(mapped) != len(set(mapped)) or set(mapped) != set(TOPIC_LABELS):
        raise ValueError("Radar dimensions must partition all curated topic headings")
    if set(counts) != set(TOPIC_LABELS):
        raise ValueError("Topic counts must include exactly the configured headings")
    if any(not isinstance(value, int) or isinstance(value, bool) or value < 0 for value in counts.values()):
        raise ValueError("Topic counts must be non-negative integers")
    return {label: sum(counts[heading] for heading in headings) for label, headings in DIMENSIONS.items()}


def render_svg(values: dict[str, int]) -> str:
    """Render a deterministic, dependency-free radar with accessible labels."""
    if list(values) != list(DIMENSIONS) or not values or max(values.values()) <= 0:
        raise ValueError("Expected positive counts in the configured dimension order")
    maximum = max(values.values())
    cx, cy, radius = 410, 245, 165
    size = len(values)

    def point(index: int, distance: float) -> tuple[float, float]:
        angle = -math.pi / 2 + 2 * math.pi * index / size
        return cx + distance * math.cos(angle), cy + distance * math.sin(angle)

    def polygon(distances: list[float]) -> str:
        return " ".join(f"{x:.1f},{y:.1f}" for i, d in enumerate(distances) for x, y in [point(i, d)])

    labels = list(values)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 820 505" role="img" aria-labelledby="title desc">',
        '<title id="title">Public portfolio activity by technical area</title>',
        f'<desc id="desc">{sum(values.values())} curated catalogue entries across six areas. '
        + "; ".join(f"{html.escape(k)}: {v}" for k, v in values.items())
        + '. Radius is relative to the largest area, not an expertise rating.</desc>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#c9d1d9}'
        '.title{font-size:21px;font-weight:700}.sub{font-size:13px;fill:#8b949e}'
        '.axis{stroke:#57606a;stroke-width:1}.ring{fill:none;stroke:#57606a;stroke-opacity:.5}'
        '.area{fill:#58a6ff;fill-opacity:.25;stroke:#58a6ff;stroke-width:3}'
        '.dot{fill:#79c0ff}.label{font-size:14px;font-weight:600}'
        '@media (prefers-color-scheme:light){text{fill:#24292f}.sub{fill:#57606a}'
        '.axis,.ring{stroke:#8c959f}.area{fill:#0969da;stroke:#0969da}.dot{fill:#0969da}}</style>',
        '<text x="24" y="32" class="title">Technical work · public evidence</text>',
        f'<text x="24" y="55" class="sub">{sum(values.values())} curated entries · radius normalised to largest group ({maximum})</text>',
    ]
    for fraction in (0.25, 0.5, 0.75, 1.0):
        parts.append(f'<polygon points="{polygon([radius * fraction] * size)}" class="ring"/>')
    for index in range(size):
        x, y = point(index, radius)
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" class="axis"/>')
    parts.append(f'<polygon points="{polygon([radius * v / maximum for v in values.values()])}" class="area"/>')
    for index, (label, count) in enumerate(values.items()):
        x, y = point(index, radius * count / maximum)
        lx, ly = point(index, radius + 31)
        anchor = "middle" if index in (0, 3) else ("start" if index in (1, 2) else "end")
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" class="dot"/>')
        parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" class="label">{html.escape(label)} · {count}</text>')
    parts.append('<text x="410" y="483" text-anchor="middle" class="sub">Catalogue activity, not skill level, output quality or professional experience</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main() -> None:
    """Regenerate the committed SVG using PROJECTS.md as the sole source."""
    counts = count_topics(PROJECTS_PATH.read_text(encoding="utf-8"))
    OUTPUT_PATH.write_text(render_svg(aggregate_topics(counts)), encoding="utf-8")


if __name__ == "__main__":
    main()
