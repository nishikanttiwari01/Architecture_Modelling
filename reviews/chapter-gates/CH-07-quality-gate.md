# Chapter 7 Quality Gate: ArchiMate

## Metadata

- **Chapter:** 7, ArchiMate
- **Review date:** 2026-06-29
- **Reviewer:** Codex
- **Status recommendation:** Under Review
- **Current gate:** Chapter 7 prose, ArchiMate 4 source note, six corrected diagram specifications, six PlantUML source files and six rendered SVG/PNG outputs are complete for author review.
- **Diagram status:** `FIG-07-01` through `FIG-07-06` are `Review`, not `Approved`.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.2 | Covers ArchiMate purpose, TOGAF distinction, model reuse, notation reading, domains, relationships, viewpoints, comparisons, mistakes, exercise, checklist and six supporting figures. |
| Beginner clarity | 9.1 | Explains element kinds, relationship meaning, direction, nesting, legends and colour usage before asking readers to interpret full views. |
| Technical accuracy | 9.0 | Uses ArchiMate 4 as the current source basis, avoids removed Gap and Constraint notation, corrects actor/role semantics, uses explicit application and technology realisation chains, and uses Influence from Requirements to Goals in the motivation view. |
| Expert depth | 9.0 | Shows enterprise architecture traceability across capability, layered, application, technology, motivation and migration views without reproducing official Open Group diagrams. |
| Logical flow | 9.1 | Moves from modelling purpose and reuse through notation, domains, relationships, viewpoints, comparisons, mistakes and practice. |
| Examples and exercises | 9.1 | Uses Horizon Bank consistently across all six views and keeps the exercise aligned with actor/role, application service realisation, technology hosting and migration concerns. |
| Diagram quality | 9.0 | Six original PlantUML diagrams render to SVG and PNG. Visual inspection found valid ArchiMate 4 teaching elements, readable legends, no clipped text, no colour-only meaning and consistent reuse of model concepts. Relationship codes are expanded in legends where full labels would crowd the view. |
| Source quality | 8.7 | Official Open Group ArchiMate 4 source notes and register entries support current-version claims. The chapter avoids copyrighted specification text and official diagrams. A final licensed human source review remains prudent before publication. |
| Consistency with rest of book | 9.2 | Follows the Chapter 5 teaching pattern, stays distinct from Chapter 6 BPMN and keeps diagram approval status consistent with repository policy. |
| Writing and editorial quality | 9.1 | Uses British English, concise paragraphs, direct explanations and review-ready figure captions. |

**Average score:** 9.1

Minimum category score: 8.7. The gate meets the requested threshold of average at least 9.0 and no category below 8.5.

## Review perspectives

### Beginner reader

The chapter now teaches how to read ArchiMate notation before showing complete views. The captions explain what each diagram is for and what it intentionally omits.

### Enterprise architect

The revision uses ArchiMate 4 terminology, including generic behaviour element names by domain. Model concepts are reused across capability, layered, application, technology, motivation and migration views.

### Solution architect

The application cooperation view shows the explicit Application Component to Function in the Application domain to Service in the Application domain chain, then shows serving, access and flow only where they support the concern.

### Technology architect

The technology view distinguishes Technology Node, System Software, Function in the Technology domain, Service in the Technology domain and Artifact. It does not treat a managed database capability automatically as a node.

### Diagram reviewer

The six specifications have been corrected and author-approved for source creation. The generated diagrams remain at `Review`, so the author can still request layout or content changes before any diagram is marked `Approved`.

### Source and copyright checker

The chapter uses `[OPEN-GROUP-ARCHIMATE-4]` for current source claims and preserves `[OPEN-GROUP-ARCHIMATE-3.2]` as historical. It paraphrases source-supported claims and uses original teaching diagrams rather than official Open Group diagrams.

## Open issues

- The author must review the six rendered Chapter 7 diagrams before any diagram can move beyond `Review`.
- The full ArchiMate 4 specification should still be checked by a licensed human reviewer under the applicable Open Group licence before final publication.
- Chapter 7 remains `Under Review` until the author completes the review and decides whether it is ready for author approval.

## Gate decision

Chapter 7 remains `Under Review`. The quality gate now passes the requested numeric threshold, but no diagram is marked `Approved` and the chapter is not advanced to `Ready for Author Approval` in this task.
