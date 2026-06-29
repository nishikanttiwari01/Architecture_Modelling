# FIG-03-01: Annotated online store context diagram

## Purpose

Teach readers how to inspect an architecture diagram by pointing out title and purpose, scope boundary, actors, external systems, relationship labels, omissions and review questions.

## Audience

Beginners reading Chapter 3.

## Question answered

What should a reader look for when interpreting a simple architecture context diagram?

## Notation

Annotated context diagram using PlantUML. The example follows C4-style context concepts without depending on C4-PlantUML macros.

## Required elements

- Diagram title and purpose cue
- Visible purpose cue: "Purpose: Identify system scope, users, external dependencies and relationships."
- Customer
- Customer Support Agent
- Online Store system boundary
- Payment Provider System
- Delivery Partner System
- Omission note
- Review-question note

## Required relationships

- Customer to Online Store: browse, order and track delivery.
- Customer Support Agent to Online Store: manage returns and exceptions.
- Online Store to Payment Provider System: request payment authorisation or refund.
- Online Store to Delivery Partner System: send delivery request.
- Delivery Partner System to Online Store: send tracking updates.

## Main flow or structure

Place the Online Store near the centre as the system in scope. Place people outside the boundary on the left and above the system. Place external systems outside the boundary below and to the right where the labels remain readable. Add callout notes around the diagram to explain how to read it.

## Alternative and exception flows

None.

## Scope

Simple Online Store context reading example for Chapter 3.

## Exclusions

No internal components, database tables, cloud infrastructure, detailed business process flow or security sequence.

## Accessibility requirements

Use concise labels, strong contrast, clear arrow labels and callout text that remains readable at book-page width. Do not rely on colour alone.

## Source references

- `[C4-OFFICIAL]`
- `[ISO-42010]`

## Review criteria

- The diagram is readable at book-page width.
- Callouts explain the purpose, omissions and reading checks without overcrowding the diagram.
- Arrow directions and labels match the Chapter 3 prose.
- Delivery request and tracking update are represented as directional relationships.
- Payment response detail is explicitly omitted.
- The diagram uses stable Simple Online Store names.
- SVG and PNG outputs have no clipped text, no unreadable font sizes and no overlapping labels.

## Authorisation note

The author explicitly accepted Chapter 2 and instructed Codex to proceed to Chapter 3 on 2026-06-28. This authorises the required Chapter 3 production artefacts. The diagram remains in `Review`.
