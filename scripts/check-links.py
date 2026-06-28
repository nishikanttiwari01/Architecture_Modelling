#!/usr/bin/env python3
"""Check local Markdown links and image references. External URLs are not fetched."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def normalise_target(raw: str) -> str:
    raw = raw.strip().split()[0].strip("<>")
    return unquote(raw.split("#", 1)[0])


def main() -> int:
    failures = []
    checked = 0
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "build", "dist"} for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = normalise_target(match.group(1))
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            path = (md.parent / target).resolve()
            try:
                path.relative_to(ROOT.resolve())
            except ValueError:
                failures.append((md, target, "points outside repository"))
                continue
            if not path.exists():
                failures.append((md, target, "not found"))
    print(f"Checked {checked} local Markdown links.")
    if failures:
        for md, target, reason in failures:
            print(f"ERROR: {md.relative_to(ROOT)} -> {target} ({reason})")
        return 1
    print("All local links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
