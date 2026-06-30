# Chapter 8 Quality Gate: Data Modelling

## Metadata

- **Chapter:** 8, Data Modelling
- **Review date:** 2026-06-30
- **Reviewer:** Codex
- **Status recommendation:** Under Review
- **Current gate:** Chapter 8 is fully drafted with five rendered teaching figures, data modelling source notes, glossary additions and register updates.
- **Diagram status:** `FIG-08-01` through `FIG-08-05` remain `Review`, not `Approved`.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.1 | Covers conceptual, logical and physical models, ERDs, DFDs, lineage, lifecycle and canonical versus local models. |
| Beginner clarity | 9.0 | Explains each model through the question it answers and separates plain language from formal terminology. |
| Technical accuracy | 8.9 | Uses classic ER, relational and DFD sources plus W3C PROV-DM for provenance and lineage. |
| Expert depth | 8.8 | Includes banking distinctions such as Party versus Customer, data ownership, lineage and canonical/local trade-offs. |
| Logical flow | 9.0 | Moves from business meaning to logical precision, physical implementation, movement, lineage and governance. |
| Examples and exercises | 9.0 | Uses Simple Online Store for basic data models and Horizon Bank for lineage and payment status reporting. |
| Diagram quality | 8.8 | Five PlantUML figures are rendered for review and kept deliberately small for beginner teaching. |
| Source quality | 8.8 | Adds source notes for Chen, Codd, W3C PROV-DM, DAMA-DMBOK2 and DeMarco. |
| Consistency with rest of book | 9.1 | Keeps data modelling distinct from BPMN, C4, ArchiMate and deployment views. |
| Writing and editorial quality | 9.0 | Uses British English, short paragraphs, original tables and actionable mistakes. |

**Average score:** 8.95

Minimum category score: 8.8.

## Mandatory Gate Checks

| Requirement | Result | Evidence |
|---|---|---|
| Required sections complete | Pass | Chapter 8 includes purpose, outcomes, prerequisites, artefacts, examples, source requirements, main sections, checklist and references. |
| Source notes added | Pass | `research/data/` contains five Chapter 8 source notes. |
| Diagrams registered | Pass | `DIAGRAM_REGISTER.md` includes `FIG-08-01` through `FIG-08-05` at `Review`. |
| Diagrams rendered | Pass | SVG and PNG outputs were generated for the five Chapter 8 PlantUML figures. |
| Diagrams remain Review | Pass | No Chapter 8 diagram is marked `Approved`. |

## Open issues

- Chapter 8 is ready for author review.
- The five Chapter 8 diagrams should receive final page-layout inspection before any diagram status changes.

## Gate decision

Chapter 8 is `Under Review`. The draft is complete enough for author review, and all diagram status values remain `Review` until the final page-layout pass.
