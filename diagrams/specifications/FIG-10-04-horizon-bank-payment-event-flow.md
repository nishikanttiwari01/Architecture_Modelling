# FIG-10-04: Horizon Bank Payment Event Flow

## Purpose

Show selected Horizon Bank payment events moving between systems and consumers in an event-driven architecture view.

## Audience

Solution architects, integration architects, developers, data architects and operations reviewers.

## Question answered

Which systems produce and consume payment events for a simplified outgoing payment scenario?

## Notation

Event-flow architecture diagram using PlantUML component or sequence-style notation. The diagram should emphasise producers, event platform and consumers rather than human task sequence.

## Required elements

- Horizon Digital Channels
- Payments Platform
- Financial Crime Platform
- Core Deposit System
- Event Platform
- Enterprise Data Platform
- Operations monitoring or payment status view
- `PaymentInstructionReceived`
- `ScreeningResultReceived`
- `PaymentPosted`
- `PaymentRejected`
- `PaymentRepairRequested`
- `FraudCaseOpened`

## Required relationships

- Horizon Digital Channels submits payment instruction to Payments Platform.
- Payments Platform publishes `PaymentInstructionReceived`.
- Payments Platform requests screening from Financial Crime Platform.
- Financial Crime Platform returns screening result and may lead to `FraudCaseOpened`.
- Payments Platform posts allowed payments to Core Deposit System.
- Payments Platform publishes posting, rejection or repair events to Event Platform.
- Enterprise Data Platform and operations status view consume selected events.

## Main flow or structure

Place event producers on the left or top, the Event Platform centrally, and consumers on the right or bottom. Label event names on arrows. Keep command/request arrows visually distinct from event publication arrows.

## Alternative and exception flows

Show repair, rejection and fraud-case events as alternate outcomes. Avoid modelling detailed retry, timeout and dead-letter handling in this beginner figure.

## Scope

Simplified outgoing payment event flow for Horizon Bank.

## Exclusions

- Full BPMN payment process.
- Physical deployment, network zones and broker internals.
- Topic partitioning, consumer groups and schema registry implementation.
- Detailed fraud investigation workflow.
- Complete payment message standards.

## Accessibility requirements

Use labelled arrows and a legend if different arrow styles are used. Ensure the event names remain readable at book-page width.

## Source references

- `[DDD-REFERENCE-2015]`
- `[CNCF-CLOUDEVENTS-1.0.2]`
- `[ASYNCAPI-3.1.0]`
- `examples/horizon-bank/system-landscape.md`

## Review criteria

- The figure distinguishes commands or requests from published events.
- Event names are past tense.
- The Event Platform is not shown as the owner of event meaning.
- Producers and consumers are visible.
- The diagram does not mix deployment topology with the event-flow concern.
- The model agrees with Chapter 10 prose and Horizon Bank system names.
