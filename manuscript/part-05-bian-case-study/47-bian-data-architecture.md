---
title: "Risk, Compliance, Financial Crime, Fraud, Audit and Legal"
chapter: 47
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 47. Risk, Compliance, Financial Crime, Fraud, Audit and Legal

## Chapter purpose

Show how to model oversight, control, investigation, assurance and legal responsibilities without collapsing them into one `risk system`. The chapter separates enterprise risk, compliance, financial crime, fraud, internal audit and legal work and traces their different authorities through Horizon Bank.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish business ownership of risk from independent oversight and independent assurance;
- separate compliance obligations, customer financial-crime controls, sanctions screening, transaction monitoring, fraud and investigations;
- model cases, alerts, decisions, disclosures, audit findings and legal matters as different governed records;
- trace the applications, data, interfaces, controls and resilience supporting an investigation;
- protect internal-audit independence while enabling controlled information exchange; and
- avoid unsupported regulatory and BIAN claims.

## Prerequisites and dependencies

- Chapter 35: Horizon Bank Information and Data Architecture
- Chapter 36: Horizon Bank Technology, Security, Resilience and Operations Architecture
- Chapter 46: Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting

## Required models and artefacts

- Governed risk, compliance, financial-crime, fraud, audit and legal responsibility records
- Application-authority, alert-to-case, evidence, control and resilience traces
- Scenario trace for `HB-SCN-17 Investigate a Financial-Crime Alert`

## Worked examples

- Horizon Bank financial-crime investigation scenario

## Source requirements

Risk, financial-crime, assurance and BIAN claims use official primary sources. Jurisdiction-specific obligations and the fictional bank's design choices are not presented as universal requirements.

## The question this architecture answers

This architecture answers: **How does the bank identify obligations and risk, make controlled decisions, investigate concerns, provide independent challenge and preserve evidence without confusing responsibility?**

The answer begins with ownership. A product or operations team owns the risks created by its decisions and activities. Risk and compliance functions establish frameworks, monitor, challenge and oversee within their mandates. Internal audit provides independent assurance. Legal advises on legal questions, contracts, disputes and privilege. Shared data and platforms can support coordination, but they must not erase these accountabilities.

The current Institute of Internal Auditors Three Lines statement distinguishes governing-body oversight, management responsibilities and independent internal audit [IIA-THREE-LINES-CURRENT]. This is a governance model, not a mandatory organisation chart for every country. Horizon Bank uses it to test authority and independence.

## Three governed domain families

### Enterprise risk

`HB-DOM-120 Enterprise Risk` covers risk framework, appetite, aggregation, challenge and risk-type oversight. It contains:

- `HB-DOM-121 Risk Framework and Appetite`;
- `HB-DOM-122 Financial Risk Oversight`;
- `HB-DOM-123 Non-Financial and Model Risk`; and
- `HB-DOM-124 Risk Data and Reporting`.

`HB-CAP-120 Enterprise Risk Management` is decomposed into capabilities `HB-CAP-121` to `HB-CAP-128`, including credit, market, liquidity, operational, model, emerging and climate risk and risk data aggregation. `HB-PROC-12 Govern Enterprise Risk` is supported by `HB-PROC-148 Set Risk Framework, Appetite and Policy`, `HB-PROC-149 Oversee Financial Risk`, `HB-PROC-150 Oversee Non-Financial, Model and Emerging Risk` and `HB-PROC-151 Aggregate and Report Risk Data`.

Enterprise risk does not originate every risk position. Credit applications, treasury applications and operational systems remain authoritative for their source records. Risk applies governed classifications, models and aggregation and records independent assessments, breaches, issues and actions.

Reputational risk is often a consequence of other events, decisions and stakeholder perceptions rather than a neatly isolated transaction type. Horizon Bank therefore links potential reputational impact to the originating conduct, operational, financial, legal or customer issue, its stakeholders and the approved response. It does not create a vague `reputation score` with no source, owner or decision use.

