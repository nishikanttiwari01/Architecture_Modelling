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

- **Status:** Accepted
- **Date:** 2026-07-01
- **Decision:** Retire planned figure `FIG-12-03`, do not reuse that figure ID, and present the Horizon Bank payment action access-control matrix as manuscript table `TABLE-12-01`.
- **Context:** The Chapter 12 review found that the former payment authorisation matrix is semantically tabular and should not be tracked as a required diagram or require an SVG/PNG output. The repository has a diagram register, but no separate table register. The author approved the reclassification on 2026-07-02.
- **Alternatives considered:** Keep the matrix as `FIG-12-03`; create an SVG-only table; invent a table register during this revision.
- **Reason:** Treating the matrix as a manuscript table keeps the artefact type honest and avoids unnecessary diagram production. Avoiding a new table register keeps the change scoped to the Chapter 12 review.
- **Consequences:** Chapter 12 now has four figure specifications: `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05`. The retired `FIG-12-03` ID remains unused and must not be reassigned. `TABLE-12-01` is tracked in the manuscript text rather than `DIAGRAM_REGISTER.md`.
- **Related chapters/files:** Chapter 12, `DIAGRAM_REGISTER.md`, `diagrams/specifications/`, `STATUS.md`.
- **Supersedes / superseded by:** Supersedes DEC-019 for the Chapter 12 figure set.

## DEC-021: Render Chapter 13 Draw.io teaching figures from the editable mxGraph source

- **Status:** Proposed
- **Date:** 2026-07-03
- **Decision:** Use `scripts/render-drawio-diagrams.py` to produce reproducible SVG and PNG previews for the Chapter 13 Draw.io figures (`FIG-13-02` through `FIG-13-06`) directly from the editable `.drawio` mxGraph geometry, styles and text. This proposes the custom repository renderer as the Draw.io export mechanism; it is not yet the author-approved final mechanism.
- **Context:** The author approved Draw.io as the editable source type for `FIG-13-02` through `FIG-13-06`, but did not explicitly approve the custom repository renderer as the final Draw.io export mechanism. No Draw.io desktop CLI is installed in this environment, and the repository had no existing Draw.io export mechanism, so a repeatable renderer was written to produce previews from the editable source without embedding screenshots.
- **Alternatives considered:** Install and drive the Draw.io desktop CLI headlessly; hand-maintain SVG files; defer all Draw.io exports until a Draw.io CLI is available.
- **Reason:** Rendering from the mxGraph source keeps the `.drawio` file as the single editable source of truth and produces previews that correspond to that source. This mirrors the BPMN render-from-source approach recorded in `DEC-012`.
- **Clarifications:**
  - The editable `.drawio` mxGraph source remains authoritative.
  - The custom renderer produces reproducible SVG and PNG previews from the editable geometry.
  - It supports only the subset of mxGraph shapes and styles used by the Chapter 13 figures (rectangles, rounded rectangles, ellipses, plain text, straight and orthogonal connectors with optional arrowheads and labels).
  - Native Draw.io graphical opening and export-fidelity comparison remain pending.
  - The previews must not be described as verified native Draw.io exports.
  - This decision may move to `Approved` only after explicit author approval of the renderer as the final Draw.io export mechanism.
- **Consequences:** The `.drawio` files remain fully editable in Draw.io. The renderer depends on Pillow (declared in `requirements-diagrams.txt`) and selects a font deterministically (Arial preferred, DejaVu Sans fallback), reporting the selection and failing loudly if none is available. A native Draw.io graphical review of layout and export fidelity is still required before the figures are marked `Approved`, in the same spirit as the Camunda note in `DEC-012`.
- **Related chapters/files:** Chapter 13, `scripts/render-drawio-diagrams.py`, `requirements-diagrams.txt`, `.github/workflows/validate.yml`, `scripts/render-all-diagrams.ps1`, `diagrams/source/drawio/FIG-13-*.drawio`, `diagrams/exported/svg/FIG-13-*.svg`, `diagrams/exported/png/FIG-13-*.png`, `reviews/chapter-gates/CH-13-quality-gate.md`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

## DEC-022: Scope Chapter 14 as strategy-to-capability selection, not notation re-teaching

