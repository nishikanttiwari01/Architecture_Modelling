# Chapter 16 Quality Gate

## Gate metadata

- Chapter: 16, Modelling Software Structure
- Gate date: 2026-07-07
- Gate owner: Codex
- Status before task: Planned, with FIG-16-01 already registered, specified, rendered and set to Review in commit `0338d27`.
- Final status after task: Ready for Author Approval.
- Approval status: Not Approved.

## Gate rule

- Critical unresolved issue means `Revision Required`.
- Major unresolved issue means `Revision Required`.
- No unresolved Critical or Major issue means `Ready for Author Approval`.
- Only the author may set `Approved`.

## Chapter completion evidence

- Manuscript scaffold replaced with a complete Chapter 16 manuscript.
- Opening bridge from Chapter 15 is present.
- The chapter is framed as a Part III selection chapter.
- The chapter distinguishes business capability, business process and software structure.
- The chapter covers system landscape, system context, container, component, package, class, dependency and deployment views.
- The chapter explains logical versus physical structure.
- The chapter includes Simple Online Store and Horizon Bank worked examples.
- The chapter includes common mistakes.
- The chapter includes review checklist, key takeaways, practical exercise and suggested answer.
- The chapter includes references and source notes section.

## Source notes checked

- `[C4-OFFICIAL]`: reused for C4 landscape, context, container, component, code and deployment framing.
- `[OMG-UML]`: reused for UML package, class, component, dependency and deployment terminology.
- No new source note was required.
- `SOURCE_REGISTER.md` did not require an update.
- No official standard diagram or long source text was copied.

## Diagram decision

- Decision record: `DEC-024`.
- Decision status: Proposed.
- Decision remains not Approved.
- Figure: `FIG-16-01`, Choosing the Right Software Structure View.
- Figure status: Review.
- Figure remains not Approved.
- Diagram purpose: selection guide for software-structure views.
- Diagram notation: Mermaid decision guide.
- PNG preview: not required by repository convention for this Mermaid selection guide because SVG is the publication output and the existing Chapter 15 Mermaid selection guide also uses SVG only.

## FIG-16-01 asset locations

- Specification: `diagrams/specifications/FIG-16-01-choosing-the-right-software-structure-view.md`.
- Editable source: `diagrams/source/mermaid/FIG-16-01-choosing-the-right-software-structure-view.mmd`.
- SVG export: `diagrams/exported/svg/FIG-16-01-choosing-the-right-software-structure-view.svg`.
- Diagram register: `DIAGRAM_REGISTER.md`.
- Chapter reference: `manuscript/part-03-diagram-selection/16-software-structure.md`.

## Review records created

- Technical review: `reviews/technical-review/chapter-16-review-2026-07-07.md`.
- Beginner review: `reviews/beginner-review/chapter-16-review-2026-07-07.md`.
- Consistency review: `reviews/consistency-review/chapter-16-review-2026-07-07.md`.
- Final review: `reviews/final-review/chapter-16-review-2026-07-07.md`.
- All review records report no unresolved Critical or Major issue.

## Validation checks to run before completion

- `python scripts/check-structure.py`
- `python scripts/check-links.py`
- `python scripts/check-terminology.py`
- `python scripts/validate-diagrams.py`
- `python scripts/check-diagram-register.py`
- `python scripts/word-count.py`
- `git diff --check`

## Status alignment required

- `STATUS.md` must show Chapter 16 as `Ready for Author Approval`.
- Chapter 16 research, draft, diagrams, review and sources verified must be 100 percent.
- `DIAGRAM_REGISTER.md` must keep `FIG-16-01` at `Review`.
- `DECISIONS.md` must keep `DEC-024` at `Proposed`.
- `CHANGELOG.md` must record Chapter 16 completion.
- Chapter 15 must remain `Ready for Author Approval`.
- Chapter 14 must remain `Revision Required`.

## Open issues

- Author approval remains pending.
- Final book-page layout inspection of FIG-16-01 remains pending under the general diagram `Review` convention.
- Author may choose to accept, revise or reject `DEC-024`.

## Final recommendation

- Recommendation: Move Chapter 16 to `Ready for Author Approval`.
- Do not mark Chapter 16 Approved.
- Do not mark FIG-16-01 Approved.
- Do not mark DEC-024 Approved.
- No unresolved Critical or Major issue blocks author review.
