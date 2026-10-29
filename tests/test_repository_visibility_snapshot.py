"""Validate the deliberately public, aggregate-only visibility snapshot."""

from __future__ import annotations

import json
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "data" / "repository_visibility_snapshot.json"


class TestRepositoryVisibilitySnapshot(unittest.TestCase):
    """Guard aggregate arithmetic and accidental release of private metadata."""

    def test_snapshot_is_aggregate_only(self) -> None:
        payload: object = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        self.assertIsInstance(payload, dict)
        snapshot: dict[str, object] = payload  # type: ignore[assignment]
        self.assertEqual(set(snapshot), {"schema_version", "captured_on", "source", "scope", "visibility", "archived", "pagination"})
        self.assertEqual(snapshot["schema_version"], 1)
        date.fromisoformat(str(snapshot["captured_on"]))
        for key in ("visibility", "archived"):
            values = snapshot[key]
            self.assertIsInstance(values, dict)
            self.assertEqual(set(values), {"public", "private"})
            self.assertTrue(all(type(number) is int and number >= 0 for number in values.values()))
        visibility = snapshot["visibility"]
        archived = snapshot["archived"]
        pagination = snapshot["pagination"]
        self.assertIsInstance(pagination, dict)
        self.assertEqual(set(pagination), {"page_size", "nonempty_pages", "unique_repository_ids", "next_page_empty"})
        self.assertEqual(sum(visibility.values()), pagination["unique_repository_ids"])
        self.assertTrue(pagination["next_page_empty"])
        for key in ("public", "private"):
            self.assertLessEqual(archived[key], visibility[key])

    def test_public_page_declares_private_limitations(self) -> None:
        page = (ROOT / "STATISTICS.md").read_text(encoding="utf-8")
        self.assertIn("cannot be independently verified", page)
        self.assertIn("data/repository_visibility_snapshot.json", page)


if __name__ == "__main__":
    unittest.main()
