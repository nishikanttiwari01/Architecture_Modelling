# FIG-11-04: Horizon Bank Hybrid Infrastructure and Placement View

## Purpose

Apply infrastructure and deployment modelling to the Horizon Bank case study without making the diagram too detailed for beginners.

## Audience

Solution architects, platform teams, operations and risk reviewers.

## Question answered

Where are the main Horizon Bank payment-related systems placed across cloud, integration and retained core environments?

## Notation

Hybrid infrastructure and placement view, rendered with PlantUML after author acceptance of this specification.

## Required elements

- Horizon Digital Channels.
- Payments Platform.
- Financial Crime Platform.
- Event Platform.
- Enterprise Integration Platform.
- Core Deposit System.
- Enterprise Data Platform.
- Cloud platform boundary.
- Retained data-centre or core-banking boundary.
- Controlled integration boundary between cloud and retained systems.

## Required relationships

- Digital Channels call the Payments Platform.
- Payments Platform calls Financial Crime Platform for screening.
- Payments Platform integrates with Core Deposit System through the Enterprise Integration Platform.
- Payments Platform publishes events to Event Platform.
- Event Platform supplies selected events to Enterprise Data Platform.
- Boundary labels state cloud, retained core and integration control points.

## Main flow or structure

Use a left-to-right or top-to-bottom view that separates customer channels, cloud-hosted platforms, event/data platforms and retained core systems. Keep relationship labels short and focused on infrastructure placement and integration control.

## Alternative and exception flows

None. Payment exception process detail belongs in BPMN and event-flow diagrams from other chapters.

## Scope

High-level Horizon Bank hybrid infrastructure and placement view for outgoing payment handling.

## Exclusions

- No BIAN Service Domain mapping.
- No detailed business process.
- No physical rack, subnet or firewall inventory.
- No security threat model.

## Accessibility requirements

Use boundary labels and relationship labels so the view remains understandable in black and white. Avoid using colour as the only indicator of cloud versus retained core.

## Source references

- [NIST-SP-800-145]
- [AWS-WA-RELIABILITY-2026]
- [C4-OFFICIAL]

## Review criteria

- Horizon Bank system names match the example register.
- The view does not imply that retained core systems are cloud-native.
- Infrastructure placement is not confused with process sequence.
- Specification must be accepted by the author before creating the PlantUML source.
