---
title: "BIAN Mapping Method and Full-Stack Traceability"
chapter: 49
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 49. BIAN Mapping Method and Full-Stack Traceability

## Chapter purpose

Explain how to map Horizon Bank responsibilities to the Banking Industry Architecture Network (BIAN) without turning a reference architecture into an implementation blueprint. The method connects a versioned BIAN candidate to business outcome, process, organisation, application, information, integration, accounting, control, resilience and operational evidence.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish semantic alignment from name matching;
- assess a candidate against the purpose, lifecycle and information of a BIAN Service Domain;
- record source, confidence and verification status separately;
- trace a mapping through the complete Horizon Bank architecture;
- recognise when one responsibility needs several BIAN candidates or when one candidate spans several implementations; and
- review a mapping without assuming that a Service Domain is an application, microservice, database or team.

## Prerequisites and dependencies

- Chapter 31: BIAN Essentials and the Case-Study Method
- Chapter 33: Enterprise Business Architecture of Horizon Bank
- Chapters 34 to 36: application, information, technology and operating foundations
- Chapters 37 to 48: governed banking-domain responsibilities

## Required models and artefacts

- `examples/horizon-bank/bian-mapping-register.md`
- The governed Horizon Bank business, application, information and operating catalogues
- `examples/horizon-bank/scenario-catalogue.md`
- `examples/horizon-bank/coverage-matrix.csv`
- A versioned evidence record for each exact BIAN object assessed

## Worked examples

- `HB-SCN-02 Execute Cross-Border Payment` and candidate `HB-BIAN-02 Payment Responsibility Candidate`

## Source requirements

BIAN concepts and versions use official BIAN sources. Horizon Bank mappings are fictional author models. An exact Service Domain name, operation or relationship is not treated as verified unless the BIAN 14.0 artefact has been inspected and the evidence recorded [BIAN-14-MAPPING-PV49-52].

## The question this method answers

The method answers: **What does a BIAN candidate mean for this bank responsibility, and what architecture evidence supports or contradicts the mapping?**

A weak answer says that an application name looks similar to a Service Domain name. A defensible answer starts with the business responsibility, compares its meaning with a versioned BIAN artefact, records uncertainty and then traces the result through the bank model. The trace must remain useful even if an application is replaced or a deployment is redesigned.

## Who uses the mapping

Business and enterprise architects use it to compare responsibilities and capabilities. Application, data, integration, security and operations architects use the trace to test implementation consequences. Product, process, data, control and application-service owners use it to confirm accountability. A BIAN mapping steward maintains source evidence and version history, while architecture reviewers challenge scope, confidence and unsupported equivalence.

## What a BIAN mapping is

A BIAN mapping is a governed semantic relationship between a bank responsibility and a BIAN reference concept. It says that the two are sufficiently related for a stated architecture purpose. It does not say that the bank has implemented BIAN in full.

BIAN arranges Service Domains in the Service Landscape. A Service Domain expresses a logical banking responsibility with a characteristic purpose and lifecycle. BIAN Business Scenarios and wireframes illustrate interactions between Service Domains, while Semantic Application Programming Interfaces (Semantic APIs) express service semantics in an implementation-oriented form. These artefacts help analysis, but they do not prescribe Horizon Bank's organisation, process, application estate or deployment [BIAN-14-MAPPING-PV49-52].

The unit being mapped must therefore be explicit. It might be a capability, process responsibility, information authority, application function or scenario participation. Mapping the word `payments` without saying which of those meanings is intended produces a relationship that cannot be reviewed.

## Separate four questions before mapping

Four related questions are often collapsed into one:

| Question | Suitable evidence | What it does not decide |
|---|---|---|
| What banking responsibility exists? | Domain, capability, value stream and process | Software or team structure |
| Which BIAN concept is semantically relevant? | Versioned Service Domain purpose, asset, lifecycle, operations and information | Whether the bank should adopt the API unchanged |
| How is the responsibility implemented? | Logical applications, software services, data authorities and interfaces | Whether one deployment unit is sufficient |
| Who is accountable and who operates it? | Business, product, data, control, application-service and operations owners | That every owner is one delivery team |

