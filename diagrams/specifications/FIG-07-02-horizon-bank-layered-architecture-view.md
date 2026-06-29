# FIG-07-02: Horizon Bank Layered Architecture View

## Purpose

Show how Horizon Bank business, application and technology elements connect in one small layered ArchiMate view.

## Audience

Beginners, enterprise architects, solution architects and architecture reviewers.

## Question answered

How does a banking business capability connect to business service, application service, application component and technology support?

## Abstraction level

Enterprise architecture overview. It shows traceability across layers, not detailed process, API or deployment design.

## Notation

ArchiMate layered view using business, application and technology elements.

## Required elements

- Business capability: Customer Onboarding
- Business service: Open Customer Profile
- Business process: Customer Onboarding
- Application service: Customer Profile Management
- Application components: Customer Onboarding Platform, Party and Customer Platform, Financial Crime Platform
- Technology service or node: Cloud Application Platform
- Data object or business object: Customer Record

## Required relationships

- Customer Onboarding capability is realised or supported by Customer Onboarding process.
- Customer Onboarding process realises Open Customer Profile business service.
- Customer Onboarding process uses Customer Profile Management application service.
- Party and Customer Platform realises Customer Profile Management application service.
- Customer Onboarding Platform collaborates with Financial Crime Platform for screening.
- Application components are served by Cloud Application Platform.
- Customer Profile Management accesses Customer Record.

## Main flow or structure

Arrange the view in horizontal bands: business at the top, application in the middle and technology at the bottom. Keep relationship crossings low.

## Alternative and exception flows

Not applicable. Exception behaviour belongs in BPMN or a separate ArchiMate view.

## Scope

Target-state customer onboarding traceability for Horizon Bank.

## Exclusions

No BPMN gateways, detailed API contracts, security controls, deployment topology, database schema or legacy migration sequencing.

## Accessibility requirements

Use readable labels, clear arrow direction and high contrast. Avoid relying on colour alone to distinguish layers.

## Source references

- `[OPEN-GROUP-ARCHIMATE-3.2]` for ArchiMate layer and relationship concepts.
- `examples/horizon-bank/system-landscape.md` for stable application component names.

## Review criteria

- Each layer has a clear purpose.
- Relationship directions match the prose in Chapter 7.
- Application component names match the Horizon Bank example files.
- The figure does not become a mixed process or deployment diagram.
