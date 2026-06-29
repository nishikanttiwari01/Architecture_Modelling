# FIG-06-03: Horizon Bank Payment Repair BPMN Exception Collaboration

## Purpose

Show a simplified BPMN exception and timer collaboration for payment repair after posting failure.

## Audience

Architects, operations stakeholders, process analysts and control reviewers.

## Question answered

What happens when a payment cannot be posted and correction information must be requested from the customer?

## Abstraction level

Exception-collaboration overview. It shows repair behaviour, message exchange, timeout and outcomes, not payment-system internals.

## Notation

BPMN collaboration diagram.

## Required elements

- Pools: Retail Customer, Horizon Bank
- Retail Customer: black-box external pool
- Horizon Bank lanes: Payments Platform, Operations Analyst
- Start event: Posting failed
- Tasks: Create repair case, Review exception, Request correction, Validate correction, Resubmit payment, Close case
- Event-based gateway: Wait for correction
- Intermediate message catch event: Correction received
- Intermediate timer catch event: Correction deadline reached
- End events: Payment resubmitted, Case timed out

## Required relationships

- Posting failed starts Create repair case.
- Create repair case leads to Review exception.
- Review exception leads to Request correction.
- Horizon Bank sends a correction request to Retail Customer using message flow.
- Wait for correction uses an event-based gateway.
- Correction received is an intermediate message catch event reached by message flow from Retail Customer.
- Correction deadline reached is an intermediate timer catch event.
- Correction received leads to Validate correction and Resubmit payment.
- Correction deadline reached leads to Close case and Case timed out.

## Main flow or structure

Show the repair process from left to right. Put Retail Customer in a separate pool and keep Payments Platform and Operations Analyst as lanes inside Horizon Bank. Make the timer path visible so the reader can see that the process does not wait indefinitely.

## Alternative and exception flows

Show only correction received versus correction deadline reached. Do not model sanctions investigation, accounting reconciliation, duplicate submission handling or payment scheme-specific rules.

## Scope

Simplified repair collaboration after account posting failure.

## Exclusions

No payment initiation happy path, core banking internals, message-broker detail, scheme settlement, ledger accounting or deployment nodes.

## Accessibility requirements

Use readable timer and gateway labels. Keep the diagram narrow enough for book-page width.

## Source references

- `[OMG-BPMN]` for BPMN process, gateway, lane and timer-event notation.
- `examples/horizon-bank/actors.md` for stable actor names.
- `examples/horizon-bank/system-landscape.md` for stable system names.

## Review criteria

- Timer outcome is explicit.
- The waiting split is an event-based gateway, not a data decision.
- Message flow crosses the customer boundary and sequence flow stays inside Horizon Bank.
- Lanes represent responsibility inside Horizon Bank, not software containers.
- Retail Customer is not modelled as a Horizon Bank lane.
- The figure does not imply full payments exception coverage.
