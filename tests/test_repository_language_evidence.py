"""Offline regression checks for aggregate-only language evidence."""

from __future__ import annotations

import json
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from refresh_repository_inventory import (  # noqa: E402
    LANGUAGES,
    VISIBILITY,
    render_radar,
    validate_snapshots,
)


class TestRepositoryLanguageEvidence(unittest.TestCase):
    """Verify denominators, privacy boundaries and deterministic rendering."""

    def setUp(self) -> None:
        self.languages = json.loads(LANGUAGES.read_text(encoding="utf-8"))
        self.visibility = json.loads(VISIBILITY.read_text(encoding="utf-8"))

    def test_counts_match_full_inventory(self) -> None:
        counts = validate_snapshots(self.languages, self.visibility)
        self.assertEqual(sum(counts.values()), 504)
        self.assertEqual(counts["Python"], 311)

    def test_private_snapshot_contains_only_aggregate_counts(self) -> None:
        self.assertEqual(
            set(self.languages),
            {"schema_version", "captured_on", "source", "scope", "public", "private"},
        )
        self.assertTrue(all(isinstance(v, int) for v in self.languages["private"].values()))

    def test_mismatch_fails(self) -> None:
        self.visibility["visibility"]["private"] += 1
        with self.assertRaises(ValueError):
            validate_snapshots(self.languages, self.visibility)

    def test_svg_is_valid_deterministic(self) -> None:
        counts = validate_snapshots(self.languages, self.visibility)
        svg = render_radar(counts, sum(counts.values()))
        self.assertEqual(svg, render_radar(counts, sum(counts.values())))
        ET.fromstring(svg)
        self.assertIn("not proficiency", svg)


if __name__ == "__main__":
    unittest.main()
