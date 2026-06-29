# FIG-07-05: Horizon Bank Motivation View

## Purpose

Show why Horizon Bank is changing its customer onboarding architecture.

## Audience

Sponsors, enterprise architects, transformation leads, reviewers and beginner readers learning motivation elements.

## Question answered

Which drivers, assessments, goals, requirements and constraints explain the target onboarding architecture?

## Abstraction level

Architecture motivation overview. It shows reasons and constraints, not solution structure in detail.

## Notation

ArchiMate motivation view.

## Required elements

- Stakeholder: Retail Banking Sponsor
- Drivers: Duplicate customer databases, Slow product launches, Limited end-to-end process visibility
- Assessments: Customer data fragmented, Onboarding duplicated across products
- Goals: Trusted customer view, Improved straight-through processing, Reusable onboarding capability
- Requirements: Reuse customer identity service, Record screening evidence, Integrate retained core systems
- Constraint: Core Deposit System retained initially

## Required relationships

- Drivers influence assessments.
- Assessments influence goals.
- Goals are realised by or refined into requirements.
- Constraint constrains relevant requirements or target architecture.

## Main flow or structure

Arrange from stakeholder and drivers on the left to goals and requirements on the right. Keep the retained legacy constraint visibly connected.

## Alternative and exception flows

Not applicable.

## Scope

Motivation for the Horizon Bank customer onboarding transformation.

## Exclusions

No detailed solution design, project plan, regulatory advice, risk-control catalogue or business-case financials.

## Accessibility requirements

Use readable labels and concise wording. Avoid vague goal labels.

## Source references

- `[OPEN-GROUP-ARCHIMATE-3.2]` for motivation element concepts.
- `examples/horizon-bank/README.md` for Horizon Bank starting problems and transformation goals.

## Review criteria

- Motivation elements explain concrete reasons for change.
- Goals are testable enough to connect to architecture choices.
- The view does not become a slogan map.
- Constraints are visible and not hidden in prose only.
