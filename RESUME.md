# Resume State

## Last completed work

Chapters 6 and 7 are approved. Chapter 6 includes BPMN modeller guidance, and Chapter 7 includes ArchiMate tool guidance plus polished ArchiMate figures.

The Chapter 7 revision added the ArchiMate 4 source note, preserved the ArchiMate 3.2 note as historical, strengthened notation-reading and model-reuse guidance, corrected actor versus role, application realisation and technology support explanations, corrected the six Chapter 7 diagram specifications, and created/rendered all six Chapter 7 diagrams for review.

Chapter 7 PlantUML source files, SVG exports and PNG review previews exist for `FIG-07-01` through `FIG-07-06`. `FIG-07-01`, `FIG-07-02`, `FIG-07-05` and `FIG-07-06` were rerendered after diagram-polish changes.

Chapter 8, **Data Modelling**, is approved by the author. Final quality score: 9.1. It includes six completed figures, `FIG-08-01` through `FIG-08-06`, plus `CH-08-quality-gate.md`. The final DFD notation correction in `FIG-08-04` has been verified.

Chapter 9, **Decision Modelling and DMN**, is approved by the author. Final quality score: 9.1. It includes four completed figures, `FIG-09-01` through `FIG-09-04`, plus `CH-09-quality-gate.md`.

Chapter 10, **Domain and Event Modelling**, is `Ready for Author Approval` with final quality score 9.1. It includes source-backed coverage of domain models, strategic DDD, tactical DDD, subdomain types, bounded contexts, context maps, aggregates, aggregate roots, repositories, domain services, domain events, EventStorming, runtime event guidance, Event Sourcing, CQRS, practical tooling and event catalogues. `FIG-10-01` through `FIG-10-04` have specifications, PlantUML sources, SVG exports and PNG previews. The Chapter 10 quality gate is `reviews/chapter-gates/CH-10-quality-gate.md`.

All Chapter 6, Chapter 7, Chapter 8, Chapter 9 and Chapter 10 diagrams remain `Review`, not `Approved`. Final book-page layout review remains pending for diagrams, particularly `FIG-09-03` and the wider Chapter 10 event figures.

## Git reference

- Chapter 9 approval commit: `b90b2b7`
- Branch: `main`
- Remote: `origin/main`

## Current status

- Chapter 1 status: `Ready for Author Approval`
- Chapter 2 status: `Approved`
- Chapter 3 status: `Approved`
- Chapter 4 status: `Approved`
- Chapter 5 status: `Approved`
- Chapter 6 status: `Approved`
- Chapter 7 status: `Approved`
- Chapter 8 status: `Approved`
- Chapter 9 status: `Approved`
- Chapter 10 status: `Ready for Author Approval`
- Diagram status for Chapter 1 figure `FIG-01-01`: `Review`
- Diagram status for Chapter 2 figure `FIG-02-01`: `Review`
- Diagram status for Chapter 3 figures `FIG-03-01` through `FIG-03-03`: `Review`
- Diagram status for Chapter 4 figures `FIG-04-01` through `FIG-04-07`: `Review`
- Diagram status for Chapter 5 figures `FIG-05-01` through `FIG-05-08`: `Review`
- Diagram status for Chapter 6 figures `FIG-06-01` through `FIG-06-03`: `Review`
- Diagram status for Chapter 7 figures `FIG-07-01` through `FIG-07-06`: `Review`
- Diagram status for Chapter 8 figures `FIG-08-01` through `FIG-08-06`: `Review`
- Diagram status for Chapter 9 figures `FIG-09-01` through `FIG-09-04`: `Review`
- Diagram status for Chapter 10 figures `FIG-10-01` through `FIG-10-04`: `Review`

## Pending non-critical issues

- Chapter 1 awaits author review.
- Chapter 1 through Chapter 10 diagrams remain `Review`; no diagram is marked `Approved`.
- The full ArchiMate 4 specification should be reviewed by a licensed human reviewer under the applicable Open Group licence before final publication source scoring is raised.
- The Chapter 4 sequence, component and deployment diagrams are wider than the simpler figures and should be checked again during final page-layout production.
- Chapter 6 BPMN XML files were manually opened in Camunda Desktop Modeler 5.48.0 without visible repair or parsing warnings. SVG/PNG exports have been regenerated and visually inspected.
- C4-PlantUML 2.9.0 was extracted from the installed PlantUML standard library; the local extracted file records the version but not the upstream release date.

## Next chapter

Chapter 10, **Domain and Event Modelling**, awaits author review. Do not begin Chapter 11 until the author has reviewed Chapter 10.

Chapter 9 now includes four rendered figures, `FIG-09-01` through `FIG-09-04`, all at `Review`. The figures use PlantUML teaching sources rather than semantic `.dmn` XML, per `DEC-015`, because current Camunda documentation describes DMN 1.3 modelling and no local DMN modeller CLI validated DMN 1.5 semantic files in this environment.

Final author-review corrections are applied for FEEL list literals, `FIG-09-02` stock checking, direct `FIG-09-03` information requirements and `FIG-09-04` cross-boundary arrow labels. Chapter 9 is now `Approved`.

## Next exact action

Author review of Chapter 10. After author approval or requested revisions, update `STATUS.md`, `CHANGELOG.md` and any affected chapter or diagram files.
