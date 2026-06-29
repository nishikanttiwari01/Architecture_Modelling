# FIG-07-05: Horizon Bank Motivation View

## Purpose

Show why Horizon Bank is changing its customer onboarding architecture using ArchiMate 4 motivation elements.

## Audience

Sponsors, enterprise architects, transformation leads, reviewers and beginner readers learning motivation elements.

## Question answered

Which stakeholders, drivers, assessments, goals, outcomes, requirements and principles explain the target onboarding architecture?

Decision or concern: decide whether the onboarding target architecture is justified by concrete drivers, assessments, goals and requirements.

## Required elements

ArchiMate 4 elements:

- Stakeholder: Retail Banking Sponsor
- Stakeholder: Compliance Reviewer
- Drivers: Duplicate customer databases, Slow product launches, Limited end-to-end process visibility
- Assessments: Customer data fragmented, Onboarding duplicated across products
- Goals: Trusted customer view, Improved straight-through processing, Reusable onboarding capability
- Outcomes: Reduced duplicate customer capture, Faster retail product onboarding
- Requirements: Reuse customer identity service, Record screening evidence, Integrate retained core systems
- Principle: Customer data has an accountable system of record

## Required relationships

Relationship types and directions:

- Association from stakeholders to their main concerns where needed.
- Influence from drivers to assessments.
- Influence from assessments to goals.
- Influence from goals to outcomes.
- Influence from requirements to goals. Do not use realisation between requirements and goals unless a later licensed ArchiMate 4 relationship review confirms a stronger relationship for this book.
- Influence from principle to requirements where the principle shapes the requirement.

## Reusable model concepts

- Trusted customer view goal must align with Chapter 7 prose and FIG-07-06 migration content.
- Reuse customer identity service requirement must trace to Customer Profile Management Service in FIG-07-02 and FIG-07-03.
- Integrate retained core systems requirement must trace to the retained Core Deposit System note in FIG-07-06.

## Notation and legend

Use ArchiMate 4 motivation notation. The legend must identify Stakeholder, Driver, Assessment, Goal, Outcome, Requirement, Principle, influence and association. Avoid using the removed ArchiMate 3.2 Constraint element.

## Main flow or structure

Arrange stakeholders and drivers on the left, assessments in the middle, and goals, outcomes, principles and requirements on the right. Keep the cause-and-effect reading direction visible.

## Alternative and exception flows

Not applicable.

## Scope

Motivation for the Horizon Bank customer onboarding transformation.

## Exclusions

No detailed solution design, project plan, regulatory advice, risk-control catalogue, financial business case or current-state application inventory.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]` for ArchiMate 4 motivation elements and relationship concepts.
- `examples/horizon-bank/README.md` for Horizon Bank starting problems and transformation goals.

## Accessibility requirements

Use readable labels and concise wording. Avoid vague goal labels. Ensure line direction is easy to follow from drivers and assessments to goals, outcomes and requirements.

## Source creation authorisation

The author authorised source creation from the corrected specification on 2026-06-29. The rendered diagram remains in `Review`.

## Review criteria

- Motivation elements explain concrete reasons for change.
- Goals and outcomes are testable enough to connect to architecture choices.
- The view does not become a slogan map.
- Removed elements such as Constraint are not used as current ArchiMate 4 notation.
- Requirements trace to Chapter 7 application and migration examples.
