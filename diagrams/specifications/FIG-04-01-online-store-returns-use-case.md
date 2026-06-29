# FIG-04-01: Online Store Returns Use Case Diagram

## Purpose

Show how a UML use case diagram defines goal-level scope for the Simple Online Store returns feature.

## Audience

Beginners, analysts and architects.

## Question answered

Who interacts with the Online Store returns feature, and what goals do they pursue?

## Abstraction level

Conceptual scope view. It shows actor goals, not workflow, screens, classes or deployment.

## Notation

UML use case diagram.

## Required elements

- Subject boundary: Online Store
- Actors: Customer, Customer Support Agent, Payment Provider System, Delivery Partner System
- Use cases: Request return, Review return exception, Request refund, Request collection

## Required relationships

- Customer is associated with Request return.
- Customer Support Agent is associated with Review return exception.
- Review return exception extends Request return with condition `[policy exception]`.
- Request return includes Request refund when the return outcome requires a refund.
- Request return includes Request collection when goods need to be collected.
- Payment Provider System is associated with Request refund.
- Delivery Partner System is associated with Request collection.

## Relationship semantics

Associations mean participation, not control flow. `include` means required reused behaviour in this simplified returns scope. `extend` means conditional behaviour added to the base use case.

## Main flow or structure

Place the Online Store subject boundary in the centre. Put human actors to the left and external systems to the right. Keep goal names concise.

## Alternative and exception flows

Show Review return exception as conditional behaviour. Do not model detailed exception sequence in this figure.

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
- Include and extend relationships have correct semantics.
