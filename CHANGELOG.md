# Changelog

All notable repository and manuscript changes are recorded here. This is a project history, not a replacement for Git commits.

## 2026-06-29

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
