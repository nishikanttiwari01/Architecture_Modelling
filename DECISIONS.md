# Architecture and Editorial Decision Log

Use the format below for all material decisions. Do not delete superseded decisions; mark their status and link the replacement.

## DEC-001: Use Markdown and Git as the source of truth

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Store the manuscript, research notes, diagrams, reviews and project-control files in this repository.
- **Reason:** It provides durable memory, version history, portability and Codex access.
- **Consequences:** Chat history is supplementary and must not be treated as the authoritative project state.

## DEC-002: Use two continuing case studies

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Use a simple online store for introductory examples and Horizon Bank for enterprise and BIAN examples.
- **Reason:** One simple example supports beginners, while one consistent banking example supports realistic traceability.
- **Consequences:** Names and facts in both examples must remain consistent across chapters.

## DEC-003: Make BIAN a complete practical part

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Dedicate Part V to a full business-and-technology BIAN implementation for a fictional full-service bank.
- **Reason:** BIAN should be taught as an enterprise banking reference architecture, not only as a technical API or microservices topic.
- **Consequences:** The part includes strategy, capabilities, all major bank process families, information, applications, security, operations and migration.

## DEC-004: Do not map Service Domains automatically to microservices

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Treat BIAN Service Domains as logical business capability boundaries. Physical service boundaries require separate design justification.
- **Reason:** Ownership, transaction consistency, scale, security, data and legacy constraints affect implementation.
- **Consequences:** Every physical mapping must state its rationale.

## DEC-005: Use British English and no em dashes

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Use British spelling and replace em dashes with commas, parentheses, colons or full stops.
- **Reason:** Maintain a consistent authorial style.

## DEC-006: Author approval is a manual gate

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Codex and automated scripts may move a chapter to `Ready for Author Approval`, but only the author can mark it `Approved`.
- **Reason:** Editorial responsibility remains with the author.

## DEC-007: Use specification-first diagram production

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Every book diagram requires a diagram specification before source creation. Codex may prepare the specification, but diagram source creation waits for author approval of the specification.
- **Reason:** The book needs diagrams that answer a clear reader question, use the right notation and remain visually suitable for publication.
- **Consequences:** Diagram specifications live under `diagrams/specifications/`, source files live under `diagrams/source/`, SVG exports live under `diagrams/exported/svg/`, and `DIAGRAM_REGISTER.md` remains the tracking point.
- **Related chapters/files:** `AGENTS.md`, `WORKFLOW.md`, `DIAGRAM_REGISTER.md`, `templates/diagram-specification-template.md`

## DEC-008: Use local version-pinned diagram libraries

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** C4-PlantUML and similar diagram libraries must be stored locally and version-pinned before use in publication diagrams.
- **Reason:** Publication diagrams must be reproducible and should not depend on unversioned remote includes.
- **Consequences:** C4-PlantUML is reserved under `diagrams/lib/C4-PlantUML/`; unversioned `!includeurl` usage is not allowed in publication PlantUML sources.
- **Related chapters/files:** `AGENTS.md`, `SOURCE_REGISTER.md`, `diagrams/lib/C4-PlantUML/README.md`

## DEC-009: Pin C4-PlantUML from the installed PlantUML standard library

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Use the C4-PlantUML 2.9.0 files extracted from the installed PlantUML 1.2024.3 standard library as the local C4-PlantUML dependency under `diagrams/lib/C4-PlantUML/`.
- **Context:** The VS Code PlantUML extension is installed and includes a working PlantUML runtime. The repository policy requires local, version-pinned C4-PlantUML files rather than unversioned remote includes.
- **Alternatives considered:** Use PlantUML's bundled `<C4/...>` standard library directly; download C4-PlantUML separately; defer C4 rendering until later.
- **Reason:** Extracting the bundled standard library gives a local, reproducible dependency without introducing remote render-time includes or third-party binaries.
- **Consequences:** The copied C4 files are stored in the repository, internal C4 include statements are localised, and source details are recorded in `SOURCE_REGISTER.md` and `research/c4/c4-plantuml-2.9.0.md`.
- **Related chapters/files:** `diagrams/lib/C4-PlantUML/`, `SOURCE_REGISTER.md`, `research/c4/c4-plantuml-2.9.0.md`, Chapter 5 diagrams.

