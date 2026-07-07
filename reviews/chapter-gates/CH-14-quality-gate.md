# Chapter 14 Quality Gate

Current status: `Revision Required` (recommended by the 2026-07-04 revision review; only the author may change this to `Approved`)

Reviewed baseline (revision start): `7d8947dc07c7c6bd4d2a7e6d5e8513d24f2f5e4b`

This gate is interim and non-passing. It stays open while the FIG-14-01 and FIG-14-02 specifications remain unapproved by the author and no diagram assets exist. It is not an author-approval gate.

## What this revision changed

- Reclassified FIG-14-01 as an ArchiMate-informed strategy traceability teaching view; connectors are simplified teaching links, not formal ArchiMate relationships.
- Recorded the ArchiMate 4 relationship-verification limitation in `research/archimate/open-group-archimate-4.md`.
- Added measurable outcomes OUT-14-01 to OUT-14-04 with metric, baseline, target, scope, time horizon, owner and evidence, using clearly illustrative placeholders.
- Separated strategic importance, current condition, current investment status, proposed priority, delivery constraint and final funding on the heat map; removed any composite score.
- Replaced the categorical goal-to-initiative rule with nuanced guidance; a goal with no work package is a finding, not automatically invalid.
- Added the `Executive Sponsor` controlled role and used it consistently.
- Recorded controlled capability levelling and the Financial Crime Screening versus Payment Screening peer scoping in `examples/horizon-bank/capabilities.md`.
- Added stable IDs (DRV, GOAL, OUT, COA, WP) and one master traceability table shared by the manuscript and FIG-14-01.
- Redesigned FIG-14-02 as a capability-by-stage matrix with an exact dataset and goal-specific strategic importance.
- Changed DEC-022 to `Proposed`.

## Interim assessment

| Category | Score | Evidence | Gate result |
|---|---:|---|---|
| Purpose and reader outcomes | 8.6 | Purpose, outcomes, concept mapping and selection table present and aligned to Part III selection role. | Conditional pass |
| Technical accuracy | 8.5 | Notation claim corrected, outcomes measurable, investment dimensions separated, levelling recorded, matrix respecified. | Conditional pass, two items open by design |
| Beginner clarity | 8.5 | Plain-language mapping, goal-versus-outcome clarity, heat-map separation explained. | Conditional pass |
| Source support | 8.4 | ArchiMate concept names, business-architecture guides, heat-map convention and ISO 42010 used; relationship-verification limitation documented. | Conditional pass |
| Example consistency | 8.6 | Executive Sponsor and levelling controlled; IDs consistent across manuscript and FIG-14-01. | Conditional pass |
| Diagram readiness | 6.5 | Specifications are precise and internally consistent, but unapproved; no source or export exists. | Interim, blocked pending author approval |
| Review evidence | 8.5 | Technical, beginner, consistency and final review records plus this gate created. | Conditional pass |

Interim average: `8.2/10`.

## Automated validation (all exit 0)

`python -m compileall -q scripts`; `check-structure.py`; `check-links.py`; `check-terminology.py`; `validate-diagrams.py`; `check-diagram-register.py`; `word-count.py`; `build-book.py`; `git diff --check`. No Chapter 14 diagram source, SVG or PNG exists; both figures are `Planned` with `Pending` source and export.

## Open author decisions

- Author approval of the FIG-14-01 and FIG-14-02 specifications for production (only the author may approve; a diagram must never be marked `Approved` by the assistant).
- Author acceptance of DEC-022 (currently `Proposed`).
- Formal ArchiMate 4 relationship verification by a licensed human reviewer before any upgrade of FIG-14-01 to a formal ArchiMate view.
- Final book-page layout review of the wide measurement, matrix and traceability tables.

## Gate decision

Open and non-passing. Keep Chapter 14 at `Revision Required` and both figures at `Planned`. Do not create diagram sources or exports, and do not mark anything `Approved`, until the author approves the specifications. Chapter 15 was not started.

## Specification clarity correction, 2026-07-07

A focused, non-semantic correction made both figure datasets properly delimited Markdown tables so no cell value is left for the diagram creator to infer:

- `FIG-14-01` traceability dataset is now an eight-column table (Driver, Goal and Outcome shown with ID and label, plus Capabilities, Course of Action, Work Package, Stakeholder owner and Open assumption or decision) and is declared the authoritative dataset for the figure.
- `FIG-14-02` matrix now uses full stage-name headers, aligned with the manuscript matrix, and is declared the authoritative dataset.

The gate remains interim and non-passing. No score changed. Chapter 14 remains `Revision Required`; both figures remain `Planned`; `DEC-022` remains `Proposed`; nothing is marked `Approved`; no diagram source or export was created; this correction did not modify Chapter 15.