- **Status:** Proposed (awaiting explicit author approval; recorded `Approved` in error on 2026-07-03 and corrected to `Proposed` on 2026-07-04, because only the author may approve a material scope decision)
- **Date:** 2026-07-03 (proposed); status corrected 2026-07-04
- **Decision:** Write Chapter 14, the first Part III chapter, as a selection-and-combination chapter that keeps a visible thread from strategy to funded change (driver, goal, measurable outcome, stakeholder concern, capability, value stream, investment heat map and initiative traceability). Reference the capability-map, value-stream, heat-map and motivation notations already taught in Chapters 7 and 13 rather than re-teaching them.
- **Context:** Chapters 7 and 13 already introduced ArchiMate motivation views, capability maps, value streams and heat maps. Chapter 13 explicitly deferred deeper strategy and capability modelling to Chapter 14. Part III is about choosing diagrams by architecture need, so Chapter 14 must add selection, combination and traceability value without duplicating notation lessons.
- **Alternatives considered:** Re-teach each notation from first principles in Chapter 14; make Chapter 14 a pure ArchiMate strategy-and-motivation chapter; defer all figures until later.
- **Reason:** Referencing the existing notation chapters avoids duplication, keeps the chapter focused on the reader's real question (which model to reach for and how the models fit together), and preserves a single controlled capability vocabulary across views.
- **Consequences:** Chapter 14 introduces two new figures that are genuinely additive: `FIG-14-01` Strategy-to-Capability Traceability View (the goal-to-initiative thread) and `FIG-14-02` Onboarding Value Stream to Capability Cross-Map (the value-stage-to-capability grid). Both remain `Planned` with `Pending` source and export until the author approves the specifications, consistent with the diagram workflow. The chapter presents each figure's content as an inline table so it reads completely before production.
- **Related chapters/files:** Chapter 14, Chapter 7, Chapter 13, `manuscript/part-03-diagram-selection/14-business-strategy-capabilities.md`, `diagrams/specifications/FIG-14-01-horizon-bank-strategy-to-capability-traceability.md`, `diagrams/specifications/FIG-14-02-horizon-bank-onboarding-value-stream-capability-cross-map.md`, `examples/horizon-bank/capabilities.md`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

## DEC-023: Scope Chapter 15 as process model selection, not BPMN re-teaching

- **Status:** Proposed
- **Date:** 2026-07-07
- **Decision:** Write Chapter 15, Modelling Business Processes, as a selection-and-combination chapter that helps readers choose between value streams, process architecture tables, BPMN process diagrams, BPMN collaboration diagrams, focused exception views, responsibility views, UML activity diagrams and DMN decision models. Reuse Chapter 6 BPMN, Chapter 4 UML activity, Chapter 9 DMN and Chapter 13 value-stream material instead of re-teaching those notations from first principles, and include one original Chapter 15 decision guide, `FIG-15-01`, after author direction to finish the diagram work.
- **Context:** Part III is about choosing diagrams by architecture need. Chapter 6 already teaches BPMN notation, Chapter 4 already introduces UML activity diagrams, Chapter 9 separates DMN decision logic from BPMN process flow, and Chapters 13 and 14 already distinguish value streams and capabilities from process detail.
- **Alternatives considered:** Re-teach BPMN in full inside Chapter 15; create a larger Chapter 15 diagram set; keep the mixed notation selection guide only as manuscript tables.
- **Reason:** Reusing approved or drafted earlier material keeps Chapter 15 focused on the reader's real decision: which model answers the current process question, at what level of detail, and with what audience. `FIG-15-01` adds a compact visual decision path while the tables keep the fuller selection guidance readable.
- **Consequences:** Chapter 15 has one new `FIG-15-*` entry with specification, Mermaid source and SVG export. It otherwise reuses existing registered figures and source notes. Any further Chapter 15 figure requires separate author direction and the normal diagram workflow.
- **Review confirmation:** The formal Chapter 15 review on 2026-07-07 confirmed that the manuscript selection tables and worked examples are sufficient for author review. A later author instruction on 2026-07-07 requested completion of the diagram work, so `FIG-15-01` was added as an original selection guide. This does not approve `DEC-023`; it remains `Proposed` pending explicit author acceptance.
- **Related chapters/files:** Chapter 15, Chapter 4, Chapter 6, Chapter 9, Chapter 13, Chapter 14, `DIAGRAM_REGISTER.md`, `research/bpmn/omg-bpmn-2.0.2.md`, `research/uml/omg-uml-2.5.1.md`, `research/dmn/omg-dmn-1.5.md`, `research/other-modelling/open-group-business-architecture-guides-2022.md`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

## DEC-024: Add a required Chapter 16 software-structure selection guide

