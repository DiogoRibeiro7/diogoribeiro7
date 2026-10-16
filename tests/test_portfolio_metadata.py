"""Contract tests for non-empty portfolio metadata values."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_portfolio_schema import validate_node  # noqa: E402


class TestPortfolioMetadata(unittest.TestCase):
    """Reject blank metadata without changing valid portfolio classifications."""

    @classmethod
    def setUpClass(cls) -> None:
        """Read the same schema used by the profile integrity workflow."""
        cls.schema: dict[str, Any] = json.loads(
            (ROOT / "data" / "portfolio.schema.json").read_text(encoding="utf-8")
        )

    def test_blank_project_summary_is_rejected(self) -> None:
        """Whitespace-only project summaries are not meaningful evidence."""
        project: dict[str, Any] = {
            "repo": "example-repo",
            "title": "Example",
            "category": "Research software",
            "maturity": "research software",
            "real_data": False,
            "research_software": True,
            "summary": "  \t  ",
        }
        errors = validate_node(
            project, self.schema["$defs"]["project"], self.schema, "$.projects[0]"
        )
        self.assertTrue(any("$.projects[0].summary" in error for error in errors))

    def test_blank_case_study_outcome_is_rejected(self) -> None:
        """A case study needs a substantive outcome field."""
        case: dict[str, Any] = {
            "repo": "example-repo",
            "domain": "Health",
            "title": "Example",
            "problem": "A question",
            "constraints": "Time",
            "method": "Regression",
            "outcome": "   ",
        }
        errors = validate_node(
            case, self.schema["$defs"]["caseStudy"], self.schema, "$.case_studies[0]"
        )
        self.assertTrue(any("$.case_studies[0].outcome" in error for error in errors))

    def test_valid_metadata_passes(self) -> None:
        """Ordinary descriptions and classification strings remain accepted."""
        for value in ("Research software", "Model validated with data.", "  An outcome  "):
            with self.subTest(value=value):
                self.assertEqual(
                    validate_node(
                        value, self.schema["$defs"]["nonEmptyString"], self.schema
                    ),
                    [],
                )


if __name__ == "__main__":
    unittest.main()
