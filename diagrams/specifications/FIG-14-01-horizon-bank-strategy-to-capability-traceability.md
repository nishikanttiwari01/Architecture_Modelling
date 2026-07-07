# FIG-14-01: Horizon Bank Strategy-to-Capability Traceability View

## Purpose

Show the navigable thread that connects Horizon Bank strategy to funded change: from a driver, through a goal and its measurable outcome, to the capabilities that must improve, and on to the course of action and work package that lift them.

## Audience

Executive Sponsor, business architects, enterprise architects and governance reviewers.

## Question answered

Which goal does each work package serve, and which capabilities does each goal depend on?

## Notation

ArchiMate-informed strategy traceability teaching view. This is not a formal ArchiMate view. It uses ArchiMate concept names as element types (Driver, Goal, Outcome, Capability, Course of Action, Work Package) but its connectors are simplified, directional teaching traceability links, not formal ArchiMate relationship notation. The exact ArchiMate 4 relationship types and directions are defined in the licensed specification text, which is out of scope for this AI-assisted drafting; see `research/archimate/open-group-archimate-4.md`. The `Constraint` element is not used, because it was removed in ArchiMate 4.

## Required elements

Every element carries the stable identifier used in the manuscript.

- Drivers: DRV-14-01 Customer expectation for fast account access; DRV-14-02 Regulatory scrutiny of financial crime; DRV-14-03 Cost of legacy integration; DRV-14-04 Competition from digital-first banks.
- Goals: GOAL-14-01 Reduce time to usable banking services; GOAL-14-02 Strengthen screening traceability; GOAL-14-03 Improve payment transparency; GOAL-14-04 Reduce integration cost and fragility.
- Outcomes: OUT-14-01 Median onboarding time reduced; OUT-14-02 Every screening decision evidenced; OUT-14-03 Payment status available promptly; OUT-14-04 Fewer point-to-point interfaces. Show each outcome with its ID and a concise measure label only; full baseline, target, scope, time horizon, owner and evidence are held in the manuscript outcome-measure table.
- Capabilities (controlled names): Identity Verification, Financial Crime Screening, Risk Assessment, Payment Initiation, Event Governance, Notification Management, Data Governance, Payment Screening.
- Courses of Action: COA-14-01 Streamline identity and screening within onboarding; COA-14-02 Modernise payments through governed reuse and events.
- Work Packages: WP-14-01 Onboarding Uplift; WP-14-02 Payment Modernisation. Display the familiar initiative name as the Work Package label, for example "Work Package WP-14-01: Onboarding Uplift".

## Required relationships

Use the exact mapping below. Each row is one traceability thread. Connectors are simplified teaching links with neutral directional verbs (for example, `raises`, `sets`, `needs`, `guides`, `delivers`); do not present them as formal ArchiMate relationships. This table is the authoritative traceability dataset for FIG-14-01: the figure must reproduce these four threads exactly, including every identifier, label, capability set, course of action, work package, stakeholder owner and open assumption. No cell value may be inferred or invented at production time, and the same four rows appear in the Chapter 14 manuscript traceability table.

| Driver ID and label | Goal ID and label | Outcome ID and label | Capabilities | Course of Action | Work Package | Stakeholder owner | Open assumption or decision |
|---|---|---|---|---|---|---|---|
| DRV-14-01 Customer expectation for fast account access | GOAL-14-01 Reduce time to usable banking services | OUT-14-01 Median onboarding time reduced | Identity Verification, Financial Crime Screening, Risk Assessment | COA-14-01 Streamline identity and screening within onboarding | WP-14-01 Onboarding Uplift | Executive Sponsor | Baseline and target to be established |
| DRV-14-02 Regulatory scrutiny of financial crime | GOAL-14-02 Strengthen screening traceability | OUT-14-02 Every screening decision evidenced | Financial Crime Screening, Payment Screening, Data Governance | COA-14-01 and COA-14-02 | WP-14-01 and WP-14-02 | Compliance Officer | Evidence-retention scope to be agreed |
| DRV-14-04 Competition from digital-first banks | GOAL-14-03 Improve payment transparency | OUT-14-03 Payment status available promptly | Payment Initiation, Event Governance, Notification Management | COA-14-02 Modernise payments through governed reuse and events | WP-14-02 Payment Modernisation | Product Manager | Latency target to be agreed |
| DRV-14-03 Cost of legacy integration | GOAL-14-04 Reduce integration cost and fragility | OUT-14-04 Fewer point-to-point interfaces | Event Governance, Data Governance | COA-14-02 Modernise payments through governed reuse and events | WP-14-02 Payment Modernisation | Platform Engineer | Interface-count baseline to be established |

Shared capabilities (for example, Financial Crime Screening in the DRV-14-01 and DRV-14-02 threads) may appear more than once as visual references only when the same capability name is shown and the caption states that repeated appearances refer to one controlled capability. GOAL-14-02 is deliberately served by both WP-14-01 and WP-14-02.

## Main flow or structure

Do not force a single many-to-many network through one central capability column, because four drivers, four goals, four outcomes, eight referenced capabilities, two courses of action and two work packages would create an unreadable connector web at book-page width. Use one of the following readable layouts:

1. Four aligned strategy threads, each a horizontal lane keyed by stable IDs (Driver to Goal to Outcome to Capabilities to Course of Action to Work Package); or
2. A hybrid: motivation chains (Driver to Goal to Outcome) above, and a capability-to-work-package matrix below; or
3. A two-part figure combining the two.

Whichever layout is used, the four threads in the relationship table must be reproducible by a reader without inference.

## Alternative and exception flows

None.

## Scope

Illustrative teaching view using controlled Horizon Bank names and stable IDs. It is not a real bank strategy, a delivery plan or a funding commitment.

## Exclusions

- Dates, budgets, staffing and programme structure.
- Process sequence, roles and exceptions (BPMN, Chapter 15).
- System or application structure (C4, Chapter 16).
- Composite scoring, prioritisation numbers or proof of funding.
- Formal ArchiMate relationship notation.

## Accessibility requirements

Every element shows its stable ID and label. Every connector carries a text label and an explicit direction. Colour is not the only carrier of meaning. Provide accessibility text listing each of the four threads in full (driver, goal, outcome, capabilities, course of action, work package and owner).

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]` (concept names and removed `Constraint`; not relationship semantics)
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`
- `research/archimate/open-group-archimate-4.md` (relationship-verification decision)
- `examples/horizon-bank/capabilities.md`
- `examples/horizon-bank/actors.md`

## Limitation note (required on the figure)

State that the figure:

- shows strategic traceability only;
- uses simplified teaching links, not formal ArchiMate relationships;
- does not prove that an outcome was achieved;
- does not prove that funding was committed or granted;
- does not replace a portfolio roadmap or a benefits-realisation plan;
- contains illustrative Horizon Bank teaching data.

## Review criteria

- Every work package traces to at least one goal, and every goal in the table traces to at least one work package.
- The four threads match the manuscript traceability table and outcome IDs exactly.
- Capability names match `examples/horizon-bank/capabilities.md`.
- Courses of Action appear as first-class elements, not only as prose.
- Outcomes show IDs and concise measure labels, with no unqualified target such as "near real time" presented as complete.
- The notation is labelled as an ArchiMate-informed teaching view, and no connector is described as formal ArchiMate semantics.
- The layout is readable at book-page width and is not a single many-to-many connector web.
