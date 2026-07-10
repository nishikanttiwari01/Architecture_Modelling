# Changelog

All notable repository and manuscript changes are recorded here. This is a project history, not a replacement for Git commits.

## 2026-07-10

### Completed Chapter 19 data architecture modelling

- Expanded Chapter 19, **Modelling Data Architecture**, from scaffold to a complete Part
  III selection chapter covering conceptual, logical and physical data views, ERDs,
  DFDs, lineage, ownership and stewardship, master and reference data, lifecycle,
  privacy, retention and data quality.
- Added `FIG-19-01`, "Choosing the Right Data Architecture View", to the diagram register
  and created its specification, with source/export deferred pending author approval.
- Created Chapter 19 technical, beginner, consistency and final review records, plus
  `reviews/chapter-gates/CH-19-quality-gate.md`.
- Updated `STATUS.md` so Chapter 19 is `Ready for Author Approval`, not `Approved`.
- Recorded `DEC-027` as `Proposed` and added controlled glossary terms for data
  ownership, stewardship, catalogues, master, reference and transaction data.
- Reused five registered data-modelling source notes; no new source was required.

## 2026-07-08

### Completed Chapter 18 integration and runtime behaviour modelling

- Expanded Chapter 18, **Modelling Integration and Runtime Behaviour**, from scaffold to a complete Part III selection chapter covering integration context views, API interaction views, message-flow views, UML sequence diagrams, C4 dynamic diagrams, event-flow views, queue and asynchronous processing views, error and retry views, interface catalogues and data-flow boundaries.
- Added `FIG-18-01`, "Choosing the Right Integration and Runtime Behaviour View", to the diagram register and created its specification, with source/export deferred pending author approval.
- Created `reviews/chapter-gates/CH-18-quality-gate.md`.
- Updated `STATUS.md` so Chapter 18 is `Ready for Author Approval`, not `Approved`.
- Recorded `DEC-026` as `Proposed`, noting the Chapter 18 scope and the deferred PlantUML selection-guide decision.
- Added glossary terms for integration context views, synchronous and asynchronous interaction, interface catalogues, idempotency and dead-letter queues.
- Reused existing registered UML, C4, BPMN, CloudEvents and AsyncAPI source notes; no new source notes were added.

### Normalised Chapter 17 formatting

- Hard-wrapped Chapter 17 prose and review evidence Markdown for readability while
  preserving wording, status and meaning.
- Added a follow-up formatting-only correction that includes the Chapter 17 PlantUML
  source file in the committed line-break changes.
- Rewrote the Chapter 17 manuscript, review evidence and PlantUML source files with
  normal LF line endings and real physical Markdown or PlantUML line breaks.
- Left Chapter 17 at `Ready for Author Approval`, `FIG-17-01` at `Review` and
  `DEC-025` at `Proposed`.

## 2026-07-07

### Completed Chapter 17 user and system interaction modelling

- Expanded Chapter 17, **Modelling User and System Interaction**, from scaffold to a complete Part III selection chapter covering use case diagrams, user journeys, service blueprints, wireframes, screen flows, UML sequence diagrams, C4 dynamic views, BPMN collaborations, activity diagrams, state machines and API interaction views.
- Added `FIG-17-01`, "Choosing the Right User and System Interaction View", as a PlantUML decision-guide diagram, with specification, editable source and SVG export, and kept the figure at `Review`, not `Approved`.
- Created Chapter 17 technical, beginner, consistency and final review records, plus `reviews/chapter-gates/CH-17-quality-gate.md`.
- Updated `STATUS.md` so Chapter 17 is `Ready for Author Approval`, not `Approved`.
- Recorded `DEC-025` as `Proposed`, noting the Chapter 17 scope and the PlantUML diagram decision.
- Reused existing registered UML, C4 and BPMN source notes; no new source notes were added.

### Completed Chapter 16 software structure modelling

- Expanded Chapter 16, **Modelling Software Structure**, from scaffold to a complete Part III selection chapter covering system landscape, system context, container, component, package, class, dependency and deployment views.
- Integrated `FIG-16-01` into the chapter with the required caption and surrounding explanatory prose, while keeping the figure at `Review`, not `Approved`.
- Created Chapter 16 technical, beginner, consistency and final review records, plus `reviews/chapter-gates/CH-16-quality-gate.md`.
- Updated `STATUS.md` so Chapter 16 is `Ready for Author Approval`, not `Approved`.
- Updated `DEC-024` consequences to reflect the completed chapter while keeping the decision `Proposed`.
- Reused existing registered C4 and UML source notes; no new source notes were added.

### Created Chapter 16 selection-guide diagram

- Added `FIG-16-01`, "Choosing the Right Software Structure View", as the required Chapter 16 visual guide for selecting between system landscape, system context, container, component, package, class, dependency and deployment boundary views.
- Created the diagram specification, Mermaid source and SVG export, and registered the figure at `Review`, not `Approved`.
- Added the figure reference and caption to the Chapter 16 selection section while keeping the chapter itself at `Planned`.
- Reused existing registered C4 and UML source notes; no new source notes were added.
- Recorded the diagram decision in `DEC-024` and updated `STATUS.md`.

### Cleaned Chapter 15 review evidence formatting

- Properly reformatted Chapter 15 review evidence and FIG-15-01 Mermaid source with real Markdown/Mermaid line breaks, correcting the earlier hygiene attempt in `887c9fe`.
- Rewrote the Chapter 15 evidence commit metadata as line-broken Markdown bullet sections so Git object content renders with real line breaks on GitHub.

### Completed Chapter 15 formal review

