# FIG-04-06: Payment Instruction Lifecycle State Machine

## Purpose

Show a UML state machine diagram for the lifecycle of a Horizon Bank payment instruction.

## Audience

Architects, developers, testers and operations.

## Question answered

What meaningful states can a payment instruction be in, and what events move it between states?

## Abstraction level

Lifecycle behaviour view for one business object or system entity.

## Notation

UML state machine diagram.

## Required elements

- Initial pseudostate
- Received
- Validated
- Screening Pending
- Rejected
- Posting Pending
- Accepted
- Sent to Scheme
- Settled
- Failed
- Final pseudostate

## Required relationships

- Initial pseudostate transitions to Received without an external event label.
- Received transitions to Validated after mandatory checks pass.
- Validated transitions to Screening Pending when screening is requested.
- Screening Pending transitions to Rejected when screening fails.
- Screening Pending transitions to Posting Pending when screening passes.
- Posting Pending transitions to Accepted when account posting succeeds.
- Posting Pending transitions to Failed when posting fails.
- Accepted transitions to Sent to Scheme when outbound payment is sent.
- Sent to Scheme transitions to Settled when settlement confirmation is received.
- Rejected, Settled and Failed may transition to the final pseudostate for this simplified view.

## Relationship semantics

Transitions are valid lifecycle moves. The initial pseudostate transition is unlabelled because it represents entry into the simplified lifecycle, not an external event. Other labels use `event [guard] / effect` where useful. States are conditions that can persist, not process tasks.

## Main flow or structure

Show the main lifecycle left to right. Keep transition labels concise and event-like.

## Alternative and exception flows

Include rejected and failed terminal outcomes. Do not model repair and resubmission in this first figure.

## Scope

Simplified lifecycle of a target-state payment instruction.

## Exclusions

No process tasks, no message sequence, no deployment detail and no complete payment-scheme status model.

## Accessibility requirements

Use readable state names and avoid crossing transition lines where possible.

## Source references

- `[OMG-UML]` for UML state machine notation.
- Horizon Bank examples for payments context.

## Review criteria

- States are conditions, not task names.
- Initial transition has no external event label.
- Transitions have meaningful triggers, guards or effects.
- The simplified lifecycle does not imply complete payment-scheme status coverage.
