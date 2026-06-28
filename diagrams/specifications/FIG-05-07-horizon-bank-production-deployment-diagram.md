# FIG-05-07: Horizon Bank Production Deployment Diagram

## Purpose

Show where the main Horizon Bank payments containers run in a simplified production environment.

## Audience

Solution architects, platform engineers, operations teams and security reviewers.

## Question answered

Where do the Payments API, Payment Orchestration Service and Payment Status Store run in production, and which neighbouring systems do they connect to?

## Notation

C4 Deployment using C4-PlantUML.

## Required elements

- Retail Customer
- Horizon Digital Channels
- Internet edge
- Horizon Bank production environment
- Application runtime node
- Managed data node
- Payments API
- Payment Orchestration Service
- Payment Status Store
- Financial Crime Platform
- Enterprise Integration Platform
- Core Deposit System
- Event Platform

## Required relationships

- Retail Customer uses Horizon Digital Channels.
- Horizon Digital Channels call Payments API through the production edge.
- Payments API calls Payment Orchestration Service.
- Payment Orchestration Service writes Payment Status Store.
- Payment Orchestration Service requests screening from Financial Crime Platform.
- Payment Orchestration Service requests account posting through Enterprise Integration Platform.
- Enterprise Integration Platform calls Core Deposit System.
- Payment Orchestration Service publishes payment events to Event Platform.

## Main flow or structure

Show a logical production deployment view. Use deployment nodes for the edge, application runtime and managed data store.

## Alternative and exception flows

No exception paths. Operational concerns such as failover and monitoring are mentioned in chapter prose only.

## Scope

The logical production placement of the payments platform containers and their main external connections.

## Exclusions

No cloud vendor product names, subnet details, firewall rules, pod replicas, certificates, monitoring tools or disaster recovery topology.

## Accessibility requirements

Keep the layout readable at book-page width. Use relationship labels and avoid excessive line crossings.

## Source references

- `[C4-OFFICIAL]`
- `examples/horizon-bank/system-landscape.md`
- `examples/horizon-bank/actors.md`

## Review criteria

- Logical containers and deployment nodes are distinct.
- The diagram remains a deployment view, not a container view with infrastructure words added.
- External systems are outside the production payments platform boundary.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 correction on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
