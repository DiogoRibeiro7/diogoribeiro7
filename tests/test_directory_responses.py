"""Offline tests for malformed GitHub directory listing responses."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import generate_portfolio_metrics as portfolio  # noqa: E402


class TestDirectoryResponseValidation(unittest.TestCase):
    """Prevent malformed provider responses from silently lowering coverage."""

    def test_valid_directory_listing(self) -> None:
        """A directory response returns its original entries."""
        entries: list[dict[str, object]] = [{"name": "tests"}, {"name": ".github"}]
        with patch.object(portfolio, "_get_json", return_value=entries):
            self.assertEqual(portfolio._contents("example"), entries)

    def test_empty_directory_is_valid(self) -> None:
        """An explicitly empty JSON array is a valid listing."""
        with patch.object(portfolio, "_get_json", return_value=[]):
            self.assertEqual(portfolio._contents("example"), [])

    def test_non_array_response_is_rejected(self) -> None:
        """An object response must not be mistaken for zero files."""
        with patch.object(portfolio, "_get_json", return_value={"message": "error"}):
            with self.assertRaisesRegex(TypeError, "must be a JSON array"):
                portfolio._contents("example", ".github")

    def test_non_object_entries_are_rejected(self) -> None:
        """A partially malformed listing must fail rather than lose evidence."""
        with patch.object(portfolio, "_get_json", return_value=[{"name": "tests"}, "bad"]):
            with self.assertRaisesRegex(TypeError, "contains invalid entries"):
                portfolio._contents("example")


if __name__ == "__main__":
    unittest.main()
