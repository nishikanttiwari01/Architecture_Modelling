---
title: "Integrated End-to-End Scenarios and Practitioner Reference"
chapter: 56
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 56. Integrated End-to-End Scenarios and Practitioner Reference

## Chapter purpose

An end-to-end scenario connects a business trigger to an observable outcome across responsibilities, applications, information, interfaces, financial consequences, controls and operations. It prevents each specialist view from appearing complete while the customer or bank outcome falls through the gaps.

This final Part V chapter answers: **How does a practitioner assemble and review the minimum coherent model set for a full banking scenario?** It consolidates the Horizon Bank method, worked traces and reusable templates. It is not a substitute for the governed catalogues or for the technique guidance in earlier chapters.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- define an end-to-end scenario with a bounded trigger and outcome;
- trace a scenario across all governed architecture dimensions;
- select complementary ArchiMate-informed, Business Process Model and Notation (BPMN), C4, Unified Modeling Language (UML) and data views;
- assess a Banking Industry Architecture Network (BIAN) candidate without turning it into an implementation boundary;
- use practical templates for scenario, application and transition decisions; and
- review integrated scenarios for gaps, contradictions and false precision.

## Prerequisites and dependencies

This chapter draws on the whole of Part V, especially Chapters 37 to 48 for banking domains, Chapter 49 for BIAN traceability, Chapters 50 to 52 for implementation and operations, and Chapters 53 to 55 for migration, governance and quality audit.

## Required models and artefacts

- governed scenario record;
- scope and responsibility map;
- process or collaboration view where human work matters;
- runtime interaction view where ordering matters;
- information, authority and lineage view;
- accounting and reconciliation trace where financial state changes;
- control and critical-operation trace;
- transition view where current and target states differ; and
- coverage row plus explicit gaps.

## Worked examples

Four scenario patterns are used:

- relationship to deposit and payment, combining `HB-SCN-01`, `HB-SCN-04` and `HB-SCN-09`;
- corporate trade finance, using `HB-SCN-03`;
- investment and custody, combining `HB-SCN-13` and `HB-SCN-14`; and
- financial close and recovery, using `HB-SCN-16` and `HB-SCN-19`.

All are Horizon Bank author models. They deliberately avoid country-specific law, vendors, volumes and unapproved quantitative service targets.

## Source requirements

BIAN Service Landscape 14.0 is the version basis for the candidate mapping register [BIAN-SERVICE-LANDSCAPE-14]. Exact BIAN objects remain unverified where the register says so. Basel Committee on Banking Supervision (BCBS) operational-resilience guidance supports critical-operation and dependency thinking [BCBS-OPERATIONAL-RESILIENCE-2021]. BCBS 239 supports governed data, lineage, reconciliation and reporting concerns [BCBS-239]. Scenario composition and notation selection are author recommendations.

## The integrated scenario contract

A scenario is complete enough to review when it answers these questions:

| Dimension | Required question |
|---|---|
| Trigger and outcome | What starts the scenario, and what observable state ends it? |
| Scope | Which business line, legal entity, jurisdiction, segment and product are in scope? |
| Business responsibility | Which domain, capability, value stream, process and organisation own the work? |
| Applications | Which logical applications decide, record, coordinate or present the outcome? |
| Information | Which data domains are used and which sources are authoritative by purpose and stage? |
| Interaction | Which APIs, commands, events, messages, files, batches, workflows and external networks are used? |
| Financial integrity | Which accounting events arise, and what proves books and operational state agree? |
| Control | Which preventive, detective and corrective controls apply? |
| Operations | Which critical operations, resilience classifications and support responsibilities matter? |
| Reference alignment | Which BIAN candidates are relevant, with what source, confidence and verification status? |
| Change | What differs across current, transition and target states? |
| Evidence and gaps | What proves the claims, and what remains unresolved? |

The contract is intentionally broader than a happy-path sequence. A successful application programming interface (API) response may be one interaction result while clearing, settlement, accounting or customer communication remains incomplete.

## Hierarchy cheat sheet

The following concepts answer different questions and should not be collapsed:

| Concept | Plain-language question | Horizon Bank example |
|---|---|---|
| Business domain | Where does a body of business knowledge and responsibility belong? | `HB-DOM-050 Payments` |
| Capability | What must the bank be able to do? | `HB-CAP-054 Payment Settlement` |
| Value stream | How is stakeholder value advanced through major stages? | `HB-VS-04 Execute and Settle Transaction` |
| Process | In what ordered work is an outcome produced? | `HB-PROC-04 Execute and Settle Payments` |
| Product | What governed proposition or service is offered? | `HB-PRD-07 Payment and Cash Management` |
| Scenario | Which participants interact for one trigger and outcome? | `HB-SCN-09 Execute an Immediate Domestic Payment` |
| BIAN Service Domain candidate | Which reference responsibility may align? | `HB-BIAN-02 Payment Responsibility Candidate` |
| Logical application | Which application responsibility supports implementation? | `HB-APP-035 Payment Routing and Clearing` |
| Software service | Which executable behaviour is exposed behind a contract? | A later design decision, not implied by the application or BIAN record |
| Team | Who builds or operates a chosen boundary? | An operating-model decision, not a synonym for any row above |

