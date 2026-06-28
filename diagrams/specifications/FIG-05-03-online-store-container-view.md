# FIG-05-03: Online store container view

## Purpose

Show how a C4 Container diagram decomposes the Online Store into separately runnable or data-storing units.

## Audience

Developers, solution architects and technical leads.

## Question answered

What are the main executable units and data stores inside the Online Store, and how do they interact?

## Notation

C4 Container using C4-PlantUML.

## Required elements

- Customer
- Web Application
- API Application
- Order Database
- Payment Provider System
- Delivery Partner System

## Required relationships

- Customer uses Web Application.
- Web Application calls API Application.
- API Application reads and writes Order Database.
- API Application sends payment requests to Payment Provider System.
- API Application sends fulfilment requests to Delivery Partner System.

## Main flow or structure

Show people outside the system boundary. Show containers inside the Online Store boundary.

## Alternative and exception flows

None.

## Scope

Container-level structure of a simple Online Store.

## Exclusions

No class diagrams, infrastructure nodes, deployment topology or business-process sequence.

## Accessibility requirements

Use readable relationship labels and technology labels where helpful. Do not depend on colour alone.

## Source references

- `[C4-OFFICIAL]`
- `examples/simple-online-store/README.md`

## Review criteria

- Each container is separately runnable or stores data.
- The diagram does not equate C4 container with Docker.
- The abstraction level is consistent.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 prototype on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