Keeping these questions separate is the main protection against accidental one-to-one mapping.

## The mapping method

### 1. Define the decision and scope

State why the mapping is needed. Possible decisions include capability coverage, application rationalisation, interface semantics, ownership clarification or scenario analysis. Record the business line, legal entity, jurisdiction, customer segment, product and architecture state.

A mapping for country retail payments may not be sufficient evidence for cross-border corporate cash management. Scope is part of the meaning, not administrative metadata.

### 2. Establish the Horizon Bank responsibility

Begin with governed bank records. Select the domain and capability, then link the value stream, process, accountable organisation and product where applicable. Describe the complete lifecycle and the state the responsibility controls.

For example, `HB-CAP-050 Payment Management` is broader than `HB-CAP-053 Payment Clearing`. `HB-PROC-04 Execute and Settle Payments` spans initiation, validation, routing, clearing, settlement and investigation. A candidate that fits clearing does not automatically cover the whole Level 1 process.

### 3. Inspect the exact BIAN 14.0 artefact

Use the current official artefact rather than memory or a secondary diagram. Record the BIAN release, object identifier or official name, source location and access date. Examine:

- the Service Domain's stated purpose;
- the asset or subject whose lifecycle it controls;
- the functional pattern and control-record behaviour;
- Service Operations and Behaviour Qualifiers that matter to the scope;
- information concepts and first-order interactions; and
- relevant scenarios, wireframes or Semantic APIs.

Service Landscape 14.0 rationalised definitions and changed some payment content. A mapping copied from an earlier release requires re-verification [BIAN-14-MAPPING-PV49-52].

### 4. Compare semantics, not labels

Write a short responsibility statement for both sides. Compare purpose, lifecycle, authority, inputs, outputs, information and exclusions. Ask whether each side controls the same kind of business state from the same beginning to the same end.

A useful working conclusion is one of these:

| Conclusion | Meaning | Required next action |
|---|---|---|
| Strong semantic fit | Purpose and lifecycle are substantially aligned for the stated scope | Trace implementation and verify operations |
| Partial overlap | Some behaviour aligns, but lifecycle or authority differs | Record included and excluded responsibilities |
| Composite requirement | Several BIAN concepts are needed for the bank responsibility | Record each relationship and interaction |
| No useful match | Similar words do not express the same responsibility | Retain the bank model without forcing alignment |

These are analysis conclusions, not replacements for the controlled record status, confidence or verification fields.

### 5. Record source, confidence and verification separately

Three fields answer different questions:

- **Source type** identifies whether the relationship comes from an official source, author model or governed derivation.
- **Confidence** states how strongly the available evidence supports the interpretation.
- **Verification status** states whether an independent check against the versioned source has occurred.

High confidence is not verification. A verified partial mapping is not an exact equivalence. The current `HB-BIAN-01` to `HB-BIAN-04` records remain candidate author models. Their controlled confidence values are `Pending`, their verification statuses are `Unverified`, and their gaps explicitly require exact BIAN 14.0 objects and rationale before the candidates can progress.

### 6. Build the full-stack trace

The mapping becomes useful when it connects to the architecture decisions that implement and control the responsibility.

| Trace dimension | Question | Horizon Bank record type |
|---|---|---|
| Business | What outcome and capability are involved? | `HB-DOM-*`, `HB-CAP-*`, `HB-VS-*`, `HB-PROC-*` |
| Commercial | Which customer and product scope applies? | `HB-BL-*`, `HB-SEG-*`, `HB-PRD-*`, `HB-LE-*` |
| Accountability | Who owns the outcome, service, data and control? | `HB-ORG-*` and owner fields |
| Application | Which logical applications perform or support the work? | `HB-APP-*` |
| Information | Which data domain and authority apply by purpose and lifecycle? | `HB-DATA-*`, `HB-SOR-*` |
| Interaction | Which APIs, commands, events, messages, files, batches, workflows and networks carry the exchange? | `HB-INT-*`, `HB-EXT-*` |
| Financial | What accounting event and reconciliation establish financial completeness? | `HB-ACC-*`, `HB-REC-*` |
| Control | Which preventive, detective and corrective controls apply? | `HB-CTRL-*` |
| Operations | Which critical outcome and technology classification drive recovery and support? | `HB-CRIT-*`, `HB-TECH-*` |
| Scenario | In which end-to-end behaviour can the mapping be tested? | `HB-SCN-*` |