Many-to-many relationships are normal. One application can support several capabilities, and one capability can require several applications. The mapping needs a rationale rather than forced symmetry.

## Choose views by question

### BIAN and an ArchiMate-informed enterprise view

Use BIAN to compare logical banking responsibilities and use an ArchiMate-informed view to relate motivation, capabilities, processes, applications and technology. Do not claim formal ArchiMate relationships unless they have been checked against the applicable specification source. Use a simple labelled relationship view when that is enough.

### BIAN and BPMN

Use BPMN when human work, decisions, messages, exceptions, timers and responsibility lanes matter. A BIAN Business Scenario and a BPMN process are complements: the first helps discuss participating Service Domains, while the second can show operational flow. Do not draw BIAN Service Domains as BPMN tasks by default.

### BIAN and C4

Use C4 to describe people, software systems, runnable containers and components. Map BIAN candidates to responsibilities served by C4 elements, not automatically to one C4 container. A container is a separately runnable or deployable unit, not a synonym for a business capability.

### BIAN and UML

Use UML sequence diagrams for runtime order, state machines for meaningful entity lifecycles, component diagrams for structural dependencies and class diagrams for selected domain or software structure. Do not put the entire bank on one UML diagram.

### BIAN and data views

Use conceptual models for shared meaning, logical models for governed entities and relationships, and physical models for an implementation. Add data flow and lineage when movement and transformation matter. The BIAN Business Object Model is a semantic reference, not a ready-made Horizon Bank database.

## Scenario pattern 1: relationship to account to payment

This pattern crosses three governed scenarios.

1. `HB-SCN-01 Establish Retail Customer Relationship` establishes party and due-diligence state through `HB-APP-015 Party Master and Customer Information`, `HB-APP-016 Customer Onboarding Orchestrator`, `HB-APP-017 Know Your Customer Case Management` and `HB-APP-018 Name and Sanctions Screening`.
2. `HB-SCN-04 Open and Fund a Transaction Account` uses `HB-PRD-02 Transaction Account` and `HB-APP-020 Deposit Account Processing`, with authority in `HB-SOR-02 Deposit Account Authority`.
3. `HB-SCN-09 Execute an Immediate Domestic Payment` uses `HB-APP-033 Payment Initiation Service`, `HB-APP-034 Payment Orchestration` and `HB-APP-035 Payment Routing and Clearing`, then exchanges through `HB-INT-064 Immediate Payment Exchange` and `HB-EXT-003 Immediate Payment Network`.

The joined information crosses `HB-DATA-01 Party and Customer`, `HB-DATA-02 Product and Agreement`, `HB-DATA-03 Account and Transaction` and `HB-DATA-08 Payments, Clearing and Settlement`. Authority changes by purpose: the party authority is `HB-SOR-01`, the account authority is `HB-SOR-02`, and payment processing uses `HB-SOR-08`.

Financial integrity requires `HB-ACC-05 Deposit Principal Received` during funding and `HB-ACC-14 Payment Settlement Recognised` during payment. `HB-REC-002`, `HB-REC-003`, `HB-REC-012`, `HB-REC-013` and `HB-REC-014` test different alignments. None can be replaced by one generic “reconciled” flag.

The key review question is whether identity, account and payment lifecycle states remain linked without making the onboarding orchestrator or operational data store authoritative for every purpose.

## Scenario pattern 2: corporate trade finance

`HB-SCN-03 Issue and Settle Trade Instrument` begins with a corporate request and ends when the instrument, contingent exposure, financial settlement and evidence are resolved. The scope is `HB-PRD-09 Trade Finance` and `HB-VS-10 Provide and Manage Trade Finance`, supported by `HB-PROC-06 Originate and Service Trade Finance`.

`HB-APP-048 Trade Finance Processing` holds the instrument responsibility, while `HB-APP-025 Business and Corporate Credit Origination`, `HB-APP-029 Limit and Covenant Management` and `HB-APP-030 Credit Exposure Aggregation` contribute credit and exposure decisions. Payments and settlement remain separate responsibilities. This boundary prevents trade finance from being misclassified as deposit acquisition.

