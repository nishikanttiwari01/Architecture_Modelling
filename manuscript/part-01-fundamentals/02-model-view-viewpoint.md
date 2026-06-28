---
title: "Model, View and Viewpoint"
chapter: 2
part: "part-01-fundamentals"
status: "Ready for Author Approval"
author: "Nishikant Tiwari"
last_updated: "2026-06-28"
---

# 2. Model, View and Viewpoint

## Chapter purpose

Build a precise vocabulary for describing architecture representations and selecting stakeholder-oriented views.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain the difference between a model, a view and a viewpoint.
- Connect stakeholders and concerns to the views they need.
- Use abstraction and decomposition without mixing unrelated levels of detail.
- Maintain consistency between views that describe the same system or enterprise.
- Create a small viewpoint map and cross-view traceability matrix.
- Apply the ideas to the Simple Online Store and Horizon Bank examples.

## Prerequisites and dependencies

- Chapter 1: What Is Architecture Modelling?

## Required models and artefacts

- Viewpoint map
- Cross-view traceability matrix

## Worked examples

- Online store viewpoints
- Banking transformation viewpoints

## Source requirements

- `[ISO-42010]` supports vocabulary for architecture descriptions, stakeholders, concerns, architecture views and architecture viewpoints.
- Chapter examples are original and use the repository's Simple Online Store and Horizon Bank case studies.

## Why these terms are often confused

People often use model, view, viewpoint and diagram as if they mean the same thing. In casual conversation that may seem harmless. In architecture work it causes practical problems because people stop asking which audience, question and level of detail a representation is meant to serve.

A developer may ask for "the architecture diagram" and expect software responsibilities. A business sponsor may hear the same phrase and expect outcomes, capabilities and scope. A security reviewer may expect trust boundaries and sensitive data flows. If the modeller responds with one crowded picture, every stakeholder receives a partial answer and several important questions remain hidden.

This chapter separates the terms so that later chapters can use them consistently:

| Term | Plain explanation | Practical test |
|---|---|---|
| Model | A purposeful abstraction of part of reality. | What facts has it selected, and what has it omitted? |
| View | A representation prepared for particular stakeholder concerns. | Who is it for, and what question does it answer? |
| Viewpoint | A reusable convention for creating a type of view. | What rules, content and review questions guide this kind of view? |
| Diagram | A visual representation of selected model content. | Is this one picture, or the whole representation package? |

The official architecture-description vocabulary includes stakeholders, concerns, architecture views and architecture viewpoints [ISO-42010]. This book uses those ideas in practical language. The aim is not to turn every beginner into a standards specialist. The aim is to help the reader ask better questions before drawing or reviewing a model.

## What is a model?

A model is a deliberate representation of something more complex than the representation itself. It may describe a software system, a business process, a banking operating model, a data domain, a deployment environment or a planned migration.

The model is not the real thing. It is an abstraction created for a purpose. A model of the Simple Online Store may include Customer, Online Store, Payment Provider System and Delivery Partner System. It may leave out tax rules, database indexes, browser versions and warehouse shifts because those facts do not matter for the current conversation.

A model can be expressed through diagrams, tables, text, catalogues and decision records. For example, a software architecture model may include a C4 Container diagram, an interface catalogue, a list of ownership responsibilities and notes about known constraints. The diagram helps people see relationships quickly, but the model is broader than the diagram.

The first discipline of modelling is therefore selection. A modeller chooses which facts matter for the question. The second discipline is honesty. The modeller says what the model includes, what it excludes and what is still uncertain.

## What is a view?

A view is a representation of a system or enterprise from the perspective of related stakeholder concerns. It is not just a drawing style. It is a prepared answer for a particular audience.

Consider the Simple Online Store. The product owner may need a context view that shows customers, support agents, the store and external partners. The development team may need a logical software structure view that shows the web application, API application, order database and integration points. The operations engineer may need a deployment view that shows runtime environments, monitoring and support ownership.

Those views can all describe the same store. They should not contain identical detail. If they did, at least two of them would be poorly designed. A useful view selects the model content that addresses the concerns of its readers.

