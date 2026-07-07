# Chapter 17 Quality Gate

## Gate metadata

- Chapter: 17, Modelling User and System Interaction
- Gate date: 2026-07-07
- Gate owner: Codex
- Status before task: Planned.
- Final status after task: Ready for Author Approval.
- Approval status: Not Approved.

## Gate rule

- Critical unresolved issue means `Revision Required`.
- Major unresolved issue means `Revision Required`.
- No unresolved Critical or Major issue means `Ready for Author Approval`.
- Only the author may set `Approved`.

## Chapter completion evidence

- Manuscript scaffold replaced with a complete Chapter 17 manuscript.
- Opening bridge from Chapter 16 is present.
- The chapter is framed as a Part III selection chapter.
- The chapter distinguishes user experience, business process, software runtime collaboration
  and lifecycle state.
- The chapter covers use case diagrams.
- The chapter covers user journeys and service blueprints.
- The chapter covers wireframes and screen flows.
- The chapter covers UML sequence diagrams and C4 dynamic views.
- The chapter covers BPMN collaboration and UML activity diagrams.
- The chapter covers state machines.
- The chapter covers API interaction views without starting Chapter 18.
- The chapter includes Simple Online Store and Horizon Bank worked examples.
- The chapter includes common mistakes.
- The chapter includes review checklist, key takeaways, practical exercise and suggested
  answer.
- The chapter includes references and source notes section.

## Source notes checked

- `[OMG-UML]`: reused for UML use case, sequence, activity and state machine terminology.
- `[C4-OFFICIAL]`: reused for C4 dynamic view framing.
- `[OMG-BPMN]`: reused for BPMN collaboration terminology.
- No new source note was required.
- `SOURCE_REGISTER.md` did not require an update.
- No official standard diagram or long source text was copied.

## Diagram decision

- Decision record: `DEC-025`.
- Decision status: Proposed.
- Decision remains not Approved.
- Figure: `FIG-17-01`, Choosing the Right User and System Interaction View.
- Figure status: Review.
- Figure remains not Approved.
- Diagram purpose: selection guide for user and system interaction views.
- Diagram notation: PlantUML decision guide.
- PNG preview: not required by repository convention because SVG is the publication output and
  Chapter 15 and Chapter 16 selection guides also use SVG only.

## FIG-17-01 asset locations

- Specification:
  `diagrams/specifications/FIG-17-01-choosing-the-right-user-and-system-interaction-view.md`.
- Editable source:
  `diagrams/source/plantuml/FIG-17-01-choosing-the-right-user-and-system-interaction-view.puml`.
- SVG export:
  `diagrams/exported/svg/FIG-17-01-choosing-the-right-user-and-system-interaction-view.svg`.
- Diagram register: `DIAGRAM_REGISTER.md`.
- Chapter reference: `manuscript/part-03-diagram-selection/17-user-system-interaction.md`.

## Review records created

- Technical review: `reviews/technical-review/chapter-17-review-2026-07-07.md`.
- Beginner review: `reviews/beginner-review/chapter-17-review-2026-07-07.md`.
- Consistency review: `reviews/consistency-review/chapter-17-review-2026-07-07.md`.
- Final review: `reviews/final-review/chapter-17-review-2026-07-07.md`.
- All review records report no unresolved Critical or Major issue.

## Validation checks to run before completion

- `python scripts/check-structure.py`
- `python scripts/check-links.py`
- `python scripts/check-terminology.py`
- `python scripts/validate-diagrams.py`
- `python scripts/check-diagram-register.py`
- `python scripts/build-book.py`
- `python scripts/word-count.py`
- `powershell -ExecutionPolicy Bypass -File .\scripts\render-all-diagrams.ps1`
- `git diff --check`

## Status alignment required

- `STATUS.md` must show Chapter 17 as `Ready for Author Approval`.
- Chapter 17 research, draft, diagrams, review and sources verified must be 100 percent.
- `DIAGRAM_REGISTER.md` must keep `FIG-17-01` at `Review`.
- `DECISIONS.md` must keep `DEC-025` at `Proposed`.
- `CHANGELOG.md` must record Chapter 17 completion.
- Chapter 15 and Chapter 16 must remain `Ready for Author Approval`.
- Chapter 14 must remain `Revision Required`.
- Chapter 18 must remain `Planned`.

## Open issues

- Author approval remains pending.
- Final book-page layout inspection of FIG-17-01 remains pending under the general diagram
  `Review` convention.
- Author may choose to accept, revise or reject `DEC-025`.

## Quality score

| Category | Score | Notes |
|---|---:|---|
| Technical accuracy | 9.1 | Source-backed UML, C4 and BPMN selection guidance. |
| Beginner comprehension | 9.1 | Plain questions introduce each view before formal terminology. |
| Educational flow | 9.0 | Progresses from question to view choice, examples, mistakes and exercise. |
| Consistency | 9.1 | Matches Part III pattern and controlled example names. |
| Diagram quality | 8.8 | PlantUML guide is complete; final book-page review remains pending. |
| Source and copyright | 9.2 | Existing sources reused; no copied standard diagrams or long text. |
| Copy-editing | 9.0 | British English and short paragraphs used. |

Average score: 9.0.

## Final recommendation

- Recommendation: Move Chapter 17 to `Ready for Author Approval`.
- Do not mark Chapter 17 Approved.
- Do not mark FIG-17-01 Approved.
- Do not mark DEC-025 Approved.
- No unresolved Critical or Major issue blocks author review.