Operational-risk events record that a process, person, system or external event caused or nearly caused harm. They need occurrence time, discovery time, affected operation, cause, consequence, loss or near-miss status, owner and remediation links. Key risk indicators (KRIs) are forward-looking or current signals used within defined thresholds and populations. A KRI is not itself an event, control or appetite decision. `HB-CAP-125 Operational and Non-Financial Risk Management`, `HB-PROC-150` and `HB-APP-064` provide the governed responsibility chain.

### Compliance, financial crime and fraud

`HB-DOM-130 Compliance, Financial Crime and Fraud` is divided into:

- `HB-DOM-131 Compliance Obligations and Change`;
- `HB-DOM-132 Customer Financial Crime Controls`;
- `HB-DOM-133 Transaction Monitoring and Investigations`; and
- `HB-DOM-134 Fraud and Conduct Management`.

The corresponding capabilities `HB-CAP-131` to `HB-CAP-139` separate obligation management, regulatory change, customer risk, sanctions and watchlist screening, transaction monitoring, enterprise fraud, investigation, disclosure and conduct. `HB-PROC-13 Manage Compliance, Financial Crime and Fraud` is decomposed into `HB-PROC-152` to `HB-PROC-155`.

The Financial Action Task Force (FATF) Recommendations provide a risk-based international framework that countries implement through their own laws and institutions [FATF-RECOMMENDATIONS-2025-PV47]. Horizon Bank therefore models jurisdiction, effective rule version and decision authority. It does not state that a fictional workflow satisfies a particular country's law.

The financial-crime scope includes anti-money laundering, counter-terrorist financing and measures addressing proliferation financing where applicable. Customer due diligence, sanctions screening, transaction monitoring, investigation and disclosure are related controls, not synonyms. The exact prohibitions, reporting routes, secrecy constraints and escalation times must come from the governing jurisdiction and legal entity.

### Legal and internal audit

`HB-DOM-190 Legal, Audit and Corporate Secretariat` includes `HB-DOM-191 Legal Advisory and Contract Management`, `HB-DOM-192 Corporate Secretariat and Records` and `HB-DOM-193 Internal Audit and Assurance Follow-up`. The relevant capabilities include `HB-CAP-191 Legal Advisory Management`, `HB-CAP-192 Contract Lifecycle Management`, `HB-CAP-193 Litigation and Legal Case Management`, `HB-CAP-195 Internal Audit Management`, `HB-CAP-196 Assurance Finding and Action Tracking` and `HB-CAP-197 Corporate Records and Legal-Hold Management`.

`HB-PROC-19 Provide Legal, Secretariat and Independent Audit Services` is refined by `HB-PROC-173 Manage Legal Advice, Contracts and Disputes`, `HB-PROC-174 Manage Corporate Secretariat and Records` and `HB-PROC-175 Plan and Deliver Internal Audit`.

Legal advice is not the same as compliance monitoring. Internal audit is not a second-line risk approval team. Corporate records are not interchangeable with every operational document. These distinctions matter even when a shared case or content platform is used.

## Responsibility comparison

| Responsibility | Primary question | Record owned | Must remain separate from |
|---|---|---|---|
| Business and operations | Are risks within approved authority while delivering the outcome? | Product decision, transaction and operational evidence | Independent challenge and assurance conclusions |
| Enterprise risk | Is risk understood, aggregated and within appetite? | Risk assessment, appetite measure, breach and issue | Source product records |
| Compliance | What obligations apply and how is adherence overseen? | Obligation, interpretation, monitoring result and action | Legal advice and operational execution |
| Financial crime | Does customer or activity require screening, monitoring, investigation or disclosure action? | Risk classification, alert, investigation and disposition | Fraud loss handling and product posting |
| Fraud | Is deceptive activity occurring and what protective action is authorised? | Fraud signal, decision, linked activity and case | Anti-money-laundering disclosure decision and card-processing authority |
| Internal audit | Is governance, risk management and control designed and operating effectively? | Audit plan, workpaper, finding and opinion | Management's risk acceptance or remediation ownership |
| Legal | What legal rights, obligations, privilege, hold or dispute action applies? | Legal matter, advice, obligation and hold | Compliance policy ownership and audit conclusion |

