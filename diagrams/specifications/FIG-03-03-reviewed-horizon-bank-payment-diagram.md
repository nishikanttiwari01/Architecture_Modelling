# FIG-03-03: Reviewed Horizon Bank Payment Diagram

## Purpose

Show how the flawed Horizon Bank payment diagram can be corrected or annotated so that scope, state, ownership, relationships, trust boundary and exceptions are reviewable.

## Audience

Beginners reading Chapter 3 and reviewers learning how to improve a diagram.

## Question answered

How can review findings from a flawed payment diagram be resolved in a clearer architecture diagram?

## Notation

Informal PlantUML box-and-line diagram with a visible trust-zone boundary and metadata.

## Required elements

- Metadata block with purpose, owner, version, status and state.
- Customer.
- Horizon Bank trust zone.
- Mobile Banking owned by Digital Channels.
- Payment Orchestration owned by Payments.
- Fraud Screening owned by Financial Crime.
- Sanctions Screening owned by Financial Crime.
- Core Banking owned by Core Accounts.
- Customer Notification owned by Digital Channels.
- Payment Operations Queue owned by Payment Operations.
- External Payment Rail owned by an external operator.
- Trust-boundary note.
- Exception-path note.

## Required relationships

- Customer to Mobile Banking: submit payment instruction.
- Mobile Banking to Payment Orchestration: send payment request.
- Payment Orchestration to Fraud Screening: request fraud screening.
- Fraud Screening to Sanctions Screening: forward for sanctions screening.
- Sanctions Screening to Payment Orchestration: return screening decision.
- Payment Orchestration to Core Banking: post accepted payment.
- Core Banking to External Payment Rail: submit cleared payment.
- Payment Orchestration to Payment Operations Queue: route rejected or repair payment.
- Payment Orchestration to Customer Notification: send customer status event.
- Settlement status from the External Payment Rail to Core Banking is stated in a note rather than drawn as a second parallel arrow.

## Main flow or structure

Place bank-controlled elements inside a visible Horizon Bank trust zone. Place the External Payment Rail outside the trust zone. Use directional relationship labels that match the arrows, show the exception path and state the omitted settlement response explicitly.

## Alternative and exception flows

Rejected, repair or manual-review payments are routed to the Payment Operations Queue.

## Scope

Target-state Horizon Bank payment submission review example for Chapter 3.

## Exclusions

This is not a complete payment process model, security design or deployment model. It omits detailed fraud rules, sanctions list sources, message schemas, runtime nodes and operational runbooks.

## Accessibility requirements

Use readable text, strong contrast and short labels. Do not rely on colour alone to identify the trust boundary or exception path.

## Source references

- Repository Horizon Bank case study.

## Review criteria

- The diagram resolves the review problems shown in `FIG-03-02`.
- The figure is readable at book-page width.
- Relationship labels match arrow direction.
- The trust boundary, ownership and exception path are visible.
- Metadata is visible and concise.

## Authorisation note

The author requested this figure as part of the Chapter 3 revision before author review. The diagram remains in `Review`.
