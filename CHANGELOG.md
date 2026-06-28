# Changelog

All notable repository and manuscript changes are recorded here. This is a project history, not a replacement for Git commits.

## 2026-06-28

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
