# FIG-14-02: Horizon Bank Onboarding Value Stream to Capability Cross-Map

## Purpose

Show each stage of the Horizon Bank customer onboarding value stream mapped to the capabilities that enable it, so a planner can see which capabilities carry a given journey and where a goal lands.

## Audience

Business architects, enterprise architects, product owners and sponsors.

## Question answered

For the onboarding journey, which capabilities enable each value stage, and where should improvement effort focus?

## Notation

Value stream to capability cross-map (grid). Consistent with the FIG-13-02 onboarding value stream, read here as a planning grid.

## Required elements

- Value stages, left to right: Need understood, Application established, Identity and eligibility confirmed, Banking relationship established, Services ready to use.
- Enabling capabilities per stage, using controlled names:
  - Need understood: Digital Servicing, Relationship Management.
  - Application established: Customer Onboarding, Document Capture.
  - Identity and eligibility confirmed: Identity Verification, Financial Crime Screening, Risk Assessment.
  - Banking relationship established: Party Management, Account Opening, Product Management.
  - Services ready to use: Digital Servicing, Notification Management, Account Servicing.
- A strategic-importance marker (`H`, `M`, `L`) beside each capability cell.
- A legend defining the markers, plus date, owner, version and an illustrative-values note.

## Required relationships

- The triggering stakeholder (Retail Customer) starts the value stream at Need understood.
- Value stages progress left to right towards the Services ready to use outcome.
- Each stage lists its enabling capabilities beneath or within the stage.

## Main flow or structure

Horizontal band of five value stages with an enabling-capability list under each stage and a text importance marker per capability. Keep the outcome (usable channels and products) at the right.

## Alternative and exception flows

None. Exceptions and sequence belong in a BPMN process, not in this cross-map.

## Scope

Illustrative teaching view using controlled Horizon Bank names. It is a value-stage and capability view, not a process model, customer journey map or Lean value stream map.

## Exclusions

- Sequence flows, roles, message flows, timers and exceptions.
- Composite scoring or investment-priority ratings (those belong on the heat map, FIG-13-05).
- System or application detail.

## Accessibility requirements

Importance markers use `H`, `M` and `L` text, not colour alone. Provide accessibility text describing each stage and its capabilities in reading order.

## Source references

- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`
- `[OPEN-GROUP-ARCHIMATE-4]`
- `examples/horizon-bank/capabilities.md`
- `examples/horizon-bank/actors.md`

## Review criteria

- Capability names match `examples/horizon-bank/capabilities.md` and the FIG-13-02 value stream.
- Value stages stay at value-stage level and do not drift into process tasks.
- Importance markers carry text, and the scoring basis, date, owner and version are visible.
- The grid reads at intended book-page width without clipped or overlapping labels.