### First line, second line and independent assurance

The first line owns products, processes, transactions and the risks created while delivering them. At Horizon Bank this includes `HB-ORG-08 Retail Banking`, `HB-ORG-09 Business and Corporate Banking`, `HB-ORG-11 Treasury and Markets` and `HB-ORG-15 Banking Operations`.

The second line provides independent framework, oversight and challenge. `HB-ORG-13 Enterprise and Financial Risk` and `HB-ORG-14 Compliance, Financial Crime and Conduct` do not take over first-line source records or execute every control. `HB-ORG-22 Internal Audit` provides independent assurance and must remain able to reach its own findings. `HB-ORG-21 Legal` advises on legal rights and obligations but is not a substitute for either compliance ownership or audit assurance.

| Trace point | Accountable organisation | Example record or decision |
|---|---|---|
| Originate and operate | `HB-ORG-08`, `HB-ORG-09`, `HB-ORG-11`, `HB-ORG-15` | Customer, product, trade, transaction and operational evidence |
| Challenge and oversee risk | `HB-ORG-13` | Risk assessment, appetite breach, KRI and challenge action |
| Oversee compliance and financial crime | `HB-ORG-14` | Obligation, screening disposition, monitoring issue and disclosure decision |
| Advise on legal constraints | `HB-ORG-21` | Legal interpretation, matter, privilege and hold |
| Provide independent assurance | `HB-ORG-22` | Audit plan, workpaper, finding and assurance conclusion |

The organisation trace exposes who owns the record and who may challenge it. A shared committee or application does not remove these distinctions.

### Control objective, activity and evidence

A **control objective** states the result the bank needs, such as preventing a prohibited payment from being released. A **control activity** is the action used to achieve it, such as pre-release screening, referral and authorised disposition. **Control evidence** shows which population, rule version, decision and exception handling actually occurred.

`HB-CTRL-02 Transaction Screening and Referral` can support the objective above. `HB-APP-018` performs screening, `HB-INT-026` provides the decision to `HB-APP-034`, and `HB-REC-035` later supports case-to-source traceability. A policy statement alone is not an operated control, and an activity without retained evidence cannot be tested reliably.

## Application boundaries

Horizon Bank uses distinct logical applications rather than a single generic risk platform.

| Application | Responsibility | Governed authority |
|---|---|---|
| `HB-APP-064 Enterprise Risk Management` | Risk taxonomy, assessments, appetite measures, issues and actions | Enterprise risk and issue records |
| `HB-APP-018 Name and Sanctions Screening` | Name, sanctions and watchlist screening | Screening decision and evidence within defined scope |
| `HB-APP-065 Anti-Money Laundering Transaction Monitoring` | Detection of suspicious activity patterns and alert generation | Monitoring alerts and detection evidence |
| `HB-APP-066 Enterprise Fraud Management` | Cross-product fraud detection and strategy | Enterprise fraud alerts and linked activity |
| `HB-APP-067 Financial Crime Investigation Case Management` | Alert triage, investigation, escalation and reporting decisions | Investigation case, disposition and evidence |
| `HB-APP-043 Card Fraud Decisioning` | Low-latency fraud decision for card authorisation | Card decision evidence, not enterprise investigation |
| `HB-APP-068 Internal Audit Management` | Audit planning, workpapers, findings and actions | Audit engagement and independent evidence |
| `HB-APP-069 Legal Matter and Obligation Management` | Legal matters, advice, holds and external counsel | Legal matter and legal-hold authority |

The boundaries reflect different lifecycle, access, latency and independence needs. `HB-APP-043` may decide within a card-authorisation time window. `HB-APP-066` can link cross-product activity. `HB-APP-067` manages an investigator's case. Merging those records because all involve fraud would mix real-time decisions, analytical signals and formal case evidence.

