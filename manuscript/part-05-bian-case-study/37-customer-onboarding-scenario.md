---
title: "Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing"
chapter: 37
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 37. Customer, Party, CRM, Sales, Onboarding, KYC and Customer Servicing

## Chapter purpose

Explain how a full-service bank establishes and maintains a governed relationship with a person or organisation. The chapter connects customer journeys to party identity, customer relationship management (CRM), sales, onboarding, Know Your Customer (KYC), customer due diligence, servicing, information authority, applications, controls and operations.

## Reader outcomes

By the end of this chapter, you should be able to:

- distinguish a party, prospect, customer, relationship and account;
- model onboarding as a long-running business process rather than a single screen or identity check;
- assign responsibilities across channels, customer relationship management, party data, onboarding and financial-crime applications;
- trace decisions, evidence, interfaces, controls and resilience needs through a customer lifecycle;
- explain why a Banking Industry Architecture Network (BIAN) mapping is not an application decomposition.

## Prerequisites and dependencies

- Chapter 33: Enterprise Business Architecture of Horizon Bank
- Chapter 34: Full Bank Application and Integration Landscape
- Chapter 35: Enterprise Information and Data Architecture
- Chapter 36: Technology, Security, Resilience and Operating Architecture

## Required models and artefacts

This chapter uses the governed Horizon Bank business-domain, capability, organisation, application, interface, data, system-of-record, control, reconciliation, resilience and scenario catalogues. Its domain records are `HB-DOM-010 Customer, Party, Sales and Service`, `HB-DOM-011 Party and Customer Management`, `HB-DOM-012 Customer Acquisition and Onboarding`, `HB-DOM-013 Sales and Relationship Management` and `HB-DOM-014 Customer Servicing and Exit`.

The capability trace uses `HB-CAP-010 Customer, Party, Sales and Service Management`, `HB-CAP-011 Party Identity Management`, `HB-CAP-012 Customer Relationship Management`, `HB-CAP-013 Customer Onboarding`, `HB-CAP-014 Customer Due-Diligence Coordination`, `HB-CAP-015 Prospect and Lead Management`, `HB-CAP-016 Sales Opportunity Management`, `HB-CAP-017 Relationship Planning`, `HB-CAP-018 Customer Servicing` and `HB-CAP-019 Complaint, Redress and Customer Exit Management`. These records relate to `HB-VS-01`, `HB-PROC-01` and `HB-SCN-01`.

The primary operating trace is to `HB-ORG-07 Customer, Sales, Channels and Service`. `HB-ORG-14 Compliance, Financial Crime and Conduct` provides independent oversight of customer due diligence and screening, while `HB-ORG-15 Banking Operations` performs authorised exceptions and fulfilment work. `HB-ORG-17 Data and Analytics` supports governed party-data ownership and quality. These organisational records identify responsibility; they do not imply that one team owns the whole relationship lifecycle.

No new diagram source is created in this drafting pass. Existing onboarding figures in earlier chapters may be reused during the later integration review; any new Chapter 37 figure requires a registered, author-approved specification first.

## Worked examples

The worked example follows a retail prospect who starts online, supplies identity evidence, is screened and risk assessed, becomes a customer, receives digital access and later requests a change of address. It is a Horizon Bank author model, not a statement of one country's legal procedure.

## Source requirements

The Financial Action Task Force (FATF) Recommendations provide the international customer due-diligence baseline used here. Exact evidence, thresholds, timing, privacy duties and reporting obligations depend on the legal entity and jurisdiction. [FATF-RECOMMENDATIONS-2025]

BIAN 14.0 is used only as a versioned reference vocabulary. Horizon Bank has not yet verified exact customer-domain Service Domain candidates in `bian-mapping-register.md`, so this chapter does not invent them. [BIAN-SERVICE-LANDSCAPE-14]

## Planned chapter structure

The sections move from customer outcome to process, information, applications, interactions, controls and operation.

