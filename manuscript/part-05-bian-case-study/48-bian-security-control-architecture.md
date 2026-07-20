---
title: "Channels, Communications, Documents, Workflow, Case Management and Shared Services"
chapter: 48
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 48. Channels, Communications, Documents, Workflow, Case Management and Shared Services

## Chapter purpose

Explain the shared capabilities through which customers and colleagues interact with a full-service bank. The chapter separates channels, identity, entitlement, communications, documents, workflow, rules and case management, then shows how they support product domains without taking over product authority.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish a channel from the product applications and records it exposes;
- separate customer identity, employee identity, consent, mandates and transaction authorisation;
- distinguish communications, documents, workflow, rules and cases by lifecycle and authority;
- decide when a shared platform is suitable and when a specialist application should remain separate;
- trace a complaint from channel intake through evidence, decision, communication and recovery; and
- review security, accessibility, privacy and resilience across shared services.

## Prerequisites and dependencies

- Chapter 33: Horizon Bank Enterprise Business Architecture
- Chapter 34: Horizon Bank Application and Integration Landscape
- Chapter 47: Risk, Compliance, Financial Crime, Fraud, Audit and Legal

## Required models and artefacts

- Governed channel, identity, communication, document, workflow and case records
- Interaction, authority, security, privacy and resilience traces
- Scenario trace for `HB-SCN-18 Resolve a Customer Complaint and Redress Case`

## Worked examples

- Horizon Bank complaint and redress scenario across assisted and digital channels

## Source requirements

Identity, accessibility, security, resilience and BIAN claims use official primary sources. The chapter does not claim a legal conformance level or control applicability for an unspecified jurisdiction.

## The question this architecture answers

This architecture answers: **How can many customer and employee journeys reuse common interaction and work services without creating a new monolith or losing domain ownership?**

A channel presents an interaction. It may capture a request and show status, but it should not become the authority for every account, payment, loan or case it displays. A workflow coordinates tasks. It does not automatically own the business decision. A document service preserves content and metadata. It does not decide whether a loan is approved. These distinctions allow reuse without moving all bank behaviour into one platform.

## Governed domains, capabilities and processes

`HB-DOM-150 Channels, Communications, Documents and Workflow` contains three Level 2 domains:

- `HB-DOM-151 Digital and Physical Channels`;
- `HB-DOM-152 Communications and Notifications`; and
- `HB-DOM-153 Documents, Content, Workflow and Cases`.

The Level 1 capability is `HB-CAP-150 Channel, Communication, Content and Workflow Management`. Its Level 2 capabilities are `HB-CAP-151 Public Web Channel Management`, `HB-CAP-152 Mobile and Online Banking`, `HB-CAP-153 Branch Servicing`, `HB-CAP-154 Contact-Centre Servicing`, `HB-CAP-155 Relationship-Manager Enablement`, `HB-CAP-156 Partner and Host Channel Management`, `HB-CAP-157 Communication and Notification Management`, `HB-CAP-158 Document and Content Management` and `HB-CAP-159 Workflow and Case Management`.

`HB-PROC-15 Operate Channels, Communications and Workflows` is decomposed into `HB-PROC-159 Operate Digital and Physical Channels`, `HB-PROC-160 Deliver Communications and Notifications` and `HB-PROC-161 Manage Documents, Content, Workflow and Cases`.

`HB-ORG-07 Customer, Sales, Channels and Service` owns customer interaction, while `HB-ORG-15 Banking Operations` owns much of the operational work. Product units remain accountable for product decisions. `HB-ORG-16 Technology Architecture, Engineering and Operations` and `HB-ORG-25 Cyber Security and Identity` operate and control enabling platforms. An organisation view should show these accountabilities rather than assigning a generic `digital team` to every decision.

## Channels are views into bank responsibilities

Horizon Bank has distinct logical channel applications:

