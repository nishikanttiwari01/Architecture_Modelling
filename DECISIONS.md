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
