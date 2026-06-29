# FIG-07-06: Horizon Bank Implementation and Migration View

## Purpose

Show a simplified current, transition and target architecture path for Horizon Bank customer onboarding.

## Audience

Transformation leads, enterprise architects, delivery planners, governance reviewers and beginner readers learning migration elements.

## Question answered

How does Horizon Bank move from product-specific onboarding to a reusable onboarding and customer platform?

## Abstraction level

Architecture migration overview. It shows major architecture states and work packages, not a detailed project schedule.

## Notation

ArchiMate implementation and migration view.

## Required elements

- Plateaus: Current State, Transition State, Target State
- Gaps: Duplicate onboarding removed, Trusted customer view established
- Work packages: Introduce Customer Onboarding Platform, Introduce Party and Customer Platform, Integrate retained Core Deposit System
- Deliverables: Reusable onboarding service, Customer profile service, Core system adapter
- Constraint or note: Core Deposit System retained initially

## Required relationships

- Work packages realise deliverables.
- Deliverables help close gaps between plateaus.
- Transition State follows Current State and precedes Target State.
- Retained Core Deposit System constrains the transition.

## Main flow or structure

Arrange plateaus from left to right. Place work packages and deliverables between the relevant plateaus.

## Alternative and exception flows

Do not show failed delivery paths or detailed rollback plans in this introductory view.

## Scope

High-level customer onboarding transformation for Horizon Bank.

## Exclusions

No Gantt chart, sprint plan, detailed dependency network, cost model, procurement plan or release-management procedure.

## Accessibility requirements

Use readable labels, clear left-to-right progression and no colour-only meaning.

## Source references

- `[OPEN-GROUP-ARCHIMATE-3.2]` for plateau, gap, work package and deliverable concepts.
- `examples/horizon-bank/README.md` and `examples/horizon-bank/system-landscape.md` for stable scenario context.

## Review criteria

- The migration view shows architecture states, not detailed delivery tasks.
- Current, transition and target states are distinct.
- Retained legacy constraints are visible.
- The view aligns with the motivation and layered views.