| Application | Audience and purpose | Important boundary |
|---|---|---|
| `HB-APP-001 Public Banking Web` | Public information and lead capture | No authenticated product authority |
| `HB-APP-002 Retail Mobile Banking` | Authenticated retail self-service | Displays and initiates; product applications own records |
| `HB-APP-003 Branch Service Workbench` | Assisted branch servicing | Employee authority and customer authentication required |
| `HB-APP-004 Contact Centre Workbench` | Assisted remote servicing and cases | Call handling does not bypass product or security controls |
| `HB-APP-005 Relationship Manager Workbench` | Managed sales and relationship work | Relationship view, not product or credit authority |
| `HB-APP-006 Corporate Digital Banking` | Corporate accounts, payments and cash services | Corporate mandate and entitlement required |
| `HB-APP-007 Partner and Open Banking Portal` | Partner onboarding and managed interface access | External trust and contract boundary |

The same journey may move between channels. A customer can begin online, provide evidence through mobile, speak to a contact-centre agent and complete a controlled step in a branch. The journey needs a stable correlation or case reference. It should not duplicate a new product application in each channel.

Channel models answer who interacts, through which touchpoint, for what outcome and with what hand-off. They should also show failure and assisted paths. They should not expose internal data that the channel does not need.

Digital accessibility is a testable quality concern. The Web Content Accessibility Guidelines (WCAG) 2.2 organise accessible web content around perceivable, operable, understandable and robust principles with testable criteria [W3C-WCAG-2.2]. Which conformance level or law applies depends on jurisdiction and policy, but `accessible` should never be an untested label.

## Identity is not entitlement

Identity answers who or what is interacting. Entitlement answers what that identity may do in the current context. Consent records an individual's permission or preference where that is the appropriate legal and business basis. A corporate mandate records authority granted within an organisation. Transaction authorisation approves a particular action under limits and controls.

Horizon Bank separates these concerns:

- `HB-APP-008 Customer Identity and Access Management` authenticates customers and manages customer credentials;
- `HB-APP-011 Workforce Identity Governance` manages employee and privileged access lifecycle;
- `HB-APP-010 Customer Entitlement and Mandate Service` evaluates customer, corporate-user, signatory and mandate permissions; and
- `HB-APP-009 Consent and Privacy Preference Service` preserves consent and preference evidence.

NIST Special Publication 800-63-4 separates identity proofing and enrolment, authentication and authenticator management, and federation [NIST-DIGITAL-IDENTITY-800-63-4]. Horizon Bank uses that separation as vendor-neutral design guidance, not as a claim that a United States government assurance profile applies.

`HB-CTRL-06 Consent, Mandate and Entitlement Enforcement` applies before protected actions. `HB-CTRL-37 Workforce and Privileged Access Governance` applies to employee and administrative access. A successful login is insufficient evidence that a user may approve a corporate payment or view a restricted legal case.

Service identity is another concern. An application calling an Application Programming Interface (API) needs an authenticated service identity, authorised purpose and protected credential. The customer identity should remain in auditable context where downstream authorisation requires it, but it must not be copied into every log or message without need.

## Communications and notifications

Communication has a business purpose, recipient, content, channel, timing, preference, classification and delivery state. `HB-APP-073 Notification and Communications Hub` selects approved templates, dispatches messages and records delivery status. `HB-INT-052 Customer Communication Request` requests a communication and `HB-INT-094 Communication Delivery Event` reports delivery, failure or response.

The originating domain owns the reason and material content. The hub owns composition and delivery within its scope. For example, a payment application owns the payment status; the hub should not infer that status from a retry count. A communication marked `sent` is not necessarily `delivered`, and `delivered` is not necessarily `read` or `accepted`.

`HB-APP-022 Statement and Correspondence Management` remains a specialist application because statements have product, period, completeness and retrieval responsibilities beyond generic notification. `HB-CTRL-43 Customer Statement and Communication Completeness` checks required populations and outcomes.

