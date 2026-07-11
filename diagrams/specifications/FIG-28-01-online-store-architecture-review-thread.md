# FIG-28-01: Online Store Architecture Review Thread

## Authorisation and status

- Authorisation to create the specification and proceed without a separate approval pause: author instruction dated 2026-07-11.
- This specification is the required checkpoint before diagram source production.
- Revision history: native inspection of the first landscape render showed an excessively wide, unreadable figure. The specification was revised on 2026-07-11 to require a compact top-to-bottom layout before regeneration.
- Correction history: the resulting 760 by 1008 pixel portrait render was readable at native width but unnecessarily tall for a book page and did not meet the stated approximate 500 pixel target. Under the author's 2026-07-11 authorisation to correct and regenerate without a further pause, this specification now requires a compact portrait export no taller than 800 pixels. Regeneration evidence is pending until source and exports are recreated from this committed specification.
- Outcome-layout clarification: under the same author authorisation dated 2026-07-11, the three outcome choices may use a compact vertically staggered arrangement rather than one horizontal rank. This keeps arrow labels separate, avoids crossings and preserves the page-fit and readability achieved by the compact portrait layout. Regeneration evidence is pending until the exports are recreated from this committed clarification.
- Consistency correction: the figure must identify the carried Online Store checkout scope rather than read as a generic review flow. The trigger and scope must name `FR-25-01`, `QA-25-01` and `ADR-26-01`; the review package must include checkout evidence; and the findings must include a checkout-specific payment-timeout risk. This correction is to be committed before source and export regeneration.
- Maximum Codex status: Review.

## Purpose

Show architecture review as an evidence-led, iterative assessment that produces decisions and owned follow-up, rather than a ceremonial meeting or design-by-committee.

## Audience

Beginner architects, delivery leads, engineers, security and data practitioners, operators, business representatives and reviewers.

## Question answered

How does a review use scoped questions and evidence to reach a proportionate outcome and follow through on unresolved concerns?

## Notation

Original PlantUML review-flow teaching view.

## Required elements

Show review trigger and scope for `FR-25-01`, `QA-25-01` and `ADR-26-01`; a review package containing focused views, Architecture Decision Records (ADRs), checkout tests and payment-timeout evidence; stakeholder questions covering functional fit, data, integration, security, performance, resilience and operability; evidence assessment; findings classified as risk, decision, action or exception, including the checkout payment-timeout risk; a review outcome; owned follow-up; and feedback to the architecture or evidence.

## Required relationships

Label preparation, questioning, assessment, outcome and follow-up relationships. Show that an evidence gap or material finding can revise the design, evidence or review scope.

## Main flow or structure

Use a compact portrait layout targeting 700 to 760 pixels wide and no more than 800 pixels high for book-page readability. Arrange preparation as one row, questions and evidence assessment as a second row, then findings, compact vertically staggered outcome choices and follow-up. The staggering must keep labels readable and avoid excessive crossings. Keep preparation, assessment, outcome and follow-up visually distinct. The outcome must allow proceed, proceed with conditions, or revise and return.

## Alternative and exception flows

Show an explicit feedback path from follow-up to architecture and evidence. An accepted exception must have an owner, rationale and review date, not disappear from the flow.

## Scope

Use the Online Store checkout architecture carried from Chapters 25 to 27.

## Exclusions

Exclude a universal governance method, product-specific review tooling, voting, claims that reviewers collectively own the design, and claims that one meeting proves architecture quality.

## Accessibility requirements

Use short labels, explicit arrow text and sufficient contrast. Colour may group stages but must not be the only carrier of meaning. Avoid clipping, overlap, small text and excessive crossings.

## Source references

Original figure informed by ISO/IEC/IEEE 42010:2022 architecture-description concepts, NIST Cybersecurity Framework 2.0 risk-governance guidance and the repository's quality-attribute scenario source. It reuses no source diagram.

## Review criteria

Regenerate SVG and PNG only after this corrected specification is committed. Confirm exact dimensions do not exceed 760 by 800 pixels. Inspect at intended page width for readable labels, correct arrow directions, no clipping or overlap, adequate contrast and agreement with Chapter 28. Only then may the register remain at or move to Review.
