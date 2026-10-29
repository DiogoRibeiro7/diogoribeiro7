"""Regression coverage for the catalogue-derived evidence radar."""

from __future__ import annotations

import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from generate_evidence_radar import aggregate_topics, render_svg  # noqa: E402
from generate_topic_statistics import TOPIC_LABELS, count_topics  # noqa: E402


class TestEvidenceRadar(unittest.TestCase):
    """Ensure counts are exhaustive, deterministic and XML-safe."""

    def test_all_entries_counted_once(self) -> None:
        source = Path(__file__).resolve().parents[1] / "PROJECTS.md"
        topics = count_topics(source.read_text(encoding="utf-8"))
        axes = aggregate_topics(topics)
        self.assertEqual(sum(axes.values()), sum(topics.values()))
        self.assertEqual(len(axes), 6)

    def test_missing_or_invalid_counts_rejected(self) -> None:
        with self.assertRaises(ValueError):
            aggregate_topics({})
        with self.assertRaises(ValueError):
            aggregate_topics({key: -1 for key in TOPIC_LABELS})

    def test_svg_is_valid_and_deterministic(self) -> None:
        values = aggregate_topics({key: 2 for key in TOPIC_LABELS})
        svg = render_svg(values)
        self.assertEqual(svg, render_svg(values))
        ET.fromstring(svg)
        self.assertIn("not skill level", svg)

    def test_empty_radar_rejected(self) -> None:
        values = aggregate_topics({key: 0 for key in TOPIC_LABELS})
        with self.assertRaises(ValueError):
            render_svg(values)


if __name__ == "__main__":
    unittest.main()