Similarly, `HB-APP-064` may exchange finding and action status with `HB-APP-068` over `HB-INT-090 Risk and Assurance Finding Exchange`. That does not permit risk management to edit an audit finding or audit to own management's remediation action.

## Alerts, cases, decisions and evidence

An alert is a signal requiring evaluation. It is not proof of wrongdoing. A decision records an authorised conclusion or action. A case groups work, parties, activity, evidence, tasks and disposition for a defined purpose. Evidence is the retained material supporting the decision.

These records need distinct identifiers and lifecycle states. An alert can be closed without a case, linked to an existing case or escalated into a new case. A case may link many alerts and transactions. The architecture should preserve the model or rule version, source data, creation time, prioritisation, assignment, investigator actions, decisions and access history.

`HB-INT-059 Screening Alert Event` and `HB-INT-091 Financial Crime Alert Event` represent governed hand-offs. `HB-INT-058 Due-Diligence Investigation Handoff` transfers a case responsibility. `HB-INT-055 Legal Document Hold` applies a hold to governed content. Direction and semantics matter: a receiving system must not silently reinterpret `referred` as `confirmed`.

The data domains are `HB-DATA-13 Enterprise Risk and Models`, `HB-DATA-14 Compliance, Financial Crime and Fraud`, and `HB-DATA-06 Case, Document and Evidence`. `HB-SOR-19 Enterprise Risk Position Authority`, `HB-SOR-20 Financial-Crime and Fraud Case Authority` and `HB-SOR-21 Enterprise Document and Record Authority` identify different sources. A copied transaction inside a case remains evidence linked to the transaction authority, not a new source of transaction truth.

## Risk data aggregation and model governance

Risk reports often combine legal entities, products, counterparties, currencies and risk types. The architecture must retain common identifiers, source lineage, transformations, data-quality results, model versions and adjustments. The Basel Committee's BCBS 239 principles connect governance, data architecture, aggregation and reporting and emphasise accuracy, completeness and timeliness for their defined scope [BCBS-239].

`HB-APP-055 Market and Counterparty Risk`, `HB-APP-030 Credit Exposure Aggregation` and other domain applications produce specialised measures. `HB-APP-064` does not need to copy every calculation. It needs governed aggregation and challenge records with links to those authorities.

`HB-CTRL-33 Risk Model Approval and Performance Monitoring` applies to models used in risk decisions. At minimum, retain purpose, owner, version, approval, input scope, limitations, monitoring results and change history. A score without its model version and data cut-off is not reproducible evidence.

Data and artificial intelligence (AI) risk crosses model, privacy, security, quality and conduct concerns. `HB-CAP-168 Analytical and Artificial-Intelligence Model Management`, `HB-APP-081 Enterprise Analytical Data Platform`, `HB-APP-083 Metadata and Data Lineage Platform` and `HB-APP-084 Data Quality Management` support this lifecycle. Governance should preserve training or reference population, intended use, features or inputs, version, approval, performance, limitations, human-override policy and retirement. A generative or predictive model is not authorised merely because it is hosted on an approved platform.

## Compliance and regulatory change

An obligation architecture traces a source requirement through interpretation, applicability, policy, control, monitoring and evidence. It must record jurisdiction, legal entity, product and effective date. `HB-CAP-131 Compliance Obligation Management` and `HB-CAP-132 Regulatory Change Management` are therefore distinct from operational control execution.

Legal may advise on interpretation. Compliance owns its governed obligation and oversight process. Product and operations owners implement controls. Internal audit may later assess design and operation. The relationship is many-to-many: one obligation can influence several policies and controls, while one control may support several obligations.

Do not place full copyrighted regulatory text in the repository. Store a lawful source reference, concise interpretation, applicability decision and accountable owner.

Regulatory examinations and supervisory requests require a controlled request, scope, accountable coordinator, evidence population, review, submission, follow-up and retained correspondence. Compliance may coordinate, business and data owners supply evidence, Legal may advise, and Internal Audit remains independent. Horizon Bank has no dedicated examination-case or supervisor-request interface in the current catalogues, so a design should record that gap rather than reuse `HB-INT-090`, which is specifically a risk-to-audit finding exchange.

