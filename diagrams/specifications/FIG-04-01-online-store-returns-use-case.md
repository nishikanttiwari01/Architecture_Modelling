# FIG-04-01: Online Store returns use case diagram

## Purpose

Show how a UML use case diagram defines goal-level scope for the Simple Online Store returns feature.

## Audience

Beginners, analysts and architects.

## Question answered

Who interacts with the Online Store returns feature, and what goals do they pursue?

## Notation

UML use case diagram.

## Required elements

- Subject boundary: Online Store
- Actors: Customer, Customer Support Agent, Payment Provider System, Delivery Partner System
- Use cases: Request return, Approve return exception, Request refund, Request collection

## Required relationships

- Customer participates in Request return
- Customer Support Agent participates in Approve return exception
- Request return may include Request refund when a refund is due
- Request return may include Request collection when goods need collection
- Payment Provider System supports Request refund
- Delivery Partner System supports Request collection

## Main flow or structure

Place the Online Store subject boundary in the centre. Put human actors to the left and external systems to the right. Keep goal names concise.

## Alternative and exception flows

Show Approve return exception as a separate use case linked to Customer Support Agent. Do not model detailed exception sequence in this figure.

## Scope

Goal-level feature scope for returns.

## Exclusions

No screen flow, database schema, class structure, deployment nodes or detailed refund workflow.

## Accessibility requirements

Use clear labels, high contrast and no colour-only meaning. The figure must remain readable at book-page width.

## Source references

- `[OMG-UML]` for UML use case notation.
- `examples/simple-online-store/README.md` for stable actors and systems.

## Review criteria

- Actor names match the repository example.
- Use cases are actor goals, not internal implementation steps.
- Subject boundary is visible.
- Relationships are not over-modelled for a beginner chapter.
