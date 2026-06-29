# FIG-04-04: Horizon Bank Payment Submission Sequence Diagram

## Purpose

Show a UML sequence diagram for one Horizon Bank payment submission path.

## Audience

Architects, developers and testers.

## Question answered

In one successful payment submission scenario, who sends which message and in what order?

## Abstraction level

Runtime interaction view for one target-state scenario.

## Notation

UML sequence diagram.

## Required elements

- Retail Customer
- Horizon Digital Channels
- Payments API
- Payment Orchestration Service
- Financial Crime Platform
- Enterprise Integration Platform
- Core Deposit System
- Payment Status Store
- Event Platform

## Required relationships

- Retail Customer submits payment through Horizon Digital Channels.
- Horizon Digital Channels sends payment instruction to Payments API.
- Payments API asks Payment Orchestration Service to create payment.
- Payment Orchestration Service requests screening from Financial Crime Platform.
- Payment Orchestration Service requests account posting through Enterprise Integration Platform.
- Enterprise Integration Platform posts to Core Deposit System.
- Payment Orchestration Service records status in Payment Status Store.
- Payment Orchestration Service publishes payment event to Event Platform.
- Success response returns to Horizon Digital Channels.

## Relationship semantics

Solid messages represent calls or requests in the scenario. Dashed messages represent returns. The alternative fragment shows mutually exclusive outcomes. Message order is top-to-bottom, not left-to-right.

## Main flow or structure

Show the main successful path from top to bottom. Use concise message labels.

## Alternative and exception flows

Include one alternative fragment for screening rejection or posting failure. Do not model settlement or repair paths.

## Scope

One target-state payment submission interaction.

## Exclusions

No full business process, no settlement detail, no fraud case workflow and no infrastructure placement.

## Accessibility requirements

Keep lifeline count manageable and label messages in readable sentence case.

## Source references

- `[OMG-UML]` for UML sequence notation.
- `examples/horizon-bank/system-landscape.md` for stable system names.
- `examples/horizon-bank/actors.md` for stable actor names.

## Review criteria

- Message order matches the chapter explanation.
- Lifelines use repository-controlled names.
- Alternative fragment does not imply a complete payments exception model.
- The figure does not imply a complete payments process.
