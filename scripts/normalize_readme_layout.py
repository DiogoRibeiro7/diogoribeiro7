from pathlib import Path

README = Path("README.md")
NAV_END = "</div>"
INTRO = "I build data and AI systems"

text = README.read_text(encoding="utf-8")
needle = f"{NAV_END}{INTRO}"
replacement = f"{NAV_END}\n\n{INTRO}"

if needle in text:
    text = text.replace(needle, replacement, 1)

if f"{NAV_END}\n\n{INTRO}" not in text:
    raise SystemExit("README navigation is not separated from the introduction by a blank line")

README.write_text(text, encoding="utf-8")
