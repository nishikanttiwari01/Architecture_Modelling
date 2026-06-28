# FIG-05-02: Online store system context

## Purpose

Show how a C4 System Context diagram places one software system among people and external systems.

## Audience

Beginners, business analysts and developers learning C4 context views.

## Question answered

Who uses the Online Store, and which external systems does it depend on?

## Notation

C4 System Context using C4-PlantUML.

## Required elements

- Customer
- Customer Support Agent
- Online Store
- Payment Provider System
- Delivery Partner System

## Required relationships

- Customer uses Online Store to browse, order and track delivery.
- Customer Support Agent uses Online Store to support orders and returns.
- Online Store sends payment requests to Payment Provider System.
- Online Store sends fulfilment requests to Delivery Partner System.

## Main flow or structure

Place Online Store at the centre, people on the left and external systems on the right.

## Alternative and exception flows

None. Exceptions belong in later dynamic or process diagrams.

## Scope

Only the context around the Online Store software system.

## Exclusions

No containers, databases, classes, cloud nodes or business-process steps.

## Accessibility requirements

Label all relationships with verbs. Use distinct stereotypes and text labels, not colour alone.

## Source references

- `[C4-OFFICIAL]`
- `examples/simple-online-store/README.md`

## Review criteria

- The diagram has one clear system of interest.
- External systems are outside the Online Store boundary.
- It does not show internal implementation detail.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 prototype on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
