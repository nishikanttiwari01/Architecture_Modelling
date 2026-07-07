# Chapter 14 Consistency Review, 2026-07-04

Reviewed baseline (revision start): `7d8947dc07c7c6bd4d2a7e6d5e8513d24f2f5e4b`

Scope: Chapter 14 manuscript, FIG-14-01 and FIG-14-02 specifications, `examples/horizon-bank/capabilities.md`, `examples/horizon-bank/actors.md`, `DIAGRAM_REGISTER.md`, `GLOSSARY.md`, `STATUS.md`, `DECISIONS.md`.

| ID | Severity | Affected file/section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH14-CON-01 | High | Manuscript stakeholder table | `Sponsor and executive` was used but is not a controlled Horizon Bank role. | Add a single controlled role and use it consistently. | Resolved. `Executive Sponsor` added to `examples/horizon-bank/actors.md` and used throughout the manuscript and both specifications. |
| CH14-CON-02 | High | Manuscript and specifications, IDs | Strategy elements had no stable IDs, so manuscript and figure could drift. | Assign DRV, GOAL, OUT, COA, WP IDs and use them identically in the manuscript and FIG-14-01. | Resolved. One master traceability table in the manuscript matches the FIG-14-01 relationship table row for row. |
| CH14-CON-03 | Medium | `examples/horizon-bank/capabilities.md` | Capability levelling was implied in the chapter but not recorded in the controlled catalogue. | Record levels and parents in the example file. | Resolved. Controlled levelling section added; the manuscript references it rather than inventing decomposition. |
| CH14-CON-04 | Medium | Manuscript notation and DIAGRAM_REGISTER | The register notation column and the manuscript must agree on the figure classification. | Align both to the ArchiMate-informed teaching classification and the matrix classification. | Resolved. `DIAGRAM_REGISTER.md` notation for FIG-14-01 and FIG-14-02 updated to match the specifications. |
| CH14-CON-05 | Medium | Manuscript required-section headings | The revision plan asked to remove several scaffolding sections, but `check-structure.py` always requires `## Required models and artefacts`, `## Worked examples` and `## Source requirements`. | Remove only the draft-only sections that a production status permits; retain the checker-required sections with reader-facing content, matching Chapter 13. | Resolved. `## Planned chapter structure` and `## Drafting notes` removed (allowed at `Revision Required`); the three checker-required sections are retained with concise reader-facing content, as in Chapter 13. |
| CH14-CON-06 | Medium | `DECISIONS.md`, DEC-022 | DEC-022 was recorded as `Approved` without explicit author approval. | Change DEC-022 to `Proposed` and record that it awaits author approval, without deleting its content. | Resolved. DEC-022 status changed to `Proposed`; content retained with an approval note. |
| CH14-CON-07 | Low | Cross-references | Chapter 14 must point forward to Chapter 15 for process detail and back to Chapters 7 and 13. | Confirm cross-references are present and accurate. | Resolved. References to Chapters 2, 3, 7, 13, 15 and 16 are present and accurate; Chapter 15 was not modified. |
| CH14-CON-08 | Low | GLOSSARY | New reader-facing terms (Course of Action, Work Package, capability levelling, cross-map) were not in the glossary. | Add concise glossary rows consistent with existing entries. | Resolved. Glossary rows added without duplicating existing terms. |

Consistency: conditional pass. Controlled names, IDs and classifications now agree across the manuscript, specifications, example files and registers.

## Specification clarity correction, 2026-07-07

- `FIG-14-01` and `FIG-14-02` datasets are now properly delimited Markdown tables and are each stated to be the authoritative dataset for their figure.
- The `FIG-14-02` matrix stage-name headers were aligned between the specification and the Chapter 14 manuscript matrix (`S4 Banking relationship established`, `S5 Services ready to use`, `Strategic importance for GOAL-14-01`). The primary, supporting and importance markers are identical in both; the specification additionally records a rationale column as production detail, which the manuscript keeps in prose for page-width readability.
- No cell value is left for the diagram creator to infer. No status changed: Chapter 14 remains `Revision Required`, both figures remain `Planned`, and `DEC-022` remains `Proposed`.
