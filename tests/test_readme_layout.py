"""Regression tests for README navigation-to-introduction layout."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from normalize_readme_layout import normalize_readme  # noqa: E402


class TestReadmeLayout(unittest.TestCase):
    """Verify normalization preserves arbitrary introduction prose."""

    NAV = '<div align="center">\n<img src="nav-home-active.svg"/>\n</div>'

    def test_current_intro_is_accepted(self) -> None:
        content = self.NAV + "\n\nOver 20 years in statistical modelling.\n"
        self.assertEqual(normalize_readme(content), content)

    def test_missing_blank_line_is_inserted(self) -> None:
        content = self.NAV + "\nOver 20 years in statistical modelling.\n"
        expected = self.NAV + "\n\nOver 20 years in statistical modelling.\n"
        self.assertEqual(normalize_readme(content), expected)

    def test_extra_newlines_are_normalized(self) -> None:
        content = self.NAV + "\n\n\nIntroduction text.\n"
        expected = self.NAV + "\n\nIntroduction text.\n"
        self.assertEqual(normalize_readme(content), expected)

    def test_missing_navigation_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "navigation"):
            normalize_readme("# README\nIntroduction\n")

    def test_normalization_is_idempotent(self) -> None:
        content = self.NAV + "\nIntroduction text.\n"
        once = normalize_readme(content)
        self.assertEqual(normalize_readme(once), once)

    def test_navigation_replacement_preserves_rewritten_header(self) -> None:
        """Regenerating navigation must not rely on fixed headline wording."""
        from profile_maintenance import replace_nav

        manifest: dict[str, object] = {"navigation": [
            ("Home", "README.md"), ("Featured", "FEATURED.md"),
            ("Projects", "PROJECTS.md"), ("Methods", "METHODS.md"),
            ("Research", "RESEARCH.md"), ("Evidence", "STATISTICS.md"),
        ]}
        old_nav = (
            '<div align="center">\n'
            '  <img src="assets/links/nav-home-active.svg" alt="Home" />\n'
            '</div>\n\n'
        )
        headline = "# Profile\n\nMachine Learning Engineer · Applied Mathematician\n\n"
        intro = "The introduction can change independently of the generator.\n"
        original = headline + old_nav + intro
        updated = replace_nav(original, "README.md", manifest)
        self.assertTrue(updated.startswith(headline))
        self.assertIn(intro, updated)
        self.assertEqual(updated.count('nav-home-active.svg'), 1)
        self.assertEqual(replace_nav(updated, "README.md", manifest), updated)

    def test_navigation_replacement_rejects_absent_block(self) -> None:
        """Fail explicitly instead of inserting navigation at an arbitrary point."""
        from profile_maintenance import replace_nav

        manifest: dict[str, object] = {"navigation": [
            ("Home", "README.md"), ("Featured", "FEATURED.md"),
            ("Projects", "PROJECTS.md"), ("Methods", "METHODS.md"),
            ("Research", "RESEARCH.md"), ("Evidence", "STATISTICS.md"),
        ]}
        with self.assertRaisesRegex(ValueError, "exactly one README navigation block"):
            replace_nav("# Profile\n\nNo navigation.\n", "README.md", manifest)


if __name__ == "__main__":
    unittest.main()
