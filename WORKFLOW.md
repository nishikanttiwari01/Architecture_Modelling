# Book Production Workflow

## 1. Plan

Confirm chapter purpose, reader outcomes, dependencies, required models, examples and word-count range.

**Exit criteria:** The chapter file has a complete section plan and the status is `Outlined`.

## 2. Research

Collect current primary sources, create source notes and identify version-sensitive facts.

**Exit criteria:** Required factual claims have adequate sources and the status is `Researching` or ready for drafting.

## 3. Draft

Write the chapter using the agreed teaching sequence and examples. Add source keys while drafting.

**Exit criteria:** All planned sections contain coherent prose and the status is `Drafting`.

## 4. Diagram

Register, specify, create, render, visually review and explain each required figure. Keep editable source and SVG export.

**Exit criteria:** Required diagrams are present or explicitly deferred with a reason; status may be `Diagramming`.

Required diagram workflow:

1. Add or confirm the `DIAGRAM_REGISTER.md` row.
2. Create a specification under `diagrams/specifications/` from `templates/diagram-specification-template.md`.
3. Obtain author approval for the specification before creating source.
4. Create source under the appropriate `diagrams/source/` subdirectory.
5. Render SVG output where the toolchain supports terminal rendering.
6. Run `python scripts/validate-diagrams.py`.
7. Run `python scripts/check-diagram-register.py`.
8. Visually review the rendered SVG or PNG for clipping, overlap, line crossings, font size, contrast, arrow direction, terminology and page-width readability.
9. Update chapter text, caption and `DIAGRAM_REGISTER.md`.

Codex may move a diagram to `Review` after successful rendering and validation. Only the author may mark a diagram `Approved`. `Exported` only means that an output file exists.

## 5. Review

Perform separate review passes:

1. Technical accuracy
2. Beginner comprehension
3. Educational flow
4. Terminology and cross-chapter consistency
5. Diagram quality and accessibility
6. Source and copyright verification
7. Copy-editing

**Exit criteria:** Critical findings are resolved and status is `Ready for Author Approval`.

## 6. Author approval

The author reviews the chapter and either approves it or records required revisions.

**Exit criteria:** Status is `Approved` only after explicit author action.

## 7. Integration

Update cross-references, glossary, registers, combined build and whole-book consistency.

## 8. Publication

Generate release formats, perform final link and source checks, archive source versions and create a Git tag only when explicitly authorised.

## Change discipline

Every meaningful task must update:

- `STATUS.md`
- `CHANGELOG.md`
- `DECISIONS.md` when a material choice was made
- `DIAGRAM_REGISTER.md` when figures change
- `SOURCE_REGISTER.md` when major sources change