- **Status:** Proposed
- **Date:** 2026-07-07
- **Decision:** Create `FIG-16-01`, "Choosing the Right Software Structure View", as the required Chapter 16 selection-guide diagram. The figure uses a Mermaid decision path to help readers choose between system landscape, system context, container, component, package, class, dependency and deployment boundary views based on the architecture question.
- **Context:** Chapter 16 is a Part III selection chapter. The author explicitly requested `FIG-16-01` as a required selection-guide diagram and instructed that the diagram should not be deferred merely because a table exists.
- **Alternatives considered:** Leave the selection guidance as a manuscript table only; defer the diagram until the full Chapter 16 draft; use Draw.io for manual layout.
- **Reason:** A compact visual decision path is genuinely additive for a selection chapter. Mermaid is sufficient because the figure is a simple flowchart and follows the successful Chapter 15 selection-guide pattern.
- **Consequences:** Chapter 16 now has one original registered figure with specification, Mermaid source and SVG export. The chapter has been fully drafted and reviewed for author approval. `FIG-16-01` is at `Review`, not `Approved`, and Chapter 16 is `Ready for Author Approval`, not `Approved`.
- **Related chapters/files:** Chapter 16, Chapter 4, Chapter 5, `DIAGRAM_REGISTER.md`, `diagrams/specifications/FIG-16-01-choosing-the-right-software-structure-view.md`, `diagrams/source/mermaid/FIG-16-01-choosing-the-right-software-structure-view.mmd`, `diagrams/exported/svg/FIG-16-01-choosing-the-right-software-structure-view.svg`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

## DEC-025: Use PlantUML for the Chapter 17 interaction selection guide

- **Status:** Proposed
- **Date:** 2026-07-07
- **Decision:** Create `FIG-17-01`, "Choosing the Right User and System Interaction View", as the required Chapter 17 selection-guide diagram. The figure uses a PlantUML mind map to help readers choose between use case diagrams, user journeys, service blueprints, wireframes or screen flows, UML sequence diagrams, C4 dynamic views, BPMN collaborations, activity diagrams, state machines and API interaction views.
- **Context:** Chapter 17 is a Part III selection chapter. The latest author instruction requires PlantUML by default for all new diagrams and says Mermaid must not be used for new diagrams unless explicitly approved. Earlier Chapter 15 and Chapter 16 Mermaid diagrams remain unchanged.
- **Alternatives considered:** Use Mermaid following the earlier Chapter 17 task brief; use Draw.io for manual layout; leave the selection guidance as a manuscript table only.
- **Reason:** PlantUML satisfies the current diagram tool rule and is suitable for a compact decision guide. A manuscript table provides detailed selection guidance, while the PlantUML figure gives readers a quick first-filter path. Draw.io is not needed because the layout is readable without manual composition.
- **Consequences:** Chapter 17 has one original registered figure with specification, PlantUML source and SVG export. `FIG-17-01` is at `Review`, not `Approved`, and Chapter 17 is `Ready for Author Approval`, not `Approved`. Any later conversion to Draw.io should happen only if author review finds the PlantUML output too cramped or unsuitable for book readability.
- **Related chapters/files:** Chapter 17, Chapter 4, Chapter 5, Chapter 6, Chapter 15, Chapter 16, `DIAGRAM_REGISTER.md`, `diagrams/specifications/FIG-17-01-choosing-the-right-user-and-system-interaction-view.md`, `diagrams/source/plantuml/FIG-17-01-choosing-the-right-user-and-system-interaction-view.puml`, `diagrams/exported/svg/FIG-17-01-choosing-the-right-user-and-system-interaction-view.svg`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

## DEC-026: Scope Chapter 18 as integration and runtime view selection