## DEC-010: Remove draft scaffolding from production-ready chapters

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Chapters in production review statuses do not need reader-facing `Planned chapter structure` or `Drafting notes` sections.
- **Context:** Chapter 5 reached `Ready for Author Approval`, and the author requested removal of those reader-facing production headings.
- **Alternatives considered:** Keep the headings to satisfy the structure checker; remove them only from Chapter 5 without updating validation.
- **Reason:** Draft scaffolding is useful while a chapter is planned or being drafted, but it should not appear in a chapter being prepared for author approval.
- **Consequences:** `scripts/check-structure.py` still requires draft scaffolding for early-status chapters, while allowing production-status chapters to omit it.
- **Related chapters/files:** `scripts/check-structure.py`, Chapter 5.

## DEC-011: Use Chapter 5 as the prototype chapter model

- **Status:** Approved
- **Date:** 2026-06-28
- **Decision:** Use Chapter 5, The C4 Model, as the structural and writing model for subsequent substantive chapters.
- **Context:** The author gave a final verdict that Chapter 5 passes as the prototype chapter at `9.1/10`.
- **Reason:** Chapter 5 now demonstrates the desired sequence of beginner explanation, formal terminology, examples, diagrams, comparison, mistakes, exercise, checklist and references.
- **Consequences:** Future chapters should follow the Chapter 5 teaching pattern unless their subject requires a deliberate variation. Chapter 5 diagrams remain `Review` until SVG visual inspection in VS Code is complete.
- **Related chapters/files:** Chapter 5, `STYLE_GUIDE.md`, `WORKFLOW.md`, `reviews/chapter-gates/CH-05-quality-gate.md`.

## DEC-012: Render Chapter 6 BPMN teaching figures from BPMNDI

- **Status:** Approved
- **Date:** 2026-06-29
- **Decision:** Use `scripts/render-bpmn-diagrams.py` to render the Chapter 6 BPMN teaching figures from the BPMN XML and BPMN Diagram Interchange coordinates.
- **Context:** Chapter 6 revisions require the XML source, SVG export and PNG preview to represent the same BPMN model. Camunda Modeler is the preferred manual BPMN tool, but it is not available in this environment.
- **Alternatives considered:** Maintain SVG files by hand; defer SVG/PNG regeneration until Camunda Modeler is available.
- **Reason:** Rendering from BPMNDI keeps the editable BPMN source as the layout source of truth and avoids SVG-only elements.
- **Consequences:** The renderer supports only the simple BPMN subset used by these teaching examples. Camunda Modeler validation remains required before Chapter 6 can return to `Ready for Author Approval`.
- **Related chapters/files:** Chapter 6, `diagrams/source/bpmn/FIG-06-*.bpmn`, `diagrams/exported/svg/FIG-06-*.svg`, `diagrams/exported/png/FIG-06-*.png`, `reviews/chapter-gates/CH-06-quality-gate.md`.

## DEC-013: Distinguish semantic repositories, drawing tools and diagrams as code

- **Status:** Approved
- **Date:** 2026-06-30
- **Decision:** Tool guidance in Chapters 6 and 7 will distinguish semantic modelling or repository tools from general drawing tools and diagrams-as-code tools.
- **Context:** The book uses `.bpmn` files as semantic BPMN source and PlantUML as reproducible source for ArchiMate teaching views. Readers also need practical tool guidance without assuming that drawing shapes, storing text source and maintaining a governed architecture repository are the same activity.
- **Alternatives considered:** Present all tools in one list; recommend only the tools used by the repository; defer tooling guidance to Chapter 61.
- **Reason:** Beginners need to understand why tool choice affects interoperability, validation, model reuse and governance.
- **Consequences:** Chapter 6 recommends Camunda Desktop Modeler when BPMN XML interoperability and execution semantics matter. Chapter 7 states that the book's PlantUML figures are reproducible teaching views, not a governed ArchiMate repository.
- **Related chapters/files:** Chapter 6, Chapter 7, Chapter 61, `SOURCE_REGISTER.md`, `research/bpmn/bpmn-tool-guidance-2026-06-30.md`, `research/archimate/archimate-tool-guidance-2026-06-30.md`.

## DEC-014: Keep diagram register status at Review until final page layout

