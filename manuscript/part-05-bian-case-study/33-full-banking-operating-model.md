---
title: "Enterprise Business Architecture of Horizon Bank"
chapter: 33
part: "part-05-bian-case-study"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-13"
---

# 33. Enterprise Business Architecture of Horizon Bank

## Chapter purpose

Establish the governed business architecture baseline that later domain chapters will refine.

## Reader outcomes

By the end of this chapter, the reader should be able to distinguish stakeholder outcomes, value streams, capabilities, processes, products and organisation; navigate Horizon Bank's business coverage; and explain how ownership and candidate BIAN mappings are recorded.

## Prerequisites and dependencies

- Chapter 32: How a Full-Service Bank Works

## Required models and artefacts

- Controlled value-stream, capability, process, product, organisation and ownership catalogues

## Worked examples

- Horizon Bank transaction execution and customer-management architecture threads

## Source requirements

- Use official business-architecture and BIAN sources; identify Horizon Bank taxonomy as an author model.

## Planned chapter structure

The following sections establish the enterprise business architecture before domain drill-downs.

## Scope and modelling levels

This chapter covers the whole bank at catalogue level. It does not attempt to show every procedure on one diagram. Enterprise views establish coverage; domain chapters provide readable detail.

Four concepts must remain separate:

- a **value stream** describes how value progresses towards a stakeholder outcome;
- a **capability** describes an ability the bank needs;
- a **process** describes ordered work triggered to produce an outcome;
- an **organisation element** assigns people and accountability.

A capability may support several processes. A process may use several capabilities. Neither relationship proves a BIAN or application boundary.

## Stakeholder outcomes

| ID | Stakeholder | Desired outcome |
|---|---|---|
| OUT-01 | Customer | Access suitable, reliable and understandable financial services |
| OUT-02 | Business customer | Control cash, financing and risk across authorised users and entities |
| OUT-03 | Board and shareholders | Maintain a sustainable, controlled and transparent bank |
| OUT-04 | Regulator and central bank | Receive reliable evidence that obligations and risks are managed |
| OUT-05 | Employee | Perform accountable work with appropriate information and tools |
| OUT-06 | Market and payment participants | Exchange obligations accurately and on time |

These are Horizon Bank modelling assumptions, not regulatory definitions.

## Value-stream portfolio

Horizon Bank uses the following Level 0 value streams:

| ID | Value stream | Starts with | Ends with |
|---|---|---|---|
| VS-01 | Establish and manage a customer relationship | Customer or bank interest | Relationship established, serviced or exited |
| VS-02 | Design and manage a product | Identified need | Product retired with obligations resolved |
| VS-03 | Acquire and service an account or facility | Customer need | Agreement closed or transferred |
| VS-04 | Execute and settle a transaction | Valid instruction or event | Transaction settled, posted and communicated |
| VS-05 | Provide and manage credit | Financing need | Exposure repaid, restructured or recovered |
| VS-06 | Safeguard and service assets | Asset received or acquired | Asset transferred, realised or returned |
| VS-07 | Manage financial position and resources | Position or forecast changes | Funding, liquidity, capital and risk within decisions |
| VS-08 | Detect, decide and resolve an exception | Alert, failure, dispute or complaint | Resolved case with evidence and learning |
| VS-09 | Record, reconcile and report | Business or accounting event | Approved internal or external report |

## Level 1 capability map

The enterprise capability map groups abilities without implying departments or applications.

| Category | Level 1 capabilities |
|---|---|
| Direction | Strategy Management; Governance; Portfolio Management; Product Management; Pricing Management |
| Customer | Party Management; Customer Onboarding; Relationship Management; Sales Management; Customer Servicing |
| Channels | Digital Servicing; Branch Servicing; Contact Centre Servicing; Partner Channel Management; Communication Management |
| Deposits | Account Opening; Deposit Processing; Account Servicing; Interest and Fee Management; Statement Management |
| Credit | Credit Assessment; Lending; Limit Management; Collateral Management; Collections and Recovery |
| Payments | Payment Initiation; Payment Execution; Clearing and Settlement; Correspondent Banking; Payment Investigation |
| Cards | Card Issuing; Card Authorisation; Card Clearing; Dispute Management; Merchant Acquiring |
| Corporate and trade | Cash Management; Trade Finance; Corporate Lending; Mandate Management |
| Wealth and securities | Advice; Portfolio Management; Order Management; Custody; Asset Servicing |
| Treasury | Funding; Liquidity Management; Asset and Liability Management; Markets; Capital Management |
| Finance | Accounting; Reconciliation; Financial Control; Tax; Management and Regulatory Reporting |
| Risk and assurance | Enterprise Risk; Financial Crime; Fraud Management; Compliance; Legal; Internal Audit |
| Shared enterprise | Data Governance; Identity and Access; Document and Case Management; Technology Operations; Supplier Management; People Management |

