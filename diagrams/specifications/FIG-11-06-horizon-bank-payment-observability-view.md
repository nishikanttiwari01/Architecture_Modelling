# FIG-11-06: Horizon Bank Payment Observability View

## Purpose

Show how Horizon Bank payment telemetry moves from business systems to collection, filtering, redaction, observability backends, dashboards and alert routing.

## Audience

Operations teams, service owners, platform teams and risk reviewers.

## Question answered

How can payment operations observe submission, screening, posting, event and customer-status behaviour across the main Horizon Bank payment systems?

## Notation

Observability architecture view, rendered with PlantUML after author acceptance of this specification.

## Required elements

- Horizon Digital Channels.
- Payments Platform.
- Financial Crime Platform.
- Enterprise Integration Platform.
- Event Platform.
- Core Deposit System.
- Traces.
- Metrics.
- Logs.
- OpenTelemetry Collector.
- Filtering and sensitive-data redaction.
- Observability backends.
- Dashboards.
- Alert routing.
- Operations Team.
- Service Owner.
- Payment submission rate.
- Screening latency.
- Posting-confirmation delay.
- Failed-payment rate.
- Event backlog.
- Customer-status update lag.

## Required relationships

- Payment systems emit traces, metrics and logs.
- Telemetry is collected by the OpenTelemetry Collector.
- Filtering and sensitive-data redaction happen before telemetry reaches shared observability backends.
- Observability backends support dashboards and alert routing.
- Dashboards are used by the Operations Team and Service Owner.
- Alert routing sends actionable alerts to the Operations Team and service-impact alerts to the Service Owner.
- Payment indicators are displayed on dashboards and can drive alert thresholds.

## Main flow or structure

Show payment systems on the left, telemetry signals and collector in the middle, processing and observability backends to the right, then dashboards, alerts and human roles. Keep the six payment indicators grouped as service indicators so readers do not confuse them with separate applications.

## Alternative and exception flows

The figure does not show every log stream, trace span or metric. It focuses on the minimum cross-system telemetry needed to discuss payment operations.

## Scope

Conceptual observability view for Horizon Bank payment operations.

## Exclusions

- No vendor-specific observability product.
- No detailed OpenTelemetry configuration.
- No incident-management process.
- No security monitoring centre process.
- No retention or cost model.

## Accessibility requirements

Use explicit labels for traces, metrics, logs, filtering, redaction, dashboards and alert routing. Do not use colour as the only way to distinguish telemetry, dashboards and alerts.

## Source references

- [OPENTELEMETRY-DOCS-2026]
- [INFRA-DIAGRAM-TOOL-GUIDANCE-2026]

## Review criteria

- All six Horizon Bank systems are visible.
- Traces, metrics, logs, OpenTelemetry Collector, filtering, redaction and observability backends are visible.
- All six required payment indicators are visible.
- Dashboards and alert routing are separate.
- Operations Team and Service Owner responsibilities are both visible.
- Specification must be accepted by the author before creating the PlantUML source.