- **Status:** Approved
- **Date:** 2026-06-30
- **Decision:** Keep all book diagrams at `Review` in `DIAGRAM_REGISTER.md` until the final page-layout pass, even when their related chapters are author-approved.
- **Context:** The author approved Chapters 6 and 7 as chapters while instructing that diagram status should remain at `Review` until final layout.
- **Alternatives considered:** Mark chapter diagrams `Approved` as soon as the chapter is approved; use `Exported` for rendered SVGs.
- **Reason:** Diagram rendering, page fit, captions and accessibility need a final publication-layout inspection before diagram status is closed.
- **Consequences:** Chapter status and diagram status are tracked separately. Codex may render and validate diagrams, but it must not mark diagrams `Approved`.
- **Related chapters/files:** Chapters 6, 7 and 8, `DIAGRAM_REGISTER.md`, `STATUS.md`.

## DEC-015: Use PlantUML teaching figures for Chapter 9 DMN concepts

- **Status:** Approved
- **Date:** 2026-06-30
- **Decision:** Use PlantUML as the editable source for Chapter 9 publication figures, including the decision table, decision tree, DMN-style DRD and BPMN/DMN responsibility split.
- **Context:** Chapter 9 uses OMG DMN 1.5 as the normative formal baseline. Current Camunda documentation describes DMN 1.3 modelling, and no local DMN modeller CLI is available in this environment to validate semantic `.dmn` files against DMN 1.5. The author requested SVG/PNG publication outputs and accurate version recording.
- **Alternatives considered:** Generate semantic `.dmn` files without local modeller validation; use Camunda-oriented DMN 1.3 XML while presenting DMN 1.5 as the chapter baseline; defer all figures until a semantic DMN modeller is available.
- **Reason:** PlantUML provides repeatable editable source and rendered SVG/PNG outputs without implying semantic DMN XML conformance. The chapter can still teach formal DMN concepts while explicitly stating that the figures are original teaching illustrations, not executable `.dmn` models.
- **Consequences:** Chapter 9 diagrams are publication teaching views. If the book later needs executable or repository-grade DMN assets, a DMN-aware modeller and explicit tool/version validation should be added before creating `.dmn` source files.
- **Related chapters/files:** Chapter 9, `diagrams/source/plantuml/FIG-09-*`, `research/dmn/camunda-dmn-1.3-docs-2026.md`, `research/dmn/trisotech-dmn-docs-2026.md`.

## DEC-016: Rename Chapter 11 hybrid diagram as an infrastructure and placement view

- **Status:** Approved
- **Date:** 2026-07-01
- **Decision:** Rename `FIG-11-04` from `Horizon Bank Hybrid Deployment View` to `Horizon Bank Hybrid Infrastructure and Placement View`.
- **Context:** The figure separates customer channels, cloud platform, controlled integration and retained core-banking placement. It does not show deployable artifacts in the narrower UML or C4 deployment sense.
- **Alternatives considered:** Keep the original title and explain the broader use of deployment in the caption; rename only the title without renaming files.
- **Reason:** The revised title is more accurate for the diagram question and avoids teaching beginners that every hybrid infrastructure placement view is a deployment view.
- **Consequences:** The manuscript reference, diagram register, specification file, PlantUML source, SVG export and PNG preview use the new name. Historical git history still contains the previous filename.
- **Related chapters/files:** Chapter 11, `DIAGRAM_REGISTER.md`, `diagrams/specifications/FIG-11-04-horizon-bank-hybrid-infrastructure-placement-view.md`, `diagrams/source/plantuml/FIG-11-04-horizon-bank-hybrid-infrastructure-placement-view.puml`.

## DEC-017: Do not create a separate Chapter 11 observability figure in this pass

- **Status:** Superseded
- **Date:** 2026-07-01
- **Decision:** Do not add `FIG-11-06` for observability during the Chapter 11 author-review correction pass.
- **Context:** The review requested that a dedicated observability view be considered but not created automatically. The revised prose and `FIG-11-05` now show workload, store and event-platform telemetry emission, collectors, processing/export, observability backend and operational alerting.
- **Alternatives considered:** Add a new planned `FIG-11-06` specification only; add a full new source and export despite the instruction not to create one automatically.
- **Reason:** The existing five-figure set remains sufficient for Chapter 11 after the resilience figure and observability prose were strengthened. A dedicated observability figure can be reconsidered in a later operations-focused chapter if the author requests it.
- **Consequences:** No `FIG-11-06` register entry, source or export was created. Chapter 11 still teaches observability, and the broader operational architecture coverage can revisit a dedicated observability view later.
- **Related chapters/files:** Chapter 11, `FIG-11-05`, Chapter 29, Chapter 49.
- **Supersedes / superseded by:** Superseded by DEC-018 after the author's explicit request to create `FIG-11-06`.

