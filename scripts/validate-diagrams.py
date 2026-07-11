#!/usr/bin/env python3
"""Validate diagram repository conventions."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    "diagrams/specifications",
    "diagrams/styles",
    "diagrams/lib",
    "diagrams/lib/C4-PlantUML",
    "diagrams/source/plantuml",
    "diagrams/source/mermaid",
    "diagrams/source/bpmn",
    "diagrams/source/dmn",
    "diagrams/source/drawio",
    "diagrams/source/archimate",
    "diagrams/exported/svg",
    "diagrams/exported/png",
]

REQUIRED_FILES = [
    "templates/diagram-specification-template.md",
    "diagrams/styles/plantuml-theme.puml",
    "diagrams/styles/diagram-style-guide.md",
    "diagrams/specifications/README.md",
    "diagrams/source/bpmn/README.md",
    "diagrams/source/dmn/README.md",
    "diagrams/lib/C4-PlantUML/README.md",
]

SPEC_REQUIRED_HEADINGS = [
    "## Purpose",
    "## Audience",
    "## Question answered",
    "## Notation",
    "## Required elements",
    "## Required relationships",
    "## Main flow or structure",
    "## Alternative and exception flows",
    "## Scope",
    "## Exclusions",
    "## Accessibility requirements",
    "## Source references",
    "## Review criteria",
]

FIG_ID = re.compile(r"FIG-\d{2}-\d{2}")


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_DIRS:
        if not (ROOT / relative).is_dir():
            errors.append(f"missing directory: {relative}")

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty file: {relative}")

    for spec in (ROOT / "diagrams/specifications").glob("FIG-*.md"):
        text = spec.read_text(encoding="utf-8")
        first_line = text.splitlines()[0] if text.splitlines() else ""
        if not first_line.startswith("# FIG-") or not FIG_ID.search(first_line):
            errors.append(f"{spec.relative_to(ROOT)}: first heading must start with figure ID")
        for heading in SPEC_REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{spec.relative_to(ROOT)}: missing heading {heading}")
        approval_status_text = re.sub(r"\bapproved change\b", "change", text, flags=re.I)
        if re.search(r"\bApproved\b", approval_status_text, re.I):
            errors.append(
                f"{spec.relative_to(ROOT)}: do not use 'Approved' in specs unless the author has explicitly approved it"
            )

    for puml in (ROOT / "diagrams/source/plantuml").rglob("*.puml"):
        text = puml.read_text(encoding="utf-8")
        if "!includeurl" in text.lower():
            errors.append(f"{puml.relative_to(ROOT)}: unversioned !includeurl is not allowed")

    if errors:
        print("Diagram validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Diagram validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