- Created Chapter 15 technical, beginner, consistency and final review records, plus the Chapter 15 quality gate.
- Confirmed the chapter remains a process-model selection chapter, with clear distinctions across value stream, process architecture, BPMN process, BPMN collaboration, focused BPMN exception view, responsibility matrix and swimlanes, UML activity, DMN, and UML sequence or C4 dynamic views.
- Confirmed all reused figures are registered and all source keys are registered; no new sources were added.
- Added `FIG-15-01`, "Choosing the Right Business Process Model", with registered specification, Mermaid source and SVG export.
- Recorded the final Chapter 15 diagram decision in `DEC-023` while keeping the decision `Proposed` pending explicit author acceptance.
- Removed draft scaffolding from the reviewed chapter and kept Chapter 15 at `Ready for Author Approval`, not `Approved`. `FIG-15-01` remains at `Review`.

### Refined Chapter 15 business process modelling draft

- Added a short bridge from Chapter 14 to Chapter 15, clarifying that capabilities say what the business needs while process models show how work moves through time, roles, decisions, waits and exceptions.
- Split or tightened the wider Chapter 15 tables for process architecture, process levels, responsibility, process metrics, process-to-capability traceability and model selection.
- Added a clear beginner choice point in the worked example for choosing value stream, BPMN collaboration, DMN, UML activity, or C4/UML sequence views.
- Checked reused figure references against the existing diagram register and kept the chapter within `DEC-023`: no `FIG-15-*` diagram, specification, source, export or preview was created, and nothing was marked `Approved`.

### Drafted Chapter 15, Modelling Business Processes

- Expanded Chapter 15 from scaffold to a complete draft and moved it from `Planned` to `Drafting`.
- Framed the chapter as a Part III selection-and-combination chapter, not a re-teaching of BPMN: process architecture, process levels, BPMN process and collaboration selection, swimlanes and responsibility views, exceptions and controls, process metrics, process-to-capability traceability, model selection, worked examples, common mistakes, key takeaways, exercise, checklist and references.
- Reused existing registered figures (`FIG-06-01`, `FIG-06-02`, `FIG-06-03`, `FIG-04-05`, `FIG-09-04` and `FIG-13-02`) and existing source notes (`[OMG-BPMN]`, `[OMG-UML]`, `[OMG-DMN-1.5]` and `[OPEN-GROUP-BIZARCH-GUIDES-2022]`).
- Added glossary terms for process architecture, process level, swimlane, process metric and straight-through processing.
- Recorded `DEC-023` as `Proposed`, making the Chapter 15 scope boundary explicit and deferring any visual Chapter 15 selection guide until a specification is requested and approved.
- Updated `STATUS.md`. No `FIG-15-*` entry, diagram specification, source or export was created. Nothing was marked `Approved`.

## 2026-07-04

### Revised Chapter 14 strategy and capability modelling

- Reviewed Chapter 14 against baseline `7d8947dc07c7c6bd4d2a7e6d5e8513d24f2f5e4b` and moved it from `Drafting` to `Revision Required` with an interim quality-gate score of `8.2/10`.
- Reclassified `FIG-14-01` as an ArchiMate-informed strategy traceability teaching view; its connectors are simplified teaching links, not formal ArchiMate relationship notation. Recorded the ArchiMate 4 relationship-verification limitation in `research/archimate/open-group-archimate-4.md`: the licensed specification text is out of scope for AI-assisted drafting, so formal relationship types and directions are not asserted; a licensed human reviewer must confirm them before any upgrade to a formal view.
- Added an outcome-measure table (`OUT-14-01` to `OUT-14-04`) with metric, baseline, target, scope, time horizon, measure owner and evidence source, using clearly illustrative placeholders, and removed unqualified phrases such as "near real time" and "reduced against baseline" from the outcome claims.
- Separated the heat map into strategic importance, current health or pain, current investment status, proposed priority, delivery constraint and final funding, with no composite score, and stated that a proposed priority is a recommendation, not proof of funding.
- Replaced the categorical goal-to-initiative rule with nuanced guidance: a goal with no work package is a review finding that may reflect deferral, business-as-usual delivery, a policy response or a portfolio gap, not automatically an invalid goal.
- Added the controlled `Executive Sponsor` role to `examples/horizon-bank/actors.md` and replaced `Sponsor and executive`.
- Recorded controlled capability levelling in `examples/horizon-bank/capabilities.md`, including levels, parents, the decomposition/contribution/dependency distinction, and the Financial Crime Screening versus Payment Screening peer scoping to avoid double counting.
- Added stable identifiers (`DRV`, `GOAL`, `OUT`, `COA`, `WP`) and one master traceability table shared by the manuscript and `FIG-14-01`.
- Redesigned `FIG-14-02` as a genuine capability-by-stage matrix with an exact cell-by-cell dataset and strategic importance assessed against `GOAL-14-01` only; kept funding, priority, delivery risk and composite scores out of it.
- Removed the draft-only `Planned chapter structure` and `Drafting notes` sections (permitted at the `Revision Required` production status); retained the `check-structure.py`-required `Required models and artefacts`, `Worked examples` and `Source requirements` sections with reader-facing content, matching Chapter 13.
- Added glossary rows for Course of Action, Work Package, capability levelling and value stream to capability cross-map.
- Created Chapter 14 technical, beginner, consistency and final review records (`chapter-14-review-2026-07-04.md`) and the interim gate `reviews/chapter-gates/CH-14-quality-gate.md`.
- Changed `DEC-022` from `Approved` to `Proposed`, because only the author may approve a material scope decision; retained its content.
- Updated `DIAGRAM_REGISTER.md` notation for both figures. Both figures remain `Planned` with `Pending` source and export. No diagram source or export was created. Nothing was marked `Approved`. Chapter 15 was not started.

## 2026-07-03

### Drafted Chapter 14, Modelling Business Strategy and Capabilities

