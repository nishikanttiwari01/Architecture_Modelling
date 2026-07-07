# FIG-14-02: Horizon Bank Onboarding Value Stream to Capability Cross-Map

## Purpose

Show, as a matrix, how each unique onboarding capability contributes to each stage of the Horizon Bank customer onboarding value stream, and how strategically important each capability is for one named onboarding goal.

## Audience

Business architects, enterprise architects, product owners and the Executive Sponsor.

## Question answered

For the onboarding journey, which capabilities are primary or supporting enablers at each value stage, and how important is each capability for reducing time to usable banking services?

## Notation

Value stream to capability cross-map, drawn as a matrix. It is deliberately different from FIG-13-02, which is a horizontal value stream with capabilities listed beneath each stage. This figure is a grid with capabilities as rows and value stages as columns.

## Required elements

- Columns: the five onboarding value stages, in order: S1 Need understood; S2 Application established; S3 Identity and eligibility confirmed; S4 Banking relationship established; S5 Services ready to use.
- Rows: the unique controlled capabilities listed in the matrix data below. The level-one parent `Customer Onboarding` is represented by its level-two children (`Document Capture`, `Identity Verification`, `Risk Assessment`) and is not itself a row, to avoid double counting.
- Cell markers: `P` primary enabler; `S` supporting enabler; blank means no material contribution in this teaching view.
- Final column: strategic importance (`H`, `M`, `L`) assessed against one named goal only.
- Legend defining `P`, `S`, blank and the importance scale.
- Metadata block: assessment date; assessment owner or workshop group; version; scoring definition; illustrative-data warning.

## Required relationships

- The triggering stakeholder (Retail Customer) starts the value stream at S1 and the outcome (usable channels and products) is reached at S5; show this as a caption or header, not as matrix cells.
- Every non-empty cell is defined exactly in the matrix data below; none is left for the diagram creator to invent.

## Main flow or structure

Render as a grid. Do not repeat a full capability list beneath every stage, and do not use colour as the only marker; the `P`, `S` and importance letters carry the meaning.

### Exact matrix data

Strategic importance is assessed against GOAL-14-01, Reduce time to usable banking services, only. This table is the authoritative matrix dataset for FIG-14-02: every `P`, `S`, blank cell and importance rating must be reproduced exactly, and none is left for the diagram creator to infer. The `P`, `S` and importance markers match the Chapter 14 manuscript matrix.

| Capability | S1 Need understood | S2 Application established | S3 Identity and eligibility confirmed | S4 Banking relationship established | S5 Services ready to use | Strategic importance for GOAL-14-01 | Rationale |
|---|---|---|---|---|---|---|---|
| Digital Servicing | P | | | | P | M | Enables self-service capture and later service use |
| Relationship Management | S | | | | | L | Helps clarify need but is not the speed bottleneck |
| Document Capture | | P | | | | M | Structured application information gates progress |
| Identity Verification | | | P | | | H | Primary gate on onboarding speed and drop-out |
| Risk Assessment | | | P | | | H | Assessment step that can delay eligibility |
| Financial Crime Screening | | | P | | | H | Screening decision can delay eligibility |
| Party Management | | | | P | | M | Establishes authoritative party record |
| Account Opening | | | | P | | M | Establishes account record and access |
| Product Management | | | | S | | L | Supplies product and eligibility references |
| Notification Management | | | | | S | L | Confirms readiness to the customer |
| Account Servicing | | | | | S | L | Supports first service use |

## Alternative and exception flows

None. Exceptions and sequence belong in a BPMN process, not in this cross-map.

## Scope

Illustrative teaching view using controlled Horizon Bank names. It is a value-stage and capability contribution view assessed against one named goal.

## Exclusions

This figure must not show:

- current funding or current investment status;
- proposed investment priority;
- delivery risk or constraint;
- any composite investment score.

Those belong in the separate heat-map discussion (FIG-13-05 and the Chapter 14 investment table). This figure also is not BPMN, a customer journey map, a Lean value-stream map, an application landscape or an interface model.

## Accessibility requirements

Markers use `P`, `S` and blank, and importance uses `H`, `M`, `L` text, never colour alone. Provide accessibility text describing, for each stage column, which capabilities are primary and which are supporting, and listing each capability's importance rating.

## Source references

- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`
- `[OPEN-GROUP-ARCHIMATE-4]` (capability concept name only)
- `examples/horizon-bank/capabilities.md`
- `examples/horizon-bank/actors.md`

## Review criteria

- The figure is a genuine matrix and not a duplicate of FIG-13-02.
- Every `P`, `S` and importance value matches the exact matrix data above; none is invented at production time.
- Capability names match `examples/horizon-bank/capabilities.md`, and the parent `Customer Onboarding` is not double counted with its children.
- Strategic importance is stated as being against GOAL-14-01 only, with date, owner, version, scoring definition and an illustrative-data warning.
- Funding, priority, delivery risk and composite scores are absent.
- The grid reads at book-page width without clipped or overlapping labels.
