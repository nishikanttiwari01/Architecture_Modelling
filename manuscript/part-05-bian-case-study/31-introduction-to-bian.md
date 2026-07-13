---
title: "BIAN Essentials and the Case-Study Method"
chapter: 31
part: "part-05-bian-case-study"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-13"
---

# 31. BIAN Essentials and the Case-Study Method

## Chapter purpose

Introduce the Banking Industry Architecture Network (BIAN) concepts needed in Part V and explain how Horizon Bank will combine them with business, application, data and technology models.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- explain why BIAN provides a banking reference architecture;
- distinguish Service Landscape, Business Area, Business Domain, Service Domain, Business Scenario and Service Operation;
- explain why a Service Domain is not automatically a microservice, application or team;
- combine BIAN with ArchiMate, Business Process Model and Notation (BPMN), C4, Unified Modeling Language (UML), Decision Model and Notation (DMN) and data models;
- assess a proposed Horizon Bank mapping by evidence, status and confidence.

## Prerequisites and dependencies

- Chapter 30: Change and Migration
- Chapters 4 to 10 for the modelling languages used in the case study

## Required models and artefacts

- BIAN 14.0 source note, candidate mapping register and `FIG-31-01` specification

## Worked examples

- Horizon Bank payment-initiation traceability thread

## Source requirements

- Verify every exact BIAN object against official 14.0 material and record version, rationale, status and confidence.

## Planned chapter structure

The following sections implement the approved Chapter 31 structure from the Part V redesign instruction.

## The question BIAN helps answer

A bank may describe the same responsibility differently in product teams, process models, application portfolios and supplier contracts. BIAN helps architects ask a more stable question: **what recognisable banking responsibility is involved, and what standard semantic reference can help describe it?**

BIAN is a banking reference architecture and semantic standard. It provides reusable classifications, responsibility partitions, scenarios, information concepts and interface-oriented material. It does not provide Horizon Bank's organisation chart, application inventory, deployment topology or transformation roadmap. Those remain bank-owned decisions.

## Why BIAN exists

Banks often have overlapping systems and locally defined interface meanings. A shared industry vocabulary can improve comparison and reduce avoidable semantic disagreement. It also gives architects a reference against which to identify gaps, duplication and different interpretations.

This benefit is strongest when BIAN is used as a reference rather than copied as a target. The architect still has to understand Horizon Bank's customers, products, processes, controls, data authority, technology constraints and legal obligations.

## Service Landscape, Business Areas and Business Domains

The **Service Landscape** organises BIAN Service Domains so that users can navigate the reference set. BIAN states that different classification criteria could produce different layouts. The landscape is therefore a navigation structure, not the bank's mandatory organisation model. [BIAN-SERVICE-LANDSCAPE-14]

**Business Areas** and **Business Domains** provide grouping levels within that landscape. They help a reader find related responsibilities. They must not be treated as proof that Horizon Bank should create matching divisions, platforms or reporting lines.

## Service Domains

A **Service Domain** describes a discrete banking responsibility in the BIAN reference model. It provides a useful unit for semantic comparison: what responsibility is being performed, what behaviour is exposed and what information is involved?

> **Important:** A BIAN Service Domain is not automatically one microservice. It is also not automatically one application, bounded context, team, capability or process step.

One Horizon Bank application may support several candidate Service Domains. One candidate Service Domain may be realised by several applications, human activities and external services. This many-to-many relationship is normal. A physical boundary is justified by cohesion, data authority, transaction needs, risk, scale, change cadence, vendor constraints and operating ownership, not by name matching.

## Business Scenarios

A **Business Scenario** shows how responsibilities collaborate to achieve an outcome. It is useful for tracing interactions across Service Domains, but it is not a substitute for a detailed BPMN process. A scenario can show that screening, payment execution and account posting participate in an outcome; a BPMN model can then describe work sequence, gateways, timers, messages and exceptions.

Horizon Bank will use scenarios as traceability threads. Each thread records a trigger, outcome, participants, candidate BIAN responsibilities, people, applications, data, interfaces, decisions, controls, exceptions and evidence.

## Service Operations, Behaviour Qualifiers and control records

**Service Operations** describe interactions associated with a Service Domain. **Behaviour Qualifiers**, where the official model uses them, distinguish significant behavioural aspects within the responsibility. These concepts can inform interface analysis, but an implementation team must still define protocol, message contract, authorisation, validation, idempotency, failure handling and service-level expectations.

The **Control Record Model** organises the information used to control or track an instance of a Service Domain's behaviour. It is a semantic analysis aid. It does not require Horizon Bank to store one physical record or use the BIAN structure as its database schema.