- Wrote the full Chapter 14 draft, the first chapter of Part III, moving it from `Planned` to `Drafting`.
- Framed the chapter as a selection-and-combination chapter that keeps a visible thread from strategy to funded change: driver and goal, measurable outcome, stakeholder concern, capability, value stream, investment heat map and initiative traceability.
- Covered all planned sections: goals, drivers and outcomes (motivation model); stakeholder concerns; capability maps for planning; value streams and the value-stream-to-capability cross-map; investment heat maps; traceability to initiatives; recommended notation combinations; a selection table; a Horizon Bank worked example; common mistakes; and the chapter endings.
- Referenced, rather than re-taught, the Chapter 7 and Chapter 13 capability-map, value-stream, heat-map and motivation figures.
- Reused only registered sources (`[OPEN-GROUP-ARCHIMATE-4]`, `[OPEN-GROUP-BIZARCH-GUIDES-2022]`, `[ISO-42010]`) and controlled example names from `examples/horizon-bank/capabilities.md`, `examples/horizon-bank/actors.md` and `examples/simple-online-store/README.md`; no new source note was required.
- Registered two figures in `DIAGRAM_REGISTER.md` and wrote their specifications: `FIG-14-01` Horizon Bank Strategy-to-Capability Traceability View and `FIG-14-02` Horizon Bank Onboarding Value Stream to Capability Cross-Map. Both remain `Planned` with `Pending` source and export; editable source and SVG export are deferred until the author approves the specifications, so no image embeds point to unrendered files.
- Recorded `DEC-022` for the Chapter 14 scope boundary against Chapters 7 and 13.
- Updated `STATUS.md` (Chapter 14 row and next-task note) and this changelog. Nothing was marked `Approved`.

### Completed Chapter 13 final review

- Completed the final technical, content, diagram and quality-gate review of Chapter 13, **Other Useful Modelling Approaches**, against commit `bd6dc47`.
- Confirmed all recorded technical, beginner and consistency findings resolved; performed a human visual and page-fit inspection of all six figures.
- Verified figure titles and controlled Horizon Bank and Online Store names match across the manuscript, specifications, sources, exports and `DIAGRAM_REGISTER.md`.
- Removed the reader-facing `Planned chapter structure` and `Drafting notes` sections on moving to a production status, consistent with `DEC-010` and with Chapters 1, 11 and 12; no reviewed prose was rewritten.
- Updated the Chapter 13 review records and the quality gate with a recalculated score of 9.0 and a recommendation.
- Moved Chapter 13 from `Diagramming` to `Ready for Author Approval`. `FIG-13-01` through `FIG-13-06` remain `Review`. `DEC-021` remains `Proposed`. Nothing was marked `Approved`. Chapter 14 was not started.
- Open author decisions: author approval; native Draw.io graphical-open and export-fidelity comparison (`DEC-021`); final book-page layout placement of the wider landscape figures (`DEC-014`).

### Applied focused Chapter 13 diagram workflow corrections

- Corrected the `FIG-13-02` trigger-label placement so the `triggers` label sits clearly above the single Retail Customer to Need understood connector and touches no box, heading or boundary; regenerated its SVG and PNG and visually inspected them.
- Added `examples/horizon-bank/capabilities.md` as a controlled source reference in the `FIG-13-02` specification.
- Integrated the Draw.io renderer into the reproducible workflow: `.github/workflows/validate.yml` now syntax-checks all scripts with `python -m compileall -q scripts`, installs the pinned dependency, runs the complete render script and checks for stale exports.
- Declared the Pillow dependency in `requirements-diagrams.txt` (pinned) and documented it in `scripts/README.md` and the renderer docstring.
- `scripts/render-all-diagrams.ps1` now invokes `render-drawio-diagrams.py` and fails when it fails (exit code not suppressed).
- Added deterministic cross-platform font selection to `render-drawio-diagrams.py` (Arial preferred, DejaVu Sans fallback); it reports the selected font and fails loudly if none is available. Windows Arial output is unchanged, so the exports stay byte-stable.
- Changed `DEC-021` status from `Approved` to `Proposed`: the author approved Draw.io as the source type but not the custom renderer as the final export mechanism; native Draw.io graphical-open and export-fidelity review remain pending, and the previews must not be described as verified native Draw.io exports.
- Changed the Owner of `FIG-13-01` through `FIG-13-06` from `Codex` to `Claude` in `DIAGRAM_REGISTER.md`.
- Chapter 13 remains `Diagramming`; all six figures remain `Review`; nothing was marked `Approved`; Chapter 14 was not started.

### Produced Chapter 13 modelling approach diagrams

- Moved Chapter 13, **Other Useful Modelling Approaches**, from `Revision Required` to `Diagramming` after the author approved the revised `FIG-13-01` through `FIG-13-06` specifications for production.
- Created `FIG-13-01` Online Store SysML-style Requirement Traceability View as a PlantUML source with SVG and PNG exports.
- Created `FIG-13-02` through `FIG-13-06` (customer onboarding value stream, application landscape map, platform evolution roadmap, capability heat map and payment modernisation Wardley map) as editable Draw.io sources with SVG and PNG exports.
- Added `scripts/render-drawio-diagrams.py` to render the Draw.io figures to SVG and PNG from the editable mxGraph source, recorded as `DEC-021`, because no Draw.io desktop CLI is available in this environment.
- Embedded the six figures in the Chapter 13 manuscript with captions, accessibility text and limitation notes, and updated the required-artefacts and drafting notes.
- Set `FIG-13-01` through `FIG-13-06` to `Review` in `DIAGRAM_REGISTER.md` with real source and export paths. No figure is `Approved`.
- Aligned the `FIG-13-02` specification with the manuscript by adding the controlled capability `Relationship Management`; recorded the finding in the consistency review.
- Updated the Chapter 13 technical, beginner, consistency and final review records and the interim quality gate, which remains open for author review.
- Chapter 14 was not started.

## 2026-07-02

### Revised Chapter 13 after review

