---
title: "Other Useful Modelling Approaches"
chapter: 13
part: "part-02-modelling-languages"
status: "Diagramming"
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

- FIG-13-01: Online Store SysML Requirement Trace, specification created, source deferred pending author approval.
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
- `[C4-OFFICIAL]` supports system landscape framing where the landscape concern is software-system relationships.
- `[WARDLEY-MAPS-OFFICIAL-2026]` supports Wardley map provenance, purpose and licence notes.
- `[NYGARD-ADR-2011]` supports lightweight ADR practice and decision-log structure.

## Planned chapter structure

1. Explain why specialised models complement the main Part II modelling approaches.
2. Introduce SysML as a systems-engineering and traceability language, with a small requirement-trace example.
3. Introduce capability maps, value streams, landscapes, roadmaps, heat maps, Wardley maps and ADRs as focused architecture tools.
4. Compare the approaches by the question they answer and the audience they serve.
5. Close with common mistakes, a cheat sheet, key takeaways, practical exercise and source notes.

## Drafting notes

- Chapter 13 is currently in `Diagramming`.
- `FIG-13-01` through `FIG-13-06` are registered and have specifications.
- Do not create diagram source or exports until the author approves the corresponding specifications.
- Keep Chapter 14 deeper business-strategy coverage in mind. Chapter 13 should introduce capability, value stream and heat-map approaches without taking over Chapter 14's role.

## Why this chapter exists

The previous chapters introduced major modelling languages and approaches: Unified Modeling Language (UML), C4, Business Process Model and Notation (BPMN), ArchiMate, data modelling, Decision Model and Notation (DMN), domain and event modelling, infrastructure modelling and security modelling. Those techniques cover many architecture questions, but real architecture work often needs smaller specialised views.

A specialised model answers a focused question. It might show which requirement is satisfied by which design element, which capabilities need investment, which systems exist in a landscape, which changes happen over time, where risk is concentrated, or why a decision was made. These models are often practical and lightweight. Some are based on standards. Some are practitioner techniques. Some are local conventions used by one organisation.

The danger is treating every useful drawing as a formal notation. A heat map is useful, but its colours are only meaningful if the scoring basis is written down. A roadmap is useful, but it is not a delivery contract unless governance makes it one. A Wardley map is useful for strategy discussion, but it records assumptions about user need, dependency and evolution. The same discipline from Chapter 3 still applies: read the title, purpose, audience, scope, notation, legend, assumptions and omissions before trusting the model.

## SysML

SysML answers: **how do requirements, system structure, behaviour and verification relate in an engineered system?**

SysML is an Object Management Group (OMG) language for modelling systems. OMG SysML 2.0 is the current formal version checked for this chapter. The public OMG specification page describes SysML as a general-purpose modelling language for systems and model-based systems engineering, with support for requirements, structure, behaviour, analysis cases and verification cases [OMG-SYSML-2.0].

For a beginner architect, the most accessible SysML idea is requirement traceability. A requirement should not float by itself. It should be related to the design elements that satisfy it, the test or verification evidence that checks it, and any higher-level objective it supports.

For the Simple Online Store, a SysML-style requirement trace might show:

| Requirement | Design response | Verification evidence |
|---|---|---|
| Checkout must protect customer payment details | Online Store uses a Payment Provider System and does not store full card details | Security test result and provider integration review |
| Customer must receive order confirmation | Order service creates an order record and sends confirmation through the web or email channel | Functional test and message log sample |
| Support must view order status without viewing full payment details | Support interface shows masked payment status and order state | Access-control test and support-role review |

FIG-13-01 is planned as a small teaching view of this pattern. It should not introduce the full SysML language. The purpose is to show why requirement, design and verification links matter.

Use SysML when traceability across requirements, engineered parts, interfaces, behaviour, analysis and verification is important. Do not use it merely because a diagram has requirements on it. A plain table may be enough for simple software work.

## Capability maps

A capability map answers: **what abilities does the organisation need, independent of the current process or application structure?**

A capability is an ability an organisation has or needs in order to achieve an outcome. A capability map groups these abilities so leaders and architects can discuss investment, ownership, gaps and duplication without starting from the current organisation chart or application estate.

In Horizon Bank, capabilities might include Customer Onboarding, Party Management, Product Management, Payment Initiation, Payment Screening, Account Servicing, Fraud Management, Data Governance and Digital Servicing. A capability map does not show the process sequence for onboarding a customer. It shows what the bank must be able to do.

Capability maps are often used with heat maps. The capability map gives stable business structure. The heat map overlays a judgement such as current pain, investment priority, strategic importance, risk, maturity or application duplication.

