# Resume State

## Last completed work

Chapters 6 and 7 are approved. Chapter 6 includes BPMN modeller guidance, and Chapter 7 includes ArchiMate tool guidance plus polished ArchiMate figures.

The Chapter 7 revision added the ArchiMate 4 source note, preserved the ArchiMate 3.2 note as historical, strengthened notation-reading and model-reuse guidance, corrected actor versus role, application realisation and technology support explanations, corrected the six Chapter 7 diagram specifications, and created/rendered all six Chapter 7 diagrams for review.

Chapter 7 PlantUML source files, SVG exports and PNG review previews exist for `FIG-07-01` through `FIG-07-06`. `FIG-07-01`, `FIG-07-02`, `FIG-07-05` and `FIG-07-06` were rerendered after diagram-polish changes.

Chapter 8, **Data Modelling**, is approved by the author. Final quality score: 9.1. It includes six completed figures, `FIG-08-01` through `FIG-08-06`, plus `CH-08-quality-gate.md`. The final DFD notation correction in `FIG-08-04` has been verified.

Chapter 9, **Decision Modelling and DMN**, is approved by the author. Final quality score: 9.1. It includes four completed figures, `FIG-09-01` through `FIG-09-04`, plus `CH-09-quality-gate.md`.

Chapter 10, **Domain and Event Modelling**, is approved by the author with final quality score 9.1. It includes source-backed coverage of domain models, strategic DDD, tactical DDD, subdomain types, bounded contexts, context maps, aggregates, aggregate roots, repositories, domain services, domain events, EventStorming, runtime event guidance, Event Sourcing, CQRS, practical tooling and event catalogues. `FIG-10-01` through `FIG-10-04` have specifications, PlantUML sources, SVG exports and PNG previews. The Chapter 10 quality gate is `reviews/chapter-gates/CH-10-quality-gate.md`.

All Chapter 6, Chapter 7, Chapter 8, Chapter 9 and Chapter 10 diagrams remain `Review`, not `Approved`. Final book-page layout review remains pending for diagrams, particularly `FIG-09-03` and the wider Chapter 10 event figures.

Chapter 11, **Infrastructure and Deployment Modelling**, is approved by the author with final quality score 9.1. Primary source notes, prose, glossary updates, source-register entries, `FIG-11-01` through `FIG-11-06` diagram specifications, PlantUML sources, SVG exports, PNG previews, manuscript figure references and the Chapter 11 quality gate are complete. The correction pass added ReplicaSet, StatefulSet, Gateway API and Ingress guidance, logical versus physical deployment guidance, cloud responsibility guidance, capacity and scalability guidance, stronger environment guidance, a warm-standby resilience scenario in `FIG-11-05`, a dedicated Horizon Bank payment observability view in `FIG-11-06`, practical infrastructure diagram tooling guidance and the renamed `FIG-11-04` infrastructure and placement view.

Final page-layout review remains pending for Chapter 11 diagrams, particularly `FIG-11-03`, `FIG-11-05` and `FIG-11-06`. All Chapter 11 figures remain `Review`, not `Approved`.

Chapter 12, **Security Modelling**, is in `Diagramming` after the review, focused correction, diagram-production and final diagram-correction passes. The revised manuscript adds the missing security-modelling foundation, access authorisation terminology, control mapping, residual risk and privacy modelling. The focused correction gives each threat scenario a unique ID from `T12-01` through `T12-08`, keeps non-causal `T12-04` and `T12-06` out of the attack tree, registers the Horizon Bank Customer Support Agent, and corrects identity-context flow wording. `DEC-020` is accepted, so the former `FIG-12-03` matrix is retired and replaced by manuscript table `TABLE-12-01`. PlantUML source, SVG exports and PNG previews exist for `FIG-12-01` Online Store Trust Boundary View, `FIG-12-02` Online Store Customer Authentication Sequence, `FIG-12-04` Horizon Bank Payment Threat-Model DFD and `FIG-12-05` Horizon Bank Payment Attack Tree. The final diagram-correction pass removed the false authenticated-at-edge implication from `FIG-12-01`, refined `FIG-12-04` routing and sensitive-information presentation flows, completed the `T12-06` event-consumer exposure path, and made `FIG-12-05` T12-08 a structural AND branch. A focused follow-up correction to `FIG-12-04` now shows the Operations Analyst receiving the assigned repair case and permitted payment context through the authorised operations interface before submitting a controlled repair action. All four figures remain `Review`, not `Approved`.

## Git reference

- Chapter 10 approval commit: `40e88d2`
- Chapter 11 completion commit: `98a793f`
- Chapter 11 approval commit: `9455d71`
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
- Chapter 10 status: `Approved`
- Chapter 11 status: `Approved`
- Chapter 12 status: `Diagramming`
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
- Diagram status for Chapter 11 figures `FIG-11-01` through `FIG-11-06`: `Review`
- Diagram status for Chapter 12 figures `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05`: `Review`

## Pending non-critical issues

- Chapter 1 awaits author review.
- Chapter 1 through Chapter 11 diagrams remain `Review`; no diagram is marked `Approved`.
- Final page-layout review remains pending for Chapter 11, particularly `FIG-11-03`, `FIG-11-05` and `FIG-11-06`.
- The full ArchiMate 4 specification should be reviewed by a licensed human reviewer under the applicable Open Group licence before final publication source scoring is raised.
- The Chapter 4 sequence, component and deployment diagrams are wider than the simpler figures and should be checked again during final page-layout production.
- Chapter 6 BPMN XML files were manually opened in Camunda Desktop Modeler 5.48.0 without visible repair or parsing warnings. SVG/PNG exports have been regenerated and visually inspected.
- C4-PlantUML 2.9.0 was extracted from the installed PlantUML standard library; the local extracted file records the version but not the upstream release date.

## Next chapter

Chapter 12, **Security Modelling**, is the current chapter after Chapter 11 approval.

## Next exact action

Complete final Chapter 12 quality-gate review after the corrected figures are checked in book layout. Keep Chapter 12 figures `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` at `Review` until author and page-layout review. Keep Chapter 11 figures `FIG-11-01` through `FIG-11-06` at `Review`.
