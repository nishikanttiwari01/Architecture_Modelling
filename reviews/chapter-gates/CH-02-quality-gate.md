# Chapter 2 Quality Gate: Model, View and Viewpoint

## Metadata

- **Chapter:** 2, Model, View and Viewpoint
- **Review date:** 2026-06-28
- **Reviewer:** Codex
- **Status recommendation:** Ready for Author Approval

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.3 | Covers model, view, viewpoint, stakeholder concerns, viewpoint specifications, model kinds, correspondences, abstraction, cross-view consistency and viewpoint selection. |
| Beginner clarity | 9.1 | Adds a bridge from Chapter 1, reduces repeated fundamentals and keeps the formal ISO 42010 note concise. |
| Technical accuracy | 9.2 | Strengthens viewpoint as a reusable specification for constructing, interpreting, analysing and reviewing views, aligned with `[ISO-42010]` vocabulary. |
| Expert depth | 9.1 | Adds architecture description, architecture model, model kind and correspondence without overloading the beginner chapter. |
| Logical flow | 9.1 | Moves from reused Chapter 1 vocabulary to viewpoint specification, ISO terminology, figure, mapping, consistency and exercise. |
| Examples and exercises | 9.0 | Preserves the Simple Online Store and Horizon Bank examples that add new learning, with scenario-based knowledge checks. |
| Diagram quality | 9.0 | `FIG-02-01` has a specification, editable PlantUML source, SVG export and PNG preview. Visual review found no clipped text, no overlapping labels and readable direction. |
| Source quality | 9.0 | Uses the recorded `ISO-42010` source note and official ISO page for vocabulary verification. No standard text or diagrams are reproduced. |
| Consistency with rest of book | 9.2 | Reduces overlap with Chapter 1, prepares Chapter 3 and aligns the glossary, source register and diagram register. |
| Writing and editorial quality | 9.1 | Uses British English, short paragraphs, no em dashes in Chapter 2 prose and more page-readable tables. |

**Average score:** 9.1

## Review perspectives

### Beginner reader

The chapter now starts from the terms Chapter 1 already introduced and explains what is new: how a viewpoint turns stakeholder concerns into repeatable view construction and review guidance.

### Solution architect

The viewpoint specification template is practical enough to reuse in project work. The cross-view matrix has been narrowed so it remains readable on a normal book page.

### Enterprise architect

The chapter now includes model kinds and correspondences, which makes it more accurate for enterprise architecture descriptions without becoming a standards summary.

### Technical editor

The viewpoint catalogue is more compact, the repeated conceptual/logical/physical explanation is shorter and the knowledge check now uses scenarios instead of repeating definitions.

### Diagram reviewer

`FIG-02-01` shows stakeholders, concerns, viewpoint, architecture view, architecture models, model kinds or notation and correspondence between related views. The SVG and PNG exports exist, and the PNG preview is readable. The diagram remains in `Review`.

### Source and copyright checker

The chapter paraphrases ISO 42010 terminology and uses the stable `[ISO-42010]` source key. No standards text, tables or diagrams are copied.

## Open issues

- `FIG-02-01` should remain in `Review` until the author has visually opened the SVG in VS Code and accepted the layout.
- Chapter 3 should now use the Chapter 2 viewpoint vocabulary when teaching how to read architecture diagrams.

## Gate decision

The revised chapter meets the quality-gate threshold for `Ready for Author Approval`. The average is at least 9.0 and no category is below 8.5. The chapter must not be marked `Approved` without explicit author action. `FIG-02-01` remains in `Review`.
