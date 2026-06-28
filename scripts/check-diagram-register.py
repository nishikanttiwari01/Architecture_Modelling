#!/usr/bin/env python3
"""Validate DIAGRAM_REGISTER.md entries."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "DIAGRAM_REGISTER.md"
VALID_STATUSES = {"Planned", "Drafting", "Review", "Approved", "Exported", "Deprecated"}
FIG_ID = re.compile(r"^FIG-(\d{2})-(\d{2})$")


def parse_rows() -> list[list[str]]:
    rows: list[list[str]] = []
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| FIG-"):
            continue
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def existing_path(value: str) -> bool:
    if value in {"", "Pending", "-"}:
        return False
    return (ROOT / value).exists()


def main() -> int:
    errors: list[str] = []
    seen: set[str] = set()

    for row in parse_rows():
        if len(row) != 10:
            errors.append(f"register row has {len(row)} cells, expected 10: {row}")
            continue

        figure_id, chapter, _title, _purpose, _audience, _notation, source, export, status, _owner = row

        match = FIG_ID.match(figure_id)
        if not match:
            errors.append(f"{figure_id}: invalid figure ID")
            continue

        if figure_id in seen:
            errors.append(f"{figure_id}: duplicate figure ID")
        seen.add(figure_id)

        if int(match.group(1)) != int(chapter):
            errors.append(f"{figure_id}: chapter column {chapter} does not match figure ID")

        if status not in VALID_STATUSES:
            errors.append(f"{figure_id}: invalid status {status!r}")

        if status in {"Review", "Approved", "Exported"}:
            if not existing_path(source):
                errors.append(f"{figure_id}: status {status} requires existing source file")
            if not existing_path(export):
                errors.append(f"{figure_id}: status {status} requires existing export file")

        if status == "Approved":
            errors.append(f"{figure_id}: Codex must not mark diagrams Approved")

    if errors:
        print("Diagram register check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Diagram register check passed. Checked {len(seen)} figure entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