The runtime may include `HB-INT-047 Trade Finance Service`, `HB-INT-048 Trade Contingent Exposure Event`, `HB-INT-073 Trade Finance Network Message` and `HB-EXT-016 Trade Finance Messaging Network`. `HB-SOR-13 Trade Finance Instrument Authority` is purpose-specific. `HB-ACC-04`, `HB-ACC-20` and `HB-ACC-21` represent distinct contingent, fee and settlement consequences.

Controls `HB-CTRL-04 Trade Document and Discrepancy Review` and `HB-CTRL-21 Trade Instrument Authority and Limit Control` complement reconciliations `HB-REC-021` and `HB-REC-022`. Instrument rules, document standards and jurisdiction details remain explicit catalogue gaps.

## Scenario pattern 3: investment through asset servicing

`HB-SCN-13 Advise and Execute an Investment` moves from mandate and suitability through order, execution, allocation and settlement. `HB-SCN-14 Safekeep Securities and Process a Corporate Action` continues from custody position through notice, eligibility, election, entitlement and client allocation.

Applications are deliberately specialised: `HB-APP-049 Portfolio and Advisory Management`, `HB-APP-050 Investment Order Management`, `HB-APP-051 Securities Processing`, `HB-APP-052 Custody and Safekeeping` and `HB-APP-053 Corporate Actions and Asset Servicing`. This is a realistic logical estate, not a requirement for five vendor products or five deployment units.

The trace must preserve the distinction among portfolio view, order authority `HB-SOR-15`, custody holding authority `HB-SOR-16` and entitlement authority `HB-SOR-17`. `HB-REC-023`, `HB-REC-024`, `HB-REC-025` and `HB-REC-026` test order, position, settlement and entitlement alignment. Suitability control `HB-CTRL-22`, custody control `HB-CTRL-23` and corporate-action control `HB-CTRL-24` answer different risks.

## Scenario pattern 4: close, reporting and recovery

`HB-SCN-16 Close the Books and Submit a Regulatory Return` shows why a transaction is not complete from a bank-wide viewpoint until governed financial and reporting consequences are traceable. `HB-APP-058 Product Subledger Platform`, `HB-APP-059 General Ledger`, `HB-APP-060 Enterprise Reconciliation`, `HB-APP-062 Regulatory Reporting` and `HB-APP-082 Regulatory Data Platform` have different responsibilities.

`HB-SOR-04 General Ledger Authority` governs approved legal-entity ledger balances, while `HB-SOR-24 Regulatory Return Authority` governs the return and submission evidence. `HB-REC-030 Subledger to General Ledger` and `HB-REC-033 Regulatory Report to Governed Source` prove different relationships.

`HB-SCN-19 Recover Payment Service after Cyber Disruption` adds containment, trusted recovery, dependency activation, restart, reconciliation, communication and failback. It depends on `HB-APP-085 Security Operations Platform`, `HB-APP-089 Secrets and Cryptographic Key Management` and proposed `HB-APP-090 Resilience Orchestration and Recovery`. The scenario must not assume those target responsibilities already operate completely.

Together these scenarios show two time horizons: transaction completion and enterprise evidence. An integrated model must represent both.

## Service Domain assessment template

Use this template before adding or changing a candidate mapping.

| Field | Prompt |
|---|---|
| Horizon responsibility | Which exact capability, process or application responsibility is being mapped? |
| BIAN source | Which versioned official artefact was inspected? |
| Candidate object | What exact BIAN object is proposed? |
| Semantic fit | Which responsibilities align and which do not? |
| Relationship | Is the mapping primary, supporting, overlapping or composite? |
| Evidence | What source passage or model supports the interpretation? |
| Confidence | High, Medium, Low or Pending, with reason |
| Verification | Who checked it and against which version? |
| Implementation caution | Why does this not prescribe an application, service, database or team? |

If the source cannot be inspected, keep the candidate unresolved. Do not fill the field from memory to make the matrix look complete.

## Business Scenario template

```text
Scenario ID and name:
Decision and audience:
Trigger:
Observable outcome:
Included and excluded scope:
Business owner:
Products, value streams, capabilities and processes:
Human participants and decisions:
Applications and responsibilities:
Information and authority by lifecycle stage:
Interfaces and external networks:
Accounting events and reconciliations:
Controls and evidence:
Critical operations and recovery considerations:
BIAN candidates, source, confidence and verification:
Current, transition and target differences:
Exceptions, assumptions and governed gaps:
```

## Application mapping template

For each participating application, record:

