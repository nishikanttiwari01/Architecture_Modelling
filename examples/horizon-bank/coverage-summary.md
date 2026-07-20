# Horizon Bank Coverage Summary

`coverage-matrix.csv` is the machine-readable source of truth. It now contains 26 governed trace rows rather than four representative placeholders.

The matrix provides at least one row for every Level 1 business domain (`HB-DOM-001` to `HB-DOM-190`) and an explicit row for every scenario used by Chapters 37 to 48 (`HB-SCN-01` to `HB-SCN-18`). Additional rows retain `HB-SCN-19` and `HB-SCN-20` as cross-cutting technology-resilience and product-change traces, while recording that neither has a Chapter 37 to 48 chapter join.

Each row joins only catalogue IDs that form a defensible trace at the stated scope. `Pending` means that the relevant catalogue record or governed relationship does not yet exist, is not applicable but lacks a governed not-applicable identifier, or cannot be selected without inventing precision. The `gap` column states the specific reason. In particular, BIAN mappings remain `Pending` outside the four verified BIAN 14.0 register entries for deposits, payments, credit and trade finance.

This is a semantic coverage baseline, not a claim that every possible relationship has been modelled. The main remaining gaps are enterprise-support applications and authoritative records, cross-domain accounting and reconciliation joins, and verified BIAN 14.0 mappings beyond the four registered areas.
