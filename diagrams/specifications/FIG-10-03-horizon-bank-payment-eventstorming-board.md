# FIG-10-03: Horizon Bank Payment EventStorming Board

## Purpose

Show a simplified EventStorming-style discovery board for Horizon Bank outgoing payment handling.

## Audience

Beginners, analysts, architects, developers, operations and risk reviewers.

## Question answered

What happens from payment instruction receipt to posting, rejection, repair or fraud investigation, and where do commands, events, policies and open questions appear?

## Notation

Original EventStorming-style teaching illustration in PlantUML, using labelled groups for events, commands, actors, policies, external systems and open questions. Colours may be used sparingly, but labels must carry the meaning.

## Required elements

- Retail Customer
- Operations Analyst
- Fraud Investigator
- Horizon Digital Channels
- Payments Platform
- Financial Crime Platform
- Core Deposit System
- Event Platform
- `SubmitPaymentInstruction`
- `ScreenPayment`
- `PostPayment`
- `OpenFraudCase`
- `PaymentInstructionReceived`
- `PaymentInstructionValidated`
- `ScreeningRequested`
- `ScreeningResultReceived`
- `PaymentRepairRequested`
- `PaymentPosted`
- `PaymentRejected`
- `FraudCaseOpened`
- Payment routing policy
- Financial-crime screening policy
- Open question about repair ownership

## Required relationships

- Commands should precede or trigger related events where appropriate.
- Policies should be shown as rules reacting to events or shaping commands.
- External systems should be labelled distinctly from actors and internal platforms.
- Open questions should be shown as unresolved workshop findings, not final architecture decisions.

## Main flow or structure

Arrange events broadly left to right in time order. Place commands above or near the events they request. Place actors and systems near the commands or events they influence. Place policies near the event-to-command reactions they shape.

## Alternative and exception flows

Include repair, rejection and fraud-case branches as simplified alternatives. Do not model every payment repair step.

## Scope

Horizon Bank outgoing payment discovery view for teaching domain and event modelling.

## Exclusions

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
- Open questions are visibly unresolved.
- The figure does not claim EventStorming is a formal standards-body notation.
- The model agrees with Chapter 10 prose and Horizon Bank example names.
