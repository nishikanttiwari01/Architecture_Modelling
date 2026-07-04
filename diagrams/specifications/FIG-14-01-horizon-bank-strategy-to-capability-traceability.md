# FIG-14-01: Horizon Bank Strategy-to-Capability Traceability View

## Purpose

Show the navigable thread that connects Horizon Bank strategy to funded change: from a driver, through a goal and its measurable outcome, to the capabilities that must improve, and on to the initiative and course of action that lift them.

## Audience

Sponsors, business architects, enterprise architects and governance reviewers.

## Question answered

Which goal does each initiative serve, and which capabilities does each goal depend on?

## Notation

ArchiMate 4 motivation, strategy and implementation traceability view (teaching view; not a full metamodel diagram).

## Required elements

- Drivers: Customer expectation for fast access, Regulatory scrutiny of financial crime, Cost of legacy integration, Competition from digital-first banks.
- Goals: Reduce time to usable banking services, Strengthen screening traceability, Improve payment transparency, Reduce integration cost and fragility.
- Outcomes: Median onboarding time reduced, Every screening decision evidenced, Payment status available in near real time, Fewer point-to-point interfaces.
- Capabilities (controlled): Identity Verification, Financial Crime Screening, Risk Assessment, Payment Initiation, Event Governance, Notification Management, Data Governance.
- Initiatives: Onboarding Uplift, Payment Modernisation.
- Courses of action: short approach label per initiative.

## Required relationships

- Each driver influences at least one goal.
- Each goal realises or targets one outcome.
- Each outcome depends on one or more capabilities.
- Each initiative lifts one or more capabilities and traces to at least one goal.
- A capability may serve more than one goal; show shared capabilities without duplicating the capability box.

## Main flow or structure

Left-to-right columns: Drivers, Goals, Outcomes, Capabilities, Initiatives. Directional links carry short verbs (`raises`, `targets`, `depends on`, `lifts`). Keep the layout readable at book-page width; group the seven capabilities in one column.

## Alternative and exception flows

None.

## Scope

Illustrative teaching view using controlled Horizon Bank names. It is not a real bank strategy, a delivery plan or a funding commitment.

## Exclusions

- Dates, budgets, staffing and programme structure.
- Process sequence, roles and exceptions (BPMN, Chapter 15).
- System structure (C4, Chapter 16).
- Composite scoring or prioritisation numbers.

## Accessibility requirements

Every relationship carries a text label; direction is explicit. Colour is not the only carrier of meaning. Provide accessibility text listing each goal, its outcome, its capabilities and its initiative.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]`
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`
- `examples/horizon-bank/capabilities.md`
- `examples/horizon-bank/actors.md`

## Review criteria

- Every initiative traces to at least one goal, and every goal traces to at least one initiative.
- Capability names match `examples/horizon-bank/capabilities.md` exactly.
- Goals and outcomes are shown as separate elements.
- No capability is drawn as a process, organisation unit, application, project or BIAN Service Domain.
- The view reads at intended book-page width without clipped or overlapping labels.
