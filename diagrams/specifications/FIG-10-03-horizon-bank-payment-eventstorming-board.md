# FIG-10-03: Horizon Bank Payment EventStorming Board

## Purpose

Show a simplified EventStorming-style discovery board for Horizon Bank outgoing payment handling using a clear command-event-policy chain.

## Audience

Beginners, analysts, architects, developers, operations and risk reviewers.

## Question answered

Which commands cause which payment events, and how does the payment routing policy react after screening?

## Notation

Original EventStorming-style teaching illustration in PlantUML. Commands, events, policies, actors and systems must be visually distinct by label and shape or grouping. Colour may help, but labels must carry the meaning.

## Required elements

- Retail Customer
- Operations Analyst
- Fraud Investigator
- Horizon Digital Channels
- Payments Platform
- Financial Crime Platform
- Core Deposit System
- `SubmitPaymentInstruction`
- `PaymentInstructionReceived`
- `ValidatePaymentInstruction`
- `PaymentInstructionValidated`
- `PaymentInstructionRejected`
- `RequestPaymentScreening`
- `PaymentScreeningCompleted`
- Payment routing policy
- `PostPayment`
- `RequestPaymentRepair`
- `RejectPayment`
- `OpenFraudCase`
- `PaymentPosted`
- `PaymentRepairRequested`
- `PaymentRejected`
- `FraudCaseOpened`
- Open question about repair ownership

## Required relationships

- `SubmitPaymentInstruction` produces `PaymentInstructionReceived`.
- `ValidatePaymentInstruction` produces either `PaymentInstructionValidated` or `PaymentInstructionRejected`.
- `RequestPaymentScreening` produces `PaymentScreeningCompleted`.
- Payment routing policy reacts to `PaymentScreeningCompleted`.
- Payment routing policy issues `PostPayment`, `RequestPaymentRepair`, `RejectPayment` or `OpenFraudCase`.
- `PostPayment` produces `PaymentPosted`.
- `RequestPaymentRepair` produces `PaymentRepairRequested`.
- `RejectPayment` produces `PaymentRejected`.
- `OpenFraudCase` produces `FraudCaseOpened`.

## Main flow or structure

Arrange the command-event chain from left to right. Place the payment routing policy after `PaymentScreeningCompleted`. Show the four routing outcomes as branches. Place actors and systems near the commands they issue or own.

## Alternative and exception flows

Include validation rejection, payment repair, payment rejection and fraud-case branches as simplified alternatives. Do not model every payment repair or fraud-investigation step.

## Scope

Horizon Bank outgoing payment discovery view for teaching domain and event modelling.

## Exclusions

- Any earlier screening-result placeholder name.
- Formal BPMN syntax.
- Full operational payment repair workflow.
- Full fraud investigation case lifecycle.
- Physical broker topics, partitions, retries or dead-letter queues.
- Sensitive real-bank payment data.

## Accessibility requirements

Use readable labels, clear grouping and sufficient contrast. Colour must not be the only indicator of element type. Include a short legend if colour or shape is used.

## Source references

- `[EVENTSTORMING-BRANDOLINI-2026]`
- `[DDD-REFERENCE-2015]`
- `examples/horizon-bank/README.md`
- `examples/horizon-bank/actors.md`
- `examples/horizon-bank/system-landscape.md`

## Review criteria

- The figure is clearly a teaching illustration, not copied EventStorming material.
- Events use past-tense names.
- Commands use imperative names.
- `PaymentScreeningCompleted` is used consistently as the payment-screening event.
- The routing policy and four issued commands are visible.
- Open questions are visibly unresolved.
- The model agrees with Chapter 10 prose and Horizon Bank example names.
