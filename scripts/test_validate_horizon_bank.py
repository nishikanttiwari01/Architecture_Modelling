import tempfile
import unittest
from pathlib import Path

from scripts.validate_horizon_bank import validate_catalogues


class HorizonBankValidationTests(unittest.TestCase):
    def test_reports_duplicate_malformed_unknown_and_invalid_values(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "controlled-vocabularies.md").write_text(
                "| Vocabulary | Value | Definition |\n|---|---|---|\n"
                "| lifecycle_status | Current | active |\n"
                "| scope | Group | group |\n",
                encoding="utf-8",
            )
            (root / "products.md").write_text(
                "| ID | Name | Definition | Level | Parent ID | Owner | Scope | Status | Relationships |\n"
                "|---|---|---|---|---|---|---|---|---|\n"
                "| BAD | One | | 2 | HB-PRD-99 | | Wrong | Invalid | HB-VS-99 |\n"
                "| BAD | Two | duplicate | 1 | HB-PRD-01 | Owner | Group | Current | |\n",
                encoding="utf-8",
            )
            (root / "value-streams.md").write_text(
                "| ID | Name | Definition | Owner | Scope | Status | Relationships |\n"
                "|---|---|---|---|---|---|---|\n"
                "| HB-VS-01 | Orphan | no governed relationship | Owner | Group | Current | |\n",
                encoding="utf-8",
            )
            errors = validate_catalogues(root)
            joined = "\n".join(errors)
            self.assertIn("duplicate ID", joined)
            self.assertIn("malformed ID", joined)
            self.assertIn("missing definition", joined)
            self.assertIn("missing owner", joined)
            self.assertIn("invalid status", joined)
            self.assertIn("invalid scope", joined)
            self.assertIn("unknown reference", joined)
            self.assertIn("conflicting parent", joined)
            self.assertIn("orphan value stream", joined)
            self.assertIn("orphan product", joined)


if __name__ == "__main__":
    unittest.main()
