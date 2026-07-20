"""Validate governed Horizon Bank catalogues and their explicit relationships."""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ID_PATTERN = re.compile(r"^HB-([A-Z]+)-([0-9]{2,3})$")
REFERENCE_PATTERN = re.compile(r"\bHB-[A-Z]+-[0-9]{2,3}\b")
ABBREVIATED_PATTERN = re.compile(r"(?<!HB-)\b(?:VS|PRD|PROC|ORG|DATA|SOR|ACC|CTRL|CRIT|BIAN|SCN)-\d{2,3}\b")
RANGE_PATTERN = re.compile(r"\bHB-[A-Z]+-\d{2,3}\s+(?:to|through|[-–])\s*(?:HB-[A-Z]+-)?\d{2,3}\b", re.I)

PREFIX_BY_FILE = {
    "accounting-events.md": "ACC", "assumptions.md": "ASM", "bank-profile.md": "BANK",
    "bian-mapping-register.md": "BIAN", "business-domains.md": "DOM", "business-lines.md": "BL",
    "capabilities.md": "CAP", "applications.md": "APP", "interfaces.md": "INT",
    "external-networks.md": "EXT", "reconciliations.md": "REC", "technology-resilience.md": "TECH",
    "controls.md": "CTRL",
    "critical-operations.md": "CRIT", "customer-segments.md": "SEG", "data-domains.md": "DATA",
    "legal-entities.md": "LE", "organisation-and-roles.md": "ORG", "processes.md": "PROC",
    "products.md": "PRD", "scenario-catalogue.md": "SCN", "systems-of-record.md": "SOR",
    "value-streams.md": "VS",
}
ALLOWED_PREFIXES = set(PREFIX_BY_FILE.values()) | {"COV", "CAP", "APP", "INT", "EXT", "REC", "TECH"}
REQUIRED_FOUNDATION_CATALOGUES = {
    "business-domains.md", "capabilities.md", "applications.md", "interfaces.md",
    "external-networks.md", "reconciliations.md", "technology-resilience.md",
}
RELATIONSHIP_TARGETS = {
    "DOM": {"BL", "CAP", "ORG", "PRD", "PROC", "VS"},
    "CAP": {"BL", "CAP", "DOM", "ORG", "PRD", "PROC", "VS"},
    "APP": {"CAP", "DATA", "DOM", "INT", "ORG", "PRD", "SOR", "TECH", "VS"},
    "INT": {"APP", "DATA", "EXT", "PRD", "PROC", "VS"},
    "EXT": {"APP", "INT", "PRD", "VS"},
    "REC": {"ACC", "APP", "CRIT", "CTRL", "DATA", "EXT", "INT", "PRD", "PROC", "SCN", "SOR", "VS"},
    "TECH": {"ACC", "APP", "CAP", "CRIT", "CTRL", "DATA", "DOM", "EXT", "INT", "PRD", "PROC", "REC", "SCN", "SOR", "VS"},
    "BL": {"PRD", "VS"}, "PRD": {"PRD", "VS"}, "VS": {"BL", "PRD", "PROC", "VS"},
    "PROC": {"CAP", "DOM", "ORG", "PROC", "VS"},
    "DATA": {"APP", "CAP", "DOM", "INT", "PRD", "REC", "SOR", "TECH", "VS"},
    "SOR": {"APP", "DATA", "PRD", "REC", "TECH"}, "ACC": {"APP", "DATA", "PRD", "REC", "SOR", "TECH", "VS"},
    "CTRL": {"ACC", "APP", "CAP", "CRIT", "DATA", "DOM", "EXT", "INT", "PROC", "REC", "SCN", "SOR", "TECH", "VS"},
    "CRIT": {"APP", "CAP", "CTRL", "DATA", "DOM", "EXT", "INT", "PRD", "PROC", "REC", "SCN", "SOR", "TECH", "VS"},
    "BIAN": {"PRD", "VS", "PROC", "CAP"},
    "SCN": {"ACC", "APP", "BIAN", "CAP", "CRIT", "CTRL", "DATA", "DOM", "EXT", "INT", "ORG", "PRD", "PROC", "REC", "SOR", "TECH", "VS"},
    "ORG": {"BANK", "BL", "CAP", "DOM", "PROC", "VS"}, "SEG": {"PRD", "BL"}, "LE": {"BANK", "BL", "LE"},
}
REQUIRED = {name: {"ID", "Name", "Definition", "Owner", "Record Status"} for name in PREFIX_BY_FILE}
for name in REQUIRED:
    if name in {"business-lines.md", "products.md", "value-streams.md", "processes.md"}:
        REQUIRED[name].add("Relationships")