- **Status:** Proposed
- **Date:** 2026-07-08
- **Decision:** Write Chapter 18, Modelling Integration and Runtime Behaviour, as a selection-and-combination chapter that helps readers choose between integration context views, API interaction views, message-flow views, UML sequence diagrams, C4 dynamic diagrams, event-flow views, queue and asynchronous processing views, error and retry views, interface catalogues and data-flow views. Reuse Chapter 4 UML, Chapter 5 C4, Chapter 6 BPMN, Chapter 10 domain-event and Chapter 17 interaction material rather than re-teaching those notations from first principles.
- **Context:** Part III is about choosing diagrams by architecture need. Chapter 17 intentionally stops before full integration design. Chapter 19 will cover data architecture, so Chapter 18 needs to connect runtime information exchange to data-flow concerns without taking over the data chapter.
- **Alternatives considered:** Re-teach sequence diagrams, C4 dynamic diagrams, BPMN message flows, CloudEvents and AsyncAPI in full inside Chapter 18; create a full diagram set immediately; leave the required mixed notation selection guide only as manuscript prose.
- **Reason:** Reusing established notation chapters keeps Chapter 18 focused on the reader's decision: which view answers the current integration question, at what runtime boundary, and for which audience. A pending `FIG-18-01` selection guide is useful, but source and export must wait for author approval of the specification under the repository diagram workflow.
- **Consequences:** Chapter 18 has one original registered figure specification, `FIG-18-01`, with source and export deferred pending author approval. The chapter includes a complete manuscript selection table and worked examples so it remains readable before the figure is produced. Any further Chapter 18 figure requires separate author direction and the normal diagram workflow.
- **Related chapters/files:** Chapter 18, Chapter 4, Chapter 5, Chapter 6, Chapter 10, Chapter 17, Chapter 19, `DIAGRAM_REGISTER.md`, `diagrams/specifications/FIG-18-01-choosing-the-right-integration-runtime-behaviour-view.md`, `research/uml/omg-uml-2.5.1.md`, `research/c4/c4-model-official.md`, `research/bpmn/omg-bpmn-2.0.2.md`, `research/domain-event/cloudevents-1.0.2.md`, `research/domain-event/asyncapi-3.1.0.md`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

## DEC-027: Scope Chapter 19 as data architecture view selection

- **Status:** Proposed
- **Date:** 2026-07-10
- **Decision:** Write Chapter 19, Modelling Data Architecture, as a selection-and-combination chapter that helps readers choose between conceptual, logical and physical data views, ERDs, DFDs, lineage views, ownership matrices, lifecycle views and master/reference data catalogues. Reuse Chapter 8 data-modelling foundations rather than re-teaching each technique, and specify one original PlantUML selection guide, `FIG-19-01`.
- **Context:** Part III helps readers choose diagrams by architecture need. Chapter 8 already explains data-modelling levels, ERDs, DFDs, lineage and lifecycle. Chapter 18 covers runtime integration, while Chapter 20 will cover infrastructure and deployment. Chapter 19 must connect structure, movement and governance without mixing those concerns or duplicating the surrounding chapters.
- **Alternatives considered:** Re-teach Chapter 8 in full; use only a manuscript table; create diagram source before author approval; combine structure, movement, governance and infrastructure on one diagram.
- **Reason:** A selection chapter gives beginners a clear route from question to view and shows how focused models work together. The manuscript table contains detailed guidance, while the planned figure provides a compact first filter. Deferring source and export follows the specification-first diagram policy.
- **Consequences:** Chapter 19 has one registered figure specification with source and export pending author approval. Existing data research sources are reused. The chapter remains complete and reviewable through its table, examples, exercise and checklist. Any additional figure requires separate justification and the normal diagram workflow.
- **Related chapters/files:** Chapter 8, Chapter 18, Chapter 19, Chapter 20, `DIAGRAM_REGISTER.md`, `diagrams/specifications/FIG-19-01-choosing-the-right-data-architecture-view.md`, `research/data/`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

## DEC-028: Scope Chapter 20 as infrastructure and deployment view selection

- **Status:** Proposed
- **Date:** 2026-07-10
- **Decision:** Write Chapter 20 as a selection-and-combination chapter for runtime deployment, network topology, cloud architecture, Kubernetes deployment, environment comparison, availability, recovery, ownership and observability views. Reuse Chapter 11 foundations and specify one PlantUML selection guide, `FIG-20-01`.
- **Context:** Chapter 11 already teaches the terminology. Chapter 19 covers data architecture and Chapter 21 covers security, so Chapter 20 must expose placement and operational evidence without absorbing data structures, process flows or threat modelling.
- **Alternatives considered:** Re-teach Chapter 11; use only a table; create source before specification approval; combine every concern in one diagram.
- **Reason:** A selection chapter moves beginners from an operational question to a suitable view and necessary companions. Deferring source follows diagram policy.
- **Consequences:** The author authorised figure production. The registered figure has PlantUML source and SVG export at `Review`, not `Approved`. Existing official research is reused.
- **Related chapters/files:** Chapters 11, 19, 20 and 21, `DIAGRAM_REGISTER.md`, `diagrams/specifications/FIG-20-01-choosing-the-right-infrastructure-deployment-view.md`, `research/infrastructure/`.
- **Supersedes / superseded by:** Not superseded. Remains `Proposed` pending explicit author approval.

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
