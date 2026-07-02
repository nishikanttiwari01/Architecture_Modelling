---
title: "Other Useful Modelling Approaches"
chapter: 13
part: "part-02-modelling-languages"
status: "Revision Required"
author: "Nishikant Tiwari"
last_updated: "2026-07-02"
---

# 13. Other Useful Modelling Approaches

## Chapter purpose

Introduce specialised modelling approaches that complement the main notations covered earlier in Part II. The chapter helps readers recognise when a focused technique is useful, when a simpler diagram is enough, and when a model should be treated as a conversation aid rather than a formal standard.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain SysML, capability maps, value streams, application landscapes, integration landscapes, roadmaps, heat maps, Wardley maps and Architecture Decision Records (ADRs) in plain language.
- Identify the architecture question each approach answers.
- Select an appropriate specialised model for a realistic situation.
- Distinguish formal standards from practitioner techniques and local conventions.
- Recognise common misuse and review each model critically.
- Apply the approaches to the Simple Online Store and Horizon Bank examples.

## Prerequisites and dependencies

- Chapter 2: Model, View and Viewpoint
- Chapter 3: How to Read Architecture Diagrams
- Chapter 5: The C4 Model
- Chapter 7: ArchiMate
- Chapter 10: Domain and Event Modelling
- Chapter 12: Security Modelling

## Required models and artefacts

- FIG-13-01: Online Store SysML-style Requirement Traceability View, specification created, source deferred pending author approval.
- FIG-13-02: Horizon Bank Customer Onboarding Value Stream, specification created, source deferred pending author approval.
- FIG-13-03: Horizon Bank Application Landscape Map, specification created, source deferred pending author approval.
- FIG-13-04: Horizon Bank Platform Evolution Roadmap, specification created, source deferred pending author approval.
- FIG-13-05: Horizon Bank Capability Heat Map, specification created, source deferred pending author approval.
- FIG-13-06: Horizon Bank Payment Modernisation Wardley Map, specification created, source deferred pending author approval.

## Worked examples

- Simple Online Store requirement traceability for checkout security and order fulfilment.
- Horizon Bank customer onboarding value stream.
- Horizon Bank application and integration landscape.
- Horizon Bank platform evolution roadmap and capability heat map.
- Horizon Bank payment modernisation Wardley map.

## Source requirements

