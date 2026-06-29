# FIG-04-03: Online Store order handling component diagram

## Purpose

Show how a UML component diagram can describe modular software responsibilities and interfaces for online store order handling.

## Audience

Architects and developers.

## Question answered

Which software components collaborate to handle orders, payments, fulfilment and notifications?

## Notation

UML component diagram.

## Required elements

- Web Application
- Order API
- Order Service
- Payment Adapter
- Fulfilment Adapter
- Notification Publisher
- Order Database
- Payment Provider System
- Delivery Partner System

## Required relationships

- Web Application calls Order API
- Order API delegates to Order Service
- Order Service reads and writes Order Database
- Order Service uses Payment Adapter for payment authorisation
- Payment Adapter calls Payment Provider System
- Order Service uses Fulfilment Adapter for delivery requests
- Fulfilment Adapter calls Delivery Partner System
- Order Service uses Notification Publisher for order events or customer notifications

## Main flow or structure

Place Online Store components together and external systems outside the boundary. Label interfaces or dependencies with concise verbs.

## Alternative and exception flows

Do not show detailed failure paths. Mention that failure handling belongs in sequence, activity or state views if needed.

## Scope

Logical component responsibilities for order handling.

## Exclusions

No deployment nodes, Kubernetes detail, source-code classes or enterprise landscape.

## Accessibility requirements

Use clear component names and relationship labels. Do not rely on colour alone.

## Source references

- `[OMG-UML]` for UML component notation.
- `examples/simple-online-store/README.md` for stable systems and processes.

## Review criteria

- Components are not presented as mandatory microservices.
- External systems are visually distinct.
- Interface responsibilities are understandable to a beginner.