- Moved Chapter 13, **Other Useful Modelling Approaches**, to `Revision Required` while applying review findings.
- Corrected SysML-style traceability, value-stream stages, capability-map guidance, integration landscape wording, roadmap states, heat-map scoring, Wardley-map components and ADR guidance.
- Added controlled Horizon Bank capability and system lifecycle records.
- Added official Open Group business architecture guide source notes and a repository-local heat-map scoring convention note.
- Revised `FIG-13-01` through `FIG-13-06` specifications only; no Chapter 13 diagram source or exports were created, and all six figures remain `Planned`.
- Added Chapter 13 review records and an interim quality gate.
- Applied a focused follow-up correction to classify each Chapter 13 approach by formality, fix `FIG-13-01` verification semantics, complete the integration landscape table, make `FIG-13-03` relationships precise, correct `FIG-13-05` source references and define `FIG-13-06` Wardley component positions.

### Approved Chapter 12 Security Modelling

- Recorded author approval for Chapter 12, **Security Modelling**, with final quality score 9.1.
- Kept `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` at `Review`, not `Approved`.
- Removed reader-facing draft scaffolding from the approved Chapter 12 manuscript.
- Set Chapter 13, **Other Useful Modelling Approaches**, as the next chapter.

### Drafted Chapter 13 Other Useful Modelling Approaches

- Expanded Chapter 13 from scaffold to a complete first draft covering SysML, capability maps, value streams, application landscapes, integration landscapes, roadmaps, heat maps, Wardley maps and ADRs.
- Added source notes for OMG SysML 2.0, official Wardley Maps material and Nygard's ADR article.
- Registered `FIG-13-01` through `FIG-13-06` and created diagram specifications only; source and exports remain deferred pending author approval.
- Added Chapter 13 glossary terms and source-register entries.
- Moved Chapter 13 to `Diagramming`.

### Applied focused Chapter 12 FIG-12-04 repair-presentation correction

- Updated `FIG-12-04` so the Authorised Operations Interface presents the assigned repair case and permitted payment context to the Operations Analyst before the analyst submits a controlled repair action through the same interface.
- Regenerated the `FIG-12-04` SVG and PNG exports and updated Chapter 12 review evidence. Chapter 12 remains `Diagramming`; all active Chapter 12 figures remain `Review`.

### Applied final Chapter 12 diagram correction pass

- Corrected `FIG-12-01` so the public-network entry is not described as authenticated and application validation responsibilities remain inside the application runtime.
- Refined `FIG-12-04` routing and semantics, including the Digital Channel Access Context, privileged-user presentation flows and the Approved Event Consumer path for `T12-06`.
- Corrected `FIG-12-05` so `T12-08` uses a structural AND node and excluded `T12-04` and `T12-06` appear only in the legend.
- Updated Chapter 12 manuscript text, specifications, register and review evidence while keeping Chapter 12 in `Diagramming` and all Chapter 12 diagrams in `Review`.

### Produced Chapter 12 security diagrams

- Recorded author acceptance of `DEC-020`, keeping `TABLE-12-01` as a manuscript table and leaving retired `FIG-12-03` unused.
- Created PlantUML source, SVG exports and PNG previews for `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05`.
- Added Chapter 12 figure references, captions, accessibility text and limitation statements to the manuscript.
- Moved the four Chapter 12 figures to `Review`, not `Approved`, and moved Chapter 12 to `Diagramming`.

### Corrected Chapter 12 threat traceability

- Corrected Chapter 12 threat IDs so each distinct scenario has one unique ID from `T12-01` through `T12-08`.
- Added `T12-07` and `T12-08` to the Horizon Bank control map and `FIG-12-04` threat labels.
- Removed non-causal `T12-04` and `T12-06` branches from the `FIG-12-05` attack-tree specification while keeping them in the DFD and control map.
- Registered the Horizon Bank `Customer Support Agent` actor.
- Corrected identity-context flow wording so the Retail Customer supplies a session reference, while Horizon Digital Channels supplies validated subject and entitlement context to the Payments Platform.
- Recorded that `TABLE-12-01` remained provisional pending author approval of `DEC-020`.

## 2026-07-01

### Revised Chapter 12 after security modelling review

- Moved Chapter 12, **Security Modelling**, to `Revision Required` while applying review findings.
- Rewrote the chapter to add a security-modelling foundation, explicit depth boundary, access authorisation terminology, control traceability, residual risk and privacy modelling.
- Retired planned figure `FIG-12-03` and replaced it with manuscript table `TABLE-12-01`.
- Revised `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` specifications without creating diagram source or exports.
- Added NIST Privacy Framework 1.0 and Schneier attack-tree source notes and updated Chapter 12 source/version records.
- Added Chapter 12 technical, beginner, consistency and final review records.

### Drafted Chapter 12 Security Modelling

- Expanded Chapter 12, **Security Modelling**, from scaffold to a complete first prose draft.
- Covered security viewpoints, trust boundaries, authentication flows, authorisation models, threat modelling, STRIDE, attack trees, threat-model DFDs, security control mapping, privacy and data classification.
- Added five Chapter 12 diagram specifications and registered `FIG-12-01` through `FIG-12-05`.
- Kept Chapter 12 diagram source and exports deferred pending author approval of the specifications.
- Added Chapter 12 glossary terms for authentication, authorisation, threats, controls, STRIDE, attack trees, policy decision and enforcement points, and data classification.
- Moved Chapter 12 to `Diagramming`.

### Approved Chapter 11 Infrastructure and Deployment Modelling

- Recorded author approval for Chapter 11, **Infrastructure and Deployment Modelling**, with final quality score 9.1.
- Kept `FIG-11-01` through `FIG-11-06` at `Review`, not `Approved`.
- Recorded that final page-layout review remains pending, particularly for `FIG-11-03`, `FIG-11-05` and `FIG-11-06`.
- Set Chapter 12, **Security Modelling**, as the next current chapter.

### Began Chapter 12 Security Modelling

- Moved Chapter 12, **Security Modelling**, to `Researching`.
- Added initial Chapter 12 source keys for NIST, OWASP and Microsoft security modelling guidance.
- Recorded the Chapter 11 approval commit reference in `RESUME.md`.

### Completed missing Chapter 11 deployment modelling revisions