## Start with the relationship, not the form

Customer onboarding is the controlled conversion of an interested party into a relationship the bank is willing and able to service. A completed form is only one input. The bank must know which real-world party is involved, why the relationship is sought, which products and legal entity are in scope, which checks and approvals apply, and what evidence supports the outcome.

The first modelling question is therefore: **what outcome must be established, for whom, and under whose authority?** Horizon Bank expresses that outcome through `HB-VS-01 Establish and Manage Relationship`. The corresponding process family, `HB-PROC-01 Acquire and Manage Customers`, includes establishment, review, service and exit. Product opening comes later. This prevents an architect from confusing customer approval with account activation.

### Party, prospect and customer are different concepts

A **party** is a person or organisation about which the bank records identity and relationships. A **prospect** is a party, or a not-yet-resolved candidate party, engaged in a possible sale. A **customer** is a party that has an established relationship with a bank legal entity. One party may have several roles, such as borrower, guarantor, beneficial owner, director or authorised signatory.

An account is not a customer. It is a product agreement or operational record linked to one or more parties in defined roles. This distinction matters when an organisation has subsidiaries, beneficial owners and signatories, or when an individual holds several products.

The authoritative concepts are grouped in `HB-DATA-01 Party and Customer`. Product, agreement, consent, mandate and entitlement concepts sit in `HB-DATA-02 Product and Agreement`. Documents, cases and decision evidence sit in `HB-DATA-06 Case, Document and Evidence`. Keeping these domains separate makes ownership and retention questions reviewable.

## Business objective and customer journey

The customer wants a predictable path with no unnecessary repetition. The bank wants a relationship that is correctly identified, permitted, supportable and traceable. Those interests overlap, but they are not identical.

The illustrative retail journey contains these stages:

1. Discover an appropriate proposition and start an application.
2. Capture contact details, purpose and consent.
3. Resolve whether the applicant is a new or existing party.
4. Collect and verify identity and relevant related-party evidence.
5. Perform customer due diligence, screening and risk classification.
6. Refer uncertainty or a potential match to an authorised reviewer.
7. Decide whether to establish, restrict, defer or decline the relationship.
8. Establish the governed party and customer relationship.
9. Create access credentials and applicable entitlements.
10. Hand off to the requested product-origination process.
11. Retain evidence and schedule event-driven or periodic review.

This sequence is not a universal legal checklist. It is a process architecture skeleton. Country policy supplies the detailed rules, while product origination supplies product-specific eligibility and contracting.

`HB-CAP-013 Customer Onboarding` coordinates the journey. It does not take over `HB-CAP-011 Party Identity Management`, `HB-CAP-014 Customer Due-Diligence Coordination`, `HB-CAP-024 Product Eligibility Management` or `HB-CAP-176 Identity and Access Management`. A capability cross-map makes these contributions visible without pretending they are consecutive tasks.

## CRM, sales and relationship planning

Customer relationship management (CRM) begins before onboarding and continues after it. Its purpose is to manage commercial and service context, not to create a second identity authority. `HB-CAP-015 Prospect and Lead Management` captures and qualifies interest. `HB-CAP-016 Sales Opportunity Management` develops a specific need or offer through an accountable sales lifecycle. `HB-CAP-017 Relationship Planning` coordinates goals, coverage, interactions and holdings for an established or managed relationship. `HB-CAP-012 Customer Relationship Management` preserves the broader customer status and relationship history.

These concepts need separate states. An enquiry can become a qualified prospect without becoming a customer. A prospect can have several opportunities, each of which can be progressed, withdrawn, lost or won. Winning an opportunity does not itself approve the customer or activate a product. Onboarding establishes an acceptable relationship with a legal entity; product origination subsequently establishes a governed agreement. Conversely, an existing customer can start a new opportunity without repeating every relationship-establishment step, although changed circumstances may trigger due-diligence review.

