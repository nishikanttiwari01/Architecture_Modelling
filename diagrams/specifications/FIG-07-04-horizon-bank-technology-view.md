# FIG-07-04: Horizon Bank Technology View

## Purpose

Show a small ArchiMate 4 technology-domain support view for Horizon Bank onboarding applications.

## Audience

Enterprise architects, platform architects, operations teams and beginner readers learning the technology domain.

## Question answered

Which technology nodes, system software, Services in the Technology domain and artifacts support the selected onboarding application components?

Decision or concern: decide which technology support concepts are needed without turning the view into a detailed deployment diagram.

## Required elements

ArchiMate 4 elements:

- Application component: Customer Onboarding Platform
- Application component: Party and Customer Platform
- Application component: Enterprise Integration Platform
- Application component: Event Platform
- Technology Node: Application Runtime Node
- Technology Node: Integration Runtime Node
- Technology Node: Data Platform Node, only if the concern is hosting or runtime placement
- System software: Container Platform
- System software: Database Management System
- Function in the Technology domain: Runtime Hosting Function
- Function in the Technology domain: Database Management Function
- Function in the Technology domain: Messaging Function
- Function in the Technology domain: API Gateway Function
- Service in the Technology domain: Runtime Hosting Service
- Service in the Technology domain: Database Service
- Service in the Technology domain: Enterprise Messaging Service
- Service in the Technology domain: API Gateway Service
- Artifact: Customer Onboarding Service Package
- Artifact: Customer Profile Service Package

## Required relationships

Relationship types and directions:

- Assignment from Application Runtime Node to Runtime Hosting Function.
- Realisation from Runtime Hosting Function to Runtime Hosting Service.
- Serving from Runtime Hosting Service to Customer Onboarding Platform and Party and Customer Platform.
- Assignment from Data Platform Node to Database Management Function, if Data Platform Node is included.
- Realisation from Database Management Function to Database Service.
- Serving from Database Service to Party and Customer Platform.
- Assignment from Application Runtime Node or another explicit technology support node to Messaging Function, depending on layout.
- Realisation from Messaging Function to Enterprise Messaging Service.
- Serving from Enterprise Messaging Service to Event Platform.
- Assignment from Integration Runtime Node to API Gateway Function.
- Realisation from API Gateway Function to API Gateway Service.
- Serving from API Gateway Service to Enterprise Integration Platform.
- Composition or aggregation from Application Runtime Node to Container Platform if the runtime node includes system software.
- Assignment or deployment-style relationship from artifacts to Application Runtime Node only if the diagram explicitly shows deployable packages.
- Do not model Managed Relational Database Service as a Technology Node unless the view is specifically about runtime hosting structure.

## Reusable model concepts

- Runtime Hosting Service must match FIG-07-02.
- Party and Customer Platform and Customer Onboarding Platform must match FIG-07-02, FIG-07-03 and FIG-07-06.
- Customer Profile Service Package should trace to Customer Profile Management Service in FIG-07-03.

## Notation and legend

Use ArchiMate 4 technology-domain notation. The legend must distinguish Technology Node, System Software, Function in the Technology domain, Service in the Technology domain, Artifact, assignment, realisation, serving and composition or aggregation. It must state that managed services are modelled according to the concern, not automatically as nodes.

## Main flow or structure

Place application components in a small upper band and technology support elements below. Show the explicit technology chain: Technology Node assigned to Function in the Technology domain, Function realises Service in the Technology domain, and Service serves application components.

## Alternative and exception flows

Not applicable. Operational failover and disaster recovery are out of scope for this introductory view.

## Scope

Target technology support for selected Horizon Bank onboarding application components.

## Exclusions

No detailed network zones, Kubernetes objects, firewall rules, cloud account structure, deployment scripts, operational runbooks or disaster-recovery design.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]` for technology-domain concepts, artifacts and serving or assignment relationships.
- `examples/horizon-bank/system-landscape.md` for stable application names.

## Accessibility requirements

Use high contrast, readable labels and clear relationship direction. Do not rely on colour alone for domain meaning. Keep the diagram readable at book-page width.

## Source creation authorisation

The author authorised source creation from the corrected specification on 2026-06-29. The rendered diagram remains in `Review`.

## Review criteria

- Technology Node, System Software, Service in the Technology domain and Artifact are distinct.
- A managed database capability is not automatically treated as a node.
- The view does not duplicate a UML or C4 deployment diagram.
- Relationship labels clarify support or hosting where direction may be ambiguous.
- The figure remains readable at book-page width.
