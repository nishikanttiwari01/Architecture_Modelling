#!/usr/bin/env python3
"""Report Markdown word counts by chapter and total."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"


def count_words(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))


def main() -> None:
    files = sorted(MANUSCRIPT.rglob("*.md"))
    total = 0
    print(f"{'Words':>8}  File")
    print("-" * 72)
    for path in files:
        words = count_words(path.read_text(encoding="utf-8"))
        total += words
        print(f"{words:8d}  {path.relative_to(ROOT)}")
    print("-" * 72)
    print(f"{total:8d}  TOTAL")


if __name__ == "__main__":
    main()
