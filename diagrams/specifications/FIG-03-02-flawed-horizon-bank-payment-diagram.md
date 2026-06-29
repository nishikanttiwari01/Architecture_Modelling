# FIG-03-02: Flawed Horizon Bank Payment Diagram

## Purpose

Show a deliberately weak payment diagram so readers can practise identifying review problems before seeing a corrected version.

## Audience

Beginners reading Chapter 3 and reviewers learning diagram quality checks.

## Question answered

What kinds of problems should a reader detect before trusting a payment architecture diagram?

## Notation

Informal PlantUML box-and-line diagram.

## Required elements

- Ambiguous metadata stating that the purpose is unclear and the state is not identified.
- Customer.
- Mobile Banking.
- Payment Orchestration.
- A business activity mixed into the diagram, such as Approve Payment.
- Fraud Screening.
- Sanctions.
- Core Banking.
- Payment Rail marked as unclear or external.
- Operations with ambiguous ownership.
- Callouts for hidden trust boundary, missing exceptions and mixed concepts.

## Required relationships

- Include at least one vague relationship label, such as "uses".
- Include at least one missing relationship label.
- Include at least one vague update relationship.
- Include an unexplained relationship to an external payment rail.
- Include a relationship involving operations without making ownership clear.

## Main flow or structure

Place the payment-related elements in a rough left-to-right flow, but deliberately leave the purpose, state, ownership, trust boundary and exception path unclear. The diagram should be realistic enough that the reader can recognise common review findings.

## Alternative and exception flows

The diagram should deliberately omit exception handling to create a review finding.

## Scope

Horizon Bank payment diagram quality example for Chapter 3.

## Exclusions

Do not make the flawed diagram correct. Do not add a complete notation legend, explicit trust boundary, full ownership model or complete exception path.

## Accessibility requirements

Use readable text, strong contrast and short labels. Problems should be visible through words and callouts, not colour alone.

## Source references

- Repository Horizon Bank case study.

## Review criteria

- The diagram deliberately includes the listed review problems.
- The figure remains readable at book-page width.
- Labels are legible and do not overlap.
- The chapter prose explains that the diagram is intentionally flawed.

## Authorisation note

The author requested this figure as part of the Chapter 3 revision before author review. The diagram remains in `Review`.