## Financial-crime and fraud control chain

Customer controls begin during onboarding and continue through periodic or event-driven review. `HB-CTRL-01 Customer Due-Diligence Review` and `HB-CTRL-02 Transaction Screening and Referral` apply across journeys. `HB-CTRL-34 Transaction Monitoring and Investigation` governs detection coverage, alert disposition and investigation. `HB-CTRL-35 Enterprise Fraud Detection and Response` governs fraud strategies and authorised protective action.

Screening, monitoring and fraud detection consume different information and may operate at different times. Screening compares relevant parties or transaction data against governed reference sources. Transaction monitoring evaluates behaviour across activity. Fraud controls seek deceptive or unauthorised activity and may need immediate protective action. A bank may coordinate them, but a model should not use one generic `risk check` box.

`HB-REC-035 Financial-Crime Case to Source Evidence` confirms that alerts and cases retain traceable parties, transactions, screening results, dispositions and evidence. This is not a financial balance reconciliation. It is a case-to-source trace that tests whether a conclusion can be reconstructed.

### Combined sanctions and fraud path

Consider a card purchase that produces both a possible sanctions concern and a fraud concern.

1. `HB-APP-043 Card Fraud Decisioning` provides the fraud decision to `HB-APP-041 Card Authorisation` through `HB-INT-044 Card Fraud Decision`.
2. When case work is needed, `HB-APP-043` initiates `HB-INT-045 Card Fraud Case Handover` to `HB-APP-044 Card Disputes and Chargebacks`.
3. `HB-APP-018 Name and Sanctions Screening` publishes a screening alert to `HB-APP-067 Financial Crime Investigation Case Management` through `HB-INT-059 Screening Alert Event`.
4. Transaction-monitoring alerts from `HB-APP-065` reach `HB-APP-067` through `HB-INT-091 Financial Crime Alert Event`.
5. The current interface catalogue has no governed exchange between `HB-APP-044` and `HB-APP-067`, or from `HB-APP-066 Enterprise Fraud Management` to `HB-APP-067`. Coordination therefore uses governed cross-references and authorised operational hand-off until a typed interface is catalogued. The chapter does not pretend that `HB-INT-091` has a producer other than `HB-APP-065`.
6. `HB-CTRL-02`, `HB-CTRL-34` and `HB-CTRL-35` preserve distinct screening, investigation and fraud decisions. `HB-REC-035` tests that the financial-crime conclusion remains traceable to source activity and alert evidence.

Customer communication is constrained. A channel may communicate an authorised service status or request permitted evidence, but it must not disclose restricted screening logic, investigation details or a protected disclosure decision. The communication purpose, audience and approved wording must be separate from the case's internal state.

Model feedback is also controlled. Only reviewed outcomes with an appropriate label, provenance and permitted use should enter model monitoring or retraining. Investigator overrides, unresolved cases and sanctions false positives must not be copied blindly as ground truth. `HB-CTRL-33` governs model approval and performance, while data-quality and lineage evidence retain how the feedback population was formed.

## Audit, legal privilege and records

Internal audit needs access to relevant records but retains its own engagement, workpaper, finding and opinion authority in `HB-APP-068`. Access controls should prevent operational owners from changing audit evidence. Management may update action status and attach remediation evidence, but audit controls closure criteria and its assurance conclusion.

Legal matters in `HB-APP-069` may have restricted access and jurisdiction-specific privilege considerations. `HB-CTRL-36 Privacy, Retention and Legal-Hold Enforcement` connects privacy, retention and holds. A legal hold suspends ordinary disposal for defined material; it does not make every copy authoritative or give unrestricted access.

`HB-TECH-023 Audit, Legal and Records Classification` highlights evidence integrity, legal holds, access history and resumable casework. The detailed access and retention rules remain policy and jurisdiction decisions.

