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
        header = ",".join(__import__("scripts.validate_horizon_bank", fromlist=["COVERAGE_COLUMNS"]).COVERAGE_COLUMNS)
        row = ",".join(["HB-COV-001"] + ["Pending"] * 20 + ["Wrong", "gap"])
        self.assertIn("invalid status Wrong", self.validate({"coverage-matrix.csv": header + "\n" + row + "\n"}))


if __name__ == "__main__":
    unittest.main()
