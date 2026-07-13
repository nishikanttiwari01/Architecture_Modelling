"""Validate governed Horizon Bank Markdown catalogues."""

from __future__ import annotations

import re
import sys
import csv
from pathlib import Path

ID_PATTERN = re.compile(r"^HB-[A-Z]+-[0-9]{2,3}$")
REFERENCE_PATTERN = re.compile(r"\bHB-[A-Z]+-[0-9]{2,3}\b")


def read_tables(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for index, line in enumerate(lines):
        if not line.startswith("|"):
            headers = None
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if index + 1 < len(lines) and re.match(r"^\|(?:\s*:?-+:?\s*\|)+$", lines[index + 1]):
            headers = cells
            continue
        if headers and not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            rows.append(dict(zip(headers, cells)))
    return rows


def validate_catalogues(root: Path) -> list[str]:
    errors: list[str] = []
    vocab_rows = read_tables(root / "controlled-vocabularies.md")
    vocab: dict[str, set[str]] = {}
    for row in vocab_rows:
        vocab.setdefault(row.get("Vocabulary", ""), set()).add(row.get("Value", ""))

    records: list[tuple[Path, dict[str, str]]] = []
    for path in sorted(root.glob("*.md")):
        if path.name in {"README.md", "controlled-vocabularies.md"}:
            continue
        for row in read_tables(path):
            if row.get("ID", "").startswith("HB-") or row.get("ID"):
                records.append((path, row))

    ids: set[str] = set()
    for path, row in records:
        identifier = row.get("ID", "")
        label = f"{path.name}:{identifier or '<blank>'}"
        if identifier in ids:
            errors.append(f"{label}: duplicate ID")
        ids.add(identifier)
        if not ID_PATTERN.fullmatch(identifier):
            errors.append(f"{label}: malformed ID")
        if "Definition" in row and not row.get("Definition"):
            errors.append(f"{label}: missing definition")
        if "Owner" in row and not row.get("Owner"):
            errors.append(f"{label}: missing owner")
        status = row.get("Status", "")
        if status and status not in vocab.get("lifecycle_status", set()):
            errors.append(f"{label}: invalid status {status}")
        scope = row.get("Scope", "")
        if scope and scope not in vocab.get("scope", set()):
            errors.append(f"{label}: invalid scope {scope}")
        parent = row.get("Parent ID", "")
        level = row.get("Level", "")
        if path.name == "products.md":
            if level == "1" and parent:
                errors.append(f"{label}: conflicting parent for level 1")
            if level not in {"", "1"} and not parent:
                errors.append(f"{label}: orphan product missing parent")
            if not row.get("Relationships", ""):
                errors.append(f"{label}: orphan product missing relationship")
        if path.name == "value-streams.md" and not row.get("Relationships", ""):
            errors.append(f"{label}: orphan value stream missing relationship")

    for path, row in records:
        identifier = row.get("ID", "")
        searchable = " ".join(value for key, value in row.items() if key != "ID")
        for reference in REFERENCE_PATTERN.findall(searchable):
            if reference not in ids:
                errors.append(f"{path.name}:{identifier}: unknown reference {reference}")

    coverage_path = root / "coverage-matrix.csv"
    if coverage_path.exists():
        coverage_ids: set[str] = set()
        with coverage_path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                identifier = row.get("coverage_id", "").strip()
                label = f"coverage-matrix.csv:{identifier or '<blank>'}"
                if identifier in coverage_ids:
                    errors.append(f"{label}: duplicate ID")
                coverage_ids.add(identifier)
                if not re.fullmatch(r"HB-COV-[0-9]{3}", identifier):
                    errors.append(f"{label}: malformed ID")
                status = row.get("status", "").strip()
                if status and status not in vocab.get("lifecycle_status", set()):
                    errors.append(f"{label}: invalid status {status}")
                for key, value in row.items():
                    if key == "coverage_id" or not value:
                        continue
                    for reference in REFERENCE_PATTERN.findall(value):
                        if reference not in ids:
                            errors.append(f"{label}: unknown reference {reference}")
    return sorted(set(errors))


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "examples" / "horizon-bank"
    errors = validate_catalogues(root)
    if errors:
        print("Horizon Bank catalogue validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Horizon Bank catalogue validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
