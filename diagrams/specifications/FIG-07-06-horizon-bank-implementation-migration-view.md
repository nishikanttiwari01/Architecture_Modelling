# FIG-07-06: Horizon Bank Implementation and Migration View

## Purpose

Show a simplified current, transition and target architecture path for Horizon Bank customer onboarding using ArchiMate 4 migration elements.

## Audience

Transformation leads, enterprise architects, delivery planners, governance reviewers and beginner readers learning migration elements.

## Question answered

How does Horizon Bank move from product-specific onboarding to reusable onboarding and customer-platform capabilities without using removed ArchiMate 3.2 Gap notation?

Decision or concern: decide the main architecture states, work packages and deliverables for the onboarding transformation.

## Required elements

ArchiMate 4 elements:

- Plateaus: Current State, Transition State, Target State
- Work packages: Introduce Customer Onboarding Platform, Introduce Party and Customer Platform, Integrate retained Core Deposit System
- Deliverables: Reusable onboarding service, Customer profile service, Core system adapter
- Outcome: Reduced duplicate customer capture
- Event: Transition release completed
- Application components: Customer Onboarding Platform, Party and Customer Platform, Core Deposit System

## Required relationships

Relationship types and directions:

- Do not use Triggering directly between Plateaus merely to show time order.
- Use left-to-right layout, labelled associations, Events, Work Packages and Deliverables to explain movement from Current State to Transition State to Target State.
- Realisation from each work package to its deliverable.
- Influence from deliverables to Reduced duplicate customer capture outcome.
- Association or aggregation from plateaus to the application components present in that state, if shown.
- Serving or access relationships should be omitted unless needed for the migration concern.
- Do not use the removed Gap element. Differences between states must be explained through labels, deliverables, outcomes or prose.

## Reusable model concepts

- Customer Onboarding Platform and Party and Customer Platform must match FIG-07-02 and FIG-07-03.
- Reduced duplicate customer capture outcome must match FIG-07-05.
- Core Deposit System must match `examples/horizon-bank/system-landscape.md` and remain identified as retained initially.

## Notation and legend

Use ArchiMate 4 implementation and migration notation. The legend must identify Plateau, Work Package, Deliverable, Outcome, Event, realisation, influence and association or aggregation. It must explicitly state that Plateau order is shown by layout and labelled associations, not by Triggering, and that Gap is not used because it is not current ArchiMate 4 notation.

## Main flow or structure

Arrange plateaus from left to right: Current State, Transition State, Target State. Place work packages and deliverables between the relevant plateaus and use Events such as Transition release completed to mark movement.

## Alternative and exception flows

Do not show failed delivery paths or detailed rollback plans in this introductory view.

## Scope

High-level customer onboarding transformation for Horizon Bank.

## Exclusions

No Gantt chart, sprint plan, detailed dependency network, cost model, procurement plan, release-management procedure, BPMN flow or C4 container internals.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]` for plateau, work package, deliverable, event and outcome concepts.
- `examples/horizon-bank/README.md` and `examples/horizon-bank/system-landscape.md` for stable scenario context.

## Accessibility requirements

Use readable labels, clear left-to-right progression and no colour-only meaning. Keep state labels and deliverable labels large enough for book-page width.

## Source creation authorisation

The author authorised source creation from the corrected specification on 2026-06-29. The rendered diagram remains in `Review`.

## Review criteria

- The migration view shows architecture states, not detailed delivery tasks.
- Current, transition and target states are distinct.
- Retained legacy limits are visible in labels or prose without using the removed Constraint element.
- The removed Gap element is not used.
- The view aligns with the motivation and layered views.
