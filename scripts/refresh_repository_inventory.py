"""Refresh aggregate repository visibility/language snapshots and language radar.

An authenticated GitHub token with metadata access to all owned repositories is
required for ``refresh``. Only anonymous aggregate counts are written to disk.
``generate`` is offline and uses the previously verified snapshot.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import os
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any, Final
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT: Final[Path] = Path(__file__).resolve().parents[1]
LANGUAGES: Final[Path] = ROOT / "data/repository_language_snapshot.json"
VISIBILITY: Final[Path] = ROOT / "data/repository_visibility_snapshot.json"
RADAR: Final[Path] = ROOT / "assets/language-radar.svg"
OWNER: Final[str] = "DiogoRibeiro7"


def collect_inventory(token: str) -> tuple[dict[str, Any], dict[str, Any]]:
    """Count all owner repositories using GitHub's authenticated REST endpoint.

    Reject incomplete pages, duplicate IDs, unexpected owners or visibility
    values. No repository identifiers are returned or saved.
    """
    if not isinstance(token, str) or not token.strip():
        raise ValueError("GITHUB_TOKEN must contain a token authorized for private metadata")
    languages: dict[str, Counter[str]] = {"public": Counter(), "private": Counter()}
    archived: Counter[str] = Counter()
    seen: set[int] = set()
    nonempty_pages = 0
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?affiliation=owner&per_page=100&page={page}"
        request = Request(url, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "diogoribeiro7-aggregate-inventory",
        })
        try:
            with urlopen(request, timeout=30) as response:
                rows: object = json.load(response)
        except (HTTPError, URLError) as exc:
            raise RuntimeError(f"GitHub inventory request failed on page {page}") from exc
        if not isinstance(rows, list):
            raise ValueError("GitHub response must be a repository list")
        if not rows:
            break
        if len(rows) > 100:
            raise ValueError("Unexpected GitHub page size")
        nonempty_pages += 1
        for repo in rows:
            if not isinstance(repo, dict) or not isinstance(repo.get("id"), int):
                raise ValueError("Invalid repository metadata")
            repo_id = repo["id"]
            if repo_id in seen:
                raise ValueError("Duplicate repository ID across pages")
            seen.add(repo_id)
            if not isinstance(repo.get("owner"), dict) or repo["owner"].get("login", "").casefold() != OWNER.casefold():
                raise ValueError("Repository not owned by the expected account")
            if type(repo.get("private")) is not bool or type(repo.get("archived")) is not bool:
                raise ValueError("Missing visibility or archived status")
            visibility = "private" if repo["private"] else "public"
            language = repo.get("language")
            if language is not None and (not isinstance(language, str) or not language.strip()):
                raise ValueError("Invalid primary language")
            languages[visibility][language or "Unclassified"] += 1
            archived[visibility] += int(repo["archived"])
        page += 1
        if page > 1000:
            raise ValueError("Exceeded the maximum number of inventory pages")

    captured_on = date.today().isoformat()
    lang_data = {
        "schema_version": 1,
        "captured_on": captured_on,
        "source": "Authenticated GitHub REST repository metadata (owner affiliation, primary language)",
        "scope": "All repositories owned by DiogoRibeiro7, including archived repositories and forks; primary language is GitHub Linguist classification",
        "public": dict(sorted(languages["public"].items())),
        "private": dict(sorted(languages["private"].items())),
    }
    vis_data = {
        "schema_version": 1,
        "captured_on": captured_on,
        "source": "Authenticated GitHub repository inventory (owner affiliation)",
        "scope": "Repositories owned by DiogoRibeiro7, including archived repositories and any forks",
        "visibility": {key: sum(languages[key].values()) for key in ("public", "private")},
        "archived": {key: archived[key] for key in ("public", "private")},
        "pagination": {"page_size": 100, "nonempty_pages": nonempty_pages,
                       "unique_repository_ids": len(seen), "next_page_empty": True},
    }
    return lang_data, vis_data


def validate_snapshots(language_data: dict[str, Any], visibility_data: dict[str, Any]) -> dict[str, int]:
    """Ensure language counts match visibility counts and contain no repo data."""
    if set(language_data) != {"schema_version", "captured_on", "source", "scope", "public", "private"}:
        raise ValueError("Language snapshot must contain aggregate fields only")
    if language_data["schema_version"] != 1 or visibility_data.get("schema_version") != 1:
        raise ValueError("Unsupported schema version")
    if language_data["captured_on"] != visibility_data.get("captured_on"):
        raise ValueError("Snapshot dates disagree")
    totals: Counter[str] = Counter()
    for visibility in ("public", "private"):
        counts = language_data[visibility]
        if not isinstance(counts, dict) or not counts:
            raise ValueError("Language breakdown is empty or invalid")
        if any(not isinstance(lang, str) or not lang or type(n) is not int or n < 0 for lang, n in counts.items()):
            raise ValueError("Invalid language count")
        if sum(counts.values()) != visibility_data["visibility"][visibility]:
            raise ValueError("Language totals disagree with visibility snapshot")
        totals.update(counts)
    if sum(totals.values()) != visibility_data["pagination"]["unique_repository_ids"]:
        raise ValueError("Inventory totals disagree")
    return dict(totals)


def render_radar(counts: dict[str, int], total: int) -> str:
    """Render six most prominent language categories as an accessible SVG."""
    if total <= 0 or any(type(n) is not int or n < 0 for n in counts.values()):
        raise ValueError("Counts must be positive and non-negative respectively")
    ranked = sorted(((name, n) for name, n in counts.items() if name != "Unclassified"), key=lambda pair: (-pair[1], pair[0]))
    axes = ranked[:6]
    if len(axes) != 6 or axes[0][1] == 0:
        raise ValueError("At least six populated languages are required")
    maximum = axes[0][1]
    cx, cy, radius = 410, 250, 160

    def point(index: int, distance: float) -> tuple[float, float]:
        angle = -math.pi / 2 + 2 * math.pi * index / 6
        return cx + distance * math.cos(angle), cy + distance * math.sin(angle)

    def polygon(distances: list[float]) -> str:
        return " ".join(f"{x:.1f},{y:.1f}" for i, distance in enumerate(distances) for x, y in [point(i, distance)])

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 820 510" role="img" aria-labelledby="title desc">',
        '<title id="title">GitHub primary languages across public and private repositories</title>',
        f'<desc id="desc">Six leading primary-language classifications across {total} repositories: '
        + "; ".join(f"{html.escape(name)} {value}" for name, value in axes)
        + '. Other classifications are excluded from the six-axis display.</desc>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#c9d1d9}'
        '.title{font-size:20px;font-weight:700}.sub{font-size:13px;fill:#8b949e}'
        '.axis{stroke:#57606a;stroke-width:1}.ring{fill:none;stroke:#57606a;stroke-opacity:.5}'
        '.area{fill:#a371f7;fill-opacity:.25;stroke:#a371f7;stroke-width:3}'
        '.dot{fill:#d2a8ff}.label{font-size:14px;font-weight:600}'
        '@media(prefers-color-scheme:light){text{fill:#24292f}.sub{fill:#57606a}'
        '.axis,.ring{stroke:#8c959f}.area{fill:#8250df;stroke:#8250df}.dot{fill:#8250df}}</style>',
        '<text x="24" y="33" class="title">GitHub primary languages · repository evidence</text>',
        f'<text x="24" y="56" class="sub">{total} owned repositories · largest language count = {maximum}</text>',
    ]
    for fraction in (.25, .5, .75, 1.0):
        parts.append(f'<polygon points="{polygon([radius * fraction] * 6)}" class="ring"/>')
    for i in range(6):
        x, y = point(i, radius)
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" class="axis"/>')
    parts.append(f'<polygon points="{polygon([radius * n / maximum for _, n in axes])}" class="area"/>')
    for i, (name, number) in enumerate(axes):
        x, y = point(i, radius * number / maximum)
        lx, ly = point(i, radius + 34)
        anchor = "middle" if i in (0, 3) else ("start" if i in (1, 2) else "end")
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" class="dot"/>')
        parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" class="label">{html.escape(name)} · {number}</text>')
    parts.append('<text x="410" y="490" text-anchor="middle" class="sub">Primary language per repository, not proficiency or code volume</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main() -> None:
    """Refresh verified aggregate snapshots or regenerate/check the SVG offline."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("refresh", "generate", "check"))
    args = parser.parse_args()
    if args.command == "refresh":
        language_data, visibility_data = collect_inventory(os.environ.get("PROFILE_INVENTORY_TOKEN", ""))
        counts = validate_snapshots(language_data, visibility_data)
        language_svg = render_radar(counts, sum(counts.values()))
        # Do not open a weekly PR solely because the verification date changed.
        if LANGUAGES.exists() and VISIBILITY.exists():
            previous_languages = json.loads(LANGUAGES.read_text(encoding="utf-8"))
            previous_visibility = json.loads(VISIBILITY.read_text(encoding="utf-8"))
            if (previous_languages.get("public") == language_data["public"]
                    and previous_languages.get("private") == language_data["private"]
                    and previous_visibility.get("archived") == visibility_data["archived"]
                    and previous_visibility.get("visibility") == visibility_data["visibility"]):
                date_of_last_change = previous_languages["captured_on"]
                language_data["captured_on"] = date_of_last_change
                visibility_data["captured_on"] = date_of_last_change
        LANGUAGES.write_text(json.dumps(language_data, indent=2) + "\n", encoding="utf-8")
        VISIBILITY.write_text(json.dumps(visibility_data, indent=2) + "\n", encoding="utf-8")
        RADAR.write_text(language_svg, encoding="utf-8")
        return
    language_data = json.loads(LANGUAGES.read_text(encoding="utf-8"))
    visibility_data = json.loads(VISIBILITY.read_text(encoding="utf-8"))
    counts = validate_snapshots(language_data, visibility_data)
    svg = render_radar(counts, sum(counts.values()))
    if args.command == "check":
        if RADAR.read_text(encoding="utf-8") != svg:
            raise SystemExit("Language radar is stale: run generate")
    else:
        RADAR.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
