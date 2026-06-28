# FIG-05-06: Online Store API Component Diagram

## Purpose

Show how a C4 Component diagram decomposes one container, the Online Store API Application, without treating components as separately deployable services.

## Audience

Software architects, developers and reviewers working on the Online Store API Application.

## Question answered

What are the major internal components inside the API Application, and which interfaces do they use?

## Notation

C4 Component using C4-PlantUML.

## Required elements

- Web Application
- API Application boundary
- Order API
- Basket Service
- Order Repository
- Payment Adapter
- Fulfilment Adapter
- Notification Publisher
- Order Database
- Payment Provider System
- Delivery Partner System

## Required relationships

- Web Application calls Order API.
- Order API delegates basket checks to Basket Service.
- Order API persists orders through Order Repository.
- Order Repository reads and writes Order Database.
- Order API requests payment through Payment Adapter.
- Payment Adapter calls Payment Provider System.
- Order API requests fulfilment through Fulfilment Adapter.
- Fulfilment Adapter calls Delivery Partner System.
- Order API publishes order events through Notification Publisher.

## Main flow or structure

Show the API Application as one container boundary with related components inside it. Keep the diagram structural, not a runtime sequence.

## Alternative and exception flows

Do not show exception flows. Payment decline and delivery failure can be explained in prose or separate dynamic views.

## Scope

The internal structure of the Online Store API Application container.

## Exclusions

No Docker containers, Kubernetes nodes, classes, database tables or user interface internals.

## Accessibility requirements

Use concise labels, readable component descriptions and relationship labels. Avoid relying on colour alone.

## Source references

- `[C4-OFFICIAL]`
- `examples/simple-online-store/system-context.md`
- `examples/simple-online-store/containers.md`

## Review criteria

- Components are inside one container.
- The diagram does not imply that each component is deployed separately.
- External dependencies remain outside the API Application boundary.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 correction on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
