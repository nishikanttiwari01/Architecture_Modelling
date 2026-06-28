# FIG-05-05: Payment submission dynamic view

## Purpose

Show how a C4 dynamic view explains one runtime interaction path across the Horizon Bank payments platform.

## Audience

Solution architects, developers and reviewers who need to understand a payment submission interaction.

## Question answered

What is the main runtime path when a customer submits a payment through Horizon Digital Channels?

## Notation

C4 Dynamic using C4-PlantUML.

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

- Retail Customer submits payment.
- Horizon Digital Channels call Payments API.
- Payments API asks Payment Orchestration Service to create payment.
- Payment Orchestration Service requests screening.
- Payment Orchestration Service requests account posting through Enterprise Integration Platform.
- Enterprise Integration Platform calls Core Deposit System.
- Payment Orchestration Service records status.
- Payment Orchestration Service publishes payment event.
- Payments API returns accepted status to Horizon Digital Channels.

## Main flow or structure

Show a numbered interaction path. Keep it at runtime interaction level.

## Alternative and exception flows

Mention screening failure and posting failure in chapter prose. Do not crowd this figure with exception branches.

## Scope

One happy-path payment submission interaction.

## Exclusions

No BPMN human workflow, no full cross-border payment process, no settlement, no reconciliation and no deployment nodes.

## Accessibility requirements

Use numbered relationships, concise labels and sufficient spacing.

## Source references

- `[C4-OFFICIAL]`
- `examples/horizon-bank/system-landscape.md`
- `examples/horizon-bank/actors.md`

## Review criteria

- The sequence is plausible and limited.
- The view does not become a full BPMN process.
- Relationship direction is correct.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 prototype on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