- Completed the remaining Chapter 11 author-review revisions and returned Chapter 11, **Infrastructure and Deployment Modelling**, to `Ready for Author Approval` with final quality score 9.1.
- Corrected the prerequisites to Chapter 4 UML, Chapter 5 C4 Model and Chapter 10 Domain and Event Modelling.
- Added a dedicated logical-versus-physical deployment section with a comparison table and Online Store worked example.
- Updated Kubernetes guidance for Deployment, ReplicaSet, Pod, StatefulSet, Gateway API and Ingress, and rerendered `FIG-11-03`.
- Finalised `FIG-11-05` as one warm-standby scenario with failover trigger, failback, data reconciliation, dependency readiness, backup and resilience cautions.
- Added `FIG-11-06`, **Horizon Bank Payment Observability View**, with specification, PlantUML source, SVG export, PNG preview, manuscript reference, accessibility text and diagram-register entry.
- Added cloud responsibility, capacity and scalability, environment, and practical infrastructure diagram tooling guidance.
- Corrected the NIST SP 800-34 Revision 1 source note to record it as historical official NIST guidance used informatively.
- Updated `DIAGRAM_REGISTER.md`, `SOURCE_REGISTER.md`, `GLOSSARY.md`, `DECISIONS.md`, `STATUS.md`, `RESUME.md` and the Chapter 11 quality gate. `FIG-11-01` through `FIG-11-06` remain at `Review`.

### Revised Chapter 11 after author review

- Returned Chapter 11, **Infrastructure and Deployment Modelling**, to `Revision Required` during corrections, then back to `Ready for Author Approval` after review findings and checks were completed.
- Corrected Kubernetes guidance and `FIG-11-03` to show Gateway API, Gateway, HTTPRoute, Services, Deployments, ReplicaSets and Pods with accurate responsibility.
- Added logical versus physical deployment guidance, tightened UML deployment terminology, and added cloud responsibility plus capacity and scalability guidance.
- Updated `FIG-11-02` to remove routine direct operations-to-database access and updated `FIG-11-05` to show telemetry emission, collection, processing/export, backend and operational alerting.
- Renamed `FIG-11-04` to **Horizon Bank Hybrid Infrastructure and Placement View** and updated the manuscript, register, specification, PlantUML source and exports.
- Updated Kubernetes and UML source notes, `SOURCE_REGISTER.md`, `GLOSSARY.md`, Chapter 11 reviews and the Chapter 11 quality gate.

## 2026-06-30

### Completed Chapter 11 Infrastructure and Deployment Modelling

- Created PlantUML sources, SVG exports and PNG previews for `FIG-11-01` through `FIG-11-05`.
- Inserted the five Chapter 11 figures into the manuscript with captions, reading guidance and accessibility text.
- Moved Chapter 11, **Infrastructure and Deployment Modelling**, to `Ready for Author Approval`.
- Moved `FIG-11-01` through `FIG-11-05` to `Review`, not `Approved`.
- Added the Chapter 11 quality gate and recorded visual review notes for the rendered infrastructure figures.

### Completed Chapter 11 Infrastructure and Deployment Modelling research and draft

- Expanded Chapter 11, **Infrastructure and Deployment Modelling**, from scaffold to a complete first prose draft.
- Added primary source notes for NIST cloud terminology, NIST contingency planning, Kubernetes concepts, AWS Well-Architected reliability guidance and OpenTelemetry observability concepts.
- Registered Chapter 11 source keys in `SOURCE_REGISTER.md` and added infrastructure, deployment, Kubernetes, resilience and observability terms to `GLOSSARY.md`.
- Added and registered Chapter 11 diagram specifications for `FIG-11-01` through `FIG-11-05`.
- Moved Chapter 11 to `Diagramming`, with diagram source and export creation deferred pending author approval of the specifications.

### Approved Chapter 10 Domain and Event Modelling

- Recorded author approval for Chapter 10, **Domain and Event Modelling**, with final quality score 9.1.
- Corrected `FIG-10-04` so the Core Deposit System response is labelled `posting confirmed`, then rerendered the SVG and PNG outputs.
- Updated the `PaymentPosted` event-catalogue entry with the approved business meaning and trigger.
- Confirmed `FIG-10-01` through `FIG-10-04` remain at `Review`, not `Approved`.
- Set Chapter 11, **Infrastructure and Deployment Modelling**, as the current chapter and moved it to `Researching`.

### Completed Chapter 10 Domain and Event Modelling draft

- Expanded Chapter 10, **Domain and Event Modelling**, from scaffold to a complete prose draft.
- Covered domain models, DDD vocabulary, subdomains, bounded contexts, context maps, aggregates, entities, value objects, domain events, EventStorming, event-driven architecture diagrams and event catalogues.
- Added four Chapter 10 diagram specifications and registered `FIG-10-01` through `FIG-10-04`.
- Kept diagram source and export creation deferred pending author approval of the Chapter 10 diagram specifications.
- Added an interim Chapter 10 quality gate documenting the diagram-source blocker.
- Moved Chapter 10 to `Under Review` with research and draft coverage complete, and with diagram source creation blocked pending author approval of specifications.

### Completed Chapter 10 final revision and diagram set

- Corrected Chapter 10 to distinguish strategic DDD and tactical DDD, including core, supporting and generic subdomains, aggregate roots, repositories and domain services.
- Strengthened context-map guidance with upstream/downstream, Customer/Supplier, Conformist, Anti-Corruption Layer, Open Host Service, Published Language and Separate Ways.
- Corrected CloudEvents guidance so only `id`, `source`, `specversion` and `type` are listed as required attributes in CloudEvents 1.0.2, with `time` optional.
- Added runtime event guidance for delivery, duplicates, idempotency, ordering, correlation, causation, retries, dead letters, replay safety, schema compatibility, eventual consistency and privacy.
- Distinguished event-driven architecture from Event Sourcing and CQRS.
- Added practical tooling guidance and a `PaymentPosted` event-catalogue entry.
- Updated all four Chapter 10 diagram specifications, created PlantUML sources, rendered SVG exports and PNG previews, and inserted all four figures into the chapter.
- Moved `FIG-10-01` through `FIG-10-04` to `Review` and moved Chapter 10 to `Ready for Author Approval` with final quality score 9.1.

