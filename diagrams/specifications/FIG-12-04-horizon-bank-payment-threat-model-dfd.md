# FIG-12-04: Horizon Bank Payment Threat-Model DFD

## Purpose

Show payment-related data movement, trust boundaries and threat-review points for outgoing retail payments.

## Audience

Security reviewers, solution architects, integration architects, developers, operations and risk reviewers.

## Question answered

Where does payment data move across trust boundaries, and which flows need threat and control review?

## Notation

Threat-model Data Flow Diagram with external entities, processes, data stores, labelled data flows and trust boundaries. PlantUML is the intended source tool after author approval.

## Required elements

- Retail Customer as external entity.
- Horizon Digital Channels as process.
- Payments Platform as process.
- Financial Crime Platform as process.
- Core Deposit System as external or retained system.
- Event Platform as process or shared platform.
- Payment record store.
- Audit log.
- Trust boundaries for customer context, bank digital platform, payment platform, retained core system and shared event platform.

## Required relationships

- Retail Customer sends payment instruction to Horizon Digital Channels.
- Horizon Digital Channels sends payment instruction to Payments Platform.
- Payments Platform sends screening request to Financial Crime Platform.
- Financial Crime Platform returns screening result.
- Payments Platform sends posting request to Core Deposit System.
- Core Deposit System returns posting result.
- Payments Platform stores payment record and audit event.
- Payments Platform publishes payment status event to Event Platform.

## Main flow or structure

Arrange the DFD so payment data movement is readable from customer submission through screening, posting, event publication and audit storage. Label every flow with the data item, not only the protocol.

## Alternative and exception flows

Show rejected screening or failed posting only if the diagram remains readable. Otherwise leave exception handling to supporting prose or a later BPMN view.

## Scope

Threat-modelling view for outgoing retail payment submission and status publication.

## Exclusions

- Detailed BPMN process flow.
- Full data model.
- Complete network topology.
- Complete incident response process.
- Vendor-specific security products.

## Accessibility requirements

Use boundary labels and flow labels. Do not rely on colour alone to show trust or sensitivity.

## Source references

- `[OWASP-THREAT-MODELLING-2026]`
- `[MICROSOFT-STRIDE-2026]`
- `[NIST-SP-800-207]`

## Review criteria

- External entities, processes, data stores and flows are distinguishable.
- Trust boundaries are explicit and meaningful.
- Important payment data flows are labelled.
- The diagram supports STRIDE review without becoming a full process model.