The master coverage row is an index into this trace, not proof that every relationship is complete. Detailed catalogues and scenario records retain the many-to-many relationships.

### 7. Test the mapping in scenarios

A mapping that looks convincing in a catalogue may fail when behaviour is examined. Walk at least one normal path, one refusal or exception and one recovery path. Confirm who requests an action, who controls state, what information crosses the boundary and how completion is observed.

A BIAN Business Scenario helps examine Service Domain interaction. Business Process Model and Notation (BPMN) is still needed where human activity, timing, escalation and exception routing matter. A runtime sequence or event-flow view is needed where calls, messages and failure behaviour matter. These views complement the mapping rather than competing with it.

### 8. Review and maintain the evidence

The mapping owner reviews source version, scope, exclusions, confidence, verification and downstream use. Recheck a mapping when BIAN changes, the bank responsibility changes, an authoritative application moves, or a material interface is redesigned. Never silently update the label while retaining old evidence.

## Worked trace: cross-border payment

`HB-BIAN-02 Payment Responsibility Candidate` relates to `HB-PRD-07 Payment and Cash Management` and `HB-VS-04 Execute and Settle Transaction`. Its gap says that exact BIAN 14.0 objects and the many-to-many rationale are pending. That is an honest starting point, not a completed mapping.

The business trace begins with `HB-DOM-050 Payments`, `HB-CAP-050 Payment Management` and `HB-PROC-04 Execute and Settle Payments`. `HB-SCN-02 Execute Cross-Border Payment` narrows the scope to instruction, entitlement, screening, foreign exchange, routing, correspondent processing, settlement, posting and reconciliation.

The application trace is deliberately plural. `HB-APP-033 Payment Initiation Service` captures the instruction. `HB-APP-034 Payment Orchestration` controls end-to-end processing. `HB-APP-035 Payment Routing and Clearing` selects and manages clearing paths. `HB-APP-036 Settlement and Nostro Management` controls settlement positions. `HB-APP-037 Payment Investigations and Exceptions`, `HB-APP-038 Correspondent Banking Management` and `HB-APP-039 Foreign Exchange Pricing and Booking` perform distinct responsibilities. No one application represents `payments`, and none is declared equivalent to one Service Domain.

The information trace uses `HB-DATA-08 Payments, Clearing and Settlement`, with `HB-SOR-08 Payment Instruction and Processing Authority` and `HB-SOR-09 Settlement and Correspondent Position Authority` divided by purpose. Interactions include `HB-INT-023 Retail Payment Initiation`, `HB-INT-026 Transaction Sanctions Screening`, `HB-INT-038 Foreign Exchange Quote`, `HB-INT-105 Cross-Border Financial Message` and `HB-INT-065 Correspondent Settlement Instruction`. `HB-EXT-004 Cross-Border Financial Messaging Network` and `HB-EXT-005 Correspondent Banking Connectivity` mark external trust and operating boundaries without claiming membership in a particular provider.

Financial completion is not the same as a successful message. `HB-ACC-14 Payment Settlement Recognised`, `HB-REC-012 Payment Instruction to Processing Status`, `HB-REC-014 Settlement Account and Payment Ledger` and `HB-REC-015 Correspondent Cash and Nostro` connect status to financial evidence. `HB-CTRL-02 Transaction Screening and Referral`, `HB-CTRL-14 Payment Instruction, Entitlement and Funds Validation`, `HB-CTRL-15 Payment Duplicate and Idempotency Control`, `HB-CTRL-16 Payment Clearing, Settlement and Nostro Break Control` and `HB-CTRL-17 Foreign-Exchange Price, Deal and Settlement Control` show why a semantic mapping cannot stop at an API.

The operational trace connects the scenario to `HB-CRIT-02 Make a Time-Critical Payment`, `HB-CRIT-05 Clear and Settle Payment Obligations`, `HB-TECH-009 Payments Processing Classification` and `HB-TECH-010 Foreign-Exchange Processing Classification`. `HB-COV-002` provides a representative coverage index, while the scenario and catalogues retain the fuller relationship set.