### Approved Chapter 9 Decision Modelling and DMN

- Recorded author approval for Chapter 9, **Decision Modelling and DMN**, with final quality score 9.1.
- Confirmed `FIG-09-01` through `FIG-09-04` remain at `Review`, not `Approved`.
- Recorded that final book-page layout review remains pending for Chapter 9 diagrams, particularly `FIG-09-03`.
- Set Chapter 10, **Domain and Event Modelling**, as the current chapter.

### Began Chapter 10 Domain and Event Modelling research

- Moved Chapter 10, **Domain and Event Modelling**, to `Researching`.
- Added primary source notes for Domain-Driven Design, EventStorming, CloudEvents 1.0.2 and AsyncAPI 3.1.0.
- Registered the Chapter 10 source keys in `SOURCE_REGISTER.md`.
- Added initial Chapter 10 glossary terms for domain and event modelling.

### Corrected Chapter 9 final review findings

- Corrected FEEL list literal examples to use square brackets and clarified the difference from decision-table unary-test alternatives.
- Corrected `FIG-09-02` so restricted and unrestricted product paths both check stock.
- Corrected `FIG-09-03` to use direct information-requirement arrows into `Determine Payment Route` without an invented connector.
- Labelled the `FIG-09-04` BPMN-to-DMN invocation and DMN-to-BPMN result arrows, regenerated changed figure exports and refreshed the Chapter 9 quality gate.

### Completed Chapter 9 Decision Modelling and DMN

- Completed Chapter 9, **Decision Modelling and DMN**, and moved it to `Ready for Author Approval`.
- Added formal DMN 1.5 coverage for decision requirements, decision logic, FEEL, decision-table structure, hit policies, quality checks, DRD relationships, BPMN/DMN integration and decision governance.
- Added official Camunda and Trisotech DMN tool source notes and registered them.
- Added four Chapter 9 diagram specifications, PlantUML sources, SVG exports and PNG previews.
- Recorded the Chapter 9 diagram-source decision in `DEC-015`.
- Created the Chapter 9 quality gate with an average score above 9.0 and no category below 8.5.

### Began Chapter 9 Decision Modelling draft

- Expanded Chapter 9, **Decision Modelling and DMN**, from scaffold to a first prose draft.
- Rechecked official OMG DMN pages and kept DMN 1.5 as the formal standard source, with later beta material treated as informational.
- Moved Chapter 9 status to `Drafting`; diagram specifications remain pending and no Chapter 9 diagram source was created.

### Approved Chapter 8 Data Modelling

- Recorded author approval for Chapter 8, **Data Modelling**, with final quality score 9.1.
- Confirmed six Chapter 8 figures are completed and remain at `Review` pending final page-layout review.
- Confirmed the final DFD notation correction for `FIG-08-04` is verified.
- Set Chapter 9, **Decision Modelling and DMN**, as the current next chapter.

### Began Chapter 9 Decision Modelling research

- Verified the current formal OMG DMN source as DMN 1.5 before drafting.
- Added the `[OMG-DMN-1.5]` source note and source-register entry.
- Moved Chapter 9 to `Researching`.

### Corrected Chapter 8 DFD notation

- Updated `FIG-08-04` so payment authorisation and shipment data are shown as labelled directional arrows, not separate data-flow boxes.
- Regenerated the `FIG-08-04` SVG and PNG exports and refreshed the Chapter 8 quality gate.

### Revised Chapter 8 data flow, lineage and lifecycle modelling

- Corrected `FIG-08-04` to show explicit directional payment authorisation and shipment data flows.
- Corrected `FIG-08-05` so screening result and posting result feed the consolidated payment status event and remain traceable to the Payment data product.
- Clarified `FIG-08-03` as a relational order implementation model rather than a fully DBMS-specific physical model.
- Added `FIG-08-06`, Horizon Bank payment instruction data lifecycle, with specification, PlantUML source, SVG export and PNG preview.
- Updated Chapter 8 prose, captions, diagram register, glossary, status, resume state and quality gate.

### Completed Chapter 8 Data Modelling draft

- Drafted Chapter 8, **Data Modelling**, using the Chapter 5 production pattern.
- Added five Chapter 8 diagram specifications, PlantUML sources and register entries for conceptual, logical, physical, data-flow and lineage views.
- Added data modelling source notes for Chen, Codd, W3C PROV-DM, DAMA-DMBOK2 and DeMarco, and registered them in `SOURCE_REGISTER.md`.
- Added data modelling glossary terms for conceptual, logical and physical models, ERDs, DFDs, keys, cardinality, optionality and canonical/local models.
- Moved Chapters 6 and 7 to `Approved` following author instruction, while keeping all diagram entries at `Review`.
- Recorded the decision to keep diagrams at `Review` until the final page-layout pass.

### Added practical BPMN and ArchiMate tool guidance

- Added Chapter 6 guidance on semantic BPMN modellers versus generic drawing tools, including Camunda Desktop Modeler, Bizagi Modeler, diagrams.net, SAP Signavio, Camunda Web Modeler and Visual Paradigm.
- Added Chapter 7 guidance on semantic ArchiMate repositories, general drawing tools and diagrams-as-code tools, including free and paid tool comparison tables.
- Added official BPMN and ArchiMate tool source notes and registered `[BPMN-TOOL-GUIDANCE-2026]` and `[ARCHIMATE-TOOL-GUIDANCE-2026]`.
- Polished `FIG-07-01`, `FIG-07-02`, `FIG-07-05` and `FIG-07-06`, then regenerated SVG exports and PNG previews.
- Moved Chapter 6 back to `Under Review` because approved prose changed.

## 2026-06-29