## Business Object Model

The BIAN **Business Object Model** provides semantic reference concepts and relationships for banking information. Horizon Bank can compare local meanings with these concepts when defining canonical terms and interfaces. It must still own its conceptual, logical and physical data models, identifiers, privacy classifications, retention rules and systems-of-record decisions.

## Semantic APIs and events

BIAN semantic material can help teams align the meaning of application programming interfaces (APIs) and events. Semantic alignment is not the same as copying an interface. Horizon Bank must decide whether an interaction is synchronous, event-driven, batch, file-based or workflow-mediated and must document its failure semantics.

An event states that something meaningful has happened. An API operation requests or queries behaviour. Converting every operation into an event, or every event into an API call, hides the different coupling and recovery characteristics.

## Version discipline

This edition uses BIAN Service Landscape 14.0, released in February 2026. BIAN reports that 14.0 rationalised Service Domain definitions, removed unnecessary Service Operations, increased links to ISO 20022 and renamed, removed or added some Service Domains, especially in payments. [BIAN-SERVICE-LANDSCAPE-14]

Consequently, every exact BIAN name used later must record:

- object type and exact official name;
- BIAN version;
- official source location;
- local element being mapped;
- relationship and rationale;
- status and confidence;
- reviewer, date and unresolved question.

Older names are not silently carried forward.

## BIAN and complementary modelling techniques

| Technique | Main question in this case study | Relationship to BIAN |
|---|---|---|
| ArchiMate | How do strategy, business, application and technology elements relate? | Places candidate BIAN responsibilities in enterprise views |
| BPMN | How does work proceed, including decisions and exceptions? | Details process behaviour across responsibilities |
| C4 | How is software structured and deployed? | Shows applications and software boundaries that realise responsibilities |
| UML | How do components, interactions, states or data structures behave? | Adds selected design precision |
| DMN | How is repeatable decision logic structured? | Separates rules from process and service interactions |
| Data modelling | What information exists, relates and is authoritative? | Compares bank-owned models with BIAN semantic concepts |

No row is an equivalence. The techniques answer different questions.

## Horizon Bank traceability method

Part V follows this chain:

```text
stakeholder outcome
→ value stream
→ capability
→ process
→ candidate BIAN responsibility
→ application responsibility
→ information authority
→ interface
→ deployment and operation
```

Each arrow means `is supported by`, `is performed through`, `is a candidate mapping to`, `is realised by`, or another qualified relationship. It never means `equals`.

## Mapping evidence, status and confidence

Mappings use four statuses: `Proposed`, `Verified`, `Rejected` and `Superseded`. `Verified` means the BIAN name and the local rationale have been reviewed; it does not claim formal BIAN conformance.

Confidence is separate from status:

- **High:** the official definition and local responsibility align closely, with clear scope boundaries;
- **Medium:** the mapping is useful but has overlap or interpretation that needs review;
- **Low:** the mapping is exploratory or based on incomplete local information.

This separation prevents a neat-looking matrix from concealing uncertainty.

## Common mistakes

- Starting with Service Domain names before understanding the business outcome.
- Treating the Service Landscape as an organisation chart.
- Mapping one Service Domain to one microservice without design evidence.
- Calling a local API BIAN-compliant merely because its operation has a similar name.
- Using BIAN information concepts as a mandatory physical schema.
- Omitting the BIAN version and mapping rationale.

## Key takeaways

- BIAN provides banking reference responsibilities and semantics, not a complete bank design.
- Service Domains and physical implementation boundaries have many-to-many relationships.
- Scenarios connect responsibilities; BPMN and other models add behavioural and technical detail.
- Horizon Bank remains responsible for ownership, controls, data authority and implementation.
- Every exact BIAN 14.0 mapping needs source evidence, status and confidence.

## Practical exercise

Take the capability `Payment Initiation` and propose a trace from customer outcome to deployment. Label every relationship. Identify which link needs BIAN verification and which links are Horizon Bank design decisions.

**Review criteria:** The answer must not use `equals`; it must distinguish business capability, candidate BIAN responsibility, application, information and deployment.

## Review checklist

- [ ] Every exact BIAN name is verified against 14.0.
- [x] BIAN facts, interpretations and Horizon Bank recommendations are separated.
- [x] The many-to-many mapping principle is explicit.
- [x] Complementary modelling techniques answer distinct questions.
- [ ] `FIG-31-01` specification is approved before source creation.

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14]

## Drafting notes

- Complete exact-object verification and the mapping register before moving beyond `Drafting`.
