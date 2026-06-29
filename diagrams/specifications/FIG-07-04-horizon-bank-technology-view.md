# FIG-07-04: Horizon Bank Technology View

## Purpose

Show a small technology support view for Horizon Bank customer onboarding applications.

## Audience

Enterprise architects, platform architects, operations teams and beginner readers learning the technology layer.

## Question answered

Which technology services or nodes support the selected onboarding application components?

## Abstraction level

Technology architecture overview. It is not a detailed physical deployment diagram.

## Notation

ArchiMate technology view.

## Required elements

- Application components: Customer Onboarding Platform, Party and Customer Platform, Enterprise Integration Platform, Event Platform
- Technology services or nodes: Cloud Application Platform, Managed Relational Database Service, Enterprise Messaging Service, API Gateway Service
- Technology artifact or data representation where useful: Customer Data Store

## Required relationships

- Cloud Application Platform serves Customer Onboarding Platform and Party and Customer Platform.
- Managed Relational Database Service serves Party and Customer Platform or stores Customer Data Store.
- Enterprise Messaging Service serves Event Platform.
- API Gateway Service serves Enterprise Integration Platform.

## Main flow or structure

Keep application elements in a small upper band and technology support elements below. Show support relationships from technology services to application components.

## Alternative and exception flows

Not applicable. Operational failover and disaster recovery are out of scope for this introductory view.

## Scope

Target technology support for selected Horizon Bank onboarding application components.

## Exclusions

No detailed network zones, Kubernetes objects, firewall rules, cloud account structure, deployment scripts or operational runbooks.

## Accessibility requirements

Use high contrast, readable labels and clear relationship direction. Do not rely on colour alone for layer meaning.

## Source references

- `[OPEN-GROUP-ARCHIMATE-3.2]` for technology layer concepts.
- `examples/horizon-bank/system-landscape.md` for stable application names.

## Review criteria

- The view stays at technology-service level.
- It does not duplicate a UML or C4 deployment diagram.
- Relationship labels clarify support where direction may be ambiguous.
- The figure remains readable at book-page width.