## Accounting and financial-control boundary

Risk or case decisions may cause a financial action, but the case application should not post an ungoverned journal. A fraud reimbursement, customer redress, legal settlement, fine, recovery or write-off needs an authorised business outcome and a governed hand-off to finance. Finance then applies the relevant accounting policy, event and approval controls.

The current accounting-event catalogue does not yet define specific legal-settlement, fraud-loss or complaint-redress events. This chapter records that as a shared-catalogue request rather than reusing an unrelated accounting ID. Until the taxonomy is extended, any implementation must retain the case decision, amount, legal entity, approval and finance acknowledgement without claiming complete catalogue traceability.

## Worked trace: investigate a financial-crime alert

`HB-SCN-17 Investigate a Financial-Crime Alert` begins when screening or transaction monitoring creates an alert. Its outcome is either a governed closure rationale or an investigated case with controlled actions and retained evidence.

1. A source application retains the customer or transaction record under its own authority.
2. `HB-APP-018` or `HB-APP-065` evaluates governed inputs and emits an alert with rule or model version.
3. `HB-INT-091` transfers the transaction-monitoring alert to `HB-APP-067` without changing its meaning.
4. `HB-APP-067` links parties, transactions, earlier alerts and documents, assigns work and records investigator actions.
5. `HB-CTRL-34` enforces disposition authority, evidence and escalation. `HB-CTRL-37 Workforce and Privileged Access Governance` restricts case access.
6. A permitted action may create a controlled transaction restriction, customer review or disclosure decision. The scenario does not expose restricted disclosure information to unauthorised users.
7. `HB-REC-035` tests the case-to-source trace at disposition and closure.
8. `HB-SOR-20` remains the authority for the case and evidence references, while source applications remain authoritative for original parties and transactions.

`HB-CRIT-16 Perform Mandatory Screening and Financial-Crime Intervention` and `HB-TECH-022 Financial Crime, Fraud and Compliance Classification` identify the operational and technology dependency. A degraded service decision must be approved in advance. `Keep processing and check later` is not an acceptable undocumented fallback.

## Security, privacy and resilience

This estate contains highly restricted data. Controls should cover least-privilege access, investigator conflict checks, privileged access, evidence integrity, secure exchange, retention, legal holds and monitoring. `HB-CTRL-38 Security Monitoring and Incident Response` and `HB-TECH-027 Cybersecurity and Secrets Control-Plane Classification` support the domain controls.

Resilience concerns include detection coverage, external screening connectivity `HB-EXT-012 Screening Data Connectivity`, case continuity, secure fallback, backlog management and recovery reconciliation. The model must show what happens when a screening source, monitoring engine or case platform is unavailable. It must not invent recovery targets before approval.

## BIAN alignment without name matching

The Horizon Bank BIAN register currently has no governed mapping for enterprise risk, compliance, financial crime, fraud, audit or legal. BIAN Service Landscape 14.0 is the current announced release [BIAN-SERVICE-LANDSCAPE-14-PV45-48], but names alone cannot establish equivalence.

A future mapping must split the responsibilities first, then inspect the versioned candidate purpose, control record and lifecycle. A BIAN Service Domain must not automatically become `HB-APP-064`, `HB-APP-067`, an investigation team or a database.

## Current-to-target considerations

The principal risk, monitoring, fraud, investigation, audit and legal applications are recorded as current, but their catalogue gaps show that current does not mean complete or well integrated. Improvement should begin with common party, transaction, alert and case references; governed rule and model versions; specialist access boundaries; and case-to-source reconciliation.

Do not migrate every investigation into a generic case platform merely to reduce application count. Rationalise only after comparing authority, secrecy, jurisdiction, latency and evidence requirements. Transition models should show coexistence, duplicate-alert treatment, historical case retention and the point at which each authority changes.

## Choose the model that matches the oversight question