Do not call every activity a capability. "Check documents" is likely a process step. "Customer Onboarding" or "Identity Verification" is more likely to be a capability. The distinction matters because capabilities are used for planning and ownership, while process steps are used for flow and operational detail.

Chapter 14 will go deeper into business strategy and capability modelling. This chapter only introduces the approach so readers recognise it as part of the broader modelling toolkit.

## Value streams

A value stream answers: **how does value move from a triggering stakeholder need to an outcome?**

A value stream is not the same as a detailed process model. It shows major stages of value creation from the perspective of a stakeholder. A BPMN process asks how work is performed in detail. A value stream asks what value is progressively achieved.

For Horizon Bank customer onboarding, a value stream might use stages such as:

| Stage | Value produced | Example enabling capabilities |
|---|---|---|
| Express need | Customer states intent to become a bank customer | Digital Servicing, Relationship Management |
| Capture information | Bank collects identity, contact and product information | Customer Onboarding, Document Capture |
| Verify and assess | Bank checks identity, eligibility and risk | Identity Verification, Financial Crime Screening, Risk Assessment |
| Open relationship | Bank creates customer and product records | Party Management, Account Opening, Product Management |
| Activate service | Customer can use selected channels and products | Digital Servicing, Notification Management, Account Servicing |

FIG-13-02 is planned as a Horizon Bank customer onboarding value stream. It should show value stages, stakeholder perspective and enabling capabilities, not BPMN tasks.

Use a value stream when the discussion is about end-to-end value, capability alignment or strategic change. Do not use it to replace the process model when exceptions, roles, sequence flows, message flows, timers or hand-offs matter.

## Application landscapes

An application landscape answers: **which applications or software systems exist in the estate, and how do they relate at a useful level of abstraction?**

Application landscapes are common in enterprise architecture because teams need to see more than one system at a time. A C4 System Landscape diagram is one structured way to show software systems and their relationships [C4-OFFICIAL]. ArchiMate application views can also show application components, services and relationships when enterprise architecture traceability matters [OPEN-GROUP-ARCHIMATE-4].

For Horizon Bank, an application landscape might show Horizon Digital Channels, Customer Onboarding Platform, Party and Customer Platform, Product Catalogue, Payments Platform, Financial Crime Platform, Core Deposit System, Enterprise Integration Platform, Event Platform and Enterprise Data Platform. The landscape should state whether it is current, target or mixed. It should also show only the relationships needed for the review question.

FIG-13-03 is planned as a Horizon Bank application landscape map. It should use stable system names from `examples/horizon-bank/system-landscape.md`.

Do not use an application landscape to show every interface, database table, batch job and business process step. If every arrow becomes important, the diagram probably needs to be split into an integration view, process view or sequence view.

## Integration landscapes

An integration landscape answers: **how do systems exchange information, and which integration mechanisms matter?**

An application landscape may show that two systems are related. An integration landscape adds how they communicate. It may show application programming interfaces (APIs), event topics, file transfers, message queues, adapters, gateways and integration platforms.

For Horizon Bank, an integration landscape might show that Horizon Digital Channels call Payments Platform APIs, Payments Platform uses Enterprise Integration Platform adapters to reach the Core Deposit System, Financial Crime Platform receives screening requests, Event Platform distributes payment-status events, and Enterprise Data Platform consumes selected events for reporting.

This view is especially useful when the problem is point-to-point complexity, duplicated interfaces or unclear ownership. It is less useful when the question is business value, user experience or detailed process sequence.

Keep integration landscapes honest. Label the integration style where it matters: synchronous API, asynchronous event, managed file transfer, replicated data, manual upload or operational report. An arrow labelled "integrates with" is often too vague for review.

## Architecture roadmaps

An architecture roadmap answers: **how does the architecture move from current state to target state through planned intermediate states?**

Roadmaps are useful because architecture change rarely happens in one release. A roadmap can show time horizons, transition states, dependencies, decision points and sequencing. ArchiMate implementation and migration concepts can support this kind of modelling, but a roadmap may also be a simpler table or timeline when formal notation is unnecessary [OPEN-GROUP-ARCHIMATE-4].

For Horizon Bank platform evolution, a roadmap might show:

| Horizon | Architecture change | Dependency or risk |
|---|---|---|
| Current | Core Deposit System and point-to-point integration remain dominant | High reconciliation effort |
| Transition 1 | Payments Platform uses Enterprise Integration Platform adapters | Adapter ownership and service-level monitoring needed |
| Transition 2 | Event Platform publishes governed payment-status events | Event schema governance and consumer access needed |
| Target | Modular payments, customer and data platforms support governed reuse | Legacy coexistence still managed deliberately |

FIG-13-04 is planned as a simple platform evolution roadmap. It should show architecture states and dependencies, not a project plan with every delivery task.