Preference and consent must not be applied blindly. Some service, security or legal notices may follow a different basis from marketing preferences. The rule must be explicit, jurisdiction-aware and owned; the architecture should not invent it.

## Documents and content

`HB-APP-070 Enterprise Document and Content Management` stores governed documents, content metadata, retention states and legal holds. `HB-SOR-21 Enterprise Document and Record Authority` defines its authority by document class. A document reference should identify content, version, classification, owner, retention class, integrity evidence and access conditions.

The bank should avoid uncontrolled copies in email, desktop folders and case attachments. A case can link to a governed document while preserving the document's own authority. `HB-INT-092 Workflow Document Service` lets a workflow store and retrieve evidence without embedding the content service inside the workflow engine.

Not every binary object is a formal record. A draft, customer upload, signed agreement, generated statement, investigator evidence and legal-hold item have different states. Model these states before defining storage tiers or user-interface labels.

`HB-CTRL-36 Privacy, Retention and Legal-Hold Enforcement` governs use, retention, disposal and holds. Privacy modelling should include purpose, access, sharing and retention, not only a `Confidential` label.

## Workflow and rules

`HB-APP-071 Enterprise Workflow Platform` coordinates reusable human tasks, queues, escalation and service-level tracking. It is a target shared platform supporting `HB-VS-01 Establish and Manage Relationship`, `HB-VS-02 Design and Manage Product`, `HB-VS-05 Provide and Manage Credit`, `HB-VS-08 Resolve Exception` and `HB-VS-10 Provide and Manage Trade Finance`.

A workflow owns its orchestration state within an approved process definition. The product application still owns the product agreement or transaction. A workflow should store references rather than uncontrolled copies, use idempotent task completion and make timeout, cancellation and compensation behaviour explicit.

`HB-APP-072 Enterprise Business Rules Platform` executes versioned deterministic rules suited to reuse. It should not become an anonymous owner of every policy decision. Each rule set needs a business owner, purpose, inputs, output, version, effective dates and evidence. Specialist decision engines such as `HB-APP-026 Credit Decision Management` remain separate when data, model governance and decision responsibility require it.

`HB-INT-093 Governed Rule Execution` provides managed access through `HB-APP-075 API Management Platform`. The gateway enforces service policies; it does not own the business rule or result.

## Case management

A case groups information and work needed to reach a governed outcome where the path may vary. `HB-APP-074 Enterprise Case Management` provides reusable case, task, evidence and disposition functions for non-specialist cases. `HB-INT-053 Service Case Exchange` is provided by `HB-APP-074` to `HB-APP-019`, while `HB-INT-060 Customer Service Workflow` is produced by `HB-APP-071` for `HB-APP-019`.

Specialist cases stay separate when their authority, secrecy, lifecycle or evidence differs. `HB-APP-017 Know Your Customer Case Management`, `HB-APP-044 Card Disputes and Chargebacks`, `HB-APP-067 Financial Crime Investigation Case Management`, `HB-APP-068 Internal Audit Management` and `HB-APP-069 Legal Matter and Obligation Management` are not redundant aliases for `HB-APP-074`.

A reusable case model can share common fields such as case identifier, type, status, priority, owner, subject, related records, tasks and evidence. Specialist extensions and access controls remain governed. A generic platform must not force a fraud disposition, audit opinion and complaint outcome into one uncontrolled status list.

## Shared platform selection

Use a shared platform when the need is genuinely common and the platform can preserve domain ownership. Keep a specialist application when one or more of these factors differ materially:

- the authoritative record and lifecycle;
- decision or control ownership;
- latency or availability needs;
- information classification and restricted access;
- jurisdiction or legal evidence requirements;
- specialist algorithms, models or network integration; or
- recovery and operational support boundary.

Reuse is valuable when it reduces repeated plumbing. It becomes harmful when domain behaviour moves into central scripts that no owner can explain. `Shared` means governed common capability, not `everyone can change it`.

## Information and integration

