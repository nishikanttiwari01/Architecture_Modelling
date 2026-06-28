# FIG-05-04: Horizon Bank payments platform view

## Purpose

Apply a C4 container view to Horizon Bank's target payments platform.

## Audience

Solution architects, enterprise architects, payments technology teams and banking stakeholders who need a software-structure view.

## Question answered

Which main containers support payment initiation and orchestration, and which neighbouring systems do they use?

## Notation

C4 Container using C4-PlantUML.

## Required elements

- Retail Customer
- Horizon Digital Channels
- Payments API
- Payment Orchestration Service
- Payment Status Store
- Core Deposit System
- Financial Crime Platform
- Enterprise Integration Platform
- Event Platform

## Required relationships

- Retail Customer uses Horizon Digital Channels.
- Horizon Digital Channels call Payments API.
- Payments API submits payment requests to Payment Orchestration Service.
- Payment Orchestration Service checks account posting with Core Deposit System through Enterprise Integration Platform.
- Payment Orchestration Service requests screening from Financial Crime Platform.
- Payment Orchestration Service writes status to Payment Status Store.
- Payment Orchestration Service publishes payment events to Event Platform.

## Main flow or structure

Show the payments platform boundary and its main containers. Keep neighbouring systems outside the boundary.

## Alternative and exception flows

Screening failure and posting failure are mentioned in chapter prose, not shown as separate paths in this static view.

## Scope

Target payments platform structure for Horizon Bank.

## Exclusions

No full BPMN process, no BIAN Service Domain mapping, no physical cloud deployment and no detailed API schema.

## Accessibility requirements

Label all arrows and keep line crossings low. Use clear text to distinguish internal containers from external systems.

## Source references

- `[C4-OFFICIAL]`
- `examples/horizon-bank/system-landscape.md`
- `examples/horizon-bank/actors.md`

## Review criteria

- The view remains software-structural, not a business-process model.
- External systems are not shown as internal containers.
- The diagram does not imply that C4 containers are Docker containers.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 prototype on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