A view may contain one diagram, several diagrams, tables, explanatory prose and open issues. For example, a security view may include a data-flow diagram, a table of trust boundaries, a short list of assumptions and a review checklist. Calling all of that "the diagram" hides the work needed to make the representation useful.

## What is a viewpoint?

A viewpoint is a reusable convention for constructing and reviewing a type of view. If a view is the specific answer prepared for a situation, a viewpoint is the recipe for preparing that kind of answer.

A context viewpoint might say:

- Show the system or enterprise area of interest.
- Show the people, organisations and external systems around it.
- Label the relationships that cross the boundary.
- Exclude internal components unless they are needed to explain scope.
- Review whether the boundary, actors and external dependencies are clear.

Using that viewpoint, the team can create a specific context view for the Simple Online Store or for Horizon Bank's Payments Platform. The resulting views are different because the subjects differ, but the construction rules are similar.

Mature architecture work also separates viewpoint from notation, method and framework. A viewpoint says what kind of view is needed and how to judge it. A notation provides symbols and rules for expression. A method explains how the work is carried out. A framework may include viewpoints, methods, governance guidance and recommended modelling languages. The same viewpoint can sometimes be expressed in more than one notation.

This distinction matters when teams reuse good practice. A viewpoint can be standardised inside an organisation. A view is created for a specific system, project, date and audience. Confusing the two leads to weak governance: teams may copy a diagram without understanding the rules that made it useful.

## Stakeholders, concerns and viewpoints

Architecture views should start with stakeholders and concerns. A stakeholder is a person, group or organisation with an interest in the architecture. A concern is something that stakeholder needs the architecture description to address.

Concerns are best written as questions. "Security" is a topic. "Where does customer data cross a trust boundary?" is a concern that can guide a model. "Cost" is a topic. "Which legacy systems must remain during the first migration release?" is a concern.

The viewpoint map below is a practical way to connect stakeholders, concerns and views before drawing anything.

| Stakeholder | Concern written as a question | Useful viewpoint | Typical view content |
|---|---|---|---|
| Business sponsor | What outcome is in scope, and which external parties are involved? | Context viewpoint | System boundary, customers, partners, major external systems |
| Product owner | Which users and journeys are affected? | User interaction viewpoint | Actors, goals, journeys, channels and major handovers |
| Developer | Which software parts own which responsibilities? | Software structure viewpoint | Containers, components, interfaces and dependencies |
| Data specialist | Where does important data originate and move? | Data viewpoint | Data entities, ownership, stores, flows and lineage |
| Security reviewer | Where do trust boundaries and sensitive flows exist? | Security viewpoint | Trust zones, identities, data classifications and controls |
| Operations engineer | Where does it run, and who supports it? | Deployment viewpoint | Environments, runtime nodes, monitoring and operational ownership |
| Enterprise architect | How does this change fit the wider estate? | Landscape or capability viewpoint | Systems, capabilities, dependencies, lifecycle and roadmap position |

The table is not a universal rule. It is a thinking aid. In real work, one stakeholder may need several views and one view may serve several stakeholders. The important habit is to state the concern first, then choose the viewpoint.

## Abstraction and decomposition

Abstraction means leaving out lower-level detail so that a higher-level question can be answered. Decomposition means breaking a subject into smaller parts so that responsibilities and relationships can be understood.

Both are useful, but they must be handled carefully. A capability map abstracts away system design so that business leaders can discuss organisational abilities. A component view decomposes a software container so developers can discuss internal responsibilities. Mixing both levels in one diagram usually creates confusion.

The modeller should decide the level before choosing the notation:

| Level | Main question | Example content | Detail to avoid at this level |
|---|---|---|---|
| Conceptual | What ideas, outcomes or business concepts matter? | Customer, Order, Payment, Account, onboarding capability | Database columns, classes, pods, server names |
| Logical | What responsibilities and relationships should exist? | Web application, API application, account service, payment orchestration | Product-specific deployment settings unless needed |
| Physical | How is it implemented or operated? | Cloud region, cluster, database product, network zone, runtime instance | Broad business motivation unless it explains a design choice |

Good decomposition preserves context. If a container view shows an Online Store API Application, a component view may decompose that API into Order Component, Payment Component and Customer Component. The child view should still make clear which parent it belongs to. Otherwise the reader sees fragments without knowing how they fit.