Use a responsibility model to test independence, a process model to show escalation and human decisions, a case lifecycle to define states and evidence, a data-lineage view to test source and model reproducibility, and an access or threat model for restricted information. A risk heat map cannot explain investigation sequence, and a case workflow cannot prove independent audit authority.

## Common mistakes

- Assigning all risk to the risk function and removing business ownership.
- Treating compliance, legal and internal audit as interchangeable reviewers.
- Calling an alert a confirmed event or a score a decision.
- Using one generic case system without specialist authority and access boundaries.
- Combining sanctions screening, transaction monitoring and fraud into one unnamed control.
- Treating reputational impact, an operational-risk event, a KRI and a control failure as the same record.
- Letting an AI model enter production or retraining without intended-use, data, approval and performance evidence.
- Reusing an unrelated interface for a regulatory examination or cross-case hand-off.
- Allowing management to edit independent audit findings.
- Copying source transactions into a case and treating the copy as authoritative.
- Hard-coding legal obligations without jurisdiction and effective date.
- Bypassing mandatory controls during disruption without an approved fallback.
- Mapping applications to BIAN from similar names.

## Chapter summary

Risk, compliance, financial crime, fraud, internal audit and legal share information but have different purposes and authority. Horizon Bank separates their domains, capabilities, processes, applications and sources of record. Alert and case semantics, independent assurance, source lineage, access and resilience make the design reviewable. Jurisdictional obligations and BIAN candidates remain explicit verification work.

## Key takeaways

- Business ownership, independent oversight and independent assurance are different accountabilities.
- Compliance obligations, financial-crime controls and legal advice are related but distinct.
- Alerts, decisions, cases, disclosures and evidence need different lifecycle semantics.
- Specialist applications remain separate where latency, access or authority differs.
- Risk data needs common identifiers, lineage, model versions and quality evidence.
- Operational-risk events, KRIs, control objectives, activities and evidence answer different governance questions.
- Customer communication and model feedback from investigations require explicit secrecy, quality and approval constraints.
- Internal audit can share action status without surrendering control of its findings.
- Case resilience must preserve mandatory controls and restricted information.
- No BIAN mapping is valid until the candidate is versioned and reviewed.

## Practical exercise

A card fraud engine, the anti-money-laundering monitoring system and a sanctions screen all flag activity for the same customer. Design the minimum record and interaction model for coordinated investigation without merging all three systems.

### Suggested answer criteria

A strong answer retains the card decision in `HB-APP-043`, the monitoring alert in `HB-APP-065`, screening evidence in `HB-APP-018` and the investigation in `HB-APP-067`. It uses stable alert and case identifiers, records model or rule versions, preserves source links, restricts access, applies `HB-CTRL-34` and `HB-CTRL-35`, and uses `HB-REC-035` at disposition. It does not call all alerts confirmed fraud or expose restricted disclosure decisions broadly.

## Review checklist

- [ ] Business, risk, compliance, audit and legal accountabilities are explicit.
- [ ] Each alert, decision and case has an owner and lifecycle.
- [ ] Specialist source authorities are preserved.
- [ ] Jurisdiction and effective date qualify obligation mappings.
- [ ] Screening, monitoring, fraud and investigation are distinct.
- [ ] Risk calculations retain data and model lineage.
- [ ] Audit evidence and conclusions remain independently controlled.
- [ ] Legal holds and restricted access are modelled.
- [ ] Degraded-control and recovery paths are explicit.
- [ ] No unsupported regulatory or BIAN compliance claim appears.

## References and source notes

- [BCBS-239]
- [FATF-RECOMMENDATIONS-2025-PV47]
- [IIA-THREE-LINES-CURRENT]
- [BCBS-OPERATIONAL-RESILIENCE-2021]
- [BIAN-SERVICE-LANDSCAPE-14-PV45-48]

## Deferred work

No diagram source is created in this pass. Horizon Bank still needs jurisdiction-specific obligation and disclosure catalogues, approved risk taxonomy and appetite measures, model inventory, specialist access rules, detailed degraded-control procedures, verified BIAN candidates and owner-approved resilience objectives.
