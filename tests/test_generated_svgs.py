"""Offline regression tests for generated SVG structure validation."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_generated_svgs import validate_svg  # noqa: E402


class TestSvgValidation(unittest.TestCase):
    """Check valid SVGs and malformed asset failure modes."""

    def assert_svg_errors(self, markup: str, expected: str | None) -> None:
        """Validate one temporary file without changing repository assets."""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "dashboard.svg"
            path.write_text(markup, encoding="utf-8")
            errors = validate_svg(path)
            if expected is None:
                self.assertEqual(errors, [])
            else:
                self.assertTrue(
                    any(expected in error for error in errors), errors
                )

    def test_valid_svg(self) -> None:
        self.assert_svg_errors(
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 400"/>',
            None,
        )

    def test_malformed_xml(self) -> None:
        self.assert_svg_errors(
            '<svg xmlns="http://www.w3.org/2000/svg"><rect>',
            "unreadable or invalid XML",
        )

    def test_wrong_root(self) -> None:
        self.assert_svg_errors("<html viewBox='0 0 900 400'/>", "expected SVG root")

    def test_invalid_viewbox(self) -> None:
        for view_box in ("", "0 0 900", "0 0 zero 400", "0 0 0 400", "0 0 900 -2"):
            with self.subTest(view_box=view_box):
                self.assert_svg_errors(
                    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}"/>',
                    "invalid viewBox",
                )

    def test_missing_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "not-found.svg"
            self.assertTrue(
                any("unreadable or invalid XML" in e for e in validate_svg(path))
            )


if __name__ == "__main__":
    unittest.main()
