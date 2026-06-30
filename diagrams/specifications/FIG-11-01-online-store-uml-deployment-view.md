# FIG-11-01: Online Store UML Deployment View

## Purpose

Teach the difference between software elements and the runtime nodes or execution environments that host them.

## Audience

Beginners, solution architects, developers and operations teams.

## Question answered

Where do the main Online Store runtime elements run, and which external systems do they connect to?

## Notation

UML deployment diagram, rendered with PlantUML after author acceptance of this specification.

## Required elements

- Customer browser or mobile client.
- Edge or load-balancing node.
- Application runtime node for the Online Store web application and API.
- Background worker runtime.
- Database node or managed database service.
- Payment Provider System.
- Delivery Partner System.

## Required relationships

- Customer client connects to the edge endpoint.
- Edge routes traffic to the Online Store web/API runtime.
- Web/API runtime reads and writes order data in the database.
- Web/API runtime calls Payment Provider System for payment authorisation.
- Worker or API sends fulfilment requests to Delivery Partner System.

## Main flow or structure

Show a small production deployment from left to right: client, edge, application runtime, data/runtime dependencies and external provider systems. Use deployment-focused labels such as protocol, runtime responsibility and environment where useful.

## Alternative and exception flows

None in the main diagram. Failure and recovery are handled in FIG-11-05.

## Scope

Simple Online Store production deployment at beginner level.

## Exclusions

- No detailed cloud provider icons.
- No database schema.
- No Kubernetes object detail.
- No security threat model.

## Accessibility requirements

Use text labels, not colour alone, to distinguish runtime zones and external systems. Keep relationship labels short and readable at book-page width.

## Source references

- [OMG-UML]
- [C4-OFFICIAL]

## Review criteria

- Diagram answers a deployment-placement question, not a process-flow question.
- Runtime nodes are distinct from software responsibilities.
- External systems are outside the Online Store boundary.
- Relationship direction is clear.
- Specification must be accepted by the author before creating the PlantUML source.
