# FIG-07-03: Horizon Bank Application Cooperation View

## Purpose

Show how selected Horizon Bank application components cooperate to support customer onboarding.

## Audience

Solution architects, application owners, integration architects and beginner readers learning application-layer ArchiMate.

## Question answered

Which application components expose or consume services during simplified customer onboarding?

## Abstraction level

Application architecture overview. It shows application services and cooperation, not component internals or API payloads.

## Notation

ArchiMate application cooperation view.

## Required elements

- Application components: Horizon Digital Channels, Customer Onboarding Platform, Party and Customer Platform, Financial Crime Platform, Enterprise Integration Platform
- Application services: Application Capture, Onboarding Orchestration, Customer Profile Management, Screening Request, Integration Routing
- Application data object: Customer Record

## Required relationships

- Horizon Digital Channels uses Application Capture or serves the customer-facing interaction.
- Customer Onboarding Platform realises Onboarding Orchestration.
- Customer Onboarding Platform uses Customer Profile Management and Screening Request.
- Party and Customer Platform realises Customer Profile Management and accesses Customer Record.
- Financial Crime Platform realises Screening Request or provides screening service.
- Enterprise Integration Platform provides Integration Routing where integration indirection is shown.

## Main flow or structure

Group application components with their services. Keep services near the component that realises them and show use or serving relationships between services.

## Alternative and exception flows

Do not show detailed exception handling. Screening exceptions are described in Chapter 6 BPMN and can be referenced in prose.

## Scope

Target application cooperation for a simplified customer onboarding scenario.

## Exclusions

No business-process sequence, C4 container internals, API resource design, event schemas, database schema or deployment nodes.

## Accessibility requirements

Use readable labels and avoid dense crossing lines. Label non-obvious relationships.

## Source references

- `[OPEN-GROUP-ARCHIMATE-3.2]` for application component, application service and access relationships.
- `examples/horizon-bank/system-landscape.md` for stable system names.

## Review criteria

- The view remains at application architecture level.
- Services are not confused with physical microservices.
- Data object use is limited to what supports the architecture question.
- The view complements, rather than duplicates, C4 container diagrams.
