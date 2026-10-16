"""Offline HTTP retry regression tests for public inventory checks."""

from __future__ import annotations

import io
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_external_inventory as inventory  # noqa: E402


class TestInventoryRequests(unittest.TestCase):
    """Verify transient failures are distinguished from real broken links."""

    @patch.object(inventory.urllib.request, "urlopen")
    def test_success(self, open_url: MagicMock) -> None:
        response = MagicMock()
        response.__enter__.return_value = response
        response.status = 200
        response.read.return_value = b'{"ok": true}'
        open_url.return_value = response
        self.assertEqual(inventory.get("https://api.github.com/example"), (200, b'{"ok": true}'))

    @patch.object(inventory.time, "sleep")
    @patch.object(inventory.urllib.request, "urlopen")
    def test_transient_failure_recovers(self, open_url: MagicMock, sleep: MagicMock) -> None:
        response = MagicMock()
        response.__enter__.return_value = response
        response.status = 200
        response.read.return_value = b"ok"
        open_url.side_effect = [
            urllib.error.HTTPError("https://example.com", 503, "unavailable", {}, None),
            response,
        ]
        self.assertEqual(inventory.get("https://example.com"), (200, b"ok"))
        sleep.assert_called_once_with(2.0)

    @patch.object(inventory.time, "sleep")
    @patch.object(inventory.urllib.request, "urlopen")
    def test_missing_resource_fails_without_retry(self, open_url: MagicMock, sleep: MagicMock) -> None:
        open_url.side_effect = urllib.error.HTTPError("https://example.com", 404, "missing", {}, None)
        with self.assertRaisesRegex(RuntimeError, "HTTP 404"):
            inventory.get("https://example.com")
        self.assertEqual(open_url.call_count, 1)
        sleep.assert_not_called()

    @patch.object(inventory.time, "sleep")
    @patch.object(inventory.urllib.request, "urlopen")
    def test_rate_limit_retry_after_is_capped(self, open_url: MagicMock, sleep: MagicMock) -> None:
        open_url.side_effect = urllib.error.HTTPError(
            "https://example.com", 429, "limited", {"Retry-After": "120"}, None
        )
        with self.assertRaisesRegex(RuntimeError, "after 2 attempts"):
            inventory.get("https://example.com", attempts=2)
        sleep.assert_called_once_with(60.0)

    def test_invalid_attempt_count(self) -> None:
        with self.assertRaises(ValueError):
            inventory.get("https://example.com", attempts=0)


if __name__ == "__main__":
    unittest.main()
