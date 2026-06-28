# Chapter 5 C4 Prototype Design

## Purpose

Create Chapter 5, **The C4 Model**, as the first complete production prototype for *Architecture Modelling: A Practical Beginner's Handbook*. The prototype establishes the writing depth, research discipline, diagram workflow, review gate and project-record updates that later chapters should follow.

## Repository Context

The repository already contains all 63 chapter stubs, appendices, front matter, validation scripts, example folders, diagram folders and control registers. Current status shows all chapters as `Planned`; the recommended next task is to develop Chapter 5 as the prototype chapter and prototype diagram set.

Baseline checks already passed before this design:

- `python scripts/check-structure.py`
- `python scripts/check-links.py`
- `python scripts/check-terminology.py`
- `python scripts/validate-diagrams.py`
- `python scripts/check-diagram-register.py`
- `python scripts/word-count.py`
- `python scripts/build-book.py`

## Scope

Chapter 5 will become a complete draft suitable for author review, subject to the repository's author-only approval rules. The chapter will cover:

- What C4 is.
- Core C4 concepts: person, software system, container and component.
- Level 1: System Context.
- Level 2: Container.
- Level 3: Component.
- Level 4: Code.
- Dynamic diagrams.
- Deployment diagrams.
- System landscape diagrams.
- C4 versus UML.
- Common mistakes.
- Chapter cheat sheet.
- Key takeaways.
- Practical exercise with suggested review criteria.
- Review checklist.
- Source keys and figure references.

The chapter will use the Simple Online Store for first exposure and Horizon Bank's payments platform for the enterprise example. It will clearly state that a C4 container is not automatically a Docker container.

## Out of Scope

The prototype will not complete other chapters, appendices or final publication metadata. It will not mark any chapter or diagram `Approved`. It will not use unversioned remote includes for publication diagrams.

## Sources

Use official and primary sources where possible:

- Official C4 model documentation for C4 terminology and diagram types.
- Structurizr documentation where useful for C4 notation, dynamic diagrams or diagrams-as-code practice.
- C4-PlantUML project source, version and licence before using C4-PlantUML macros in publication diagrams.

Create source notes under `research/c4/` using `templates/source-note-template.md`. Update `SOURCE_REGISTER.md` for major reusable sources.

## Diagram Design

Use the installed PlantUML runtime for rendering SVG outputs. Before using C4-PlantUML macros in publication diagrams, verify or add a local, version-pinned C4-PlantUML library under `diagrams/lib/C4-PlantUML/` and record the version, source and licence in `SOURCE_REGISTER.md`.

Planned Chapter 5 figures:

| Figure ID | Title | Purpose | Tooling |
|---|---|---|---|
| FIG-05-01 | C4 levels of zoom | Introduce context, container, component and code levels | PlantUML or C4-PlantUML |
| FIG-05-02 | Online store system context | Show people and external systems around the online store | C4-PlantUML |
| FIG-05-03 | Online store container view | Show separately runnable or data-storing units | C4-PlantUML |
| FIG-05-04 | Horizon Bank payments platform view | Apply C4 to a banking software system | C4-PlantUML |
| FIG-05-05 | Payment submission dynamic view | Show a runtime interaction path without full process detail | C4-PlantUML or PlantUML sequence |

For each figure:

- Add or update the `DIAGRAM_REGISTER.md` row.
- Create a specification under `diagrams/specifications/`.
- Confirm the specification is author-approved before creating diagram source if applying the strict diagram workflow.
- Store source under `diagrams/source/plantuml/`.
- Export SVG under `diagrams/exported/svg/`.
- Run diagram validation and visually inspect the output.

## Review and Quality Gate

Create a Chapter 5 quality-gate review under `reviews/chapter-gates/CH-05-quality-gate.md`. Review as:

- Beginner reader.
- Solution architect.
- Enterprise architect.
- Technical editor.
- Diagram reviewer.
- Source and copyright checker.
- Consistency reviewer.

The chapter may be moved only to a status allowed by `STATUS.md` and `WORKFLOW.md`. Codex must not mark it `Approved`.

## Project Records

Update:

- `STATUS.md`
- `CHANGELOG.md`
- `RESUME.md`
- `SOURCE_REGISTER.md`
- `DIAGRAM_REGISTER.md`
- `GLOSSARY.md` if new controlled terms are introduced
- `DECISIONS.md` only if a material decision is made

## Verification

Before completion, run:

- `python scripts/check-structure.py`
- `python scripts/check-links.py`
- `python scripts/check-terminology.py`
- `python scripts/validate-diagrams.py`
- `python scripts/check-diagram-register.py`
- `python scripts/word-count.py`
- `python scripts/build-book.py`

Review `git diff` before committing. Commit only focused, passing work. Do not push unless explicitly authorised and network/authentication allow it.

## Open Constraint

The PlantUML VS Code extension and `plantuml.jar` are installed locally. The repository's local C4-PlantUML library directory currently contains only a policy README, so C4-PlantUML must be verified or added before publication diagrams use C4 macros.