## DEC-018: Add a dedicated Chapter 11 payment observability view

- **Status:** Approved
- **Date:** 2026-07-01
- **Decision:** Create `FIG-11-06`, `Horizon Bank Payment Observability View`, as a dedicated observability architecture view for Chapter 11.
- **Context:** The author explicitly requested `FIG-11-06` and asked for it to show Horizon Digital Channels, Payments Platform, Financial Crime Platform, Enterprise Integration Platform, Event Platform, Core Deposit System, traces, metrics, logs, OpenTelemetry Collector, filtering and sensitive-data redaction, observability backends, dashboards, alert routing, Operations Team and Service Owner. The author also requested named payment indicators.
- **Alternatives considered:** Keep observability inside `FIG-11-05`; defer observability to a later operations chapter.
- **Reason:** A separate observability figure keeps `FIG-11-05` focused on one warm-standby resilience scenario and gives payment operations telemetry enough room to be readable.
- **Consequences:** Chapter 11 now has six figures at `Review`. `FIG-11-05` covers warm standby, failover, failback and reconciliation. `FIG-11-06` covers observability telemetry flow and operational consumption.
- **Related chapters/files:** Chapter 11, `FIG-11-05`, `FIG-11-06`, `DIAGRAM_REGISTER.md`, `reviews/chapter-gates/CH-11-quality-gate.md`.
- **Supersedes / superseded by:** Supersedes DEC-017.

## DEC-019: Use five specification-first security teaching figures for Chapter 12

- **Status:** Superseded
- **Date:** 2026-07-01
- **Decision:** Use five planned Chapter 12 teaching figures: Online Store trust boundary view, Online Store customer authentication sequence, Horizon Bank payment authorisation matrix, Horizon Bank payment threat-model DFD and Horizon Bank payment attack tree.
- **Context:** Chapter 12 needs to teach security modelling through focused views without combining trust boundaries, identity, access control, threats, controls and data sensitivity into one unreadable diagram.
- **Alternatives considered:** Create one large security architecture diagram; defer all diagrams until Chapter 21; create diagram source immediately from draft specifications.
- **Reason:** Focused security figures match the chapter's teaching sequence and repository diagram rules. Source creation must wait for author approval of the specifications.
- **Consequences:** `FIG-12-01` through `FIG-12-05` are registered as `Planned`, with specifications under `diagrams/specifications/`. Source and exports remain pending author approval.
- **Related chapters/files:** Chapter 12, `DIAGRAM_REGISTER.md`, `diagrams/specifications/FIG-12-*`.
- **Supersedes / superseded by:** Superseded by DEC-020.

## DEC-020: Reclassify the Chapter 12 payment access matrix as a manuscript table

- **Status:** Proposed
- **Date:** 2026-07-01
- **Decision:** Retire planned figure `FIG-12-03`, do not reuse that figure ID, and present the Horizon Bank payment action access-control matrix as manuscript table `TABLE-12-01`.
- **Context:** The Chapter 12 review found that the former payment authorisation matrix is semantically tabular and should not be tracked as a required diagram or require an SVG/PNG output. The repository has a diagram register, but no separate table register. The implementation is provisional until the author explicitly approves the reclassification.
- **Alternatives considered:** Keep the matrix as `FIG-12-03`; create an SVG-only table; invent a table register during this revision.
- **Reason:** Treating the matrix as a manuscript table keeps the artefact type honest and avoids unnecessary diagram production. Avoiding a new table register keeps the change scoped to the Chapter 12 review.
- **Consequences:** Chapter 12 now has four planned figure specifications: `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05`. The retired `FIG-12-03` ID remains unused and must not be reassigned. `TABLE-12-01` is tracked in the manuscript text rather than `DIAGRAM_REGISTER.md`, provisionally pending author approval.
- **Related chapters/files:** Chapter 12, `DIAGRAM_REGISTER.md`, `diagrams/specifications/`, `STATUS.md`.
- **Supersedes / superseded by:** Supersedes DEC-019 for the Chapter 12 figure set.

## Decision template

```markdown
## DEC-NNN: Decision title

- **Status:** Proposed | Approved | Superseded | Rejected
- **Date:** YYYY-MM-DD
- **Decision:**
- **Context:**
- **Alternatives considered:**
- **Reason:**
- **Consequences:**
- **Related chapters/files:**
- **Supersedes / superseded by:**
```
