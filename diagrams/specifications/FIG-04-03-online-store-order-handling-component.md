# FIG-04-03: Online Store Order Handling Component Diagram

## Purpose

Show how a UML component diagram can describe modular software responsibilities and interfaces for online store order handling.

## Audience

Architects and developers.

## Question answered

Which software components collaborate to handle orders, payments, fulfilment and notifications?

## Abstraction level

Logical software structure. It shows components and interfaces, not deployment artefacts or runtime nodes.

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
- Interfaces: Order Submission, Payment Authorisation, Fulfilment Request

## Required relationships

- Web Application requires Order Submission.
- Order API provides Order Submission and delegates to Order Service.
- Order Service reads and writes Order Database.
- Order Service requires Payment Authorisation from Payment Adapter.
- Payment Adapter depends on Payment Provider System.
- Order Service requires Fulfilment Request from Fulfilment Adapter.
- Fulfilment Adapter depends on Delivery Partner System.
- Order Service uses Notification Publisher.

## Relationship semantics

Provided interfaces are contracts a component offers. Required interfaces are contracts a component needs. Dependencies show usage, not deployment. Component boundaries do not imply separate microservices.

## Main flow or structure

Place Online Store components together and external systems outside the boundary. Label interfaces or dependencies with concise verbs.

## Alternative and exception flows

Do not show detailed failure paths. Failure handling belongs in sequence, activity or state views if needed.

## Scope

Logical component responsibilities for order handling.

## Exclusions

No deployment nodes, Kubernetes detail, source-code classes, artefact packaging or enterprise landscape.

## Accessibility requirements

Use clear component names and relationship labels. Do not rely on colour alone.

## Source references

- `[OMG-UML]` for UML component notation.
- `examples/simple-online-store/README.md` for stable systems and processes.

## Review criteria

- Components are not presented as mandatory microservices or deployable artefacts.
- Provided and required interfaces are visible or clearly labelled.
- External systems are visually distinct.
- Interface responsibilities are understandable to a beginner.
