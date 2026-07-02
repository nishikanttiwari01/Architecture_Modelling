# FIG-13-01: Online Store SysML-style Requirement Traceability View

## Purpose

Show a small SysML-style teaching view that connects selected Online Store requirements to design responses, verification cases and verification evidence.

## Audience

Beginners, analysts, architects and testers.

## Question answered

Which requirements are addressed by which design responses, and what verification cases and evidence support review?

## Notation

SysML-style requirement trace teaching view. Use simple labelled boxes and relationships rather than full SysML 2.0 notation depth.

## Required elements

- Requirement `REQ-OS-01`: checkout shall not store full customer card details in the Online Store.
- Requirement `REQ-OS-02`: customer shall receive an order confirmation after the order is accepted.
- Requirement `REQ-OS-03`: support users shall view order status without seeing full payment details.
- Design element: Payment Provider System delegation.
- Design element: order record and confirmation behaviour.
- Design element: masked support view.
- Verification case: checkout card-data storage boundary.
- Verification case: accepted-order confirmation.
- Verification case: support-role masked payment information.
- Verification evidence: security test result and provider integration review.
- Verification evidence: functional test result and message-log sample.
- Verification evidence: access-control test result and support-role review.

## Required relationships

- Each requirement must connect to at least one design response with `addressed by`.
- Each requirement must connect directly to at least one verification case with `verified by`.
- Each verification case must connect to verification evidence with `evidenced by`.
- No relationship label should imply proof beyond the evidence shown.

## Main flow or structure

Arrange requirements on the left, design responses in the centre, verification cases to the right of design responses and evidence on the far right. Keep the direction left to right: Requirement | Design response | Verification case | Evidence. A requirement may have two outgoing relationships, `addressed by` and `verified by`.

## Alternative and exception flows

None. This is a traceability view, not a behavioural sequence.

## Scope

Only the Simple Online Store checkout and support examples used in Chapter 13.

## Exclusions

- Full SysML 2.0 metamodel detail.
- Complete checkout process.
- Full payment-provider protocol.
- Security control catalogue.

## Accessibility requirements

Do not rely on colour alone. Use clear labels, relationship text and sufficient spacing.

## Source references

- `[OMG-SYSML-2.0]`

## Review criteria

- The view is understandable without prior SysML expertise.
- Requirements, design responses, verification cases and verification evidence are visually distinct.
- No relationship implies proof beyond the named verification evidence.
- Terminology matches the Simple Online Store example.
