"""Validate syntax and dimensions of generated profile SVG dashboards."""

from __future__ import annotations

import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Final

ASSETS: Final[tuple[Path, ...]] = tuple(
    Path("assets") / name
    for name in (
        "portfolio-overview.svg",
        "topic-statistics.svg",
        "portfolio-evidence.svg",
        "star-metrics.svg",
    )
)
SVG_TAG: Final[str] = "{http://www.w3.org/2000/svg}svg"


def validate_svg(path: Path) -> list[str]:
    """Return actionable SVG errors without modifying the source file."""
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        return [f"{path}: unreadable or invalid XML: {exc}"]
    errors: list[str] = []
    if root.tag != SVG_TAG:
        errors.append(f"{path}: expected SVG root element")
    view_box = root.attrib.get("viewBox", "").split()
    try:
        dimensions = [float(value) for value in view_box]
        if (
            len(dimensions) != 4
            or not all(math.isfinite(value) for value in dimensions)
            or dimensions[2] <= 0
            or dimensions[3] <= 0
        ):
            raise ValueError("non-positive or missing dimensions")
    except ValueError:
        errors.append(f"{path}: invalid viewBox (expected four finite numbers and positive dimensions)")
    return errors


def main() -> int:
    """Check all published dashboard assets before proposing an update."""
    errors = [error for path in ASSETS for error in validate_svg(path)]
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"Validated {len(ASSETS)} generated SVG dashboards.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
