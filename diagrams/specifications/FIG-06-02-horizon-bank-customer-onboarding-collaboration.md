# FIG-06-02: Horizon Bank Customer Onboarding BPMN Collaboration

## Purpose

Show how a BPMN collaboration diagram can describe participant interaction during customer onboarding.

## Audience

Business analysts, architects, compliance reviewers and operations stakeholders.

## Question answered

Which participants exchange messages during a simplified Horizon Bank customer onboarding scenario?

## Abstraction level

Business-process collaboration overview. It shows message exchange between participants, not internal application structure.

## Notation

BPMN collaboration diagram.

## Required elements

- Pools: Retail Customer, Horizon Bank, Financial Crime Platform
- Horizon Bank lanes: Digital Channels, Onboarding Operations, Compliance
- Retail Customer: black-box external pool
- Financial Crime Platform: black-box external pool
- Customer message: Submit application
- Bank tasks: Capture application, Validate application, Request screening, Review screening exception, Open customer profile, Send onboarding outcome
- Intermediate message catch event: Receive result
- Exclusive gateways: Screening clear?, Exception clear?
- End events: Profile opened, Application rejected

## Required relationships

- Retail Customer sends application to Horizon Bank.
- Horizon Bank captures and validates the application.
- Horizon Bank sends screening request to Financial Crime Platform.
- Financial Crime Platform returns a screening result to the receiving event in the Horizon Bank process.
- Screening clear? is evaluated only after the result is received.
- `[clear]` leads to opening the customer profile and sending outcome.
- `[possible match]` leads to compliance review.
- Review screening exception leads to Exception clear?, with guarded `[clear]` and `[reject]` paths.
- Horizon Bank sends the final onboarding outcome to Retail Customer.

## Main flow or structure

Use separate pools for the customer, the bank and the financial-crime platform. Keep Retail Customer and Financial Crime Platform as black-box external participants. Keep sequence flow inside the Horizon Bank process and use message flow between pools.

## Alternative and exception flows

Show only the possible-match review path and rejection outcome. Do not model full Know Your Customer casework, document upload retry, account opening or product fulfilment.

## Scope

Simplified onboarding collaboration for a retail customer.

## Exclusions

No user-interface screens, API design, data model detail, financial-crime investigation process, account product fulfilment or deployment architecture.

## Accessibility requirements

Use readable pool and lane labels, clear message-flow direction and concise task names.

## Source references

- `[OMG-BPMN]` for BPMN collaboration, pool, lane, sequence-flow and message-flow notation.
- `examples/horizon-bank/actors.md` for stable actor names.
- `examples/horizon-bank/system-landscape.md` for stable system names.

## Review criteria

- Message flows cross pools.
- Sequence flows stay within the Horizon Bank process.
- The Retail Customer and Financial Crime Platform pools contain no internal tasks.
- The Financial Crime Platform is shown as a separate participant, not as a Horizon Bank lane.
- Screening clear? appears after the result has been received.
- Review screening exception does not have uncontrolled outgoing flows.
- The figure does not imply a complete onboarding operating procedure.
