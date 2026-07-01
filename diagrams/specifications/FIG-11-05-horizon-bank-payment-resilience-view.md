# FIG-11-05: Horizon Bank Payment Resilience View

## Purpose

Show one explicit warm-standby payment recovery scenario without implying that duplicated boxes alone prove resilience.

## Audience

Platform architects, operations, resilience and risk reviewers.

## Question answered

How does Horizon Bank intend the payment capability to fail over to a warm-standby region, recover data safely and fail back after validation?

## Notation

Resilience view, rendered with PlantUML after author acceptance of this specification.

## Required elements

- Primary production region or site.
- Secondary recovery region or site.
- Payments Platform active runtime.
- Payments Platform warm-standby runtime.
- Event Platform or replicated event store.
- Managed payment database or payment records store.
- Core Deposit System dependency.
- Operations team or incident response function.
- Failover trigger.
- Dependency readiness check.
- Data reconciliation activity.
- Failback path.
- Separate backup store or note that replication is not a backup.
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) labels.
- Visible note that redundancy alone does not prove resilience.

## Required relationships

- Primary runtime serves normal payment traffic.
- Secondary site or region is warm standby and becomes active only after failover.
- Payment data replication direction is shown and labelled.
- Event or status replication is shown where relevant.
- Operations declares or receives the failover trigger.
- Dependency readiness is checked before traffic moves to the secondary region.
- Failback is shown as a controlled path after validation.
- Data reconciliation is shown before or during failback.
- Backup is distinguished from replication.
- Core Deposit System dependency is visible as a constraint or external dependency.

## Main flow or structure

Show normal path and recovery path separately. Use the warm-standby scenario only, with failover, reconciliation and failback labels.

## Alternative and exception flows

The figure may mention that Core Deposit System readiness constrains recovery, but it should not model all incident runbook steps.

## Scope

Conceptual payment resilience view for Horizon Bank.

## Exclusions

- No detailed backup schedule or restore procedure.
- No full incident-management process.
- No regulatory claim about required RTO or RPO.
- No cost model.
- No detailed observability pipeline. That is covered by FIG-11-06.

## Accessibility requirements

Use explicit labels for primary, secondary, normal path, failover, failback, reconciliation and backup. Use line style plus text rather than colour alone to distinguish replication from live traffic.

## Source references

- [NIST-SP-800-34R1]
- [AWS-WA-RELIABILITY-2026]

## Review criteria

- RTO and RPO are shown as modelled objectives, not guaranteed facts.
- Failover trigger, dependency readiness, failback and data reconciliation are visible.
- Replication is explicitly not treated as a backup.
- Redundancy alone is explicitly not treated as proof of resilience.
- Dependencies and recovery assumptions are explicit.
- Specification must be accepted by the author before creating the PlantUML source.
