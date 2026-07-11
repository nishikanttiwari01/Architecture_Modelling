# FIG-31-01: From BIAN reference concepts to implementation choices

## Specification checkpoint

- Author instruction: create and continue without a separate approval pause
- Checkpoint date: 2026-07-11
- Maximum lifecycle state after rendering: Review
- Author-authorised correction: 2026-07-11. The first render measured 1656 by 1009 pixels and did not meet the intended book-page width despite being legible. Regenerate as a compact page-width landscape no wider than 760 pixels and preferably no taller than 950 pixels.

## Purpose and question

Show how BIAN reference concepts inform, but do not determine, Horizon Bank implementation decisions.

## Question answered

How do BIAN's logical reference concepts lead to governed physical implementation choices?

## Audience and notation

Beginners and architecture teams. Original PlantUML teaching flow, not formal BIAN notation.

## Notation

Original PlantUML conceptual teaching flow.

## Required content

Show Service Landscape, Business Scenario, Service Operation, Business Object Model and semantic API/event guidance informing Horizon Bank assessment. Cross a labelled logical-reference boundary into application, contract, data, security and deployment choices. State that a Service Domain is not automatically a microservice. Show evidence feeding back to mapping decisions.

## Required elements

All reference, assessment, implementation and evidence elements stated above.

## Required relationships

Labelled informing, design-decision, evidence and feedback relationships.

## Main flow or structure

Compact landscape flow. Reference concepts feed a single Horizon Bank assessment. The assessment feeds four implementation-choice groups. Every implementation choice then feeds evidence through its own explicitly labelled relationship. Evidence can revise mapping.

## Alternative and exception flows

Many-to-many logical-to-physical mappings are permitted.

## Scope and exclusions

Conceptual orientation only. Do not claim conformance or prescribe an organisation, process or deployment topology. Do not reproduce a BIAN diagram.

## Exclusions

Formal BIAN notation, complete process and deployment topology.

## Accessibility and review

Use high contrast and textual labels, with no clipping or overlap at book-page width. Ensure caption and chapter agree and no one-to-one Service Domain to microservice mapping is implied.

## Accessibility requirements

High contrast, text labels and no colour-only meaning. Target no more than 760 pixels wide and preferably no more than 950 pixels tall at generated PNG size.

## Review criteria

No clipping, overlap, incorrect direction or one-to-one physical implication. Each `APP`, `API`, `DATA` and `OPS` to evidence relationship must carry a visible label. Confirm the compact landscape size target at native and intended book-page width.

## Sources

- `research/bian/bian-service-landscape-14.0.md`
- `research/bian/bian-introduction-how-to-guide-v7.md`
- `research/bian/bian-semantic-api-practitioner-guide-v8.1.md`

## Source references

The three recorded BIAN source notes above.
