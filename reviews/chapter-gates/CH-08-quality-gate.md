# Chapter 8 Quality Gate: Data Modelling

## Metadata

- **Chapter:** 8, Data Modelling
- **Review date:** 2026-06-30
- **Reviewer:** Codex
- **Status recommendation:** Ready for Author Approval
- **Current gate:** Chapter 8 has been revised after initial review. It now includes six rendered teaching figures, corrected data-flow direction, corrected payment lineage, a new payment instruction lifecycle view, updated source and diagram tracking, glossary additions and register updates.
- **Diagram status:** `FIG-08-01` through `FIG-08-06` remain `Review`, not `Approved`.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.3 | Covers conceptual, logical and relational implementation models, ERDs, DFDs, lineage, lifecycle and canonical versus local models. |
| Beginner clarity | 9.2 | Explains each model through the question it answers, clarifies Basket scope and separates plain language from formal terminology. |
| Technical accuracy | 9.1 | Corrects FIG-08-04 with explicit directional flows and FIG-08-05 with traceable lineage inputs to a consolidated event. |
| Expert depth | 9.0 | Includes Party versus Customer, data ownership, authoritative status, lifecycle responsibility and canonical/local trade-offs. |
| Logical flow | 9.1 | Moves from business meaning to logical precision, relational implementation, data movement, lineage, lifecycle and governance. |
| Examples and exercises | 9.1 | Uses Simple Online Store for basic data models and Horizon Bank for lineage, lifecycle and payment status reporting. |
| Diagram quality | 9.0 | Six PlantUML figures render to SVG and PNG, remain readable, and keep scope and exclusions explicit. |
| Source quality | 9.0 | Source notes and register entries cover Chen, Codd, W3C PROV-DM, DAMA-DMBOK2 and DeMarco. |
| Repository tracking | 9.2 | `STATUS.md`, `RESUME.md`, `DIAGRAM_REGISTER.md`, `SOURCE_REGISTER.md` and Chapter 8 frontmatter agree on current state and assets. |
| Consistency with rest of book | 9.2 | Keeps data modelling distinct from BPMN, C4, ArchiMate, deployment and process views. |
| Writing and editorial quality | 9.1 | Uses British English, short paragraphs, original tables, actionable mistakes and no reader-facing draft scaffolding. |

**Average score:** 9.12

Minimum category score: 9.0.

## Mandatory Gate Checks

| Requirement | Result | Evidence |
|---|---|---|
| Required sections complete | Pass | Chapter 8 includes purpose, outcomes, prerequisites, artefacts, examples, source requirements, main sections, checklist and references. |
| Repository tracking files agree | Pass | Chapter 8 is `Ready for Author Approval`; Chapters 6 and 7 are `Approved`; Chapter 8 has six registered figures at `Review`. |
| Source notes added and registered | Pass | `research/data/` contains five Chapter 8 source notes, and `SOURCE_REGISTER.md` records all five source keys. |
| Diagrams registered | Pass | `DIAGRAM_REGISTER.md` includes `FIG-08-01` through `FIG-08-06` at `Review` and records Chapter 8 specification, source, SVG and PNG paths. |
| Diagrams rendered | Pass | SVG and PNG outputs exist for all six Chapter 8 PlantUML figures. |
| FIG-08-04 data flows corrected | Pass | Payment authorisation request/result and shipment request/confirmation are explicit directional flows. |
| FIG-08-05 lineage corrected | Pass | Payment instruction, screening result, posting result and consolidated status all trace to the Payment data product. |
| FIG-08-06 lifecycle added | Pass | Lifecycle view covers Captured, Validated, Screened, Posted, Distributed, Curated, Retained and Archived or Disposed. |
| Diagrams remain Review | Pass | No Chapter 8 diagram is marked `Approved`. |
| Repository validations pass | Pass | Final validation run includes structure, links, terminology, diagrams, diagram register and word count. |

## Diagram Review

`FIG-08-01` remains a conceptual data model. Basket is included because the conceptual scope covers the wider ordering vocabulary.

`FIG-08-02` and `FIG-08-03` deliberately narrow to placed orders. Basket is excluded from those later examples because they answer order-domain structure and relational implementation questions after placement.

`FIG-08-03` is now described as a relational implementation model, not a fully DBMS-specific physical model.

`FIG-08-04` now replaces vague exchange labels with explicit directional data flows.

`FIG-08-05` no longer leaves screening and posting results as dead-end lineage outputs. Those results feed the consolidated payment status event and then the downstream data product.

`FIG-08-06` adds the missing lifecycle view and shows responsible systems, owners and authoritative status points.

## Open issues

- The author must review Chapter 8 and decide whether to approve it.
- All Chapter 8 diagrams remain at `Review` until the final page-layout pass.
- Chapter 9 must not begin until Chapter 8 is approved.

## Gate decision

Chapter 8 is `Ready for Author Approval`. The revised gate passes the required average score, no category is below 8.5, repository tracking agrees, all six diagrams render, all sources and figures are registered, and final validations pass.