Only after this trace is understood should the mapper compare exact BIAN 14.0 Service Domains and interactions. If different BIAN concepts cover initiation, screening, clearing, settlement and investigation, the result should be composite. It must not be compressed into one convenient name.

## How mapping supports architecture decisions

Use the mapping method when a decision needs shared banking semantics, cross-domain responsibility analysis, application rationalisation or interface alignment. It is especially useful when two applications claim the same responsibility, when a target service boundary is being proposed or when a programme needs to compare its vocabulary with BIAN.

Do not use the method to bypass process discovery, product policy, data ownership, security design or deployment design. Do not map every technical platform to a Service Domain. `HB-APP-075 API Management Platform`, for example, governs transport access and policy. Its existence does not create a banking responsibility mapping.

## Common mistakes

- Matching on a similar noun without comparing purpose and lifecycle.
- Mapping a whole process to one candidate because the process has one headline.
- Treating a BIAN diagram as Horizon Bank's current state.
- Calling a candidate `verified` without recording the versioned evidence.
- Using `High` confidence as a substitute for independent verification.
- Mapping one Service Domain directly to one application, software service, database or team.
- Omitting accounting, reconciliation, controls and recovery from the trace.
- Recording only the happy path and ignoring refusal, investigation and restoration.
- Copying a mapping from an older BIAN release without review.
- Hiding an unresolved relationship behind an empty field rather than an explicit gap.

## Chapter summary

A defensible BIAN mapping starts with a governed bank responsibility and a stated decision. It compares meaning against a versioned BIAN artefact, records source, confidence and verification separately, and connects the result to the complete business and technology stack. The cross-border payment example shows why a candidate can involve many capabilities, applications, data authorities, interfaces, controls and operational dependencies. BIAN supplies a semantic reference. Horizon Bank remains responsible for its implementation choices.

## Key takeaways

- Map responsibilities, not names.
- Record scope and architecture state before comparing artefacts.
- Verify exact objects against BIAN 14.0.
- Keep confidence separate from verification.
- Expect many-to-many relationships.
- Trace applications, information, finance, controls and operations.
- Test normal, exception and recovery behaviour.
- Treat a coverage row as an index, not proof of completeness.

## Practical exercise

Assess `HB-BIAN-03 Credit Responsibility Candidate` for `HB-SCN-07 Approve and Manage a Corporate Credit Facility`. Create a one-page mapping assessment.

### Suggested answer criteria

A strong answer starts with `HB-DOM-040`, `HB-CAP-040`, `HB-PROC-03`, `HB-PRD-06` and `HB-VS-05`. It separates origination, decisioning, facility servicing, limits, collateral and exposure rather than forcing them into one candidate. It traces `HB-APP-025`, `HB-APP-026`, `HB-APP-027`, `HB-APP-029` and `HB-APP-030`, plus `HB-DATA-04`, `HB-SOR-03`, relevant interfaces, accounting, controls, reconciliations and `HB-TECH-008`. It records the exact BIAN 14.0 objects still needing verification, gives a confidence rationale and identifies exclusions.

## Review checklist

- [ ] The architecture decision and scope are explicit.
- [ ] The Horizon Bank responsibility has governed IDs.
- [ ] The exact BIAN version and source are recorded.
- [ ] Purpose, lifecycle, information and exclusions were compared.
- [ ] Source type, confidence and verification are separate.
- [ ] Many-to-many relationships are preserved.
- [ ] Application and information authority are traced.
- [ ] Accounting, reconciliation and controls are traced where relevant.
- [ ] Critical operations and recovery dependencies are traced.
- [ ] Normal, exception and recovery behaviour were tested.
- [ ] No Service Domain is presented as an automatic implementation boundary.

## References and source notes

- [BIAN-14-MAPPING-PV49-52]

## Deferred work

No diagram source is created in this pass. The mapping register now contains controlled confidence and verification fields. For `HB-BIAN-01` to `HB-BIAN-04`, those fields remain `Pending` and `Unverified`; exact BIAN 14.0 object identifiers, mapping evidence and review decisions are still required before any candidate can advance through formal review.
