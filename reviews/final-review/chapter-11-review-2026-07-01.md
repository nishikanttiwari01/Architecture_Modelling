# Chapter 11 Final Review, 2026-07-01

## Scope

- Chapter: 11, Infrastructure and Deployment Modelling
- Manuscript: `manuscript/part-02-modelling-languages/11-infrastructure-deployment-modelling.md`
- HEAD reviewed: `99837319de0a9aa00358e83662fa3b7270e764b1`
- Review type: Final quality gate readiness

## Findings

| ID | Severity | Affected file / section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH11-FINAL-01 | Critical | `reviews/chapter-gates/CH-11-quality-gate.md` | Current quality gate predates this review and records score 9.0 with known open technical issues. | Rewrite the quality gate after corrections and fresh checks. | Resolved, gate rewritten with 2026-07-01 evidence. |
| CH11-FINAL-02 | Major | Chapter 11 diagrams | Changed PlantUML sources must be rendered and visually reviewed before returning the chapter to author approval readiness. | Render changed figures to SVG and PNG, confirm files exist and inspect output for clipping, overlap, readability, arrow direction and contrast. | Resolved, affected figures rerendered and visually inspected, including new `FIG-11-06`. |
| CH11-FINAL-03 | Major | Repository validation | Required checks and build must be rerun after the corrections. | Run structure, links, terminology, diagram validation, diagram register, word count and book build checks. | Resolved, required checks and `build-book.py` completed with exit code 0 on 2026-07-01; final rerun recorded in task report. |
| CH11-FINAL-04 | Major | Observability figure decision | Initial review instruction said not to create `FIG-11-06` automatically and to record whether a dedicated observability view is needed. The author later explicitly requested `FIG-11-06`. | Supersede the earlier decision, create the dedicated observability figure and record the decision. | Resolved, DEC-017 superseded by DEC-018 and `FIG-11-06` specification, PlantUML source, SVG, PNG, manuscript reference and register entry created. |
| CH11-FINAL-05 | Minor | Git safety | The later task explicitly requests commit and push, and still says not to begin Chapter 12. | Commit and push only after validations pass, and do not draft Chapter 12. | Resolved for review readiness: validations passed and no Chapter 12 drafting was performed. Commit and push are the final task action. |

## Notes

- Chapter 11 was moved to `Revision Required` while corrections were in progress, then returned to `Ready for Author Approval` after the six-figure quality gate passed.
- Diagrams remain `Review`; Codex must not mark them `Approved`.