## Consistency between views

Different views may show different facts, but they should not contradict each other without explanation. Consistency is not the same as duplication. A context view and a deployment view do not need the same detail, but they should use compatible names, boundaries and assumptions.

Common consistency checks include:

- The same element has the same name unless there is a stated reason.
- A system shown as external in one view is not silently treated as internal in another.
- A relationship shown in a detailed view is traceable to a higher-level dependency.
- Current-state, transition-state and target-state views are labelled.
- Security boundaries, data ownership and operational ownership are not contradicted across views.

A cross-view traceability matrix helps teams manage this without forcing every detail into every diagram.

| Architecture element or concern | Context view | Software structure view | Data view | Deployment view | Security view |
|---|---|---|---|---|---|
| Customer identity | Customer actor uses account features | Identity responsibility allocated to API or identity service | Customer and identity records identified | Runtime identity provider placement shown if relevant | Authentication and trust boundary reviewed |
| Order submission | Customer submits order to store | Web application calls API application | Order data ownership identified | Runtime path shown for production support | Sensitive data exposure checked |
| Payment authorisation | Store depends on payment provider | Payment component or integration owns call | Payment reference and status modelled | Network path to provider shown if needed | External trust boundary and control points shown |
| Delivery handover | Store depends on delivery partner | Delivery integration owns notification | Delivery address and tracking data identified | Integration runtime shown if operationally relevant | Personal data sharing reviewed |

The matrix does not replace views. It helps reviewers see whether important subjects are covered by the right views and whether the views agree.

## Viewpoint catalogue

A viewpoint catalogue is a reusable list of common viewpoint types. It helps teams avoid starting every modelling conversation from a blank page.

| Viewpoint | Main question | Common audience | Useful notation or form | Common mistake |
|---|---|---|---|---|
| Context | What is in scope, and what surrounds it? | Sponsors, product owners, delivery teams | C4 context, simple box-and-line view | Adding internal design too early |
| Capability | What abilities does the organisation need? | Business and enterprise architects | Capability map | Turning process steps into capabilities |
| Process | What happens over time to produce an outcome? | Business analysts, operations teams | BPMN, swimlane, activity view | Hiding decisions and exceptions |
| Software structure | Which software parts own which responsibilities? | Architects and developers | C4 container or component, UML component | Mixing deployment nodes with logical parts |
| Interaction | How do participants collaborate at runtime? | Developers, testers, analysts | Sequence diagram, C4 dynamic view | Showing only the happy path when failure matters |
| Data | What information exists, moves and changes? | Data architects, analysts, engineers | Conceptual data model, data-flow view, lineage view | Treating a physical schema as the whole data model |
| Deployment | Where does the system run? | Operations, platform, security teams | C4 deployment, UML deployment, cloud view | Omitting environment and support boundaries |
| Security | Where are threats, controls and trust boundaries? | Security and risk reviewers | Threat-model data-flow view, trust-boundary view | Using colour without labels or control meaning |
| Migration | How do we move from current to target? | Programme and architecture teams | Roadmap, transition architecture, dependency map | Drawing only the target and ignoring transition risk |

This catalogue is intentionally modest. Later chapters expand the individual notations. At this stage, the reader should focus on matching the viewpoint to the concern.

## Worked mapping exercise

Imagine the Simple Online Store is adding returns. Customers can request a return, support agents can approve exceptions, the store may trigger a refund through the payment provider and the delivery partner may collect the parcel.

A sensible first modelling plan might be:

| Step | Modelling choice | Reason |
|---|---|---|
| 1 | Create a context view | Establish customers, support agents, payment provider and delivery partner before internal design detail. |
| 2 | Create a process view | Show how a return request moves through approval, refund and collection. |
| 3 | Create a software structure view | Allocate responsibilities between web application, API application, order data and integrations. |
| 4 | Create a data view | Clarify which return, refund and delivery data is stored or shared. |
| 5 | Create a security view if sensitive data or refund controls are material | Review trust boundaries, authorisation and fraud risk. |

For Horizon Bank, consider a digital onboarding transformation. The stakeholder set is wider, so the viewpoint map becomes more important:

