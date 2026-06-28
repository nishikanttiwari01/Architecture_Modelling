# Chapter 1 Quality Gate: What Is Architecture Modelling?

## Metadata

- **Chapter:** 1, What Is Architecture Modelling?
- **Review date:** 2026-06-28
- **Reviewer:** Codex
- **Status recommendation:** Ready for Author Approval

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.1 | Covers the purpose of architecture modelling, key vocabulary, simplification, stakeholders, structure, behaviour, abstraction levels and time states. |
| Beginner clarity | 9.2 | Uses plain explanations before formal terms and keeps the opening chapter free of notation-specific detail. |
| Technical accuracy | 9.0 | Uses repository glossary terms and ISO 42010 concepts for views, viewpoints, stakeholders and concerns without copying standard text. |
| Expert depth | 8.8 | Gives enough nuance for an opening chapter, with deeper treatment deliberately deferred to Chapter 2 and later notation chapters. |
| Logical flow | 9.1 | Moves from why models exist to vocabulary, examples, model families, mistakes, cheat sheet and practice. |
| Examples and exercises | 9.0 | Uses Simple Online Store first and Horizon Bank second, with a practical returns-feature exercise. |
| Diagram quality | 8.9 | `FIG-01-01` is rendered, readable and conceptually appropriate. It should still be opened in VS Code before any diagram approval. |
| Source quality | 8.9 | Adds `ISO-42010` as a primary source for architecture-description vocabulary. |
| Consistency with rest of book | 9.1 | Follows the Chapter 5 structural model and introduces terms used throughout the manuscript. |
| Writing and editorial quality | 9.1 | Uses British English, short paragraphs, concrete language and no reader-facing draft scaffolding. |

**Average score:** 9.0

## Review perspectives

### Beginner reader

The chapter starts with the practical reason for modelling and avoids overwhelming the reader with notation detail. It makes the central distinction between reality, model, diagram and view early.

### Solution architect

The chapter gives a usable framing for selecting views by audience, concern and decision. It also introduces structural versus behavioural and conceptual versus logical versus physical distinctions.

### Enterprise architect

The Horizon Bank examples connect the foundations to enterprise-scale change without introducing BIAN or detailed banking architecture too early.

### Technical editor

The chapter removes draft scaffolding, uses stable source keys and follows the Chapter 5 prose pattern.

### Diagram reviewer

`FIG-01-01` has a specification, editable PlantUML source, SVG export and PNG preview. Visual inspection of the PNG found no clipped text or unreadable labels.

### Source and copyright checker

The chapter uses `[ISO-42010]` as a vocabulary source and paraphrases the standard. No standard text or diagrams are reproduced.

## Open issues

- Chapter 2 will deepen model, view and viewpoint, so Chapter 1 should remain introductory.
- `FIG-01-01` should be opened in VS Code before any diagram approval.

## Gate decision

The chapter meets the quality-gate threshold for `Ready for Author Approval`. The chapter must not be marked `Approved` without explicit author action. The diagram remains `Review`.