The main data domains are `HB-DATA-20 Customer Interaction and Communication`, `HB-DATA-06 Case, Document and Evidence`, `HB-DATA-19 Security, Identity and Access` and `HB-DATA-01 Party and Customer`. Each retains a different meaning.

Important interface examples include:

- `HB-INT-002 Mobile Customer Authentication`, `HB-INT-003 Branch Customer Authentication` and `HB-INT-004 Contact Centre Customer Authentication`;
- `HB-INT-007 Retail Entitlement Check` and `HB-INT-015 Payment Entitlement Decision`;
- `HB-INT-013 Consent Preference Change` and `HB-INT-014 Consent Evidence Archive`;
- `HB-INT-052 Customer Communication Request` and `HB-INT-094 Communication Delivery Event`;
- `HB-INT-053 Service Case Exchange`, `HB-INT-060 Customer Service Workflow` and `HB-INT-092 Workflow Document Service`; and
- `HB-INT-056 Partner API Publication` through the managed external boundary.

An interface model should name producer, consumer, direction, information, security classification, version and failure behaviour. A line labelled `integration` is insufficient.

## Worked trace: complaint and redress

`HB-SCN-18 Resolve a Customer Complaint and Redress Case` begins when a customer or representative submits a complaint. It ends with an authorised outcome, communication and any approved redress, supported by retained evidence.

1. `HB-APP-002`, `HB-APP-003` or `HB-APP-004` captures the interaction after appropriate identity and representative checks.
2. The current catalogue has no governed channel-to-`HB-APP-019 Customer Service Management` intake interface. The captured interaction therefore reaches customer service through a documented gap rather than an invented interface.
3. `HB-APP-019` consumes `HB-INT-053 Service Case Exchange`, an API provided by `HB-APP-074 Enterprise Case Management`, to create or update the reusable complaint case. The stable case reference follows later contacts.
4. `HB-APP-071 Enterprise Workflow Platform` produces `HB-INT-060 Customer Service Workflow` for `HB-APP-019` to receive and track reusable service tasks.
5. `HB-APP-071` consumes `HB-INT-092 Workflow Document Service`, an API provided by `HB-APP-070 Enterprise Document and Content Management`, to store or retrieve evidence with classification, access and retention metadata.
6. Product applications remain authoritative for the transaction or agreement under investigation.
7. An authorised complaint owner records the decision and any redress. Segregation applies where maker and approver must differ.
8. The catalogue has no case-to-correspondence instruction, so the authorised decision reaches `HB-APP-022 Statement and Correspondence Management` through another documented gap. `HB-APP-022` then produces `HB-INT-052 Customer Communication Request` for `HB-APP-073 Notification and Communications Hub`. `HB-APP-073` produces `HB-INT-094 Communication Delivery Event` for `HB-APP-004 Contact Centre Workbench`.
9. Closure requires decision evidence, fulfilled redress where applicable, communication outcome and retained records. An undelivered decision must enter a governed exception path.

The scenario uses shared services, but the shared services do not decide the complaint. It also demonstrates why customer, case, document and communication state must be linked without being merged.

### Worked trace: mobile address change

A mobile address change exposes a different governed boundary.

1. `HB-APP-008 Customer Identity and Access Management` provides `HB-INT-002 Mobile Customer Authentication` to `HB-APP-002 Retail Mobile Banking`.
2. The mobile channel captures the requested change, but the current interface catalogue has no governed mobile-to-party-master address-change command or API. The architecture must record this missing contract rather than misuse `HB-INT-021` in the opposite direction.
3. After the request has been authorised, validated and applied through the future governed contract, `HB-APP-015 Party Master and Customer Information` remains the party authority under `HB-SOR-01 Party Identity Authority`.
4. `HB-APP-015` then produces `HB-INT-021 Party Master Change Event` for `HB-APP-076 Enterprise Event Streaming Platform`. Consumers receive the governed fact; they do not use the event to approve the original change.
5. If customer correspondence is required, the current catalogue also needs a typed party-or-service-to-correspondence request. `HB-INT-052` cannot be reused unless `HB-APP-022` is genuinely the producer of the approved correspondence request.