| Field | Question |
|---|---|
| Application ID | Which governed logical application participates? |
| Scenario responsibility | What does it decide, record, coordinate, transform or present? |
| Inputs and outputs | Which exact interfaces and information are used? |
| Authority | Is it authoritative, derived, initiating or evidential for this purpose? |
| Financial effect | Which accounting event or reconciliation applies? |
| Control | Which control is enforced or evidenced here? |
| Operations | Who owns service health, alerts, recovery and exceptions? |
| State | Is the responsibility Current, Transition or Target? |
| Boundary rationale | Why is this a coherent logical application responsibility? |

## Implementation decision tree

Use this sequence as a first filter:

1. **Is the business responsibility understood?** If no, refine the domain, capability, process and outcome before choosing software.
2. **Is the information meaning and authority understood?** If no, define concepts, lifecycle and ownership.
3. **Does an existing application already own the responsibility adequately?** If yes, consider retain, improve or encapsulate.
4. **Can a responsibility move behind a stable contract without splitting indivisible state?** If yes, consider extraction or replacement.
5. **Does the interaction require immediate response?** Choose a synchronous contract only where the caller genuinely needs it.
6. **Is the message a request or a fact?** Use a command for requested action and an event for an occurrence. Design duplicate and ordering behaviour.
7. **Does a BIAN candidate help clarify semantics?** Record the mapping, source and confidence, but decide implementation separately.
8. **Can the transition operate and recover safely?** If no, redesign coexistence, data authority, reconciliation and rollback.
9. **Is evidence sufficient for the relevant quality gate?** If no, keep the status and gap honest.

## Common integrated-modelling mistakes

- Starting the scenario at a user click and ending it at an API response.
- Showing applications but omitting human decisions and operational queues.
- Treating one system as authoritative for every use and lifecycle stage.
- Hiding accounting and reconciliation behind “core banking”.
- Drawing external networks as generic clouds without contracts or ownership.
- Listing controls without locating their decision or evidence point.
- Claiming resilience without dependencies, degraded operation and recovery.
- Forcing one-to-one BIAN, application, software-service and team mappings.
- Presenting target applications as current capability.
- Filling gaps with plausible but uncontrolled names.

## Chapter summary

An integrated scenario is a controlled trace from trigger to observable outcome. It joins business responsibility, software, information, interaction, accounting, control and operations while keeping their meanings distinct. The practitioner reference helps select the minimum views, test BIAN candidates and expose transition gaps. The catalogues remain the source of truth.

## Completion checklist

- [ ] Trigger, outcome, scope and owner are explicit.
- [ ] Business domain, capability, value stream, process and product are distinguished.
- [ ] Every participating application has a named responsibility.
- [ ] Data authority is stated by purpose and lifecycle stage.
- [ ] Interfaces include type, direction and external network where relevant.
- [ ] Accounting events and reconciliations cover financial or governed state changes.
- [ ] Controls are connected to decisions and evidence.
- [ ] Critical operations, support and recovery are included.
- [ ] BIAN candidates have version, confidence and verification status.
- [ ] Current, transition and target elements are not confused.
- [ ] The coverage row records `Pending` and a gap where evidence is absent.

## Key takeaways

- Start and end with a business state, not a screen or technical response.
- Use several small views when one overloaded diagram would mix concerns.
- Authority is purpose-specific and may change through a lifecycle.
- Accounting and reconciliation extend the scenario beyond transaction processing.
- A logical application is neither a vendor product nor automatically a deployable service.
- BIAN contributes reference semantics, not an implementation blueprint.
- Honest gaps are more useful than invented completeness.

## Practical exercise

Create an integrated scenario pack for `HB-SCN-11 Onboard and Fund a Merchant`. Use the scenario and catalogue records to complete the Business Scenario and Application Mapping templates.

A strong answer will distinguish merchant onboarding from transaction acquisition, include `HB-APP-045`, `HB-APP-046`, `HB-EXT-007`, `HB-SOR-12`, `HB-ACC-18`, `HB-REC-020`, `HB-CTRL-20` and `HB-CRIT-07`, and record merchant-risk, device, scheme-pricing and negative-funding details as gaps rather than inventions.

## Review checklist

- [ ] Does the model answer one named stakeholder decision?
- [ ] Are all IDs exact and valid in the governed catalogues?
- [ ] Are process order, software structure and deployment placement kept distinct?
- [ ] Is every authoritative-data claim qualified by purpose?
- [ ] Can finance and operations reviewers follow the same scenario?
- [ ] Are reference-model facts separated from Horizon Bank choices?
- [ ] Could another practitioner reproduce the trace and identify the same gaps?

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14], source note: `research/bian/bian-service-landscape-14.0.md`.
- [BCBS-OPERATIONAL-RESILIENCE-2021], source note: `research/banking/bcbs-operational-resilience-2021.md`.
- [BCBS-239], source note: `research/banking/bcbs-239-risk-data-aggregation.md`.
