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

Chapter 12, **Security Modelling**, is approved by the author with final quality score 9.1. The revised manuscript adds the missing security-modelling foundation, access authorisation terminology, control mapping, residual risk and privacy modelling. The focused correction gives each threat scenario a unique ID from `T12-01` through `T12-08`, keeps non-causal `T12-04` and `T12-06` out of the attack tree, registers the Horizon Bank Customer Support Agent, and corrects identity-context flow wording. `DEC-020` is accepted, so the former `FIG-12-03` matrix is retired and replaced by manuscript table `TABLE-12-01`. PlantUML source, SVG exports and PNG previews exist for `FIG-12-01` Online Store Trust Boundary View, `FIG-12-02` Online Store Customer Authentication Sequence, `FIG-12-04` Horizon Bank Payment Threat-Model DFD and `FIG-12-05` Horizon Bank Payment Attack Tree. The final diagram-correction pass removed the false authenticated-at-edge implication from `FIG-12-01`, refined `FIG-12-04` routing and sensitive-information presentation flows, completed the `T12-06` event-consumer exposure path, and made `FIG-12-05` T12-08 a structural AND branch. A focused follow-up correction to `FIG-12-04` now shows the Operations Analyst receiving the assigned repair case and permitted payment context through the authorised operations interface before submitting a controlled repair action. All four figures remain `Review`, not `Approved`.

Chapter 13, **Other Useful Modelling Approaches**, is in `Diagramming`. The manuscript covers SysML-style requirement traceability, capability maps, value streams, application landscapes, integration landscapes, architecture roadmaps, heat maps, Wardley maps and ADRs. Earlier review passes added controlled Horizon Bank capability and system lifecycle examples, official Open Group business architecture guide source notes, a local heat-map scoring convention note, an original Horizon Bank ADR example, formal-versus-practitioner classification, and the revised `FIG-13-01` through `FIG-13-06` specifications.

The author then approved the revised specifications for production, and the six figures have now been produced and recorded as `Review`. `FIG-13-01` (Online Store SysML-style Requirement Traceability View) uses PlantUML. `FIG-13-02` Customer Onboarding Value Stream, `FIG-13-03` Application Landscape Map, `FIG-13-04` Platform Evolution Roadmap, `FIG-13-05` Capability Heat Map and `FIG-13-06` Payment Modernisation Wardley Map use Draw.io. The Draw.io figures are exported to SVG and PNG from the editable `.drawio` source by `scripts/render-drawio-diagrams.py` (`DEC-021`), because no Draw.io desktop CLI is available in this environment. Each figure has one editable source, one SVG export and one PNG preview, is embedded in the manuscript with a caption, accessibility text and a limitation note, and was visually inspected. The `FIG-13-02` specification was aligned with the manuscript by adding the controlled capability `Relationship Management`. No Chapter 13 figure is `Approved`. A Draw.io graphical review of the five Draw.io figures and final book-page layout review remain pending.

A focused correction pass then: fixed the `FIG-13-02` trigger-label placement (single connector, label clearly above it, touching no box) and added `examples/horizon-bank/capabilities.md` to that figure's specification; integrated `scripts/render-drawio-diagrams.py` into the reproducible workflow (compileall syntax check, pinned Pillow in `requirements-diagrams.txt`, invocation from `render-all-diagrams.ps1` with failure propagation, and a CI stale-export check `git diff --exit-code -- diagrams/exported/svg diagrams/exported/png`); added deterministic cross-platform font selection (Arial preferred, DejaVu Sans fallback, reported, fail-loud); moved `DEC-021` to `Proposed`; and set the Owner of `FIG-13-01` through `FIG-13-06` to `Claude`.

The final Chapter 13 review (2026-07-03, reviewed commit `bd6dc47`) then confirmed technical accuracy, beginner comprehension, educational flow, terminology and example consistency, diagram quality, accessibility, source and copyright, copy-editing and page-fit readability across all six figures, and removed the reader-facing draft scaffolding on moving to a production status (per `DEC-010`). All non-author findings are resolved. Chapter 13 is now `Ready for Author Approval` with final score 9.0. All six figures stay `Review`. Open author decisions: author approval of the chapter and figures; native Draw.io graphical-open and export-fidelity comparison (`DEC-021`, Proposed); and final 6 by 9 book-page layout placement of the wider landscape figures `FIG-13-01`, `FIG-13-03` and `FIG-13-04` (`DEC-014`).

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
- Chapter 12 status: `Approved`
- Chapter 13 status: `Ready for Author Approval`
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
- Diagram status for Chapter 13 figures `FIG-13-01` through `FIG-13-06`: `Review`

## Pending non-critical issues

- Chapter 1 awaits author review.
- Chapter 1 through Chapter 11 diagrams remain `Review`; no diagram is marked `Approved`.
- Final page-layout review remains pending for Chapter 11, particularly `FIG-11-03`, `FIG-11-05` and `FIG-11-06`.
- The full ArchiMate 4 specification should be reviewed by a licensed human reviewer under the applicable Open Group licence before final publication source scoring is raised.
- The Chapter 4 sequence, component and deployment diagrams are wider than the simpler figures and should be checked again during final page-layout production.
- Chapter 6 BPMN XML files were manually opened in Camunda Desktop Modeler 5.48.0 without visible repair or parsing warnings. SVG/PNG exports have been regenerated and visually inspected.
- C4-PlantUML 2.9.0 was extracted from the installed PlantUML standard library; the local extracted file records the version but not the upstream release date.

## Next chapter

Chapter 13, **Other Useful Modelling Approaches**, has passed final review and is `Ready for Author Approval` with all six figures at `Review`. Chapter 14, **Modelling Business Strategy and Capabilities**, has not started and remains `Planned`.

## Next exact action

Author review of Chapter 13 for approval. If the author approves the chapter, they may mark it `Approved`; only the author may do that. The six figures (`FIG-13-01` through `FIG-13-06`) remain `Review` pending a native Draw.io graphical-open and export-fidelity comparison (which would allow `DEC-021` to move from `Proposed` to `Approved`) and the final 6 by 9 book-page layout placement (`DEC-014`), particularly for the wider landscape figures `FIG-13-01`, `FIG-13-03` and `FIG-13-04`. Do not begin Chapter 14. Keep Chapter 12 figures `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` at `Review` until final page-layout review. Keep Chapter 11 figures `FIG-11-01` through `FIG-11-06` at `Review`.