| Stakeholder | First concern | First useful view |
|---|---|---|
| Retail banking sponsor | Which customer outcome and channels are in scope? | Capability or context view |
| Compliance team | Where are Know Your Customer and Anti-Money Laundering checks performed? | Process and control view |
| Data office | Which party, identity and account data is mastered where? | Conceptual data and lineage view |
| Solution architecture team | Which systems collaborate during onboarding? | System landscape and container views |
| Security team | Where are identity proofing, consent and sensitive data protected? | Trust-boundary and authentication views |
| Operations team | Which services must be monitored and supported? | Deployment and operations view |

No single view should carry all of that detail. The modelling task is to create a coherent set of views, each with a clear purpose, and then maintain traceability between them.

## Chapter summary and knowledge check

The central idea of this chapter is straightforward: a model selects facts, a view presents selected model content for stakeholder concerns, and a viewpoint guides how a type of view should be created and reviewed.

Use these questions to test understanding:

| Question | Good answer should include |
|---|---|
| Why is a model not the real system? | It is a purposeful abstraction that selects and omits facts. |
| Why is a view not just a diagram? | It may include diagrams, tables, prose, assumptions and review questions for stakeholder concerns. |
| What is the difference between a view and a viewpoint? | A view is specific to a system and situation. A viewpoint is the reusable convention for that type of view. |
| Why should concerns be written as questions? | Questions guide scope, content, notation and review. |
| What does cross-view consistency mean? | Views can differ in detail but should not contradict names, boundaries, relationships or assumptions. |

If the reader can answer those questions, later chapters on UML, C4, BPMN, ArchiMate, data and BIAN will be easier to understand.

## Key takeaways

- A model is a purposeful abstraction, not a complete copy of reality.
- A view is prepared for stakeholder concerns, not for decoration.
- A viewpoint is a reusable convention for creating and reviewing a type of view.
- Concerns are most useful when written as concrete questions.
- Abstraction hides detail for a purpose, while decomposition breaks a subject into understandable parts.
- Different views should be consistent without containing identical detail.
- A viewpoint catalogue helps teams choose suitable views repeatably.
- Traceability between views prevents architecture descriptions from becoming disconnected fragments.

## Practical exercise

You are helping Horizon Bank plan a new mobile payment feature. Customers can submit payments through the mobile app. The bank must validate the payment, check fraud and sanctions rules, post to accounts, notify the customer and support operations after release.

Create a modelling plan with four views:

1. Identify the stakeholder for each view.
2. Write one concern as a question for each stakeholder.
3. Choose a viewpoint for each concern.
4. State one thing each view should deliberately exclude.

Suggested answer:

| Stakeholder | Concern | Viewpoint | Deliberate exclusion |
|---|---|---|---|
| Retail banking sponsor | Which customer and business outcome is in scope? | Context or capability viewpoint | Internal class or database detail |
| Compliance reviewer | Where are sanctions and fraud checks performed? | Process and control viewpoint | Cloud node names unless relevant to control operation |
| Solution architect | Which systems collaborate during payment submission? | System landscape or container viewpoint | Detailed user-interface screens |
| Operations engineer | Where does the payment capability run and how is it supported? | Deployment viewpoint | Business capability taxonomy unless needed for ownership |

The exact answer can vary. A strong answer connects each view to a stakeholder concern and explains what is intentionally left out.

## Review checklist

- [ ] The model has a clear purpose and stated omissions.
- [ ] Each view names its stakeholder audience.
- [ ] Each stakeholder concern is written as a question.
- [ ] The chosen viewpoint fits the concern and abstraction level.
- [ ] Conceptual, logical and physical details are not mixed accidentally.
- [ ] Decomposed views identify the parent element they explain.
- [ ] Cross-view names, boundaries and relationships are consistent.
- [ ] Current, transition and target states are labelled when time matters.
- [ ] Tables, diagrams and prose agree with each other.
- [ ] Source keys are preserved for normative vocabulary.

## References and further reading

Chapter source notes are maintained in the repository under `research/fundamentals/` and registered in `SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index once the appendix is completed.

- `[ISO-42010]`: ISO/IEC/IEEE 42010:2022, architecture-description vocabulary and concepts.
