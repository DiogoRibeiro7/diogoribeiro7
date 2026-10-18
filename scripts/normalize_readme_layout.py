"""Normalize the gap between the profile navigation and introduction.

This script deliberately does not depend on the wording of the introduction.
"""

from __future__ import annotations

import re
from pathlib import Path

README = Path("README.md")
NAV_CLOSE = "</div>"


def normalize_readme(text: str) -> str:
    """Ensure exactly one blank line after the first navigation container.

    The first closing div in this profile belongs to its primary navigation.
    Do not modify the subsequent introduction or any other layout.
    """
    header, separator, remainder = text.partition(NAV_CLOSE)
    if not separator:
        raise ValueError("README primary navigation closing tag is missing")
    if "nav-home-active.svg" not in header:
        raise ValueError("README primary navigation was not found")
    # Only normalize line separators at the navigation boundary.
    return header + separator + "\n\n" + remainder.lstrip("\r\n")


def main() -> None:
    """Normalize the checked-out README in place when necessary."""
    original = README.read_text(encoding="utf-8")
    updated = normalize_readme(original)
    if updated != original:
        README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
