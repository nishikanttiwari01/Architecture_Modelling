# FIG-04-07: Horizon Bank Payments Deployment Diagram

## Purpose

Show a simplified UML deployment diagram for Horizon Bank payment artefacts and neighbouring runtime systems.

## Audience

Platform, operations and security teams.

## Question answered

Where do the main payment artefacts run, and which neighbouring systems do they communicate with?

## Abstraction level

Runtime placement view. It shows deployment nodes, execution environments, artefacts and communication paths.

## Notation

UML deployment diagram.

## Required elements

- Customer device or browser
- Internet edge
- Application runtime node
- Payments API artefact
- Payment Orchestration Service artefact
- Managed data service node
- Payment Status Store artefact
- Financial Crime Platform
- Enterprise Integration Platform
- Event Platform

## Required relationships

- Customer device communicates with Internet edge.
- Internet edge routes to Payments API.
- Payments API and Payment Orchestration Service are deployed on the application runtime node.
- Payment Status Store is deployed on the managed data service node.
- Payment Orchestration Service communicates with Financial Crime Platform.
- Payment Orchestration Service communicates with Enterprise Integration Platform.
- Payment Orchestration Service publishes to Event Platform.

## Relationship semantics

Communication paths mean runtime connectivity between nodes. Deployment relationships mean artefacts are placed on or hosted by a node or execution environment. Node relationships do not describe class, component or process decomposition.

## Main flow or structure

Place internal Horizon Bank runtime nodes together and neighbouring systems outside the payment runtime boundary.

## Alternative and exception flows

Not applicable. This is a runtime placement view.

## Scope

Simplified target production runtime placement.

## Exclusions

No full cloud landing zone, subnet design, firewall rules, high-availability zones or disaster-recovery topology.

## Accessibility requirements

Keep node and artefact labels readable. Use colour only as a secondary cue.

## Source references

- `[OMG-UML]` for UML deployment notation.
- `examples/horizon-bank/system-landscape.md` for stable system names.

## Review criteria

- Distinguishes deployed artefacts from runtime nodes.
- Represents UML nodes as computational resources, usually devices or execution environments.
- Does not duplicate the C4 deployment figure without explaining UML notation.
- Runtime scope and exclusions are clear.
