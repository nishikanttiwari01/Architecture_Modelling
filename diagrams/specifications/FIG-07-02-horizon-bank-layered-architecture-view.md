# FIG-07-02: Horizon Bank Layered Architecture View

## Purpose

Show how Horizon Bank strategy, business, application and technology-domain concepts connect in one small ArchiMate 4 traceability view.

## Audience

Beginners, enterprise architects, solution architects and architecture reviewers.

## Question answered

How does a customer-onboarding capability connect to a Service in the Business domain, a Service in the Application domain, an application component and technology support?

Decision or concern: decide whether the target onboarding architecture has traceable support from business need through application and technology support.

## Required elements

ArchiMate 4 elements:

- Capability: Customer Management
- Capability: Customer Onboarding
- Business actor: Horizon Bank
- Role: Account Provider
- Process in the Business domain: Customer Onboarding Process
- Service in the Business domain: Open Customer Profile Service
- Business object: Customer Record
- Application component: Customer Onboarding Platform
- Application component: Party and Customer Platform
- Application component: Financial Crime Platform
- Function in the Application domain: Customer Profile Management Function
- Service in the Application domain: Customer Profile Management Service
- Technology Node: Application Runtime Node
- Function in the Technology domain: Runtime Hosting Function
- Service in the Technology domain: Runtime Hosting Service

## Required relationships

Relationship types and directions:

- Composition from Customer Management capability to Customer Onboarding capability.
- Assignment from Horizon Bank actor to Account Provider role.
- Assignment from Account Provider role to Customer Onboarding Process.
- Realisation from Customer Onboarding Process to Open Customer Profile Service.
- Serving from Open Customer Profile Service to Retail Customer or the customer-facing concern if included.
- Assignment from Party and Customer Platform to Customer Profile Management Function.
- Realisation from Customer Profile Management Function to Customer Profile Management Service.
- Serving from Customer Profile Management Service to Customer Onboarding Process.
- Access from Customer Profile Management Function to Customer Record.
- Assignment from Application Runtime Node to Runtime Hosting Function.
- Realisation from Runtime Hosting Function to Runtime Hosting Service.
- Serving from Runtime Hosting Service to Party and Customer Platform and Customer Onboarding Platform.
- Assignment or deployment relationship from Application Runtime Node to relevant deployed artifacts only if artifacts are included. Do not imply that the Service in the Technology domain itself is a Node.

## Reusable model concepts

- Customer Onboarding capability must match FIG-07-01 and FIG-07-06.
- Customer Record must match the application cooperation view in FIG-07-03.
- Party and Customer Platform must match the Horizon Bank system landscape and FIG-07-03, FIG-07-04 and FIG-07-06.
- Runtime Hosting Service must match FIG-07-04.

## Notation and legend

Use ArchiMate 4 notation. The diagram may use horizontal bands labelled Strategy domain, Business domain, Application domain and Technology domain for readability, while the caption should note that ArchiMate 4 formally uses the term domain. The legend must identify active structure, behaviour, passive structure, service, composition, assignment, realisation, serving and access.

## Main flow or structure

Split the view into two labelled panels: business-to-application traceability and application-to-technology traceability. Use full relationship labels on arrows. If a concept is repeated across panels, label it as reused and explain that it is the same model concept.

## Alternative and exception flows

Not applicable. Exception behaviour belongs in BPMN or a separate ArchiMate view.

## Scope

Target-state customer onboarding traceability for Horizon Bank.

## Exclusions

No BPMN gateways, detailed API contracts, security controls, deployment topology, database schema, legacy migration sequencing or BIAN Service Domain mapping.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]` for ArchiMate 4 domains, elements and relationship concepts.
- `examples/horizon-bank/system-landscape.md` for stable application component names.

## Accessibility requirements

Use readable labels, clear arrow direction and high contrast. Avoid relying on colour alone to distinguish domains. Keep relationship crossings low.

## Source creation authorisation

The author authorised source creation from the corrected specification on 2026-06-29. The rendered diagram remains in `Review`.

## Review criteria

- Each domain has a clear purpose and does not mix abstraction levels accidentally.
- The application realisation chain is explicit.
- Relationship directions match Chapter 7 prose.
- Application component names match the Horizon Bank example files.
- Full relationship labels are readable at book-page width.
- The figure does not become a mixed BPMN process or C4 deployment diagram.