REQUIRED["assumptions.md"] = {"ID", "Assumption", "Owner"}
REQUIRED["business-domains.md"] = {
    "ID", "Name", "Definition", "Level", "Parent ID", "Owner", "Record Status",
    "Architecture State", "Relationships", "Source Type", "Confidence", "Verification Status", "Gap",
}
REQUIRED["capabilities.md"] = set(REQUIRED["business-domains.md"])
REQUIRED["bian-mapping-register.md"].update({"Confidence", "Verification Status"})
REQUIRED["applications.md"] = {
    "ID", "Name", "Definition", "Responsibility Family", "Owner", "Ownership Type",
    "Business Responsibilities", "Product and Value Stream Relationships", "Data Domain Relationships",
    "Data Authority Role", "System-of-Record Relationships", "Interface Relationships",
    "Architecture State", "Record Status", "Resilience Class", "Source Type", "Gap",
}
REQUIRED["interfaces.md"] = {
    "ID", "Name", "Definition", "Type", "Direction", "Producer Application",
    "Consumer Application", "Information", "Security Classification", "Owner",
    "Architecture State", "Record Status", "Source Type", "Gap",
}
REQUIRED["external-networks.md"] = {
    "ID", "Name", "Definition", "Network Class", "Connectivity Purpose", "Owner",
    "Connected Applications", "Interface Relationships", "Architecture State", "Record Status",
    "Source Type", "Confidence", "Verification Status", "Gap",
}
REQUIRED["reconciliations.md"] = {
    "ID", "Name", "Definition", "Reconciliation Type", "Compared Record A", "Compared Record B",
    "Trigger or Cadence", "Owner", "Exception Owner", "Record Status", "Architecture State",
    "Relationships", "Source Type", "Confidence", "Verification Status", "Gap",
}
REQUIRED["technology-resilience.md"] = {
    "ID", "Name", "Definition", "Technology Class", "Resilience Class", "Continuity Focus",
    "Recovery Authority", "Owner", "Record Status", "Architecture State", "Relationships",
    "Source Type", "Confidence", "Verification Status", "Gap",
}
CONTROLLED_FIELDS = {
    "Record Status": "record_status", "Architecture State": "architecture_state",
    "Source Type": "source_type", "Confidence": "confidence",
    "Verification Status": "verification_status", "Organisational Scope": "organisational_scope",
    "Legal Entity Scope": "legal_entity_scope", "Jurisdiction Scope": "jurisdiction_scope",
    "Segment Scope": "customer_segment_scope", "Ownership Type": "ownership_type",
}
FILE_CONTROLLED_FIELDS = {
    "applications.md": {"Resilience Class": "application_resilience_tier"},
    "interfaces.md": {"Type": "interface_type", "Security Classification": "security_classification"},
    "technology-resilience.md": {"Technology Class": "technology_class", "Resilience Class": "resilience_class"},
}
COVERAGE_COLUMNS = [
    "coverage_id", "business_domain", "business_line", "legal_entity", "segment", "product", "value_stream",
    "capability", "process", "organisation", "application", "authoritative_data/system_of_record",
    "interface", "external_network", "accounting_event", "reconciliation", "control",
    "critical_operation", "technology_or_resilience_classification", "bian_mapping", "scenario",
    "chapter", "status", "gap",
]


def read_tables(path: Path, errors: list[str]) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    rows, headers = [], None
    for index, line in enumerate(lines):
        if not line.startswith("|"):
            headers = None
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if index + 1 < len(lines) and re.match(r"^\|(?:\s*:?-+:?\s*\|)+$", lines[index + 1]):
            headers = cells
            for column, count in Counter(headers).items():
                if count > 1:
                    errors.append(f"{path.name}: duplicate column {column}")
            continue
        if headers and not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            if len(cells) != len(headers):
                errors.append(f"{path.name}:{index + 1}: table row width {len(cells)} does not match {len(headers)}")
            rows.append(dict(zip(headers, cells)))
    return rows


