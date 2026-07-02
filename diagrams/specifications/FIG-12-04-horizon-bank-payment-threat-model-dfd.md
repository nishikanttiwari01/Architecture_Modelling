# FIG-12-04: Horizon Bank Payment Threat-Model DFD

## Purpose

Show payment-related data movement, trust-boundary basis and threat-review points for outgoing retail payments.

## Audience

Security reviewers, solution architects, integration architects, developers, operations and risk reviewers.

## Question answered

Where does payment data move across trust contexts, and which flows need threat and control review?

## Notation

Threat-model Data Flow Diagram with external entities, processes, data stores, labelled data flows and trust boundaries. PlantUML is the intended source tool after author approval.

## Required elements

- Retail Customer as external entity.
- Operations Analyst as external entity to the Payments Platform scope.
- Compliance Officer as external entity to the Payments Platform scope.
- Horizon Digital Channels as process.
- Payments Platform as process.
- Financial Crime Platform as process.
- Core Deposit System as retained system outside the Payments Platform modelling scope.
- Event Platform as shared event-distribution process outside the Payments Platform modelling scope.
- Payment record store.
- Audit log.
- Trust boundaries for customer access, digital-channel responsibility, payment-platform responsibility, retained-core responsibility, event distribution and data custody. Each boundary must state its basis.

## Required relationships

- Retail Customer sends payment instruction and session reference to Horizon Digital Channels.
- Horizon Digital Channels sends payment instruction, validated subject context and entitlement context to Payments Platform.
- Payments Platform sends screening request to Financial Crime Platform.
- Financial Crime Platform returns screening result.
- Compliance Officer reviews or records screening case action through the Financial Crime Platform.
- Operations Analyst submits repair action through a controlled operations path to the Payments Platform.
- Payments Platform sends posting request to Core Deposit System.
- Core Deposit System returns posting result.
- Payments Platform stores payment record.
- Payments Platform writes audit event.
- Payments Platform publishes payment status event to Event Platform.

Authentication and session validation are outside the detailed scope of this DFD and are represented separately by the Chapter 12 authentication modelling guidance. Do not add a full Identity Service flow unless the author later approves expanding the DFD scope.

## Threat review labels

Use the following threat IDs so the figure can connect to the manuscript control map:

- T12-01: stolen or replayed customer session creates a payment.
- T12-02: payment amount or beneficiary is tampered with between channel and platform.
- T12-03: stolen service credential is used to submit a posting request.
- T12-04: sensitive staff repair or release action cannot be attributed.
- T12-05: prohibited payment is released outside financial-crime policy authority.
- T12-06: payment-status event exposes excessive customer or account data.
- T12-07: weak entitlement or ownership validation permits payment from the wrong account.
- T12-08: operations repair authority combined with broken separation of duties permits unauthorised release.

## Main flow or structure

Arrange the DFD so payment data movement is readable from customer submission through screening, posting, event publication and audit storage. Label every flow with the data item, not only the protocol. Keep business-process sequence detail out of the DFD unless it is needed to explain data movement.

## Alternative and exception flows

Show rejected screening or failed posting only if the diagram remains readable. Otherwise leave exception handling to supporting prose or a later BPMN view.

## Scope

Threat-modelling view for outgoing retail payment submission, screening, posting, status publication and audit capture.

## Exclusions

- Detailed BPMN process flow.
- Full data model.
- Complete network topology.
- Complete incident response process.
- Vendor-specific security products.
- Quantitative risk scoring.

## Accessibility requirements

Use boundary labels and flow labels. Do not rely on colour alone to show boundary type, threat category or data sensitivity.

## Source references

- `[OWASP-THREAT-MODELLING-2026]`
- `[MICROSOFT-STRIDE-2026]`
- `[NIST-SP-800-207]`

## Review criteria

- External entities, processes, data stores and flows are distinguishable.
- Each boundary has a stated basis.
- Important payment data flows are labelled.
- Threat IDs connect to the manuscript control map.
- The diagram supports STRIDE review without becoming a full process model.
