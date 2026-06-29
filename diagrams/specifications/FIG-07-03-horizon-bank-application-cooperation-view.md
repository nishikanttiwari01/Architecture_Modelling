# FIG-07-03: Horizon Bank Application Cooperation View

## Purpose

Show how selected Horizon Bank application components cooperate through application behaviour, services and data to support customer onboarding.

## Audience

Solution architects, application owners, integration architects and beginner readers learning application-domain ArchiMate.

## Question answered

Which application components perform behaviour, realise services and consume or update customer data during simplified customer onboarding?

Decision or concern: decide how selected application components cooperate through explicit behaviour and services.

## Required elements

ArchiMate 4 elements:

- Application component: Horizon Digital Channels
- Application component: Customer Onboarding Platform
- Application component: Party and Customer Platform
- Application component: Financial Crime Platform
- Application component: Enterprise Integration Platform
- Application function: Application Capture Function
- Application function: Onboarding Orchestration Function
- Application function: Customer Profile Management Function
- Application function: Screening Request Function
- Application function: Integration Routing Function
- Application service: Application Capture Service
- Application service: Onboarding Orchestration Service
- Application service: Customer Profile Management Service
- Application service: Screening Request Service
- Application service: Integration Routing Service
- Data object: Customer Record

## Required relationships

Relationship types and directions:

- Assignment from each application component to its named function.
- Realisation from each function to its corresponding application service.
- Serving from Application Capture Service to Onboarding Orchestration Function or Customer Onboarding Process, depending on whether the business process is included.
- Serving from Customer Profile Management Service to Onboarding Orchestration Function.
- Serving from Screening Request Service to Onboarding Orchestration Function.
- Serving from Integration Routing Service to Onboarding Orchestration Function where integration indirection is shown.
- Access from Customer Profile Management Function to Customer Record.
- Flow from Onboarding Orchestration Function to Screening Request Function only if the diagram needs to show screening request transfer.

## Reusable model concepts

- Customer Profile Management Function and Customer Profile Management Service must match FIG-07-02.
- Party and Customer Platform, Customer Onboarding Platform, Financial Crime Platform and Enterprise Integration Platform must match `examples/horizon-bank/system-landscape.md`.
- Customer Record must match FIG-07-02 and later Chapter 8 data modelling.

## Notation and legend

Use ArchiMate 4 application-domain notation. The legend must distinguish Application Component, Function, Application Service, Data Object, assignment, realisation, serving, access and optional flow. Use colour only as a secondary aid.

## Main flow or structure

Group each application component with its assigned function and realised service. Place consuming functions near the services they use so serving relationships are easy to follow.

## Alternative and exception flows

Do not show detailed exception handling. Screening exceptions are described in Chapter 6 BPMN and can be referenced in prose.

## Scope

Target application cooperation for a simplified customer onboarding scenario.

## Exclusions

No business-process sequence, BPMN exception handling, C4 container internals, API resource design, event schemas, database schema, deployment nodes or project migration tasks.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]` for application-domain concepts, generic behaviour elements and relationships.
- `examples/horizon-bank/system-landscape.md` for stable system names.

## Accessibility requirements

Use readable labels and avoid dense crossing lines. Label non-obvious serving and flow relationships. Keep the component to function to service chain visually traceable.

## Review criteria

- The view remains at application architecture level.
- Application services are not confused with physical microservices.
- Every application service is realised by behaviour assigned to an application component.
- Data object use is limited to what supports the architecture concern.
- The view complements, rather than duplicates, C4 container diagrams.