At Horizon Bank, `HB-APP-012 Customer Relationship Management` is authoritative for relationship and opportunity history, but not for legal identity. `HB-APP-015 Party Master and Customer Information` remains the qualified party identity authority under `HB-SOR-01`. The interaction boundary is explicit:

```text
HB-APP-001 --HB-INT-001--> HB-APP-012  interested-party enquiry and consent reference
HB-APP-013 --HB-INT-017--> HB-APP-012  approved product and distribution eligibility
HB-APP-012 --HB-INT-009--> HB-APP-004  customer, relationship and interaction context
```

For managed small and medium-sized enterprise (SME), corporate or wealth relationships, `HB-APP-005 Relationship Manager Workbench` supports planning, proposals and service requests. It is a governed workspace, not a replacement for CRM, party authority, credit decisioning or product records. A relationship plan should identify the legal entities and parties covered, accountable coverage team, customer goals, agreed actions, product holdings, open opportunities, service issues and review dates. It should not turn an employee's notes into an unqualified bank-wide fact.

Useful CRM measures include source-to-qualified-lead conversion, opportunity ageing, lost or withdrawn reasons, overdue relationship actions and duplicate-prospect resolution. Each measure needs a defined population and owner. Sales performance pressure must not weaken `HB-CTRL-01 Customer Due-Diligence Review`, consent handling or the separation between commercial recommendation and authorised approval.

## Customer due diligence and KYC

KYC is commonly used as a broad label for understanding and controlling customer risk. When referring to the FATF standard, this chapter uses **customer due diligence (CDD)**. CDD includes identifying and verifying the customer and beneficial owner, understanding the purpose and intended nature of the relationship, and conducting ongoing due diligence. Record keeping is also an explicit part of the international baseline. [FATF-RECOMMENDATIONS-2025]

An architect should separate four concerns:

| Concern | Architecture question | Horizon Bank responsibility |
|---|---|---|
| Evidence capture | What has the applicant supplied, and through which trusted route? | `HB-APP-016`, `HB-APP-070` |
| Identity resolution | Does this evidence refer to an existing or new party? | `HB-APP-015`, `HB-CTRL-05` |
| Independent checks | What screening, verification and risk work is required? | `HB-APP-017`, `HB-APP-018`, `HB-CAP-133`, `HB-CAP-134` |
| Relationship decision | Who may approve, restrict, refer or decline? | `HB-CTRL-01`, accountable business and compliance roles |

This separation prevents the onboarding orchestrator from becoming an uncontrolled master-data system or a hidden financial-crime decision engine. It also makes exception ownership explicit.

## Model the process and decisions separately

A Business Process Model and Notation (BPMN) collaboration can show work between the applicant, channel, onboarding operations and specialist reviewers. The process model answers **what happens next, including waits and exceptions?** It should include incomplete evidence, timeout, possible duplicate, screening referral, manual review, abandonment and declined outcomes, not only the happy path.

A Decision Model and Notation (DMN) model can support repeatable classifications, such as which due-diligence route is required from customer type, geography, product, ownership complexity and other approved inputs. The decision model answers **how is a repeatable result derived?** It should retain the rule or model version, inputs, result, reasons and override. It must not hide the subsequent investigation process inside a large decision table.

Horizon Bank's controlled application boundary reflects this distinction. `HB-APP-071 Enterprise Workflow Platform` can run reusable human tasks, and `HB-APP-072 Enterprise Business Rules Platform` can execute controlled deterministic rules. Specialist ownership remains with `HB-APP-017 Know Your Customer Case Management` and the appropriate reviewer.

## Application responsibilities

The full journey uses several logical applications because their responsibilities, owners and authority differ.

