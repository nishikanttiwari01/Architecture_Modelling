# Chapter 14 Final Review, 2026-07-04

Reviewed baseline (revision start): `7d8947dc07c7c6bd4d2a7e6d5e8513d24f2f5e4b`

Scope: Chapter 14 manuscript, FIG-14-01 and FIG-14-02 specifications, and the supporting example, research, glossary, decision and register changes made in this revision.

## Consolidated finding status

| Review | Findings | Status |
|---|---|---|
| Technical | CH14-TECH-01 to CH14-TECH-09 | All resolved in manuscript and specifications; two items remain open by design (author approval of specifications; formal ArchiMate relationship verification by a licensed human reviewer). |
| Beginner | CH14-BEG-01 to CH14-BEG-06 | All resolved. |
| Consistency | CH14-CON-01 to CH14-CON-08 | All resolved. |

## Verification against the objective

| ID | Severity | Affected file/section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH14-FIN-01 | High | Whole chapter | The revision objective requires the chapter to be technically precise and internally consistent before diagram production. | Confirm every figure relationship is either formally supported or clearly labelled as a simplified teaching trace. | Resolved. FIG-14-01 is a labelled teaching view; no formal ArchiMate relationship semantics are claimed. |
| CH14-FIN-02 | High | Outcomes | Outcomes must be genuinely measurable. | Confirm each outcome has metric, baseline, target, scope, time horizon, owner and evidence, with illustrative placeholders. | Resolved. Outcome-measure table present for OUT-14-01..04. |
| CH14-FIN-03 | High | Investment model | Priority must not be presented as proof of funding. | Confirm importance, condition, funding and priority are separated and no composite score exists. | Resolved. Six separated dimensions; no composite. |
| CH14-FIN-04 | High | FIG-14-02 | The cross-map must be a genuine matrix, not a duplicate of FIG-13-02. | Confirm matrix structure and exact dataset. | Resolved. Capability-by-stage matrix with an exact dataset assessed against GOAL-14-01. |
| CH14-FIN-05 | Medium | Governance | Only the author may approve a material scope decision. | Confirm DEC-022 is `Proposed` and Chapter 14 is `Revision Required`. | Resolved. DEC-022 is `Proposed`; Chapter 14 status is `Revision Required`; both figures remain `Planned`. |
| CH14-FIN-06 | Medium | Diagram production | No diagram source or export may be created before author approval. | Confirm no `.puml`, `.drawio`, `.mmd`, SVG or PNG exists for FIG-14-01 or FIG-14-02. | Resolved. No Chapter 14 diagram source or export exists; both are `Pending` in the register. |

## Automated validation

All commands run at the end of the revision returned exit 0: `python -m compileall -q scripts`, `check-structure.py`, `check-links.py`, `check-terminology.py`, `validate-diagrams.py`, `check-diagram-register.py`, `word-count.py`, `build-book.py`, and `git diff --check`. Results are recorded in `reviews/chapter-gates/CH-14-quality-gate.md`.

## Recommendation

Chapter 14 is recommended to remain `Revision Required` until the author reviews this revision, approves the FIG-14-01 and FIG-14-02 specifications for production, and accepts DEC-022. No diagram assets exist, so the quality gate stays interim and non-passing. Nothing is marked `Approved`. Chapter 15 was not started.

## Specification clarity correction, 2026-07-07

A focused correction made both figure datasets properly delimited Markdown tables: `FIG-14-01` now has an eight-column traceability table (IDs with labels plus an open-assumption column) and `FIG-14-02` has a full-header capability-by-stage matrix. Each specification states it is the authoritative dataset, so no cell value is left for the diagram creator to infer. This did not change any finding status or any control status. Chapter 14 remains `Revision Required`; both figures remain `Planned`; `DEC-022` remains `Proposed`; nothing is marked `Approved`; diagram production remains deferred pending author approval; this correction did not modify Chapter 15.
