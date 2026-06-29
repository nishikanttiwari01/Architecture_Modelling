# FIG-04-05: Horizon Bank Payment Validation Activity Diagram

## Purpose

Show a UML activity diagram for payment validation and screening inside the Payments Platform.

## Audience

Architects, analysts and developers.

## Question answered

What flow of actions and decisions occurs before a payment instruction is accepted or rejected?

## Abstraction level

System behaviour view. It shows validation flow inside a software platform, not a full banking process.

## Notation

UML activity diagram.

## Required elements

- Initial node
- Receive payment instruction
- Validate mandatory fields
- Check payment limits
- Request financial-crime screening
- Decision: checks passed?
- Reject payment instruction
- Accept payment for posting
- Record status
- Final node
- Swimlanes for Payments Platform and Financial Crime Platform

## Required relationships

- Initial node flows to Receive payment instruction.
- Mandatory-field validation precedes limit checking.
- Limit checking precedes screening request.
- Failed validation or screening flows to Reject payment instruction.
- Passed validation and screening flows to Accept payment for posting.
- Both accepted and rejected outcomes record status before the final node.

## Relationship semantics

Control flows show possible order of actions. Guard labels on decision edges define path conditions. Swimlanes show responsibility, not deployment ownership.

## Main flow or structure

Use a simple top-to-bottom activity flow with one decision diamond and clear guard labels.

## Alternative and exception flows

Keep exception handling minimal. Do not show operational repair, sanctions investigation or reconciliation.

## Scope

System-level validation flow inside the Payments Platform.

## Exclusions

No BPMN pools, lanes, timers, message events, human operational workflow or deployment detail.

## Accessibility requirements

Decision labels must be readable. Avoid crowded branching.

## Source references

- `[OMG-UML]` for UML activity notation.
- `examples/horizon-bank/system-landscape.md` for Payments Platform and Financial Crime Platform naming.

## Review criteria

- The diagram is not presented as a full banking process.
- Branch outcomes are labelled with guards.
- Activity names are verbs or verb phrases.
- Swimlanes do not imply physical deployment.