| Application | Responsibility in this chapter |
|---|---|
| `HB-APP-001 Public Banking Web` | Public discovery and application entry |
| `HB-APP-002 Retail Mobile Banking` | Authenticated continuation and later servicing |
| `HB-APP-005 Relationship Manager Workbench` | Managed-client relationship planning, proposals and service requests |
| `HB-APP-008 Customer Identity and Access Management` | Customer authentication and session control |
| `HB-APP-009 Consent and Privacy Preference Service` | Purpose-specific consent and preference state |
| `HB-APP-012 Customer Relationship Management` | Prospect, opportunity and interaction history |
| `HB-APP-015 Party Master and Customer Information` | Resolved party identity and governed customer attributes |
| `HB-APP-016 Customer Onboarding Orchestrator` | End-to-end onboarding coordination |
| `HB-APP-017 Know Your Customer Case Management` | CDD assessment, reviews, evidence and exceptions |
| `HB-APP-018 Name and Sanctions Screening` | Screening requests, match candidates and dispositions |
| `HB-APP-019 Customer Service Management` | Enquiries, complaints and service-request tracking |
| `HB-APP-070 Enterprise Document and Content Management` | Governed evidence and retention metadata |
| `HB-APP-073 Notification and Communications Hub` | Approved notices and delivery outcomes |

This is a logical application view, not a product procurement list. One package could implement several responsibilities, or one logical responsibility could be realised by several deployable services. The architecture still preserves the distinctions so ownership, data authority and change impact can be reviewed.

## Interaction path and interface catalogue

An interaction model answers **which responsibility exchanges what information, in which direction and with what failure behaviour?** A concise onboarding path is:

```text
HB-APP-001 --HB-INT-001--> HB-APP-012
HB-APP-016 --HB-INT-020--> HB-APP-015
HB-APP-015 --HB-INT-021--> HB-APP-076
HB-APP-018 --HB-INT-022--> HB-APP-017
HB-APP-071 --HB-INT-057--> HB-APP-016
HB-APP-017 --HB-INT-058--> HB-APP-067, when specialist investigation is required
HB-APP-073 --HB-INT-094--> HB-APP-004
```

The arrow does not mean each step succeeds immediately. For `HB-INT-020 Onboarded Party Establishment`, the design needs idempotency, a correlation identifier and an explicit response if the party already exists. `HB-INT-022 Screening Decision for Due Diligence` must distinguish a screening result from the authorised disposition of a potential match. As registered, `HB-INT-057 Onboarding Workflow Handoff` is produced by `HB-APP-071 Enterprise Workflow Platform` for `HB-APP-016 Customer Onboarding Orchestrator`; it needs task ownership, deadline, escalation and restart behaviour. `HB-INT-094 Communication Delivery Event` is produced by `HB-APP-073 Notification and Communications Hub` for `HB-APP-004 Contact Centre Workbench`. Other service-channel consumers would require their own governed interface records.

A Unified Modeling Language (UML) sequence diagram is useful for one interaction path, but it cannot replace the BPMN model of human work, the data model of party relationships or the control catalogue.

## Information authority and lifecycle

`HB-SOR-01 Party Identity Authority` assigns qualified authority for verified identity and relationship attributes to the responsibility represented by `HB-APP-015`. The qualification matters. The onboarding application may hold an application-in-progress copy. The KYC case application may be authoritative for a due-diligence decision and evidence. The customer identity platform may be authoritative for credentials. None is automatically authoritative for every customer attribute.

The minimum conceptual relationships are:

```text
Party
  has Party Role
  participates in Relationship
  may be represented by Identifier
  may control or beneficially own another Party

Customer Relationship
  belongs to a Legal Entity
  has Due-Diligence Profile
  may hold Product Agreement
  grants Mandate or Entitlement
```

Effective dates and provenance are essential. A corrected legal name must not erase which value supported an earlier decision. A merged duplicate must retain an auditable link and a controlled way to reverse an incorrect merge. `HB-REC-001 Party Identity and Due-Diligence Alignment` compares party and due-diligence state, while `HB-REC-002 Customer-to-Account Relationship` tests that party roles and account relationships agree.