A roadmap is not a promise by itself. It records an intended sequence under known assumptions. If funding, regulation, vendor constraints or operational risk change, the roadmap should be reviewed.

## Heat maps

A heat map answers: **where is attention needed most?**

Heat maps overlay a rating onto a stable structure such as capabilities, applications, processes, data domains or technology platforms. The rating may represent risk, cost, maturity, business value, technical debt, regulatory exposure, operational pain or investment priority.

For Horizon Bank, a capability heat map might mark Payment Screening as high regulatory importance, Core Account Servicing as high legacy dependency, Digital Servicing as high strategic value, and Data Governance as high cross-bank dependency. The map becomes useful only when the scoring basis is explicit.

FIG-13-05 is planned as a capability heat map. It should use labels and a legend so colour is not the only carrier of meaning.

Common heat-map mistakes are easy to spot. The model may use red, amber and green without saying what they mean. It may mix several scoring dimensions into one colour. It may imply false precision from subjective workshop votes. It may hide disagreement by averaging scores. A good heat map says who scored it, what criteria they used, when it was scored and what action the rating should trigger.

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
| Screening and fraud checks | Regulatory and risk capability | Specialist platforms may mature |
| Event distribution | Shared integration capability | Standardise governance and reuse |
| Compute, storage and network | Supporting platform | Treat as commodity where possible |

FIG-13-06 is planned as a payment modernisation Wardley map. It should be labelled as a strategic discussion map, not as a factual inventory.

Wardley maps are powerful because they expose assumptions. They are risky when teams treat the position of every component as objective truth. The map should invite challenge: Who is the user? What is the need? Which components really create value? Which dependencies are missing? Which components are becoming commodities? Which parts deserve innovation investment?

## Architecture Decision Records

An Architecture Decision Record answers: **what decision was made, why was it made, what alternatives were considered, and what consequences follow?**

An ADR is a small text record rather than a diagram. Michael Nygard's 2011 article popularised a lightweight pattern: keep records for architecturally significant decisions, number them, record their status, describe context, state the decision and record consequences [NYGARD-ADR-2011].

This repository uses `DECISIONS.md` in the same spirit. For example, the decision not to map BIAN Service Domains automatically to microservices matters because it shapes later design, examples and review criteria. If that decision were hidden in a conversation, future readers would not know why the book keeps making that distinction.

ADRs are useful when a diagram shows what the architecture is, but not why it became that way. A roadmap can show a transition path. An ADR can explain why the team chose incremental migration rather than a big-bang replacement. A security model can show a controlled support interface. An ADR can explain why privileged support access must be separate from customer traffic.

Do not write an ADR for every small preference. Record decisions that are significant, costly to reverse, likely to be questioned later, or important for compliance, risk, ownership or long-term maintainability.

## When to use specialised approaches

Use a specialised approach when the question would be awkward or misleading in the main notation.

| Question | Better specialised approach | Why |
|---|---|---|
| Which requirement is satisfied and verified? | SysML-style requirement trace | Shows requirement, design and verification links |
| Which business abilities need attention? | Capability map or heat map | Separates business ability from process and application detail |
| How does value progress for a stakeholder? | Value stream | Shows value stages before detailed process |
| Which systems exist in the estate? | Application landscape | Gives a wider estate view |
| How do systems exchange information? | Integration landscape | Adds integration mechanisms and ownership |
| How do we move from current to target? | Roadmap | Shows transition states and dependencies |
| Where is risk, cost or maturity weak? | Heat map | Overlays a rating on a stable structure |
| What strategic choices follow from user need and evolution? | Wardley map | Relates value chain to component evolution |
| Why did we choose this architecture? | ADR | Captures rationale and consequences |

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
| Integration landscape | How is information exchanged? | API, event, adapter and integration ownership review | Vague "integrates with" arrows |
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

1. Which model should show the customer need, payment experience, orchestration, screening, event distribution and commodity platform components against an evolution axis?
2. Which model should show the current Core Deposit System, Payments Platform, Financial Crime Platform, Enterprise Integration Platform and Event Platform relationships?
3. Which model should show whether Payment Screening, Event Governance and Data Governance have high risk or low maturity?
4. Which model should show the transition from point-to-point integration to platform-mediated APIs and governed events over time?
5. Which model should explain why the bank chose incremental migration rather than replacing all payment systems at once?
6. Which model should show whether a checkout security requirement is satisfied by design and verified by a test?
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
- `[C4-OFFICIAL]`: Official C4 model documentation.
- `[WARDLEY-MAPS-OFFICIAL-2026]`: Simon Wardley / SWARDLEYMAPS LTD, official Wardley Maps site and book resources.
- `[NYGARD-ADR-2011]`: Michael Nygard, Documenting Architecture Decisions.