The valid trace distinguishes authentication, request capture, party authority and downstream event publication. It also shows two precise catalogue gaps without reversing a registered interface.

## Accounting and settlement boundary

A complaint decision may require a refund, fee reversal, compensation or other redress. `HB-APP-074` can preserve the decision and approval, but it should not alter a product balance or General Ledger directly. The relevant product application must execute the authorised adjustment and finance must record its accounting effect.

The current catalogue has no complaint-redress accounting event or dedicated reconciliation. That is a shared-catalogue gap. A safe interim contract retains the case identifier, decision, amount, product record, legal entity, approver, execution outcome and finance reference. The case remains open or enters an exception state until fulfilment and accounting acknowledgement are observable.

## Security and trust boundaries

Each channel crosses a different trust boundary. Public internet, customer device, branch network, contact-centre workstation, partner connection and internal service identity require different threat and control analysis. The model should show authentication, authorisation, data classification, encryption boundary, audit event and sensitive-data handling.

`HB-APP-085 Security Operations Platform`, `HB-APP-089 Secrets and Cryptographic Key Management` and `HB-APP-011 Workforce Identity Governance` provide supporting control-plane capabilities. `HB-INT-096 Security-Relevant Observability Event` and `HB-INT-097 Cryptographic Audit Event` support monitoring. NIST Cybersecurity Framework (CSF) 2.0 can help organise outcomes across Govern, Identify, Protect, Detect, Respond and Recover, but the bank must select its own controls and applicability [NIST-CSF-2.0].

Do not put credentials, full customer documents or sensitive case text into general logs. Audit records should capture who performed which action, on what governed reference, when and with what outcome, while observing minimisation and access requirements.

## Resilience and operations

The important classifications include `HB-TECH-001 Customer Identity and Access Classification`, `HB-TECH-002 Digital and Partner Channel Classification`, `HB-TECH-003 Assisted Channel Classification`, `HB-TECH-006 Statement and Correspondence Classification`, `HB-TECH-024 Document, Workflow, Rules and Case Platform Classification`, `HB-TECH-025 Integration and External Connectivity Classification` and `HB-TECH-030 Backup, Recovery and Continuity Services Classification`.

`HB-CRIT-03 Authenticate and Authorise Customer Access` and `HB-CRIT-20 Deliver Material Customer Communications` express observable business outcomes. Recovery must consider identity, entitlement, case state, timers, document integrity, pending communications and duplicate tasks. After restoration, reconcile requests and outcomes rather than replaying every message blindly.

The Basel Committee's operational-resilience principles connect governance, dependency mapping, third parties, incident management, business continuity and resilient information and communication technology [BCBS-OPERATIONAL-RESILIENCE-2021]. Horizon Bank does not invent numerical impact tolerances, Recovery Time Objectives (RTOs) or Recovery Point Objectives (RPOs).

## BIAN alignment and limits

The Horizon Bank BIAN register does not yet contain governed mappings for these channel and shared-service responsibilities. BIAN Service Landscape 14.0 is the current announced release [BIAN-SERVICE-LANDSCAPE-14-PV45-48], but the chapter does not infer Service Domains from application names.

A future mapping must compare a complete responsibility with versioned BIAN artefacts. Even where a candidate exists, a BIAN Service Domain would not automatically equal a channel application, workflow engine, case platform, team or microservice.

## Current-to-target considerations

The channel and identity estate is largely current, while `HB-APP-071 Enterprise Workflow Platform`, `HB-APP-072 Enterprise Business Rules Platform` and `HB-APP-074 Enterprise Case Management` are proposed target applications. Their introduction should start with a small number of reusable patterns, explicit domain owners and measurable exit criteria.