## Security, privacy and control

Authentication proves an identity to an appropriate level of confidence. Access authorisation decides which protected action that identity may perform. Business approval decides whether the bank accepts a relationship or transaction. These are different decisions.

The main controlled relationships are:

- `HB-CTRL-01 Customer Due-Diligence Review`, which prevents activation without the approved risk-based path and evidence;
- `HB-CTRL-05 Party Identity Resolution and Duplicate Review`, which governs possible matches, merges and separations;
- `HB-CTRL-06 Consent, Mandate and Entitlement Enforcement`, which checks action-specific authority;
- `HB-CTRL-36 Privacy, Retention and Legal-Hold Enforcement`, which governs purpose, access, retention and disposal.

Sensitive evidence should not be copied into logs, analytics or agent notes by default. Access should follow purpose and role. A case must record who decided, which inputs and policy version were used, what exception occurred and what evidence was retained. The control record defines intent and expected evidence; it does not prove the control operated effectively.

## Customer servicing and ongoing review

Onboarding does not finish the relationship lifecycle. `HB-CAP-018 Customer Servicing` and `HB-DOM-014 Customer Servicing and Exit` cover enquiries, changes, complaints, reviews and closure. A change of address, ownership or authorised signatory can affect party data, CDD, product agreements, communications and tax or reporting obligations.

A good servicing design uses the party authority rather than allowing every channel to maintain its own customer record. The contact-centre workbench obtains relationship context through `HB-INT-009 Contact Centre Relationship View`; branch servicing uses `HB-INT-008 Branch Customer View`. Service work is tracked in `HB-APP-019`, and reusable tasks can use `HB-INT-060 Customer Service Workflow`.

Ongoing review should be event-aware. A material relationship change may trigger reassessment before the next scheduled review. Exact triggers and timing remain a jurisdiction and policy decision, not an architecture assumption.

## Resilience and operating ownership

The technology classification `HB-TECH-004 Party, CRM, Onboarding and KYC Classification` treats the customer foundation as a business-record and workflow service. Recovery must preserve verified identity, relationship state, due-diligence status, evidence and resumable work. Restarting a web form is not enough if specialist review state has been lost.

`HB-CRIT-03 Authenticate and Authorise Customer Access` protects customer access as an end-to-end outcome. `HB-CRIT-16 Perform Mandatory Screening and Financial-Crime Intervention` protects screening and case decisions. A degraded mode may queue work or restrict higher-risk activity, but it must not silently bypass a mandatory control.

Operational measures should be defined without fictional targets. Useful candidates include completed and abandoned applications by stage, unresolved duplicate candidates, referred screening cases, aged work queues, decision reversals, customer-data-quality exceptions and failed notification deliveries. Each measure needs a definition, owner, population and reason for use.

## BIAN candidate mapping

BIAN helps classify banking responsibilities and establish a shared semantic reference. It does not decide Horizon Bank's application, workflow, database or team boundaries. The Service Landscape is a reference organisation of Service Domains, and release 14.0 changed some definitions and operations. [BIAN-SERVICE-LANDSCAPE-14]

The current `HB-BIAN` register has no verified customer and party mapping record. Therefore the architecture trace remains:

```text
customer outcome and value stream
-> Horizon Bank capabilities and process
-> logical application and information responsibilities
-> candidate BIAN responsibilities, pending version-14 verification
```

An eventual mapping must name the exact BIAN 14.0 objects, cite the source, state confidence and explain many-to-many relationships. It must not relabel every application as a Service Domain.

## Current, transition and target considerations

The author-model current state permits duplicate party data and point-to-point integration (`HB-ASM-02`). The target direction uses governed party data and managed interfaces (`HB-ASM-03`). A safe transition does not attempt a single uncontrolled customer-data merge.

A practical sequence is:

1. establish ownership and common identifiers;
2. publish qualified party views without changing authority;
3. add duplicate detection and stewardship queues;
4. move selected attributes to `HB-SOR-01` authority by legal entity and effective date;
5. reroute onboarding and servicing through managed interfaces;
6. reconcile old and new records before retiring a source;
7. retain decision evidence and rollback or correction paths.

The transition view should show coexistence, migration batches, exception capacity and exit criteria. A target-state box without those concerns is not a migration design.

## Common mistakes

- Treating a party, customer, user identity and account holder as the same record.
- Calling identity-document upload complete KYC.
- Putting party authority, screening decisions and workflow state in one undocumented database.
- Drawing only the happy path and omitting incomplete, duplicate, referred and declined cases.
- Treating a screening match as a confirmed prohibited party.
- Copying sensitive evidence into every consuming application.
- Assuming a customer approved by one legal entity is automatically approved for every entity and product.
- Mapping one BIAN Service Domain to one application or team without analysis.

## Chapter summary

Customer architecture begins with a governed relationship, not a form. Capabilities describe the abilities the bank needs, processes describe coordinated work, applications allocate logical responsibilities, data models preserve meaning and controls make decisions reviewable. Horizon Bank separates party authority, onboarding orchestration, KYC casework, screening, access identity and customer servicing because their ownership and evidence differ.

## Completion checklist

- [x] Party, prospect, customer, relationship and account are distinguished.
- [x] Lead, opportunity and relationship-planning responsibilities are separated from onboarding and identity authority.
- [x] The journey includes decisions, exceptions, servicing and ongoing review.
- [x] Applications, interfaces, data authority, controls, reconciliation and resilience use governed identifiers.
- [x] BIAN is treated as a candidate reference mapping, not a deployable decomposition.
- [x] Jurisdiction-specific obligations and numerical targets remain explicit gaps.
- [x] Diagram production is deferred under the approved specification-first workflow.

## Key takeaways

- Onboarding establishes a governed relationship; product opening fulfils a separate agreement.
- Party identity, customer status, credentials and due-diligence decisions have different authorities.
- BPMN, DMN, information and interaction models answer different questions.
- Exceptions and retained evidence are part of the architecture, not operational afterthoughts.
- Customer servicing can trigger new due-diligence and data-governance work.
- BIAN candidates must be versioned and justified independently of application boundaries.

## Practical exercise

Model an organisation applying for a corporate current account. Include the organisation, two directors, a beneficial owner and an authorised signatory. Produce:

1. a conceptual party-role model;
2. a BPMN-style stage list including duplicate and screening referral paths;
3. an application interaction list using governed Horizon Bank IDs;
4. an authority table stating which application is authoritative for identity, CDD decision, credentials and product agreement;
5. evidence expected for `HB-CTRL-01` and `HB-CTRL-05`.

A strong answer keeps the parties and roles distinct, separates onboarding from product opening, includes manual case ownership and does not invent a verified BIAN mapping.

## Review checklist

- [ ] Does every model state its question, audience, scope and architecture state?
- [ ] Are party roles and legal-entity relationships explicit?
- [ ] Are CDD, screening, identity resolution and business approval separated?
- [ ] Are incomplete, duplicate, referred, declined and abandoned outcomes represented?
- [ ] Are authoritative data, working copies and evidence stores distinguished?
- [ ] Are interface direction, information, security and failure behaviour stated?
- [ ] Are controls linked to owners and expected evidence?
- [ ] Are jurisdiction assumptions and unresolved BIAN mappings visible?

## References and further reading

- [FATF-RECOMMENDATIONS-2025](../../research/banking/part-v-37-40/fatf-recommendations-2025.md)
- [BIAN-SERVICE-LANDSCAPE-14](../../research/bian/bian-service-landscape-14.0.md)

## Drafting notes

- A customer and party BIAN mapping record remains a shared-catalogue request.
- Detailed jurisdiction rules, evidence schedules and quantitative service targets remain deliberately open.