### Completed Chapter 7 ArchiMate diagram set

- Corrected the six Chapter 7 diagram specifications to use ArchiMate 4 generic behaviour element names and the explicit technology-domain Node to Function to Service chain.
- Created original PlantUML source files, SVG exports and PNG review previews for `FIG-07-01` through `FIG-07-06`.
- Inserted all six rendered diagrams into Chapter 7 with captions and explanations.
- Updated `DIAGRAM_REGISTER.md` so Chapter 7 figures are `Review`, not `Approved`.
- Recalculated the Chapter 7 quality gate at 9.1 while keeping the chapter `Under Review`.

### Revised Chapter 7 to ArchiMate 4

- Updated Chapter 7, **ArchiMate**, from the historical ArchiMate 3.2 source basis to the current ArchiMate 4 source basis.
- Added the official Open Group ArchiMate 4 source note and preserved the ArchiMate 3.2 source note as historical.
- Added explicit guidance on reading ArchiMate notation, model reuse, actor versus role, application component to behaviour to service realisation, and technology node/service/artifact distinctions.
- Rewrote the six Chapter 7 diagram specifications to use ArchiMate 4 elements, relationship directions, reusable model concepts, notation legends, accessibility requirements and review criteria.
- Kept Chapter 7 at `Under Review` and did not create diagram source files.

### Drafted Chapter 7 ArchiMate

- Recorded the author's approval of Chapter 6 while keeping Chapter 6 diagrams at `Review`.
- Added the official The Open Group ArchiMate 3.2 source note and registered `[OPEN-GROUP-ARCHIMATE-3.2]`.
- Drafted Chapter 7, **ArchiMate**, using the Chapter 5 prototype pattern and keeping ArchiMate distinct from TOGAF, C4 and BPMN.
- Added six Chapter 7 diagram specifications and registered the planned figures, with source/export deferred pending author approval of the specifications.
- Added ArchiMate glossary terms for ArchiMate, TOGAF, strategy layer, motivation element, plateau and gap.
- Moved Chapter 7 to `Under Review` because diagram source creation is blocked until the new specifications are author-approved.

### Completed Chapter 6 modeler and layout validation

- Recorded manual Camunda Desktop Modeler 5.48.0 validation for all three Chapter 6 BPMN files.
- Improved Chapter 6 BPMN publication rendering so parent participant names remain visible for lane-based pools.
- Adjusted BPMNDI label bounds and regenerated SVG exports and PNG previews for the final Chapter 6 layout pass.
- Recalculated the Chapter 6 quality gate at 9.1 and returned the chapter to `Ready for Author Approval`.

### Corrected Chapter 6 BPMN collaboration and event semantics

- Corrected `FIG-06-01` to use an Order received message start event.
- Corrected `FIG-06-02` so Retail Customer and Financial Crime Platform are black-box pools, Horizon Bank receives the screening result before evaluating it, and compliance review uses a guarded gateway.
- Corrected `FIG-06-03` so Retail Customer is a separate pool, correction messages use message flow, and the response-versus-timeout wait uses an event-based gateway.
- Added BPMNDI layout information to all three Chapter 6 BPMN XML files and regenerated SVG exports and PNG previews.
- Recalculated the Chapter 6 quality gate honestly and moved the chapter to `Revision Required` because Camunda Modeler validation could not be completed in this environment.

### Completed Chapter 6 before author approval

- Drafted Chapter 6, **BPMN: Business Process Model and Notation**, using the Chapter 5 prototype pattern.
- Added three Chapter 6 BPMN figure specifications, editable BPMN XML sources, SVG exports and PNG review previews.
- Added BPMN glossary terms for pools, lanes, sequence flows, message flows and gateways.
- Recalculated the Chapter 6 quality gate and moved the chapter to `Ready for Author Approval`.

### Approved Chapter 4 and opened Chapter 6

- Recorded the author's approval of Chapter 4 while keeping all Chapter 4 diagrams at `Review`.
- Moved Chapter 6, **BPMN: Business Process Model and Notation**, to `Researching`.
- Added the official OMG BPMN 2.0.2 source note and registered `[OMG-BPMN]`.
- Added BPMN to the working glossary.

### Corrected Chapter 4 UML example semantics

- Corrected `FIG-04-01` so required eligibility checking uses `include` and conditional exception, refund and collection behaviour uses guarded `extend`.
- Corrected `FIG-04-02` by replacing Basket to Product aggregation with Basket Line composition and Product reference.
- Corrected `FIG-04-03`, `FIG-04-04` and `FIG-04-06` for component notation, nested sequence alternatives and state-machine initial transition semantics.
- Regenerated changed Chapter 4 SVG exports and PNG previews, then recalculated the Chapter 4 quality gate.

### Completed Chapter 4 before author approval

- Corrected the UML component explanation so components are not presented as automatically deployable.
- Added notation-reading guidance for use case, class, component, sequence, activity, state machine and deployment diagrams.
- Completed seven Chapter 4 diagram specifications with abstraction level and relationship semantics.
- Added PlantUML sources, SVG exports and PNG review previews for `FIG-04-01` through `FIG-04-07`.
- Inserted all seven Chapter 4 figures with captions and explanatory notes.
- Recalculated the Chapter 4 quality gate and moved the chapter to `Ready for Author Approval`.

### Drafted Chapter 4 UML

- Added the official OMG UML 2.5.1 source note and updated `SOURCE_REGISTER.md`.
- Drafted Chapter 4, **UML: Unified Modeling Language**, using the Chapter 5 prototype pattern.
- Added seven planned Chapter 4 figure entries and diagram specifications for UML use case, class, component, sequence, activity, state machine and deployment diagrams.
- Updated glossary terms for UML, use case, class, lifeline and state.
- Moved Chapter 4 to `Diagramming` while holding diagram source creation for author approval of specifications.

### Approved Chapter 3 and moved focus to Chapter 4

