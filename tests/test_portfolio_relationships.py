"""Offline tests for canonical portfolio uniqueness and foreign keys."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_portfolio_schema import (  # noqa: E402
    validate_references,
    validate_uniqueness,
)


class TestPortfolioRelationships(unittest.TestCase):
    """Enforce integrity without external services."""

    def test_valid_references(self) -> None:
        manifest = {
            "projects": [{"repo": "alpha"}],
            "outputs": [{"repo": "alpha"}],
            "case_studies": [{"repo": "alpha"}],
        }
        self.assertEqual(validate_references(manifest), [])

    def test_orphan_output(self) -> None:
        manifest = {
            "projects": [{"repo": "alpha"}],
            "outputs": [{"repo": "missing"}],
            "case_studies": [],
        }
        self.assertEqual(
            validate_references(manifest),
            ["$.outputs[0].repo: 'missing' is not in $.projects"],
        )

    def test_orphan_case_study(self) -> None:
        manifest = {
            "projects": [{"repo": "alpha"}],
            "outputs": [],
            "case_studies": [{"repo": "missing"}],
        }
        self.assertEqual(
            validate_references(manifest),
            ["$.case_studies[0].repo: 'missing' is not in $.projects"],
        )

    def test_duplicate_project_is_detected(self) -> None:
        manifest = {
            "projects": [{"repo": "alpha"}, {"repo": "alpha"}],
            "outputs": [],
            "case_studies": [],
        }
        self.assertIn(
            "$.projects: repository names must be unique",
            validate_uniqueness(manifest),
        )


if __name__ == "__main__":
    unittest.main()