def validate_catalogues(root: Path) -> list[str]:
    errors: list[str] = []
    for filename in sorted(REQUIRED_FOUNDATION_CATALOGUES):
        if not (root / filename).exists():
            errors.append(f"missing required catalogue {filename}")
    vocab: dict[str, set[str]] = {}
    vocab_path = root / "controlled-vocabularies.md"
    if vocab_path.exists():
        for row in read_tables(vocab_path, errors):
            vocab.setdefault(row.get("Vocabulary", ""), set()).add(row.get("Value", ""))

    records: list[tuple[Path, dict[str, str]]] = []
    for filename, expected in PREFIX_BY_FILE.items():
        path = root / filename
        if not path.exists():
            continue
        rows = read_tables(path, errors)
        if rows:
            columns = set(rows[0])
            for column in sorted(REQUIRED[filename] - columns):
                errors.append(f"{filename}: missing required column {column}")
        for row in rows:
            identifier = row.get("ID", "")
            if identifier:
                records.append((path, row))
                match = ID_PATTERN.fullmatch(identifier)
                if match and match.group(1) != expected:
                    errors.append(f"{filename}:{identifier}: expected prefix HB-{expected}")

    ids: set[str] = set()
    by_id = {row.get("ID", ""): row for _, row in records}
    for path, row in records:
        identifier = row.get("ID", "")
        label = f"{path.name}:{identifier or '<blank>'}"
        if identifier in ids:
            errors.append(f"{label}: duplicate ID")
        ids.add(identifier)
        match = ID_PATTERN.fullmatch(identifier)
        if not match or match.group(1) not in ALLOWED_PREFIXES:
            errors.append(f"{label}: malformed ID")
        if "Definition" in row and not row.get("Definition"):
            errors.append(f"{label}: missing definition")
        if "Owner" in row and not row.get("Owner"):
            errors.append(f"{label}: missing owner")
        for field, vocabulary in CONTROLLED_FIELDS.items():
            value = row.get(field, "")
            if value and value not in vocab.get(vocabulary, set()):
                errors.append(f"{label}: invalid {field} {value}")
        for field, vocabulary in FILE_CONTROLLED_FIELDS.get(path.name, {}).items():
            value = row.get(field, "")
            if value and value not in vocab.get(vocabulary, set()):
                errors.append(f"{label}: invalid {field} {value}")
        if path.name == "interfaces.md":
            for field in ("Producer Application", "Consumer Application"):
                value = row.get(field, "")
                if value and not value.startswith("HB-APP-"):
                    errors.append(f"{label}: {field} must reference HB-APP")
        searchable = " ".join(row.values())
        if ABBREVIATED_PATTERN.search(searchable):
            errors.append(f"{label}: abbreviated reference")
        if RANGE_PATTERN.search(searchable):
            errors.append(f"{label}: range reference")

        source_prefix = match.group(1) if match else ""
        relationships = row.get("Relationships", "")
        if source_prefix == "PRD" and not relationships:
            errors.append(f"{label}: orphan product missing relationship")
        if source_prefix == "VS" and not relationships:
            errors.append(f"{label}: orphan value stream missing relationship")
        for reference in REFERENCE_PATTERN.findall(relationships):
            target_prefix = ID_PATTERN.fullmatch(reference).group(1)
            if source_prefix in RELATIONSHIP_TARGETS and target_prefix not in RELATIONSHIP_TARGETS[source_prefix]:
                errors.append(f"{label}: invalid relationship target {reference}")

    for path, row in records:
        identifier = row.get("ID", "")
        searchable = " ".join(value for key, value in row.items() if key != "ID")
        for reference in REFERENCE_PATTERN.findall(searchable):
            if reference not in ids:
                errors.append(f"{path.name}:{identifier}: unknown reference {reference}")

    for prefix, filename, noun in (
        ("PRD", "products.md", "product"),
        ("DOM", "business-domains.md", "business domain"),
        ("CAP", "capabilities.md", "capability"),
    ):
        hierarchy_rows = {i: r for i, r in by_id.items() if i.startswith(f"HB-{prefix}-")}
        for identifier, row in hierarchy_rows.items():
            parent, level = row.get("Parent ID", ""), row.get("Level", "")
            label = f"{filename}:{identifier}"
            if parent == identifier:
                errors.append(f"{label}: self-parent")
            if level == "1" and parent:
                errors.append(f"{label}: conflicting parent for level 1")
            if level in {"2", "3"} and not parent:
                errors.append(f"{label}: orphan {noun} missing parent")
            if parent in hierarchy_rows:
                expected_level = str(int(hierarchy_rows[parent].get("Level", "0")) + 1)
                if level != expected_level:
                    errors.append(f"{label}: parent level constraint")
            seen, current = set(), identifier
            while current in hierarchy_rows and hierarchy_rows[current].get("Parent ID"):
                if current in seen:
                    errors.append(f"{label}: hierarchy cycle")
                    break
                seen.add(current)
                current = hierarchy_rows[current].get("Parent ID", "")

    coverage = root / "coverage-matrix.csv"
    if coverage.exists():
        with coverage.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = reader.fieldnames or []
            for column in COVERAGE_COLUMNS:
                if column not in columns:
                    errors.append(f"coverage-matrix.csv: missing required column {column}")
            coverage_ids = set()
            for row in reader:
                identifier = (row.get("coverage_id") or "").strip()
                label = f"coverage-matrix.csv:{identifier or '<blank>'}"
                if identifier in coverage_ids:
                    errors.append(f"{label}: duplicate ID")
                coverage_ids.add(identifier)
                if not re.fullmatch(r"HB-COV-[0-9]{3}", identifier):
                    errors.append(f"{label}: malformed ID")
                status = (row.get("status") or "").strip()
                if status and status not in vocab.get("record_status", set()):
                    errors.append(f"{label}: invalid status {status}")
                for key, value in row.items():
                    if key == "coverage_id":
                        continue
                    for reference in REFERENCE_PATTERN.findall(value or ""):
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