Level 2 decomposition belongs in the controlled catalogue. A child capability is counted within its parent, while a contributing peer remains independently scoped.

## Process architecture

Horizon Bank's Level 0 process groups are:

1. Direct and govern the bank.
2. Understand markets and manage products.
3. Acquire and manage customers.
4. Originate and service products.
5. Execute, clear and settle transactions.
6. Manage positions, funding, liquidity and capital.
7. Manage risk, compliance and assurance.
8. Record, reconcile and report.
9. Operate technology and enterprise services.
10. Manage change, incidents and resilience.

Each Level 1 process record needs an identifier, trigger, outcome, owner, participants, input and output information, controls, exceptions, supporting capabilities, applications, candidate BIAN mappings and source.

For example, `Acquire and manage customers` decomposes into prospect management, due diligence, relationship establishment, entitlement setup, periodic review, servicing and exit. A Level 3 onboarding process may use BPMN to show document repair, screening referral and rejection. That behaviour does not belong on the Level 0 landscape.

## Products, services and operating-model variation

The product catalogue records product family, customer segment, legal entity, lifecycle, owner, pricing authority, processor, authoritative agreement data, accounting treatment and controls. A current account sold to a retail customer and a corporate operating account may share deposit-processing capabilities while differing in mandates, channels, fees and servicing.

Operating models may vary by segment, geography and legal entity. Group functions can provide standards and platforms; country entities can retain contractual and regulatory accountability; shared services can perform work; external providers can supply services. Every variation needs an explicit rationale and retained owner.

## Organisation and decision rights

Important owners include:

- **capability owner:** maintains the ability and improvement roadmap;
- **process owner:** owns end-to-end performance and controls;
- **product owner:** owns proposition, terms and lifecycle;
- **data owner:** is accountable for meaning, access, quality and use;
- **control owner:** ensures a control is designed, operated and evidenced;
- **application service owner:** owns service performance, support and lifecycle.

One person may hold several roles, but the responsibilities should not be collapsed in the model.

## Capability-to-process and BIAN relationships

A capability-to-process matrix exposes missing support and unnecessary duplication. Candidate BIAN responsibilities are then mapped to the capability or process responsibility with a qualified many-to-many relationship. BIAN does not replace the process owner or capability owner.

Example:

| Capability | Process | Candidate BIAN mapping | Application | Status |
|---|---|---|---|---|
| Payment Initiation | Accept payment instruction | Requires 14.0 verification | Payments Platform | Proposed |
| Financial Crime Screening | Screen payment | Requires 14.0 verification | Financial Crime Platform | Proposed |
| Accounting | Post financial consequence | Requires 14.0 verification | General Ledger family, to catalogue | Proposed |

The explicit `Requires 14.0 verification` value is safer than an invented name.

## Maturity and pain-point heat maps

Heat maps are decision aids, not facts without evidence. Horizon Bank uses a one-to-five illustrative score for business criticality, current effectiveness and change urgency. Every score needs a date, owner, evidence and comment. Colour is never the only carrier of meaning.

The initial hypothesis is that party data, payment repair, reconciliation, data governance and event governance need improvement. This remains a hypothesis until catalogue evidence is reviewed.

## Enterprise controls and measures

Business architecture connects outcomes and processes to controls and measures. Useful measures include service completion, failure and repair rates, time to decision, manual intervention, reconciliation breaks, customer complaints and control exceptions. Measures must state population, calculation, owner, frequency and decision use.

## Common mistakes

- Calling a department, process step or application a capability.
- Treating a value-stream stage as a detailed process.
- Building separate maps with inconsistent names and no identifiers.
- Assigning maturity colours without evidence or date.
- Mapping BIAN names before defining the local responsibility.

## Key takeaways

- Enterprise maps establish coverage; drill-downs establish readability.
- Value streams, capabilities, processes, products and organisation answer different questions.
- Ownership is part of architecture, not an administrative afterthought.
- BIAN mappings are qualified references and need versioned evidence.
- Controls and measures must connect to real outcomes and processes.

## Practical exercise

Choose `Execute and settle a transaction`. Identify three supporting capabilities, two Level 1 processes, two owners and one control. Explain why none of these elements is automatically a Service Domain or application.

## Review checklist

- [x] Whole-bank value streams, Level 1 capabilities and Level 0 processes are represented.
- [x] Ownership roles and operating-model variations are explicit.
- [x] Candidate BIAN mappings are not asserted without verification.
- [ ] Complete Level 2 catalogues and matrices remain Phase 1 controlled-artefact work.
- [ ] Figure specifications require author approval before source creation.

## Drafting notes

- Complete Level 2 catalogues, capability-to-process matrix and explicit heat-map evidence before review.
