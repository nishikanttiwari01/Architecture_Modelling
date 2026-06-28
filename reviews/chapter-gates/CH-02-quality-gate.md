# Chapter 2 Quality Gate: Model, View and Viewpoint

## Metadata

- **Chapter:** 2, Model, View and Viewpoint
- **Review date:** 2026-06-28
- **Reviewer:** Codex
- **Status recommendation:** Ready for Author Approval

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.1 | Covers model, view, viewpoint, stakeholder concern, abstraction, decomposition, cross-view consistency and viewpoint selection. It also distinguishes viewpoint from notation, method and framework. |
| Beginner clarity | 9.2 | Opens with the common confusion, defines one idea at a time and uses practical tests before moving into examples. |
| Technical accuracy | 9.0 | Aligns with `[ISO-42010]` vocabulary while paraphrasing rather than reproducing standard text. |
| Expert depth | 8.8 | Gives enough depth for a fundamentals chapter, with detailed notation treatment intentionally deferred to later chapters. |
| Logical flow | 9.1 | Moves from vocabulary to stakeholder concerns, abstraction, consistency, viewpoint catalogue, worked examples and practice. |
| Examples and exercises | 9.0 | Uses both Simple Online Store and Horizon Bank, with a practical mobile-payment viewpoint exercise and suggested answer. |
| Artefact quality | 8.9 | Provides the required viewpoint map and cross-view traceability matrix as reader-facing tables. No publication diagram was created because the required artefacts are tabular and no author-approved Chapter 2 diagram specification exists. |
| Source quality | 8.9 | Uses the recorded `ISO-42010` source note for architecture-description vocabulary and preserves the source key. |
| Consistency with rest of book | 9.2 | Builds directly on Chapter 1 and prepares Chapter 3 by clarifying how views should be selected before diagrams are read. |
| Writing and editorial quality | 9.1 | Uses British English, short paragraphs, direct language and no reader-facing draft scaffolding. |

**Average score:** 9.0

## Review perspectives

### Beginner reader

The chapter gives a usable mental model: a model selects facts, a view presents selected content for stakeholder concerns, and a viewpoint guides how to construct and review a type of view. The examples avoid notation overload.

### Solution architect

The viewpoint map and traceability matrix are practical enough to use in early project conversations. The chapter also warns against mixing conceptual, logical and physical levels without purpose.

### Enterprise architect

The Horizon Bank example treats transformation as a set of coordinated stakeholder concerns, not a single diagram. It supports later enterprise, BIAN and migration chapters.

### Technical editor

The chapter follows the Chapter 5 production pattern and removes the planned-chapter scaffolding. It connects source notes to Appendix H in the same way as Chapters 1 and 5.

### Artefact reviewer

The required artefacts are present as tables rather than diagrams. This is appropriate for Chapter 2 because the purpose is to teach selection and traceability before notation-specific diagrams begin.

### Source and copyright checker

The chapter uses `[ISO-42010]` as a vocabulary source, paraphrases the standard and does not reproduce standard text or diagrams.

## Open issues

- No Chapter 2 publication figure was created. If the author wants a visual viewpoint map later, create a diagram specification first and wait for author approval before creating source.
- Chapter 3 should now teach how to inspect diagrams using the vocabulary introduced in Chapters 1 and 2.

## Gate decision

The chapter meets the quality-gate threshold for `Ready for Author Approval`. The average is at least 9.0 and no category is below 8.5. The chapter must not be marked `Approved` without explicit author action.
