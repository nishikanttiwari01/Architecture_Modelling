# FIG-09-03: Horizon Bank Payment Routing DRD

## Purpose

Show a DMN-style decision requirements view for routing a Horizon Bank payment instruction.

## Audience

Business analysts, solution architects, payment architects, risk reviewers and operations reviewers.

## Question answered

Which input data, business knowledge and policy authorities support the Determine Payment Route decision?

## Notation

DMN-style DRD teaching view rendered with PlantUML. It is not semantic `.dmn` XML.

## Required elements

- Decision: Determine Payment Route.
- Input Data: Payment Instruction, Account Status, Screening Result, Payment Cut-Off Status.
- Business Knowledge Model: Payment Routing Rules.
- Knowledge Sources: Payments Operations Policy, Financial Crime Screening Policy.
- Output note: Payment route result values.
- Relationship labels for information, knowledge and authority requirements.

## Required relationships

- Each input data element points directly to the decision as an information requirement.
- Business knowledge model points to the decision as a knowledge requirement.
- Knowledge sources point to the governed knowledge model or decision as authority requirements.

## Main flow or structure

Inputs and reusable rules feed the payment routing decision directly. Policies govern the reusable rules and screening-related decision authority.

## Alternative and exception flows

The decision may return Proceed, Repair, Manual Review or Reject. Detailed process handling of those outcomes is outside this figure.

## Scope

Horizon Bank payment routing requirements-level decision view.

## Exclusions

BPMN payment repair workflow, API binding, payment scheme rules, fraud case management, data lineage and deployment.

## Accessibility requirements

Use stereotypes or labels so meaning is not carried by colour alone. Relationship labels must be readable.

## Source references

- `[OMG-DMN-1.5]`

## Review criteria

- Relationship direction points into the decision or governed element.
- The diagram does not introduce a connector element for information requirements.
- DRD is not shown as process sequence.
- Decision, Input Data, Business Knowledge Model and Knowledge Source are distinguished.
- The diagram status remains `Review`.

## Authorisation

The author authorised source creation through the Chapter 9 completion request on 2026-06-30.
