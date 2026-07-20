# Source Note: OPENTELEMETRY-PV52-2026

## Bibliographic details

- Organisation or author: OpenTelemetry project
- Title: OpenTelemetry Concepts and Signals documentation
- Version: Current public documentation
- Publication date: Continuously maintained documentation
- Access date: 2026-07-20
- URL or identifier: https://opentelemetry.io/docs/concepts/; https://opentelemetry.io/docs/concepts/signals/; https://opentelemetry.io/docs/collector/
- Source type: Official project documentation

## Supported claims

- Claim: Traces, metrics and logs are distinct telemetry signals that answer different operational questions.
- Claim: Instrumentation, collection, processing and export are separate responsibilities in an observability architecture.
- Claim: The OpenTelemetry Collector can receive, process and export telemetry, but an organisation must still govern redaction, retention, access, alerting and ownership.
- Intended chapter(s): 52
- Normative or interpretive: Official for OpenTelemetry concepts; interpretive for Horizon Bank operational architecture.

## Relevant summary

OpenTelemetry provides vendor-neutral instrumentation and telemetry pipelines. Chapter 52 uses it to explain why operational models should show the route from an instrumented application through collection and processing to analysis and alerting. Business outcome monitoring, incident ownership and sensitive-data controls remain bank responsibilities.

## Terminology and version notes

Do not reduce observability to dashboards. Avoid relying on experimental signal features for the chapter's baseline; traces, metrics and logs are sufficient for the teaching example.

## Copyright or reuse notes

Paraphrase documentation and use original operational examples.

## Verification status

Checked
