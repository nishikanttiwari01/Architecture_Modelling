# Changelog

All notable repository and manuscript changes are recorded here. This is a project history, not a replacement for Git commits.

## 2026-06-28

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