Do not move all existing workflows and cases at once. First establish stable references, identity and entitlement contracts, document authority and operational monitoring. During coexistence, define which engine owns each process instance, how timers and tasks migrate, how duplicates are prevented and how in-flight work is reconciled. Specialist cases remain separate unless their authority and control needs genuinely converge.

## When these models should and should not be used

Use a journey map for experience across channels, a Business Process Model and Notation (BPMN) model for human work and exceptions, a sequence view for runtime interactions, a data-lifecycle model for records and retention, and a threat model for trust boundaries. Do not use a journey map as an authorisation design or a platform landscape as a case-state specification.

## Common mistakes

- Making the mobile application authoritative for every product it displays.
- Treating authentication, entitlement, mandate, consent and transaction approval as synonyms.
- Letting a notification hub invent business status.
- Storing the only copy of evidence inside a workflow task.
- Centralising specialist decisions in an ownerless rules platform.
- Forcing every specialist case into one generic lifecycle.
- Calling a platform shared while allowing uncontrolled tenant changes.
- Omitting assisted and failure paths from a digital journey.
- Logging credentials or sensitive case content for convenience.
- Claiming BIAN alignment from similar application names.

## Chapter summary

Channels and shared services provide interaction, coordination and evidence capabilities across the bank. Horizon Bank separates channel applications, identity, entitlement, consent, communications, content, workflow, rules and case management because each has a different question and authority. Shared platforms support product journeys without taking over product decisions. Security, accessibility, privacy and resilience are built into the relationships and lifecycles, not added as labels.

## Key takeaways

- A channel presents and initiates; product applications remain authoritative.
- Identity, entitlement, mandate, consent and transaction authorisation are distinct.
- Communications carry domain-owned meaning and have their own delivery lifecycle.
- Documents, workflows, rules and cases solve different problems.
- Shared platforms must preserve specialist ownership, access and evidence boundaries.
- Accessibility and security require testable criteria.
- Recovery includes pending work, timers, documents and communication outcomes.
- BIAN mappings require versioned verification and do not dictate deployment units.

## Practical exercise

A corporate customer reports a failed bulk payment through mobile messaging, later telephones the bank and uploads supporting evidence. Design the shared-service trace without moving payment authority into the case platform.

### Suggested answer criteria

A strong answer uses a channel such as `HB-APP-006` or `HB-APP-004`, verifies identity through `HB-APP-008` and mandate through `HB-APP-010`, creates a case in `HB-APP-074`, stores evidence in `HB-APP-070`, coordinates tasks with `HB-APP-071` and communicates through `HB-APP-073`. It links, rather than copies as authority, the payment record in `HB-APP-034 Payment Orchestration` or `HB-APP-037 Payment Investigations and Exceptions`. It includes access, duplicate-contact, delivery-failure and recovery behaviour.

## Review checklist

- [ ] Each channel has a stated audience, trust boundary and authority limit.
- [ ] Identity, entitlement, consent, mandate and approval are separate.
- [ ] Product truth remains in product applications.
- [ ] Communication request and delivery state are both modelled.
- [ ] Documents have version, classification, retention and integrity evidence.
- [ ] Workflow and rules have explicit business owners.
- [ ] Generic and specialist case boundaries are justified.
- [ ] Accessibility, privacy and security have testable outcomes.
- [ ] Recovery covers pending work and post-recovery reconciliation.
- [ ] No unverified BIAN equivalence is asserted.

## References and source notes

- [NIST-DIGITAL-IDENTITY-800-63-4]
- [W3C-WCAG-2.2]
- [NIST-CSF-2.0]
- [BCBS-OPERATIONAL-RESILIENCE-2021]
- [BIAN-SERVICE-LANDSCAPE-14-PV45-48]

## Deferred work

No diagram source is created in this pass. Horizon Bank still needs approved channel journey variants, accessibility conformance decisions, communications-policy rules, case taxonomies, specialist access models, platform tenant boundaries, delivery-provider inventory, verified BIAN candidates and owner-approved resilience objectives.
