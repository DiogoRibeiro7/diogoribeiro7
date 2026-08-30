"""Generate portfolio-wide statistics from the canonical manifest."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "portfolio.json"
OUTPUT = ROOT / "assets" / "portfolio-overview.svg"


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def render(manifest: dict) -> str:
    projects = manifest["projects"]
    outputs = manifest["outputs"]
    cases = manifest["case_studies"]
    total = len(projects)
    real_data = sum(bool(p.get("real_data")) for p in projects)
    research_software = sum(bool(p.get("research_software")) for p in projects)
    pypi = sum(bool(p.get("pypi")) for p in projects)
    featured = sum(bool(p.get("featured")) for p in projects)
    domains = len({c["domain"] for c in cases})
    maturity = Counter(p["maturity"] for p in projects)

    headline = [
        ("Manifest-backed projects", str(total), "public projects with explicit portfolio metadata"),
        ("Substantial outputs", str(len(outputs)), "software, research, empirical and decision artifacts"),
        ("Case studies", f"{len(cases)} · {domains} domains", "end-to-end problem → method → outcome narratives"),
        ("Real-data / empirical", f"{real_data}/{total} · {100 * real_data / total:.0f}%", "explicit manifest classification"),
        ("Research software / methods", f"{research_software}/{total} · {100 * research_software / total:.0f}%", "explicit manifest classification"),
        ("Published PyPI packages", str(pypi), "verified package releases"),
        ("Curated flagships", str(featured), "reviewer-oriented subset, not the main denominator"),
    ]

    maturity_order = [
        "published software",
        "empirical study",
        "production-style system",
        "research programme",
        "decision system",
        "research software",
        "replication study",
        "decision study",
        "research portfolio",
    ]
    maturity_rows = [(label, maturity.get(label, 0)) for label in maturity_order if maturity.get(label, 0)]

    width = 920
    card_w = 278
    card_h = 102
    gap = 18
    start_y = 82
    cards_rows = 3
    maturity_y = start_y + cards_rows * (card_h + gap) + 24
    bar_left = 260
    bar_width = 600
    row_h = 31
    height = maturity_y + len(maturity_rows) * row_h + 54

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Portfolio-wide evidence dashboard</title>',
        f'<desc id="desc">Statistics across {total} manifest-backed public projects, {len(outputs)} outputs and {len(cases)} case studies.</desc>',
        '<style>',
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#c9d1d9}',
        '.title{font-size:23px;font-weight:700}.sub{font-size:13px;fill:#8b949e}',
        '.card{fill:#161b22;stroke:#30363d}.label{font-size:13px;font-weight:600}.value{font-size:23px;font-weight:700;fill:#58a6ff}.note{font-size:10.5px;fill:#8b949e}',
        '.track{fill:#21262d}.bar{fill:#58a6ff}.maturity{font-size:13px}',
        '@media (prefers-color-scheme: light){text{fill:#24292f}.sub,.note{fill:#57606a}.card{fill:#f6f8fa;stroke:#d0d7de}.track{fill:#d8dee4}.bar,.value{fill:#0969da}}',
        '</style>',
        '<text x="24" y="31" class="title">Portfolio-wide evidence</text>',
        f'<text x="24" y="54" class="sub">Canonical manifest · {total} public projects · derived metrics, not popularity signals</text>',
    ]

    for i, (label, value, note) in enumerate(headline):
        col = i % 3
        row = i // 3
        x = 24 + col * (card_w + gap)
        y = start_y + row * (card_h + gap)
        parts.extend([
            f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="10" class="card"/>',
            f'<text x="{x + 16}" y="{y + 25}" class="label">{escape(label)}</text>',
            f'<text x="{x + 16}" y="{y + 57}" class="value">{escape(value)}</text>',
            f'<text x="{x + 16}" y="{y + 80}" class="note">{escape(note)}</text>',
        ])

    parts.extend([
        f'<text x="24" y="{maturity_y - 8}" class="label">Maturity mix</text>',
        f'<text x="24" y="{maturity_y + 13}" class="sub">Counts are mutually exclusive manifest labels; topic and maturity are separate dimensions.</text>',
    ])
    max_count = max(count for _, count in maturity_rows)
    for i, (label, count) in enumerate(maturity_rows):
        y = maturity_y + 34 + i * row_h
        length = bar_width * count / max_count
        parts.extend([
            f'<text x="24" y="{y + 14}" class="maturity">{escape(label)}</text>',
            f'<rect x="{bar_left}" y="{y}" width="{bar_width}" height="17" rx="8.5" class="track"/>',
            f'<rect x="{bar_left}" y="{y}" width="{length:.1f}" height="17" rx="8.5" class="bar"/>',
            f'<text x="{width - 24}" y="{y + 14}" text-anchor="end" class="label">{count}</text>',
        ])

    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render(load_manifest()), encoding="utf-8")


if __name__ == "__main__":
    main()
