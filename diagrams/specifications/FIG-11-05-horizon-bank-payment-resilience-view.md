# FIG-11-05: Horizon Bank Payment Resilience View

## Purpose

Show how availability, resilience and disaster recovery can be modelled without only drawing duplicate boxes.

## Audience

Platform architects, operations, resilience and risk reviewers.

## Question answered

How does Horizon Bank intend the payment capability to continue or recover during infrastructure disruption?

## Notation

Resilience view, rendered with PlantUML after author acceptance of this specification.

## Required elements

- Primary production region or site.
- Secondary recovery region or site.
- Payments Platform active runtime.
- Event Platform or replicated event store.
- Managed payment database or payment records store.
- Core Deposit System dependency.
- Observability and alerting path.
- Operations team or incident response function.
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) labels.

## Required relationships

- Primary runtime serves normal payment traffic.
- Secondary site or region is available for failover or recovery.
- Payment data replication direction is shown and labelled.
- Event or status replication is shown where relevant.
- Observability feeds operations monitoring.
- Core Deposit System dependency is visible as a constraint or external dependency.

## Main flow or structure

Show normal path and recovery path separately. Include concise labels for active-active, active-standby or warm-standby if the author accepts that scenario.

## Alternative and exception flows

The figure may show degraded operation if Core Deposit System is unavailable, but it should not model all incident runbook steps.

## Scope

Conceptual payment resilience view for Horizon Bank.

## Exclusions

- No detailed backup schedule.
- No full incident-management process.
- No regulatory claim about required RTO or RPO.
- No cost model.

## Accessibility requirements

Use explicit labels for primary, secondary, normal path and recovery path. Use line style plus text rather than colour alone to distinguish replication from live traffic.

## Source references

- [NIST-SP-800-34R1]
- [AWS-WA-RELIABILITY-2026]
- [OPENTELEMETRY-DOCS-2026]

## Review criteria

- RTO and RPO are shown as modelled objectives, not guaranteed facts.
- Observability and operations ownership are visible.
- Dependencies and recovery assumptions are explicit.
- Specification must be accepted by the author before creating the PlantUML source.
