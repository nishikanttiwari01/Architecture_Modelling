# FIG-13-01: Online Store SysML Requirement Trace

## Purpose

Show a small SysML-style teaching view that connects selected Online Store requirements to design responses and verification evidence.

## Audience

Beginners, analysts, architects and testers.

## Question answered

Which requirements are addressed by which design elements, and what evidence verifies them?

## Notation

SysML-style requirement trace teaching view. Use simple labelled boxes and relationships rather than full SysML 2.0 notation depth.

## Required elements

- Requirement: protect customer payment details.
- Requirement: provide order confirmation.
- Requirement: support can view order status without full payment details.
- Design element: Payment Provider System delegation.
- Design element: order record and confirmation behaviour.
- Design element: masked support view.
- Verification evidence: security test, functional test, access-control test.

## Required relationships

- Each requirement must connect to at least one design response.
- Each design response must connect to at least one verification evidence item.
- Relationship labels should use simple verbs such as `satisfied by` and `verified by`.

## Main flow or structure

Arrange requirements on the left, design responses in the centre and verification evidence on the right. Keep the direction left to right.

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
- Requirements, design responses and verification evidence are visually distinct.
- No relationship implies proof beyond the named verification evidence.
- Terminology matches the Simple Online Store example.
