# Chapter 12 Quality Gate, 2026-07-02

## Scope

- Chapter: `manuscript/part-02-modelling-languages/12-security-modelling.md`
- Status reviewed: `Diagramming`
- Figures reviewed: `FIG-12-01`, `FIG-12-02`, `FIG-12-04`, `FIG-12-05`
- Decision basis: Author acceptance of `DEC-020` and the four remaining Chapter 12 figure specifications.

## Gate decision

Chapter 12 is `Approved` by explicit author instruction on 2026-07-02.

Final quality score: `9.1 / 10`

Diagram status: `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` remain `Review`, not `Approved`, pending final book-page layout review.

## Completed since the review pass

- Recorded author approval of Chapter 12.
- Removed reader-facing `Planned chapter structure` and `Drafting notes` sections from the approved manuscript.
- Accepted `DEC-020`, retaining `TABLE-12-01` as a manuscript table and leaving retired `FIG-12-03` unused.
- Created PlantUML source for `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05`.
- Rendered SVG exports and PNG previews for all four active Chapter 12 figures.
- Added figure references, captions, accessibility text and limitation statements to the Chapter 12 manuscript.
- Updated `DIAGRAM_REGISTER.md`, `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`, `RESUME.md` and Chapter 12 review records.
- Applied the final diagram correction pass to `FIG-12-01`, `FIG-12-04` and `FIG-12-05`.
- Applied the focused `FIG-12-04` follow-up correction so the Operations Analyst receives the assigned repair case and permitted payment context through the authorised operations interface before submitting a controlled repair action.

## Visual review

| Figure | Result | Notes |
|---|---|---|
| `FIG-12-01` | Pass for review | The incoming public request is not called authenticated. The edge-to-runtime flow is labelled as filtered and routed, while validation responsibilities remain inside the application runtime. The diagram is wide and should receive page-layout review. |
| `FIG-12-02` | Pass for review | Sequence order is readable and separates authentication, session creation and access authorisation. |
| `FIG-12-04` | Pass for review | Focused routing and semantic corrections were applied. The Digital Channel Access Context is labelled correctly, the Operations Analyst receives the assigned repair case and permitted payment context through the authorised operations interface before submitting a controlled repair action, the `T12-06` event-consumer exposure path is complete, and labels remain readable. |
| `FIG-12-05` | Pass for review | Attack paths, exclusions, OR semantics and mitigation notes are readable. `T12-08` now has a structural AND node with two visible child conditions. |

## Checks

| Check | Result |
|---|---|
| `python scripts/check-structure.py` | Passed |
| `python scripts/check-links.py` | Passed, 191 local Markdown links checked |
| `python scripts/check-terminology.py` | Passed |
| `python scripts/validate-diagrams.py` | Passed |
| `python scripts/check-diagram-register.py` | Passed, 54 figure entries checked |
| `python scripts/word-count.py` | Passed, total manuscript word count 84,337 |
| `python scripts/build-book.py` | Passed, combined Markdown created from 75 manuscript files |

Rendering verification:

- `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` were rendered from the latest PlantUML sources to SVG and PNG on 2026-07-02.
- The final correction render updated `FIG-12-01`, `FIG-12-04` and `FIG-12-05`; `FIG-12-02` was unchanged in this pass.
- The focused follow-up render updated `FIG-12-04` only, adding the authorised-operations-interface presentation flow to the Operations Analyst.

## Remaining work and risks

- The four Chapter 12 figures remain `Review`, not `Approved`.
- Final page-layout review should check the wider figures, especially `FIG-12-01` and `FIG-12-04`, at intended book-page width.
- No new sources were required for diagram production.
