# Chapter 7 Quality Gate: ArchiMate

## Metadata

- **Chapter:** 7, ArchiMate
- **Review date:** 2026-06-29
- **Reviewer:** Codex
- **Status recommendation:** Under Review
- **Current gate:** Chapter 7 prose has been revised to use ArchiMate 4 as the current source basis. The gate remains open because the author has not yet reviewed the six Chapter 7 diagram specifications and no diagram source or export files should exist yet.
- **Diagram status:** `FIG-07-01` through `FIG-07-06` remain `Planned`. No Chapter 7 PlantUML, Archi or Draw.io source file should be created before author approval of the specifications.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 8.9 | Covers ArchiMate purpose, TOGAF distinction, model reuse, notation reading, domains, relationships, viewpoints, comparisons, mistakes, exercise and checklist. |
| Beginner clarity | 8.9 | Adds explicit reading guidance for element kinds, relationships, direction, nesting, legends and colour usage. |
| Technical accuracy | 8.7 | Replaces ArchiMate 3.2 as the normative basis with ArchiMate 4 and corrects actor/role, application realisation and technology support semantics. Full licensed specification review remains a final publication task because the public product page records access and AI-use restrictions. |
| Expert depth | 8.8 | Gives practical enterprise architecture traceability guidance without reproducing The Open Group specification. |
| Logical flow | 8.8 | Moves from purpose and model reuse through notation, domains, relationships, viewpoints and comparisons. |
| Examples and exercises | 8.8 | Uses Horizon Bank consistently and revises the exercise to include actor/role, application service realisation and migration without Gap notation. |
| Diagram readiness | 6.8 | Six specifications are expected for author review. Source files and exports are intentionally blocked until author approval. |
| Source quality | 8.4 | The public official Open Group pages verify ArchiMate 4 metadata and release changes, but the full licensed specification was not downloaded or incorporated into the AI-assisted draft. Keep this below the 8.5 threshold until source review is completed under the applicable licence. |
| Consistency with rest of book | 8.9 | Follows the Chapter 5 teaching pattern and keeps ArchiMate distinct from Chapter 6 BPMN and Chapter 5 C4. |
| Writing and editorial quality | 8.9 | Uses British English, concise paragraphs and review-ready structure. |

**Average score:** 8.6

## Review perspectives

### Beginner reader

The chapter now explains ArchiMate through model reuse, notation reading and small Horizon Bank examples before presenting more formal terminology.

### Enterprise architect

The revision uses ArchiMate 4 terminology, including domain rather than older layer-only language, and avoids using removed elements such as Gap and Constraint as current notation.

### Solution architect

The application section now teaches the explicit chain from Application Component to assigned behaviour to realised Application Service to served consumer. This should reduce component-to-service shortcuts in beginner diagrams.

### Technology architect

The technology section now distinguishes Technology Node, System Software, Technology Service and Artifact. It warns that a managed database capability should not automatically be modelled as a node.

### Diagram reviewer

The six specifications must be reviewed before any diagram source is created. They should be checked for ArchiMate 4 element validity, relationship direction, reusable model concepts, legend adequacy and accessibility.

### Source and copyright checker

The chapter uses `[OPEN-GROUP-ARCHIMATE-4]` for current source claims and preserves `[OPEN-GROUP-ARCHIMATE-3.2]` as historical. The draft paraphrases public official source metadata and does not reproduce official diagrams, metamodel tables or long specification text.

## Open issues

- The author must approve or revise `FIG-07-01` through `FIG-07-06` specifications before Codex creates diagram source.
- The full ArchiMate 4 specification should be reviewed by a licensed human reviewer under the applicable Open Group licence before publication-quality source scoring is raised.
- Chapter 7 must stay `Under Review` until specifications are reviewed, all six diagrams are created, all diagrams render successfully and this gate is recalculated at 9.0 or above.

## Gate decision

Chapter 7 remains `Under Review`. It is not ready for author approval because required diagrams have not been produced and the source-quality gate remains below threshold pending full ArchiMate 4 source review under the applicable licence.
