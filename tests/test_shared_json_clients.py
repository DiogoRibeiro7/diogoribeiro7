"""Offline regression tests for the shared API clients used by profile metrics."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import generate_portfolio_metrics as portfolio  # noqa: E402
import generate_star_metrics as stars  # noqa: E402


class TestSharedJsonClients(unittest.TestCase):
    """Check decoding, HTTP handling and delegation to the shared client."""

    def test_both_clients_decode_json(self) -> None:
        for module in (portfolio, stars):
            with self.subTest(module=module.__name__):
                with patch.object(module, "get", return_value=(200, b'{"value": 3}')) as fetch:
                    self.assertEqual(module._get_json("https://api.github.com/example"), {"value": 3})
                    fetch.assert_called_once_with(
                        "https://api.github.com/example", attempts=4
                    )

    def test_both_clients_reject_non_success_status(self) -> None:
        for module in (portfolio, stars):
            with self.subTest(module=module.__name__):
                with patch.object(module, "get", return_value=(206, b"{}")):
                    with self.assertRaisesRegex(RuntimeError, "Unexpected HTTP 206"):
                        module._get_json("https://api.github.com/example")

    def test_both_clients_reject_invalid_json(self) -> None:
        for module in (portfolio, stars):
            with self.subTest(module=module.__name__):
                with patch.object(module, "get", return_value=(200, b"invalid")):
                    with self.assertRaises(ValueError):
                        module._get_json("https://api.github.com/example")

    def test_both_clients_propagate_transport_failure(self) -> None:
        for module in (portfolio, stars):
            with self.subTest(module=module.__name__):
                with patch.object(module, "get", side_effect=RuntimeError("rate limited")):
                    with self.assertRaisesRegex(RuntimeError, "rate limited"):
                        module._get_json("https://api.github.com/example")


if __name__ == "__main__":
    unittest.main()
