"""Offline regression tests for generated portfolio evidence.

Run with: python -m unittest discover -s tests -v
"""

from __future__ import annotations

import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_portfolio_metrics import (  # noqa: E402
    AuditResult,
    RepoEvidence,
    _coverage,
    _render_controls_table,
    _render_svg,
    _replace_controls,
)


def sample_audit() -> AuditResult:
    """Build a synthetic audit without making GitHub API requests."""
    evidence = (
        RepoEvidence("repo-a", True, True, True, True, True),
        RepoEvidence("repo-b", True, False, True, False, False),
    )
    return AuditResult(("repo-a", "repo-b"), evidence, 1, 1)


class TestPortfolioMetrics(unittest.TestCase):
    """Test the deterministic rendering and marker replacement contract."""

    def test_coverage_uses_expected_denominator(self) -> None:
        self.assertEqual(_coverage(1, 2), "1 / 2 (50%)")

    def test_controls_table_matches_synthetic_audit(self) -> None:
        table = _render_controls_table(sample_audit())
        self.assertIn("| CI workflow present | **2 / 2 (100%)** |", table)
        self.assertIn("| Automated-test marker present | **1 / 2 (50%)** |", table)
        self.assertIn("| Citation / archive metadata | **1 / 2 (50%)** |", table)

    def test_svg_is_valid_and_deterministic(self) -> None:
        result = sample_audit()
        first = _render_svg(result)
        self.assertEqual(first, _render_svg(result))
        root = ET.fromstring(first)
        self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
        self.assertIn("2 flagship repositories", first)
        self.assertIn("1/2 · 50%", first)

    def test_marker_replacement_preserves_unrelated_content(self) -> None:
        old = "Before\n<!-- statistics:controls:start -->\nOld\n<!-- statistics:controls:end -->\nAfter"
        updated = _replace_controls(old, _render_controls_table(sample_audit()))
        self.assertTrue(updated.startswith("Before\n"))
        self.assertTrue(updated.endswith("\nAfter"))
        self.assertNotIn("\nOld\n", updated)

    def test_marker_replacement_rejects_missing_or_duplicate_blocks(self) -> None:
        valid = "<!-- statistics:controls:start -->old<!-- statistics:controls:end -->"
        for invalid in ("No markers", valid + "\n" + valid):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    _replace_controls(invalid, "updated")


if __name__ == "__main__":
    unittest.main()
