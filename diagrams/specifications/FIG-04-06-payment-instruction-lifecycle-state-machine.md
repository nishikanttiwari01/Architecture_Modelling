# FIG-04-06: Payment instruction lifecycle state machine

## Purpose

Show a UML state machine diagram for the lifecycle of a Horizon Bank payment instruction.

## Audience

Architects, developers, testers and operations.

## Question answered

What meaningful states can a payment instruction be in, and what events move it between states?

## Notation

UML state machine diagram.

## Required elements

- Initial state
- Received
- Validated
- Screening Pending
- Rejected
- Posting Pending
- Accepted
- Sent to Scheme
- Settled
- Failed
- Final state

## Required relationships

- Initial state transitions to Received
- Received transitions to Validated after mandatory checks pass
- Validated transitions to Screening Pending when screening is requested
- Screening Pending transitions to Rejected when screening fails
- Screening Pending transitions to Posting Pending when screening passes
- Posting Pending transitions to Accepted when account posting succeeds
- Posting Pending transitions to Failed when posting fails
- Accepted transitions to Sent to Scheme when outbound payment is sent
- Sent to Scheme transitions to Settled when settlement confirmation is received
- Rejected, Settled and Failed may transition to final state for this simplified view

## Main flow or structure

Show the main lifecycle left to right. Keep transition labels concise and event-like.

## Alternative and exception flows

Include rejected and failed terminal outcomes. Do not model repair and resubmission in this first figure.

## Scope

Simplified lifecycle of a target-state payment instruction.

## Exclusions

No process tasks, no message sequence and no deployment detail.

## Accessibility requirements

Use readable state names and avoid crossing transition lines where possible.

## Source references

- `[OMG-UML]` for UML state machine notation.
- Horizon Bank examples for payments context.

## Review criteria

- States are conditions, not task names.
- Transitions have meaningful triggers or outcomes.
- The simplified lifecycle does not imply complete payment-scheme status coverage.
