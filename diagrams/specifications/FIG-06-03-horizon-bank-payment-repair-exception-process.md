# FIG-06-03: Horizon Bank Payment Repair BPMN Exception Process

## Purpose

Show a simplified BPMN exception and timer process for payment repair after posting failure.

## Audience

Architects, operations stakeholders, process analysts and control reviewers.

## Question answered

What happens when a payment cannot be posted and correction evidence is required?

## Abstraction level

Exception-process overview. It shows repair behaviour, timeout and outcomes, not payment-system internals.

## Notation

BPMN process diagram.

## Required elements

- Pool: Horizon Bank Payments Operations
- Lanes: Payments Platform, Operations Analyst, Retail Customer
- Start event: Posting failed
- Tasks: Create repair case, Review exception, Request correction, Provide correction, Resubmit payment, Close case
- Intermediate timer event: Correction timeout
- Exclusive gateway: Correction received in time?
- End events: Payment resubmitted, Case timed out

## Required relationships

- Posting failed starts Create repair case.
- Create repair case leads to Review exception.
- Review exception leads to Request correction.
- Request correction waits for either customer correction or timeout.
- `[response received]` leads to Provide correction and Resubmit payment.
- `[timer expired]` leads to Close case and Case timed out.

## Main flow or structure

Show the repair process from left to right. Make the timer path visible so the reader can see that the process does not wait indefinitely.

## Alternative and exception flows

Show only response received versus timer expired. Do not model sanctions investigation, accounting reconciliation, duplicate submission handling or payment scheme-specific rules.

## Scope

Simplified repair flow after account posting failure.

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
- Gateway conditions are readable.
- Lanes represent responsibility, not software containers.
- The figure does not imply full payments exception coverage.
