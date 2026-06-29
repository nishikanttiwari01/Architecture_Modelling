# FIG-04-04: Horizon Bank payment submission sequence diagram

## Purpose

Show a UML sequence diagram for one Horizon Bank payment submission path.

## Audience

Architects, developers and testers.

## Question answered

In one successful payment submission scenario, who sends which message and in what order?

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

- Retail Customer submits payment through Horizon Digital Channels
- Horizon Digital Channels sends payment instruction to Payments API
- Payments API asks Payment Orchestration Service to create payment
- Payment Orchestration Service requests screening from Financial Crime Platform
- Payment Orchestration Service requests account posting through Enterprise Integration Platform
- Enterprise Integration Platform posts to Core Deposit System
- Payment Orchestration Service records status in Payment Status Store
- Payment Orchestration Service publishes payment event to Event Platform
- Success response returns to Horizon Digital Channels

## Main flow or structure

Show the main successful path from top to bottom. Use concise message labels.

## Alternative and exception flows

Include at most one note that rejected screening or failed posting requires a separate exception view.

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
- The figure does not imply a complete payments process.