- `[OMG-SYSML-2.0]` supports current SysML version, purpose and systems-modelling scope.
- `[OPEN-GROUP-ARCHIMATE-4]` supports formal enterprise architecture concepts used when explaining capabilities, value streams, implementation and migration views.
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]` supports public official guide metadata for business capability and value-stream modelling.
- `[C4-OFFICIAL]` supports system landscape framing where the landscape concern is software-system relationships.
- `[WARDLEY-MAPS-OFFICIAL-2026]` supports Wardley map provenance, purpose and licence notes.
- `[NYGARD-ADR-2011]` supports lightweight ADR practice and decision-log structure.
- `[AUTHOR-HEAT-MAP-CONVENTIONS-2026]` records the local Chapter 13 heat-map scoring and legend convention.

## Planned chapter structure

1. Explain why specialised models complement the main Part II modelling approaches.
2. Introduce SysML as a systems-engineering and traceability language, with a small requirement-trace example.
3. Introduce capability maps, value streams, landscapes, roadmaps, heat maps, Wardley maps and ADRs as focused architecture tools.
4. Compare the approaches by the question they answer and the audience they serve.
5. Close with common mistakes, a cheat sheet, key takeaways, practical exercise and source notes.

## Drafting notes

- Chapter 13 is currently in `Revision Required` while review findings are being resolved.
- `FIG-13-01` through `FIG-13-06` are registered and have specifications.
- Do not create diagram source or exports until the author approves the corresponding specifications.
- Keep Chapter 14 deeper business-strategy coverage in mind. Chapter 13 should introduce capability, value stream and heat-map approaches without taking over Chapter 14's role.

## Why this chapter exists

The previous chapters introduced major modelling languages and approaches: Unified Modeling Language (UML), C4, Business Process Model and Notation (BPMN), ArchiMate, data modelling, Decision Model and Notation (DMN), domain and event modelling, infrastructure modelling and security modelling. Those techniques cover many architecture questions, but real architecture work often needs smaller specialised views.

A specialised model answers a focused question. It might show which requirement is addressed by which design element, which capabilities need investment, which systems exist in a landscape, which changes happen over time, where risk is concentrated, or why a decision was made. These models are often practical and lightweight. Some are based on standards. Some are practitioner techniques. Some are local conventions used by one organisation.

This chapter groups the approaches into four useful types:

| Type | Approaches in this chapter | Main use |
|---|---|---|
| Traceability views | SysML-style requirement traceability | Connect requirements, design responses, verification cases and evidence. |
| Business architecture views | Capability maps and value streams | Discuss stable business abilities and stakeholder value. |
| Estate and change views | Application landscapes, integration landscapes and roadmaps | Understand systems, information exchange and architecture evolution. |
| Decision and strategy views | Heat maps, Wardley maps and ADRs | Expose attention areas, strategic assumptions and decision rationale. |

The approaches also differ in formality. Some are standards-body modelling languages, some are architecture viewpoints that can use several notations, and some are practitioner techniques.

| Approach | Classification | Notation status | Typical audience |
|---|---|---|---|
| SysML | Formal Object Management Group (OMG) modelling language | Defined modelling language | Systems engineers, analysts, architects and verification teams |
| Capability maps | Formal concepts when modelled through a language such as ArchiMate, but frequently presented through organisation-specific views | Formal or local, depending on the notation used | Business architects, sponsors and portfolio teams |
| Value streams | Formal business architecture concept, often shown through simplified local views | Formal concept with varied visual presentation | Business architects, product owners and sponsors |
| Application landscapes | Architecture viewpoint with varying notation | Usually local, C4 or ArchiMate-style depending on purpose | Enterprise architects, solution architects and application owners |
| Integration landscapes | Architecture viewpoint with varying notation | Usually local, sometimes supported by C4, UML, ArchiMate or data-flow views | Integration architects, solution architects and operations teams |
| Architecture roadmaps | Formal or informal depending on the notation used | ArchiMate implementation and migration view, timeline, table or local roadmap | Transformation leads, enterprise architects and sponsors |
| Heat maps | Organisation-specific visual overlay and scoring convention | Local convention; scoring basis must be stated | Business architects, portfolio teams, risk reviewers and sponsors |
| Wardley maps | Practitioner-origin strategy technique | Practitioner notation with common conventions | Strategy, product and architecture leaders |
| ADRs | Practitioner-origin textual decision-record technique | Textual record, not a diagram notation | Architects, maintainers and governance reviewers |

The danger is treating every useful drawing as a formal notation. A heat map is useful, but its colours are only meaningful if the scoring basis is written down. A roadmap is useful, but it is not a delivery contract unless governance makes it one. A Wardley map is useful for strategy discussion, but it records assumptions about user need, dependency and evolution. The same discipline from Chapter 3 still applies: read the title, purpose, audience, scope, notation, legend, assumptions and omissions before trusting the model.

## SysML

SysML answers: **how do requirements, system structure, behaviour and verification relate in an engineered system?**

SysML is an Object Management Group (OMG) language for modelling systems. OMG SysML 2.0 is the current formal version checked for this chapter. The public OMG specification page describes SysML as a general-purpose modelling language for systems and model-based systems engineering, with support for requirements, structure, behaviour, analysis cases and verification cases [OMG-SYSML-2.0].

For a beginner architect, the most accessible SysML idea is requirement traceability. A requirement should not float by itself. It should be related to the design responses that address it, the verification cases that check it, the evidence produced by those checks, and any higher-level objective it supports. A traceability link is not proof by itself. It is a navigable claim that reviewers can inspect.

For the Simple Online Store, a SysML-style requirement trace might show:

| Requirement ID | Testable requirement | Design response | Verification case | Evidence |
|---|---|---|---|---|
| REQ-OS-01 | Checkout shall not store full customer card details in the Online Store. | Payment details are delegated to the Payment Provider System; the Online Store stores only payment status and provider reference. | Verify card-data storage boundary during checkout. | Security test result and provider integration review. |
| REQ-OS-02 | The customer shall receive an order confirmation after the order is accepted. | Order service creates an order record and triggers web or email confirmation. | Verify accepted-order confirmation. | Functional test result and message-log sample. |
| REQ-OS-03 | Support users shall view order status without seeing full payment details. | Support interface shows order state and masked payment status only. | Verify support-role access to masked payment information. | Access-control test result and support-role review. |

FIG-13-01 is planned as a small teaching view of this pattern. It should not introduce the full SysML language. The purpose is to show why requirement, design, verification case and evidence links matter. In the figure, each requirement may have two outgoing relationships: `addressed by` to a design response, and `verified by` to a verification case. The verification case then points to evidence with `evidenced by`. This avoids implying that the design response itself is what the verification case formally verifies.

Use SysML when traceability across requirements, engineered parts, interfaces, behaviour, analysis and verification is important. Do not use it merely because a diagram has requirements on it. A plain table may be enough for simple software work.

## Capability maps

A capability map answers: **what abilities does the organisation need, independent of the current process or application structure?**

A capability is an ability an organisation has or needs in order to achieve an outcome. A capability map groups these abilities so leaders and architects can discuss investment, ownership, gaps and duplication without starting from the current organisation chart or application estate. The Open Group's public guide metadata for business capabilities describes capability maps as a way to support business planning and align business architecture viewpoints [OPEN-GROUP-BIZARCH-GUIDES-2022].

In Horizon Bank, capabilities might include Customer Onboarding, Party Management, Product Management, Payment Initiation, Payment Screening, Account Servicing, Fraud Management, Data Governance and Digital Servicing. A capability map does not show the process sequence for onboarding a customer. It shows what the bank must be able to do.

The controlled illustrative Horizon Bank capability catalogue is maintained in `examples/horizon-bank/capabilities.md`. The names are teaching examples, not an authoritative bank taxonomy. They are capabilities, not process steps, organisation units, applications or BIAN Service Domains.

Capability maps are often used with heat maps. The capability map gives stable business structure. The heat map overlays one explicit judgement at a time, such as operational pain, strategic value, delivery exposure, maturity or application duplication.

Do not call every activity a capability. "Check documents" is likely a process step. "Customer Onboarding" or "Identity Verification" is more likely to be a capability. The distinction matters because capabilities are used for planning and ownership, while process steps are used for flow and operational detail.

Chapter 14 will go deeper into business strategy and capability modelling. This chapter only introduces the approach so readers recognise it as part of the broader modelling toolkit.

## Value streams

A value stream answers: **how does value move from a triggering stakeholder need to an outcome?**

A value stream is not the same as a detailed process model. It shows major stages of value creation from the perspective of a stakeholder. A BPMN process asks how work is performed in detail. A value stream asks what value is progressively achieved. The Open Group's public value-stream guide metadata describes value streams as a core business architecture element and as something that can be mapped to other business architecture components [OPEN-GROUP-BIZARCH-GUIDES-2022].

For Horizon Bank customer onboarding, a value stream might use stages such as:

| Stage | Stakeholder value produced | Example enabling capabilities |
|---|---|---|
| Need understood | The prospective customer has made the banking need clear enough for the bank to respond. | Digital Servicing, Relationship Management |
| Application established | The bank has enough structured application information to proceed. | Customer Onboarding, Document Capture |
| Identity and eligibility confirmed | The customer can be assessed against identity, eligibility and financial-crime expectations. | Identity Verification, Financial Crime Screening, Risk Assessment |
| Banking relationship established | Customer and product records exist in the bank's authoritative systems. | Party Management, Account Opening, Product Management |
| Services ready to use | The customer can use the selected channels and products. | Digital Servicing, Notification Management, Account Servicing |

FIG-13-02 is planned as a Horizon Bank customer onboarding value stream. It should show value stages, stakeholder perspective and enabling capabilities, not BPMN tasks.

Use a value stream when the discussion is about end-to-end value, capability alignment or strategic change. Do not use it to replace the process model when exceptions, roles, sequence flows, message flows, timers or hand-offs matter. Do not confuse this business architecture use of value streams with Lean value stream mapping, which is aimed at analysing operational flow, waste and improvement in a production or service-delivery stream. Do not confuse it with a customer journey map either. A customer journey map usually emphasises touchpoints, emotion and experience. A business architecture value stream emphasises value stages and enabling capabilities.

## Application landscapes

An application landscape answers: **which applications or software systems exist in the estate, and how do they relate at a useful level of abstraction?**

Application landscapes are common in enterprise architecture because teams need to see more than one system at a time. A C4 System Landscape diagram is one structured way to show software systems and their relationships [C4-OFFICIAL]. ArchiMate application views can also show application components, services and relationships when enterprise architecture traceability matters [OPEN-GROUP-ARCHIMATE-4].

For Horizon Bank, an application landscape might show Horizon Digital Channels, Customer Onboarding Platform, Party and Customer Platform, Product Catalogue, Payments Platform, Financial Crime Platform, Core Deposit System, Enterprise Integration Platform, Event Platform and Enterprise Data Platform. The controlled system list in `examples/horizon-bank/system-landscape.md` uses lifecycle markers: `Target`, `Mixed`, `Legacy retained initially` and `Transitional`. A mixed-state landscape must explain which parts already exist, which are being retained, and which are directionally target. It should also show only the relationships needed for the review question.

FIG-13-03 is planned as a Horizon Bank application landscape map. It should use stable system names from `examples/horizon-bank/system-landscape.md`.

Do not use an application landscape to show every interface, database table, batch job and business process step. If every arrow becomes important, the diagram probably needs to be split into an integration view, process view or sequence view.

## Integration landscapes

An integration landscape answers: **how do systems exchange information, and which integration mechanisms matter?**

An application landscape may show that two systems are related. An integration landscape adds how they communicate. It may show application programming interfaces (APIs), event topics, file transfers, message queues, adapters, gateways and integration platforms.

For Horizon Bank, an integration landscape might show these selected exchanges:

| Source | Destination | Information exchanged | Integration style | Direction | Contract or ownership concern |
|---|---|---|---|---|---|
| Horizon Digital Channels | Payments Platform | Payment instruction and payment status request | Synchronous API | Channel to platform request and platform response | Channel and payments contract ownership |
| Payments Platform | Financial Crime Platform | Payment-screening request and result | Synchronous request and response | Payments request, financial-crime response | Timeout and screening-decision ownership |
| Payments Platform | Enterprise Integration Platform | Account-posting instruction | Adapter-mediated service call | Payments platform invokes integration service | Adapter ownership and monitoring |
| Enterprise Integration Platform | Core Deposit System | Posting request, posting result and reconciliation reference | Retained-core adapter | Integration platform mediates core request and response | Legacy contract and reconciliation ownership |
| Payments Platform | Event Platform | Governed payment-status event | Asynchronous publication | Payments platform publishes event | Event-schema ownership and replay policy |
| Event Platform | Enterprise Data Platform | Governed payment-status subscription | Asynchronous event subscription | Data platform subscribes to governed event | Lineage, retention and consumer-access ownership |

This view is especially useful when the problem is point-to-point complexity, duplicated interfaces or unclear ownership. It is less useful when the question is business value, user experience or detailed process sequence.

Keep integration landscapes honest. Label the integration style where it matters: synchronous API, asynchronous event, managed file transfer, replicated data, manual upload or operational report. An unlabelled relationship between two systems is often too vague for review.

## Architecture roadmaps

An architecture roadmap answers: **how does the architecture move from current state to target state through planned intermediate states?**

Roadmaps are useful because architecture change rarely happens in one release. A roadmap can show time horizons, transition states, dependencies, decision points and sequencing. ArchiMate implementation and migration concepts can support this kind of modelling, but a roadmap may also be a simpler table or timeline when formal notation is unnecessary [OPEN-GROUP-ARCHIMATE-4].

For Horizon Bank platform evolution, a roadmap might show:

| Horizon | Architecture change | Dependency or risk |
|---|---|---|
| Current | Core Deposit System and point-to-point integration remain dominant | High reconciliation effort |
| Near-term transition | Payments Platform uses Enterprise Integration Platform adapters | Adapter ownership, service-level monitoring and operating model decision needed |
| Later transition | Event Platform publishes governed payment-status events | Event schema governance, consumer access control and replay policy needed |
| Target direction | Modular payments, customer and data platforms support governed reuse | Legacy coexistence remains explicit until exit evidence is accepted |

FIG-13-04 is planned as a simple platform evolution roadmap. It should show architecture states and dependencies, not a project plan with every delivery task.

A roadmap is not a promise by itself. It records an intended sequence under known assumptions. A useful roadmap states dependencies, risks, assumptions, decision points and exit evidence for each state. If funding, regulation, vendor constraints or operational risk change, the roadmap should be reviewed.

## Heat maps

A heat map answers: **where is attention needed most?**

Heat maps overlay a rating onto a stable structure such as capabilities, applications, processes, data domains or technology platforms. The rating may represent risk, cost, maturity, business value, technical debt, regulatory exposure, operational pain or investment priority.

For Horizon Bank, a capability heat map might score the same capability across separate dimensions:

| Capability | Current pain | Strategic importance | Delivery risk | Basis |
|---|---|---|---|---|
| Payment Screening | H | H | M | Regulatory scrutiny and screening traceability need attention. |
| Account Servicing | M | H | H | Legacy dependency affects change sequencing. |
| Digital Servicing | H | H | M | Customer experience is strategically visible. |
| Data Governance | M | H | H | Cross-bank data quality and access rules affect many initiatives. |
| Event Governance | M | M | H | Reuse depends on schema ownership and consumer controls. |

Use `H`, `M` and `L` labels even when colour is also used. The map becomes useful only when the scoring basis is explicit. The figure should record date, owner and version, and should state that the scores are illustrative.

FIG-13-05 is planned as a capability heat map. It should use labels and a legend so colour is not the only carrier of meaning.

Common heat-map mistakes are easy to spot. The model may use red, amber and green without saying what they mean. It may mix several scoring dimensions into one colour. It may imply false precision from subjective workshop votes. It may hide disagreement by averaging scores. A good heat map says who scored it, what criteria they used, when it was scored, which version is being viewed and what action the rating should trigger.

## Wardley maps

A Wardley map answers: **what do users need, what components support that need, how evolved are those components, and what strategic options follow?**

Wardley mapping is a strategy mapping technique created by Simon Wardley. The official Wardley Maps site describes the technique as a way to map the competitive landscape, improve situational awareness, identify dependencies and discuss component evolution [WARDLEY-MAPS-OFFICIAL-2026].

A Wardley map normally starts with a user need. Below that, it places components in a value chain. Across the horizontal axis, it places components by evolution, from novel or uncertain on the left toward commodity or utility on the right. Dependencies connect the components.

For Horizon Bank payment modernisation, a simplified Wardley map might include:

| Component | Why it appears | Possible evolution discussion |
|---|---|---|
| Retail Customer payment need | Anchor for the map | Stable need, but expectations evolve |
| Digital payment experience | Visible customer value | Differentiation may matter |
| Payment orchestration | Core capability for the bank | Build or modernise deliberately |
| Financial crime screening service | Regulatory screening capability | Specialist service maturity may change build-versus-buy options |
| Fraud decisioning service | Risk decisioning capability | Product maturity and bank-specific rules may need separate treatment |
| Payment-status event distribution | Shared integration capability | Standardise governance and reuse |
| Customer and account data access | Data dependency for payment execution | Visibility is lower than customer experience, but reliability matters |
| Compute service | Supporting platform capability | Treat as commodity where possible |
| Storage service | Supporting platform capability | Treat as commodity where possible |
| Network service | Supporting platform capability | Treat as commodity where possible |

The dependency lines on a Wardley map show value-chain dependency, not API direction, data lineage or implementation sequence. For the Horizon Bank example, the assumed chain is: customer need depends on the digital payment experience; that experience depends on payment orchestration; payment orchestration depends on screening, fraud decisioning, customer and account data access, payment-status event distribution and commodity platform services. These positions are illustrative positions for discussion, not factual assessments of a real bank.

| Component | Depends on | Visibility | Assumed evolution stage | Rationale | Confidence or open question |
|---|---|---|---|---|---|
| Digital payment experience | Payment orchestration | High | Custom-built | Customer-visible experience may differentiate the bank. | Medium; challenge whether parts are becoming standard products. |
| Payment orchestration | Screening, fraud decisioning, customer and account data access, payment-status event distribution and platform utilities | Medium to high | Custom-built | Bank-specific payment sequencing and controls remain important. | Medium. |
| Financial crime screening service | Customer and account data access and platform utilities | Medium | Product or rental | Specialist products exist, while bank policy and integration remain specific. | Medium. |
| Fraud decisioning service | Customer and account data access and platform utilities | Medium | Product or rental | Mature products exist, with bank-specific models and rules. | Medium. |
| Payment-status event distribution | Compute, storage and network services | Low to medium | Product or rental | Event-platform products are mature, while governance remains organisation-specific. | Medium. |
| Customer and account data access | Retained banking systems and platform utilities | Low to medium | Custom-built | Access is shaped by the bank's domain models, controls and legacy estate. | Medium. |
| Compute service | Platform utility dependencies | Low | Commodity or utility | Standard infrastructure capability. | High. |
| Storage service | Platform utility dependencies | Low | Commodity or utility | Standard infrastructure capability. | High. |
| Network service | Platform utility dependencies | Low | Commodity or utility | Standard connectivity capability. | High. |

FIG-13-06 is planned as a payment modernisation Wardley map. It should be labelled as a strategic discussion map, not as a factual inventory.

Wardley maps are powerful because they expose assumptions. They are risky when teams treat the position of every component as objective truth. The map should invite challenge: Who is the user? What is the need? Which components really create value? Which dependencies are missing? Which components are becoming commodities? Which parts deserve innovation investment?

## Architecture Decision Records

An Architecture Decision Record answers: **what decision was made, why was it made, what alternatives were considered, and what consequences follow?**

An ADR is a small text record rather than a diagram. Michael Nygard's 2011 article popularised a lightweight pattern: keep records for architecturally significant decisions, number them, record their status, describe context, state the decision and record consequences [NYGARD-ADR-2011].

This repository uses `DECISIONS.md` in the same spirit. It keeps a central decision log rather than one ADR file per decision, because the book is still small enough for one indexed log to work. A software team may prefer one ADR per file so each decision can be linked, reviewed and superseded independently. Both patterns can be valid if the records are stable, searchable and retained.

An original Horizon Bank ADR might look like this:

| Field | Example content |
|---|---|
| ID | ADR-HB-001 |
| Title | Modernise payments incrementally through platform-mediated integration |
| Status | Proposed for teaching example |
| Context | Horizon Bank needs better payment status visibility, stronger screening traceability and reduced point-to-point integration, while the Core Deposit System remains operationally critical. |
| Decision | Use a Payments Platform with Enterprise Integration Platform adapters first, then publish governed payment-status events through the Event Platform. Do not replace all payment and core systems in one step. |
| Consequences | The bank must fund adapter ownership, monitoring, event-schema governance and legacy reconciliation during the transition. The approach reduces migration shock but extends coexistence work. |
| Alternatives considered | Big-bang core replacement; continue point-to-point integration; event-first migration without adapter governance. |

Nygard's original lightweight pattern emphasises status, context, decision and consequences. An `Alternatives considered` field is a useful local extension, but it should not be presented as mandatory in the original pattern [NYGARD-ADR-2011].

ADRs are useful when a diagram shows what the architecture is, but not why it became that way. A roadmap can show a transition path. An ADR can explain why the team chose incremental migration rather than a big-bang replacement. A security model can show a controlled support interface. An ADR can explain why privileged support access must be separate from customer traffic.

Do not write an ADR for every small preference. Record decisions that are significant, costly to reverse, likely to be questioned later, or important for compliance, risk, ownership or long-term maintainability.

## When to use specialised approaches

Use a specialised approach when the question would be awkward or misleading in the main notation.

| Question | Better specialised approach | Main audience | Why |
|---|---|---|---|
| Which requirement is addressed and verified? | SysML-style requirement trace | Analysts, architects and testers | Shows requirement, design response, verification case and evidence links. |
| Which business abilities need attention? | Capability map or heat map | Business architects, sponsors and portfolio teams | Separates business ability from process and application detail. |
| How does value progress for a stakeholder? | Value stream | Business architects, product owners and sponsors | Shows value stages before detailed process. |
| Which systems exist in the estate? | Application landscape | Enterprise architects, solution architects and application owners | Gives a wider estate view. |
| How do systems exchange information? | Integration landscape | Integration architects, solution architects and operations teams | Adds integration mechanisms and ownership. |
| How do we move from current to target? | Roadmap | Transformation leads, enterprise architects and sponsors | Shows transition states and dependencies. |
| Where is risk, cost or maturity weak? | Heat map | Portfolio teams, risk reviewers and sponsors | Overlays explicit ratings on a stable structure. |
| What strategic choices follow from user need and evolution? | Wardley map | Strategy, product and architecture leaders | Relates value-chain dependency to component evolution. |
| Why did we choose this architecture? | ADR | Architects, maintainers and governance reviewers | Captures rationale and consequences. |

The safest pattern is to use the smallest model that answers the question. Add another view only when it removes confusion or supports a real decision.

## Common mistakes

The first mistake is treating a specialised model as a universal diagram. A Wardley map is not a process model. A heat map is not a system landscape. An ADR is not a diagram.

The second mistake is skipping the question. A model called "architecture overview" often becomes a mixture of capabilities, applications, integrations, risks and roadmap items with no reviewable purpose.

The third mistake is hiding the scoring basis. Heat maps and maturity views need clear criteria, date, owner and scale.

The fourth mistake is using colour as the only meaning carrier. Labels, legends and text must carry the meaning.

The fifth mistake is mixing current state, target state and roadmap without labels. Readers must know whether a box exists now, is planned, or is only an option.

The sixth mistake is confusing value stream stages with process tasks. A value stream should stay at value-stage level unless the chapter deliberately switches to BPMN.

The seventh mistake is using landscapes as interface inventories. A landscape should show the relationships needed for the question. Detailed interface catalogues belong elsewhere.

The eighth mistake is deleting superseded decisions. A replaced decision is often still useful because it explains why the architecture changed.

## Chapter cheat sheet

| Approach | Question answered | Useful for | Watch out for |
|---|---|---|---|
| SysML | How do requirements, structure, behaviour and verification relate? | Systems engineering and traceability | Using too much formal notation for a simple software question |
| Capability map | What abilities does the organisation need? | Strategy, ownership and investment discussion | Calling process tasks capabilities |
| Value stream | How is value achieved for a stakeholder? | End-to-end value and capability alignment | Turning it into BPMN detail |
| Application landscape | Which systems exist and relate? | Estate understanding and rationalisation | Showing every interface and process step |
| Integration landscape | How is information exchanged? | API, event, adapter and integration ownership review | Vague unlabelled relationship arrows |
| Roadmap | How do we move through transition states? | Sequencing architecture change | Treating assumptions as delivery promises |
| Heat map | Where is attention needed? | Risk, maturity, cost or investment prioritisation | Hidden scoring and colour-only meaning |
| Wardley map | What strategic options follow from user need and evolution? | Strategy and situational awareness | Treating assumptions as objective facts |
| ADR | Why was this decision made? | Rationale, governance and future review | Recording every minor preference |

## Key takeaways

- Specialised models are useful when they answer a focused question better than the main notations.
- SysML is valuable for requirements, system structure, behaviour and verification traceability, especially in systems engineering.
- Capability maps and value streams support business architecture, but they should not be confused with detailed process flow.
- Landscapes help readers understand estates, while integration landscapes add exchange mechanisms and ownership.
- Roadmaps show intended architecture evolution through transition states and dependencies.
- Heat maps need explicit scoring criteria, date, owner and legend.
- Wardley maps are strategic assumption maps, not factual inventories.
- ADRs preserve decision rationale so future readers understand why the architecture is the way it is.

## Practical exercise

Horizon Bank is planning a payment modernisation initiative. The bank wants to improve customer payment experience, reduce point-to-point integration, strengthen screening traceability, publish governed payment-status events and retire some legacy integration paths over several years.

Choose the right model for each question:

1. Which model should show the customer need, payment experience, orchestration, screening, payment-status event distribution and commodity platform components against an evolution axis?
2. Which model should show the current Core Deposit System, Payments Platform, Financial Crime Platform, Enterprise Integration Platform and Event Platform relationships?
3. Which model should show whether Payment Screening, Event Governance and Data Governance have high risk or low maturity?
4. Which model should show the transition from point-to-point integration to platform-mediated APIs and governed events over time?
5. Which model should explain why the bank chose incremental migration rather than replacing all payment systems at once?
6. Which model should show whether a checkout security requirement is addressed by design and verified by a test?
7. Which model should show the end-to-end value stages for onboarding a new customer?

Suggested answer:

- Use a Wardley map for user need, components and evolution.
- Use an application landscape for the systems and their high-level relationships.
- Use a capability heat map for risk or maturity over stable capabilities.
- Use an architecture roadmap for transition states and sequencing.
- Use an ADR for the migration decision and its consequences.
- Use a SysML-style requirement trace for requirement, design and verification links.
- Use a value stream for stakeholder value stages.

## Review checklist

- [ ] The question answered by each model is explicit.
- [ ] The audience and abstraction level are clear.
- [ ] Formal terms are introduced after a plain-language explanation.
- [ ] Formal standards are distinguished from practitioner techniques and local conventions.
- [ ] The simple and banking examples are consistent with repository example files.
- [ ] Comparisons do not imply that one notation is universally superior.
- [ ] Common mistakes are concrete and actionable.
- [ ] Required source notes and diagram specifications are registered.
- [ ] No diagram source is created until the author approves the corresponding specification.
- [ ] Terminology, link and word-count checks pass.

## References and further reading

Chapter source notes are maintained in the repository under `research/other-modelling/`, with related notes under `research/archimate/` and `research/c4/`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index once the appendix is completed.

- `[OMG-SYSML-2.0]`: Object Management Group, SysML, version 2.0.
- `[OPEN-GROUP-ARCHIMATE-4]`: The Open Group, ArchiMate 4 Specification.
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`: The Open Group, TOGAF Series Guides for Business Capabilities and Value Streams.
- `[AUTHOR-HEAT-MAP-CONVENTIONS-2026]`: Repository-local Chapter 13 heat-map scoring and legend convention.
- `[C4-OFFICIAL]`: Official C4 model documentation.
- `[WARDLEY-MAPS-OFFICIAL-2026]`: Simon Wardley / SWARDLEYMAPS LTD, official Wardley Maps site and book resources.
- `[NYGARD-ADR-2011]`: Michael Nygard, Documenting Architecture Decisions.
