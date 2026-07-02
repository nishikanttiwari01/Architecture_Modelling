# Chapter 12 Consistency Review, 2026-07-01

## Scope

- Chapter: `manuscript/part-02-modelling-languages/12-security-modelling.md`
- Related repository files: `BOOK_PLAN.md`, `STATUS.md`, `DIAGRAM_REGISTER.md`, `SOURCE_REGISTER.md`, `GLOSSARY.md`, `DECISIONS.md`, `RESUME.md`
- Status after review: `Revision Required`

## Findings

| ID | Severity | Evidence | Required action | Resolution status |
|---|---|---|---|---|
| CH12-CON-01 | Major | `STATUS.md` and frontmatter showed `Diagramming`, but the review requires corrections. | Move Chapter 12 to `Revision Required`. | Resolved. |
| CH12-CON-02 | Major | `FIG-12-03` was registered as a figure even though the content is a table. | Retire `FIG-12-03`, do not reuse the ID, and record `TABLE-12-01` in the manuscript. | Resolved. |
| CH12-CON-03 | Major | `DEC-019` approved five security figures, conflicting with the revised artefact set. | Supersede `DEC-019` and add an artefact-type decision. | Resolved. |
| CH12-CON-04 | Minor | Chapter 12 source register lacked a stable privacy source and attack-tree source. | Add source notes and register entries. | Resolved. |
| CH12-CON-05 | Minor | Glossary did not distinguish access authorisation, business approval and payment-provider authorisation. | Add or revise glossary terms. | Resolved. |
| CH12-CON-06 | Major | Diagram specification references needed to avoid implying author approval or created source files. | Keep four specifications at planned status and source/export pending author approval. | Resolved. |
| CH12-CON-07 | Major | `Customer Support Agent` appeared in `TABLE-12-01` and the exercise, but the Horizon Bank actor model did not register that role. | Add the Horizon Bank Customer Support Agent to `examples/horizon-bank/actors.md`. | Resolved. |
| CH12-CON-08 | Major | Threat IDs did not align across manuscript control map, `FIG-12-04` and `FIG-12-05`. | Align `T12-01` through `T12-08` across manuscript, DFD spec and attack-tree spec. | Resolved. |
| CH12-CON-09 | Minor | `DEC-020` reclassification is implemented but not author-approved. | Keep `DEC-020` as `Proposed` and record the table implementation as provisional. | Resolved. |

## Consistency conclusion

Repository tracking now matches the revised Chapter 12 scope. `FIG-12-03` is intentionally absent from the active diagram register and its retired state is recorded in the decision log as provisional pending author approval of `DEC-020`. No Chapter 13 work was started.

## Diagram-production update, 2026-07-02

The author approved `DEC-020`, so the `FIG-12-03` retirement and `TABLE-12-01` replacement are no longer provisional. `DEC-020` is now `Accepted`.

Repository tracking now records:

- Chapter 12 status: `Diagramming`
- `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` status: `Review`
- PlantUML source under `diagrams/source/plantuml/`
- SVG exports under `diagrams/exported/svg/`
- PNG previews under `diagrams/exported/png/`

No Chapter 13 work was started.

## Final diagram-correction update, 2026-07-02

Repository tracking remains consistent after the final diagram correction pass:

- Chapter 12 status remains `Diagramming`.
- `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05` remain `Review`.
- `TABLE-12-01` remains a manuscript table and retired `FIG-12-03` remains unused.
- `DEC-020` remains `Accepted`.
- `FIG-12-04` remains a PlantUML source diagram.
- The `FIG-12-04` Operations Analyst flow now includes both assigned repair case presentation from the authorised operations interface and controlled repair action back to that interface.
- Chapter 13 remains `Planned` and was not started.