- Recorded the author's approval of Chapter 3 while keeping Chapter 3 diagrams at `Review`.
- Updated project tracking so Chapter 4, **UML: Unified Modeling Language**, is the next recommended task.

### Revised Chapter 3 before author approval

- Corrected `FIG-03-01` relationship labels and added a visible purpose cue.
- Added `FIG-03-02` and `FIG-03-03` with specifications, PlantUML sources, SVG exports and PNG review previews.
- Clarified trust-boundary interpretation, diagram metadata, spatial positioning and Horizon Bank review practice.
- Recalculated the Chapter 3 quality gate and updated project tracking.

## 2026-06-28

### Completed Chapter 3 draft

- Recorded the author's approval of Chapter 2 while keeping `FIG-02-01` at `Review`.
- Drafted Chapter 3, **How to Read Architecture Diagrams**, to `Ready for Author Approval`.
- Added `FIG-03-01` with diagram specification, editable PlantUML source, SVG export and PNG review preview.
- Added a Chapter 3 quality gate and updated project tracking.

### Revised Chapter 2 before author approval

- Reduced Chapter 2 repetition with Chapter 1 and strengthened the viewpoint definition.
- Added a practical viewpoint specification template and an ISO 42010 expert note.
- Added `FIG-02-01` with specification, PlantUML source, SVG export and PNG review preview.
- Recalculated the Chapter 2 quality gate and updated registers and tracking.

### Completed Chapter 2 draft

- Drafted Chapter 2, **Model, View and Viewpoint**, to `Ready for Author Approval`.
- Added the required viewpoint map and cross-view traceability matrix as reader-facing tables.
- Reused `[ISO-42010]` for architecture-description vocabulary and updated Chapter 2 tracking.

### Aligned book plan and tracking

- Replaced the compressed root `BOOK_PLAN.md` detail section with the full 63-chapter subsection structure.
- Updated current project tracking so Chapter 1 author review is the next action before Chapter 2.
- Recorded the current pushed commit in `RESUME.md`.

### Refined Chapter 1 before author approval

- Refined the Chapter 1 architecture definition.
- Added `Method` to the terminology table and glossary.
- Clarified the framework definition and updated reader outcomes.
- Updated Chapter 1 tracking, resume state and quality-gate scores.

### Completed Chapter 1 draft

- Drafted Chapter 1, **What Is Architecture Modelling?**, using Chapter 5 as the approved structural and writing model.
- Added the `ISO-42010` source note and source-register entry for architecture-description vocabulary.
- Added `FIG-01-01` with diagram specification, PlantUML source, SVG export and PNG review preview.
- Updated Chapter 1 status, diagram register and quality-gate review.

### Approved Chapter 5 prototype

- Recorded the author verdict that Chapter 5 passes as the prototype chapter at `9.1/10`.
- Marked Chapter 5 `Approved` while keeping Chapter 5 diagrams at `Review`.
- Recorded Chapter 5 as the structural and writing model for subsequent chapters.

### Corrected Chapter 5 before author approval

- Added Chapter 5 figures `FIG-05-06` through `FIG-05-08` with diagram specifications, PlantUML source, SVG exports and PNG review previews.
- Updated `DIAGRAM_REGISTER.md` so all Chapter 5 diagrams are listed with `Review` status and no diagram is marked `Approved`.
- Corrected the C4 Component definition to state that components are related functionality behind a well-defined interface inside one deployable container.
- Removed reader-facing production headings from Chapter 5 and moved production status into `RESUME.md`, `CHANGELOG.md` and the Chapter 5 quality gate.
- Added a reader-facing references and further-reading section connected to Appendix H.
- Updated the Chapter 5 quality gate after re-reviewing the corrected chapter and all eight figures.
- Recorded the production-chapter scaffolding rule in `DECISIONS.md`.

### Completed Chapter 5 prototype

- Drafted Chapter 5, **The C4 Model**, as the prototype chapter.
- Added official C4, Structurizr and C4-PlantUML source notes under `research/c4/`.
- Pinned C4-PlantUML 2.9.0 locally under `diagrams/lib/C4-PlantUML/`.
- Added five Chapter 5 diagram specifications, PlantUML sources, SVG exports and PNG review previews.
- Updated `DIAGRAM_REGISTER.md`, `SOURCE_REGISTER.md`, `GLOSSARY.md`, `DECISIONS.md`, `STATUS.md` and the Chapter 5 quality-gate review.

### Added diagram production controls

- Added diagram specification, library and style directories.
- Added BPMN and DMN source directories.
- Added a diagram specification template.
- Added PlantUML and Mermaid rendering scripts.
- Added diagram validation and register-check scripts.
- Added GitHub Actions validation for structure, links, terminology, diagrams, build and word count.
- Added specification-first diagram workflow, author-only diagram approval rules and visual-review gates.
- Added local version-pinned C4-PlantUML dependency policy.
- Updated Mermaid guidance to use the installed `bierner.markdown-mermaid` extension for Markdown preview.

### Corrected after repository verification

- Removed duplicate `Practical exercise` and `Review checklist` headings from chapter stubs.
- Added `scripts/check-structure.py` for repository-wide structural validation.
- Revalidated chapter numbering, metadata, internal links and terminology.
- Corrected manuscript build order and added a cross-platform Python builder.
- Added GitHub Actions validation and research folders for DMN, domain/event, infrastructure, modelling tools and banking.


### Added

- Repository governance and Codex instructions
- Six-part book plan with 63 chapters
- Complete BIAN implementation part
- Chapter stubs with outcomes, models, examples and completion criteria
- Front matter and appendices
- Research, diagram, example and review structures
- Templates and quality scripts

### Decisions

- Markdown and Git are the source of truth
- British English is used
- Horizon Bank is the principal enterprise case study
- BIAN Service Domains are not automatically mapped to microservices
- Only the author can approve a chapter

### Next

- Review the repository structure
- Confirm the final title and subtitle
- Develop Chapter 5 as the prototype chapter
