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
    _render_reproducibility_index,
    _tree_files,
    ReproductionReference,
    _audit_repo,
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

    def test_reproducibility_index_links_to_concrete_source(self) -> None:
        evidence = (
            RepoEvidence(
                "repo-a", True, True, True, True, True,
                "examples/reproduce_table.py", "Reproduction script", "Needs inputs",
            ),
            RepoEvidence("repo-b", True, False, True, False, False),
        )
        rendered = _render_reproducibility_index(
            AuditResult(("repo-a", "repo-b"), evidence, 1, 1)
        )
        self.assertIn(
            "repo-a/blob/main/examples/reproduce_table.py", rendered
        )
        self.assertIn("Not yet curated", rendered)
        self.assertIn("Needs inputs", rendered)

    def test_audit_uses_verified_file_not_directory_name(self) -> None:
        """A directory alone must not meet the evidence requirement."""
        from unittest.mock import patch

        with patch(
            "generate_portfolio_metrics._tree_files",
            return_value={
                ".github/workflows/ci.yml", "tests/test_example.py",
                "docs/index.md", "CITATION.cff", "examples/experiment.py",
            },
        ):
            actual = _audit_repo(
                "repo-a",
                ReproductionReference("examples/experiment.py", "Experiment", "Synthetic"),
            )
            self.assertTrue(actual.has_reproducibility_assets)
            self.assertTrue(actual.has_ci)
            self.assertTrue(actual.has_tests)
            self.assertTrue(actual.has_docs)

            with self.assertRaisesRegex(ValueError, "artifact missing"):
                _audit_repo(
                    "repo-a",
                    ReproductionReference("data/.gitkeep", "Placeholder", "none"),
                )
            self.assertFalse(_audit_repo("repo-a").has_reproducibility_assets)

    def test_tree_excludes_empty_placeholder_files(self) -> None:
        """The recursive tree audit ignores tracked empty placeholders."""
        from unittest.mock import patch

        payload = {
            "truncated": False,
            "tree": [
                {"path": "data/.gitkeep", "type": "blob", "size": 0},
                {"path": "examples/run.py", "type": "blob", "size": 123},
                {"path": "docs", "type": "tree"},
            ],
        }
        with patch("generate_portfolio_metrics._get_json", return_value=payload):
            self.assertEqual(_tree_files("repo-a"), {"examples/run.py"})

        payload["truncated"] = True
        with patch("generate_portfolio_metrics._get_json", return_value=payload):
            with self.assertRaisesRegex(ValueError, "truncated"):
                _tree_files("repo-a")


if __name__ == "__main__":
    unittest.main()
