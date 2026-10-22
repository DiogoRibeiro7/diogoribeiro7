"""Offline regression tests for GitHub recursive-tree audit responses.

The flagship audit queries the Git tree API rather than shallow directory
listings. Invalid or truncated responses must fail closed instead of
silently lowering coverage.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import generate_portfolio_metrics as portfolio  # noqa: E402


class TestTreeResponseValidation(unittest.TestCase):
    """Check type and completeness constraints for remote tree responses."""

    def test_valid_tree_returns_nonempty_tracked_files(self) -> None:
        """The audit counts files, not directories or empty placeholders."""
        payload: dict[str, Any] = {
            "truncated": False,
            "tree": [
                {"path": "tests", "type": "tree"},
                {"path": "tests/test_example.py", "type": "blob", "size": 123},
                {"path": "data/.gitkeep", "type": "blob", "size": 0},
                {"path": "examples/study.R", "type": "blob", "size": 456},
            ],
        }
        with patch.object(portfolio, "_get_json", return_value=payload) as getter:
            files = portfolio._tree_files("example")
        self.assertEqual(files, {"tests/test_example.py", "examples/study.R"})
        getter.assert_called_once_with(
            "https://api.github.com/repos/DiogoRibeiro7/example/"
            "git/trees/main?recursive=1"
        )

    def test_empty_tree_is_valid(self) -> None:
        """An explicitly complete empty tree is a valid zero-file response."""
        with patch.object(
            portfolio, "_get_json", return_value={"truncated": False, "tree": []}
        ):
            self.assertEqual(portfolio._tree_files("example"), set())

    def test_non_array_tree_is_rejected(self) -> None:
        """An API error object must not be interpreted as an empty file set."""
        for malformed in (
            {"message": "error"},
            {"truncated": False, "tree": {"path": "example"}},
            {"truncated": False, "tree": None},
        ):
            with self.subTest(payload=malformed):
                with patch.object(portfolio, "_get_json", return_value=malformed):
                    with self.assertRaisesRegex(TypeError, "must contain a tree array"):
                        portfolio._tree_files("example")

    def test_invalid_tree_entries_are_rejected(self) -> None:
        """A partially malformed tree must fail, not silently lose evidence."""
        base: dict[str, Any] = {"truncated": False}
        for entries in (
            ["not an object"],
            [{"path": "src/example.py", "type": "blob", "size": "100"}],
            [{"path": None, "type": "blob", "size": 100}],
            [{"path": "src/example.py", "type": "blob", "size": -1}],
        ):
            with self.subTest(entries=entries):
                with patch.object(
                    portfolio, "_get_json", return_value={**base, "tree": entries}
                ):
                    with self.assertRaises(TypeError):
                        portfolio._tree_files("example")

    def test_truncated_or_unconfirmed_tree_is_rejected(self) -> None:
        """Do not trust incomplete responses, including missing status."""
        for payload in (
            {"truncated": True, "tree": []},
            {"tree": []},
        ):
            with self.subTest(payload=payload):
                with patch.object(portfolio, "_get_json", return_value=payload):
                    with self.assertRaisesRegex(ValueError, "truncated"):
                        portfolio._tree_files("example")


if __name__ == "__main__":
    unittest.main()
