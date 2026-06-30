# Chapter 7 Quality Gate: ArchiMate

## Metadata

- **Chapter:** 7, ArchiMate
- **Review date:** 2026-06-30
- **Reviewer:** Codex
- **Status recommendation:** Approved
- **Current gate:** Chapter 7 includes practical ArchiMate tool guidance, updated official tool source notes and polished rendered outputs for `FIG-07-01`, `FIG-07-02`, `FIG-07-05` and `FIG-07-06`. The author approved the chapter on 2026-06-30.
- **Diagram status:** `FIG-07-01` through `FIG-07-06` remain `Review`, not `Approved`.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.3 | Covers ArchiMate purpose, TOGAF distinction, tool guidance, model reuse, notation reading, domains, relationships, viewpoints, comparisons, mistakes, exercise, checklist and six supporting figures. |
| Beginner clarity | 9.2 | Adds practical tool categories and neutral comparison tables while keeping the modelling explanation beginner-friendly. |
| Technical accuracy | 9.0 | Uses ArchiMate 4 as the current source basis, avoids removed Gap and Constraint notation, corrects actor/role semantics and avoids unsupported ArchiMate 4 tool-certification claims. |
| Expert depth | 9.1 | Distinguishes semantic repositories, drawing tools and diagrams-as-code, and explains why PlantUML teaching views are not a governed ArchiMate repository. |
| Logical flow | 9.1 | Moves from purpose and tool choice through model reuse, notation, domains, relationships, viewpoints and comparisons. |
| Examples and exercises | 9.1 | Uses Horizon Bank consistently across the six views and keeps the exercise aligned with actor/role, application service realisation, technology hosting and migration concerns. |
| Diagram quality | 9.1 | Removed the unverified capability Serving relationship from `FIG-07-01`, improved `FIG-07-02` with panelled traceability and full labels, separated `FIG-07-05` into two motivation threads and replaced `FIG-07-06` shorthand codes with direct labels. |
| Source quality | 8.8 | Uses official Open Group ArchiMate source notes and the new official tool source note `[ARCHIMATE-TOOL-GUIDANCE-2026]`. A final licensed human review of the full ArchiMate 4 specification remains prudent. |
| Consistency with rest of book | 9.2 | Aligns with the repository diagram-as-code workflow while distinguishing it from governed semantic repositories. |
| Writing and editorial quality | 9.1 | Uses British English, concise paragraphs, original neutral tables and updated figure captions. |

**Average score:** 9.1

Minimum category score: 8.8. The gate meets the threshold of average at least 9.0 and no category below 8.5.

## Tool Guidance Review

The new section correctly states that Archi is independent and not owned by The Open Group. It states that Archi 5.9 currently supports ArchiMate 3.2, not ArchiMate 4. It does not claim ArchiMate 4 certification for any tool. The free and paid comparison tables are original neutral summaries, not copied vendor material.

## Diagram Review

`FIG-07-01` no longer shows an unverified Serving relationship between Financial Crime Management and Customer Management.

`FIG-07-02` now separates business-to-application and application-to-technology traceability and uses full relationship labels.

`FIG-07-05` now presents two separated motivation threads: trusted customer data and faster reusable onboarding.

`FIG-07-06` now uses direct labels and a compact plateau-plus-work-package layout instead of A1 to A6 shorthand.

## Open issues

- The full ArchiMate 4 specification should still be checked by a licensed human reviewer under the applicable Open Group licence before final publication.
- Chapter 7 diagrams remain at `Review` until the final page-layout pass.

## Gate decision

Chapter 7 is `Approved` following author instruction on 2026-06-30. The quality gate passes the numeric threshold, and no diagram is marked `Approved`.
