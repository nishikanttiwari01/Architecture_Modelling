import tempfile
import unittest
from pathlib import Path

from scripts.validate_horizon_bank import validate_catalogues


VOCAB = """| Vocabulary | Value | Definition |
|---|---|---|
| record_status | Proposed | proposed |
| architecture_state | Current | current |
| source_type | Author model | authored |
| confidence | High | high |
| verification_status | Verified | verified |
| organisational_scope | Group | group |
| legal_entity_scope | Group | group |
| jurisdiction_scope | Cross-border | cross-border |
| customer_segment_scope | SME and Corporate | segments |
| ownership_type | Accountable owner | accountable |
"""


class HorizonBankValidationTests(unittest.TestCase):
    def validate(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "controlled-vocabularies.md").write_text(VOCAB, encoding="utf-8")
            for name, content in files.items():
                (root / name).write_text(content, encoding="utf-8")
            return "\n".join(validate_catalogues(root))

    def test_rejects_duplicate_and_malformed_ids(self):
        text = "| ID | Name | Definition | Owner |\n|---|---|---|---|\n| BAD | A | a | O |\n| BAD | B | b | O |\n"
        errors = self.validate({"products.md": text})
        self.assertIn("malformed ID", errors)
        self.assertIn("duplicate ID", errors)

    def test_rejects_wrong_catalogue_prefix(self):
        text = "| ID | Name | Definition | Owner |\n|---|---|---|---|\n| HB-VS-01 | A | a | O |\n"
        self.assertIn("expected prefix HB-PRD", self.validate({"products.md": text}))

    def test_rejects_bad_table_width_and_duplicate_columns(self):
        text = "| ID | Name | Name |\n|---|---|---|\n| HB-PRD-01 | A |\n"
        errors = self.validate({"products.md": text})
        self.assertIn("duplicate column", errors)
        self.assertIn("table row width", errors)

    def test_rejects_missing_required_columns(self):
        text = "| ID | Name |\n|---|---|\n| HB-PRD-01 | A |\n"
        self.assertIn("missing required column Definition", self.validate({"products.md": text}))

    def test_requires_bian_mapping_confidence_and_verification(self):
        text = "| ID | Name | Definition | Owner | Record Status |\n|---|---|---|---|---|\n| HB-BIAN-01 | A | a | O | Proposed |\n"
        errors = self.validate({"bian-mapping-register.md": text})
        self.assertIn("missing required column Confidence", errors)
        self.assertIn("missing required column Verification Status", errors)

    def test_rejects_unknown_and_wrong_typed_relationships(self):
        products = "| ID | Name | Definition | Owner | Relationships |\n|---|---|---|---|---|\n| HB-PRD-01 | A | a | O | HB-CTRL-01; HB-VS-99 |\n"
        controls = "| ID | Name | Definition | Owner |\n|---|---|---|---|\n| HB-CTRL-01 | C | c | O |\n"
        errors = self.validate({"products.md": products, "controls.md": controls})
        self.assertIn("invalid relationship target HB-CTRL-01", errors)
        self.assertIn("unknown reference HB-VS-99", errors)

    def test_rejects_abbreviated_and_ranged_references(self):
        text = "| ID | Name | Definition | Owner | Relationships |\n|---|---|---|---|---|\n| HB-PRD-01 | A | a | O | VS-03; HB-VS-01 to 03 |\n"
        errors = self.validate({"products.md": text})
        self.assertIn("abbreviated reference", errors)
        self.assertIn("range reference", errors)

    def test_rejects_self_parent_cycle_and_bad_level(self):
        text = "| ID | Name | Definition | Level | Parent ID | Owner | Relationships |\n|---|---|---|---|---|---|---|\n| HB-PRD-01 | A | a | 2 | HB-PRD-01 | O | HB-VS-01 |\n| HB-PRD-02 | B | b | 2 | HB-PRD-03 | O | HB-VS-01 |\n| HB-PRD-03 | C | c | 2 | HB-PRD-02 | O | HB-VS-01 |\n"
        errors = self.validate({"products.md": text})
        self.assertIn("self-parent", errors)
        self.assertIn("hierarchy cycle", errors)
        self.assertIn("parent level", errors)

    def test_rejects_orphan_product_and_value_stream(self):
        products = "| ID | Name | Definition | Level | Parent ID | Owner | Record Status | Relationships |\n|---|---|---|---|---|---|---|---|\n| HB-PRD-01 | A | a | 1 | | O | Proposed | |\n"
        streams = "| ID | Name | Definition | Owner | Record Status | Relationships |\n|---|---|---|---|---|---|\n| HB-VS-01 | V | v | O | Proposed | |\n"
        errors = self.validate({"products.md": products, "value-streams.md": streams})
        self.assertIn("orphan product missing relationship", errors)
        self.assertIn("orphan value stream missing relationship", errors)

    def test_rejects_invalid_controlled_values_and_missing_governance(self):
        text = "| ID | Name | Definition | Owner | Record Status | Architecture State | Source Type | Confidence | Verification Status | Organisational Scope | Legal Entity Scope | Jurisdiction Scope | Segment Scope | Ownership Type |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| HB-PRD-01 | A | | | Wrong | Wrong | Wrong | Wrong | Wrong | Wrong | Wrong | Wrong | Wrong | Wrong |\n"
        errors = self.validate({"products.md": text})
        self.assertIn("missing definition", errors)
        self.assertIn("missing owner", errors)
        for field in ("Record Status", "Architecture State", "Source Type", "Confidence", "Verification Status", "Organisational Scope", "Legal Entity Scope", "Jurisdiction Scope", "Segment Scope", "Ownership Type"):
            self.assertIn(f"invalid {field}", errors)

    def test_rejects_incomplete_coverage_schema(self):
        errors = self.validate({"coverage-matrix.csv": "coverage_id,product,status\nHB-COV-001,Pending,Proposed\n"})
        self.assertIn("missing required column legal_entity", errors)
        self.assertIn("missing required column gap", errors)

    def test_rejects_invalid_coverage_status(self):
        columns = __import__("scripts.validate_horizon_bank", fromlist=["COVERAGE_COLUMNS"]).COVERAGE_COLUMNS
        header = ",".join(columns)
        values = {column: "Pending" for column in columns}
        values.update(coverage_id="HB-COV-001", status="Wrong", gap="gap")
        row = ",".join(values[column] for column in columns)
        self.assertIn("invalid status Wrong", self.validate({"coverage-matrix.csv": header + "\n" + row + "\n"}))

    def test_requires_full_bank_foundation_catalogues(self):
        errors = self.validate({})
        for filename in (
            "business-domains.md", "capabilities.md", "applications.md",
            "interfaces.md", "external-networks.md", "reconciliations.md",
            "technology-resilience.md",
        ):
            self.assertIn(f"missing required catalogue {filename}", errors)

    def test_rejects_wrong_application_and_interface_prefixes(self):
        applications = (
            "| ID | Name | Definition | Owner | Record Status |\n"
            "|---|---|---|---|---|\n"
            "| HB-INT-01 | Wrong | wrong prefix | Owner | Proposed |\n"
        )
        interfaces = (
            "| ID | Name | Definition | Owner | Record Status |\n"
            "|---|---|---|---|---|\n"
            "| HB-APP-01 | Wrong | wrong prefix | Owner | Proposed |\n"
        )
        errors = self.validate({"applications.md": applications, "interfaces.md": interfaces})
        self.assertIn("applications.md:HB-INT-01: expected prefix HB-APP", errors)
        self.assertIn("interfaces.md:HB-APP-01: expected prefix HB-INT", errors)

    def test_rejects_domain_and_capability_hierarchy_cycles(self):
        domains = (
            "| ID | Name | Definition | Level | Parent ID | Owner | Record Status |\n"
            "|---|---|---|---|---|---|---|\n"
            "| HB-DOM-001 | One | one | 2 | HB-DOM-002 | Owner | Proposed |\n"
            "| HB-DOM-002 | Two | two | 2 | HB-DOM-001 | Owner | Proposed |\n"
        )
        capabilities = (
            "| ID | Name | Definition | Level | Parent ID | Owner | Record Status |\n"
            "|---|---|---|---|---|---|---|\n"
            "| HB-CAP-001 | One | one | 2 | HB-CAP-001 | Owner | Proposed |\n"
        )
        errors = self.validate({"business-domains.md": domains, "capabilities.md": capabilities})
        self.assertIn("business-domains.md:HB-DOM-001: hierarchy cycle", errors)
        self.assertIn("capabilities.md:HB-CAP-001: self-parent", errors)

    def test_rejects_invalid_interface_type_and_endpoint_prefix(self):
        interfaces = (
            "| ID | Name | Definition | Type | Producer Application | Consumer Application | Owner | Record Status |\n"
            "|---|---|---|---|---|---|---|---|\n"
            "| HB-INT-001 | Bad | bad interface | Carrier pigeon | HB-VS-01 | HB-APP-01 | Owner | Proposed |\n"
        )
        errors = self.validate({"interfaces.md": interfaces})
        self.assertIn("invalid Type Carrier pigeon", errors)
        self.assertIn("Producer Application must reference HB-APP", errors)

    def test_rejects_invalid_application_resilience_tier(self):
        applications = (
            "| ID | Name | Definition | Owner | Record Status | Resilience Class |\n"
            "|---|---|---|---|---|---|\n"
            "| HB-APP-001 | App | app | Owner | Proposed | Urgent |\n"
        )
        self.assertIn("invalid Resilience Class Urgent", self.validate({"applications.md": applications}))


if __name__ == "__main__":
    unittest.main()
