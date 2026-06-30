# FIG-10-04: Horizon Bank Payment Event Flow

## Purpose

Show selected Horizon Bank payment commands, synchronous requests, responses and published events while keeping event ownership clear.

## Audience

Solution architects, integration architects, developers, data architects and operations reviewers.

## Question answered

Which systems issue commands or requests, which systems respond, which systems publish events and how does the Event Platform distribute those events?

## Notation

Event-flow architecture diagram using PlantUML sequence-style notation. Use visibly different arrow styles and labels for commands or synchronous requests, responses and published domain or integration events.

## Required elements

- Horizon Digital Channels
- Payments Platform
- Financial Crime Platform
- Core Deposit System
- Event Platform
- Enterprise Data Platform
- Operations payment status view
- Fraud Investigation capability or case handling responsibility
- `SubmitPaymentInstruction`
- `PaymentInstructionReceived`
- `RequestPaymentScreening`
- `PaymentScreeningCompleted`
- `PostPayment`
- `PaymentPosted`
- `PaymentRepairRequested`
- `PaymentRejected`
- `OpenFraudCase`
- `FraudCaseOpened`

## Required relationships

- Horizon Digital Channels sends `SubmitPaymentInstruction` to Payments Platform.
- Payments Platform publishes `PaymentInstructionReceived` to Event Platform.
- Payments Platform sends `RequestPaymentScreening` to Financial Crime Platform.
- Financial Crime Platform returns a screening response to Payments Platform.
- Financial Crime Platform publishes `PaymentScreeningCompleted` to Event Platform.
- Payments Platform applies routing policy after screening.
- Payments Platform sends `PostPayment` to Core Deposit System for allowed payments.
- Core Deposit System returns a posting response to Payments Platform.
- Payments Platform publishes `PaymentPosted`, `PaymentRepairRequested` or `PaymentRejected` to Event Platform.
- Payments Platform sends `OpenFraudCase` to the fraud investigation responsibility when required.
- The fraud investigation responsibility publishes `FraudCaseOpened` to Event Platform.
- Event Platform distributes events to Enterprise Data Platform and Operations payment status view.

## Main flow or structure

Use left-to-right sequence lifelines. Label commands or synchronous requests, responses and published events explicitly. Show Event Platform as an intermediary that distributes events, not as the owner of event meaning.

## Alternative and exception flows

Show posted, repair, rejected and fraud-case outcomes. Avoid detailed retry, timeout and dead-letter handling in the figure; cover those runtime topics in prose.

## Scope

Simplified outgoing payment event flow for Horizon Bank.

## Exclusions

- Full BPMN payment process.
- Physical deployment, network zones and broker internals.
- Topic partitioning, consumer groups and schema registry implementation.
- Detailed fraud investigation workflow.
- Complete payment message standards.

## Accessibility requirements

Use labelled arrows and a legend for arrow styles. Ensure event names remain readable at book-page width. Colour must not be the only way to tell commands, responses and events apart.

## Source references

- `[DDD-REFERENCE-2015]`
- `[CNCF-CLOUDEVENTS-1.0.2]`
- `[ASYNCAPI-3.1.0]`
- `examples/horizon-bank/system-landscape.md`

## Review criteria

- Commands or synchronous requests, responses and published events cannot be confused.
- Every published event originates from its owning producer.
- The Event Platform is an intermediary, not the owner of event meaning.
- `PaymentScreeningCompleted` is used consistently as the payment-screening event.
- Producers and consumers are visible.
- The diagram does not mix deployment topology with the event-flow concern.
- The model agrees with Chapter 10 prose and Horizon Bank system names.
