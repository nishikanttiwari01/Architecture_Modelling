---
title: "ArchiMate"
chapter: 7
part: "part-02-modelling-languages"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-06-29"
---

# 7. ArchiMate

## Chapter purpose

Explain enterprise architecture modelling across strategy, business, application, technology and transformation layers.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain what ArchiMate is and where it helps enterprise architecture work.
- Read basic ArchiMate elements across strategy, business, application, technology, motivation and migration views.
- Distinguish ArchiMate from The Open Group Architecture Framework (TOGAF), C4 and Business Process Model and Notation (BPMN).
- Select an ArchiMate view for a realistic architecture question.
- Apply ArchiMate ideas to the Simple Online Store and Horizon Bank examples.
- Avoid common ArchiMate mistakes, especially over-large layered diagrams, mixed abstraction and notation decoration.

## Prerequisites and dependencies

- Chapter 6: BPMN: Business Process Model and Notation

## Required models and artefacts

- FIG-07-01: Retail banking capability map, specification prepared, source deferred pending author approval
- FIG-07-02: Horizon Bank layered architecture view, specification prepared, source deferred pending author approval
- FIG-07-03: Horizon Bank application cooperation view, specification prepared, source deferred pending author approval
- FIG-07-04: Horizon Bank technology view, specification prepared, source deferred pending author approval
- FIG-07-05: Horizon Bank motivation view, specification prepared, source deferred pending author approval
- FIG-07-06: Horizon Bank implementation and migration view, specification prepared, source deferred pending author approval

## Worked examples

- Retail bank capability map
- Horizon Bank layered architecture

## Source requirements

- `[OPEN-GROUP-ARCHIMATE-3.2]` supports ArchiMate 3.2 terminology and language structure.
- Chapter guidance is the author's practical interpretation for beginner architecture work.
- Diagrams are planned as original teaching examples and must not reproduce The Open Group specification diagrams.

## What ArchiMate is

ArchiMate is a modelling language for enterprise architecture. In plain language, it helps architects show how business needs, capabilities, processes, applications, data, technology and change work relate to each other.

It answers questions such as: **which business capability is supported by which application service, which application component provides that service, and which technology platform hosts it?** That is a different question from "what are the steps in this process?" or "what classes are inside this component?"

The official ArchiMate specification is maintained by The Open Group [OPEN-GROUP-ARCHIMATE-3.2]. This chapter does not reproduce the full language. It teaches the subset that beginners most often need for architecture conversations: layers, common elements, common relationships and practical viewpoints.

ArchiMate is useful when a team needs traceability across different architecture domains. A single view might show that the Customer Onboarding capability is realised by a business process, supported by the Customer Onboarding Platform, exposed through an application service and hosted on a target cloud platform. That trace is difficult to express in BPMN or C4 alone.

ArchiMate is not a process notation, a user-interface design tool or a replacement for detailed software design. It is strongest when the question crosses business, application and technology boundaries at enterprise architecture level.

## ArchiMate and TOGAF

ArchiMate and TOGAF are related, but they are not the same thing. TOGAF is an enterprise architecture framework and method. ArchiMate is a modelling language that can be used to describe architecture content.

A practical way to remember the distinction is this: TOGAF helps structure the work, while ArchiMate helps represent selected results of the work. TOGAF may guide an architecture team through baseline architecture, target architecture, migration planning and governance. ArchiMate can then show the baseline application landscape, target capabilities, motivation for change and transition plateaus.

An organisation can use ArchiMate without adopting the full TOGAF method. It can also use TOGAF and choose other notations for some work products. The two are compatible, but one does not force the other.

For beginners, the important point is to choose the notation because it answers a question. Do not draw ArchiMate symbols only because a governance template asks for an enterprise architecture model. A useful ArchiMate view should still have a title, purpose, audience, scope and clear exclusions.

## Strategy layer

The strategy layer answers: **what abilities and resources does the organisation need, and how will it pursue its goals?**

Common strategy elements include capabilities, resources, value streams and courses of action. A capability describes an ability the organisation has or needs, such as Customer Onboarding, Payment Processing or Fraud Investigation. A value stream describes stages that deliver value to a stakeholder. A course of action describes an approach or direction, such as "consolidate customer identity across products".

For Horizon Bank, a retail banking capability map might include Customer Management, Account Management, Payments, Lending, Cards, Financial Crime Management and Customer Support. This is not a process model. It does not show the order of onboarding tasks. It shows stable abilities that the bank must manage, improve and govern.

The strategy layer is useful early in architecture work because it separates what the organisation needs to be able to do from the current applications that happen to do it. That distinction matters in Horizon Bank because the starting problems include product-specific silos and duplicate customer databases.

Use strategy elements when capability ownership, investment planning or transformation scope is the main question. Do not use them to describe detailed workflow steps.

## Business layer

The business layer answers: **what business roles, behaviour, services and information are involved?**

Common business elements include business actors, roles, collaborations, interfaces, processes, functions, events, services, objects, contracts and products. A business actor might be Retail Customer or Horizon Bank. A business role might be Customer Support Agent. A business process might be Customer Onboarding. A business service might be Open Current Account or Submit Payment Instruction.

This layer overlaps with the territory of BPMN, but the purpose is different. BPMN is usually better for detailed process flow, gateways, timers, pools and message exchange. ArchiMate is better when the process needs to connect upward to capabilities and downward to applications and technology.

For example, Chapter 6 used BPMN to show the flow of customer onboarding. In ArchiMate, the same area might be represented as the Customer Onboarding business process realising the Open Customer Profile business service, serving the Retail Customer role and using the Identity Evidence business object.

The business layer should stay at architecture level. If the view contains every click, screen and exception branch, it has probably moved beyond what ArchiMate is meant to communicate.

## Application layer

The application layer answers: **which application components provide which services and use which data?**

Common application elements include application components, collaborations, interfaces, functions, processes, events, services and data objects. An application component is a modular part of the application architecture. An application service is behaviour exposed by an application for use by people, business processes or other applications.

For Horizon Bank, Customer Onboarding Platform, Party and Customer Platform, Financial Crime Platform, Payments Platform and Enterprise Integration Platform are application components from the repository example landscape. Customer Screening Request, Customer Profile Management and Payment Status Query could be application services, depending on the view's scope.

The application layer is often where ArchiMate becomes useful for traceability. It can show that a business process uses an application service, and that the service is realised by one or more application components. This helps a team avoid a common problem: discussing application replacement without knowing which business capabilities or services depend on the application.

Do not confuse an ArchiMate application component with a C4 component. A C4 component sits inside one container. An ArchiMate application component is an enterprise architecture element and may represent a larger application or a modular part of an application estate. Use the term that matches the notation and level of abstraction.

## Technology layer

The technology layer answers: **which technology services, nodes, devices, networks and artefacts support the applications?**

Common technology elements include nodes, devices, system software, technology services, communication networks, paths and artefacts. At architecture level, a node might represent a cloud application runtime, an integration platform runtime or a managed database service. An artefact might represent a deployable package, configuration item or stored data structure when that detail is needed.

For Horizon Bank, a technology view might show that Customer Onboarding Platform runs on a target cloud application platform, uses a managed relational database, sends events through the Event Platform and connects to retained legacy systems through the Enterprise Integration Platform.

This layer is not the same as a detailed deployment diagram. A UML deployment diagram or C4 deployment view may be better when the question is runtime placement, execution nodes, protocols and operational responsibility. ArchiMate is useful when the technology view must remain connected to business and application architecture.

Keep technology views readable. If every subnet, firewall rule, cluster, pod and storage volume appears in one ArchiMate diagram, the view will stop answering an enterprise architecture question.

## Physical layer

The physical layer answers: **which physical facilities, equipment, distribution networks or materials matter to the architecture?**

Many digital architecture models do not need physical elements. They become useful when the architecture depends on branches, cash machines, devices, warehouses, telecommunications equipment, production facilities or material movement.

For a retail bank, a physical view might show branch locations, cash devices and network connectivity at a high level. For the Simple Online Store, physical elements might matter if the architecture discussion includes fulfilment centres, packing stations or delivery hand-off points.

Use the physical layer only when physical reality affects the design decision. Do not add it just because the language provides the elements.

## Motivation elements

Motivation elements answer: **why does this architecture need to change, and what constraints shape the answer?**

Common motivation elements include stakeholders, drivers, assessments, goals, outcomes, principles, requirements and constraints. They help connect architecture views to reasons rather than treating diagrams as neutral pictures.

For Horizon Bank, drivers might include slow product launches, duplicate customer databases and limited end-to-end process visibility. Goals might include improved straight-through processing and a trusted party and customer view. Requirements might include reusable customer identity services, auditability of screening decisions and integration with retained core systems.

Motivation views are useful in review meetings because they expose the logic behind the design. If the target application view does not support the stated goals, the inconsistency is visible. If a constraint is missing, such as a retained legacy system or regulatory record-keeping need, the team can correct the model before turning it into delivery work.

Avoid turning motivation views into slogan maps. Goals should be concrete enough to test against architecture choices. A goal such as "be digital" is too vague. A goal such as "reduce duplicate customer capture across retail products" gives the architecture team something to trace.

## Implementation and migration elements

Implementation and migration elements answer: **how does the architecture move from current state to target state?**

Common elements include work packages, deliverables, implementation events, plateaus and gaps. A plateau represents a stable architecture state, such as Current State, Transition State 1 or Target State. A gap represents the difference between two plateaus.

For Horizon Bank, a migration view might show a current plateau with product-specific onboarding and duplicate customer stores, a transition plateau where Customer Onboarding Platform and Party and Customer Platform are introduced for new retail products, and a target plateau where onboarding services are reused across retail and small business channels.

This view helps keep transformation realistic. It shows that enterprise architecture is not only a target picture. It must also describe sequencing, dependency, risk and temporary coexistence.

Do not use migration elements as a project plan substitute. They show architecture-level change, not every task in a delivery schedule.

## Core relationships

ArchiMate diagrams are only useful when the relationships carry meaning. Boxes without clear relationships are inventory, not architecture.

Common relationships include composition, aggregation, assignment, realisation, serving, access, flow, triggering, influence, association and specialisation [OPEN-GROUP-ARCHIMATE-3.2]. A beginner does not need to memorise every relationship on day one, but the modeller must use them consistently.

Some practical interpretations are:

| Relationship | Plain meaning | Example |
|---|---|---|
| Composition | This thing is made of these parts | Customer Management capability contains Customer Onboarding capability |
| Realisation | This element fulfils or implements another | Customer Onboarding Platform realises Customer Capture service |
| Serving | This element provides useful behaviour to another | Customer Profile Management service serves Customer Onboarding process |
| Assignment | This active element performs this behaviour | Customer Support Agent performs Review Exception |
| Access | This behaviour uses or changes information | Open Customer Profile process accesses Customer Record |
| Flow | Something passes from one element to another | Screening Request flows to Financial Crime Platform |
| Triggering | One behaviour starts or follows another | Application Submitted triggers Customer Onboarding |
| Influence | One motivation element affects another | Duplicate customer data influences the goal of trusted customer view |

Relationship direction matters. If the arrow direction is wrong, the model can imply the wrong dependency. Label relationships when the meaning is not obvious to the audience.

## Common viewpoints

An ArchiMate viewpoint is a reusable way to select content for a concern. The important beginner question is: **which view will help this audience make a decision?**

Useful early viewpoints include:

| Viewpoint | Question answered | Typical audience |
|---|---|---|
| Capability map | What abilities does the organisation need or improve? | Business architects, sponsors and portfolio teams |
| Layered view | How do business, application and technology elements connect? | Enterprise and solution architects |
| Application cooperation view | How do application components collaborate and expose services? | Solution architects and application owners |
| Technology view | What technology services and nodes support the applications? | Platform, infrastructure and operations teams |
| Motivation view | Why is the change needed and what constrains it? | Sponsors, architects and reviewers |
| Implementation and migration view | What changes between current, transition and target states? | Transformation, delivery and governance teams |

Do not put every element in every view. A capability map should not include database tables. A technology view should not include every business goal. A migration view should show meaningful architecture states, not a detailed Gantt chart.

## ArchiMate versus C4

ArchiMate and C4 can both show systems and relationships, but they serve different levels of discussion.

C4 is strongest for software architecture communication. It helps teams explain a software system, its containers, components, dynamic interactions and deployment. It is compact and familiar to developers.

ArchiMate is stronger when the view must connect strategy, business services, application services, technology services, motivation and migration. It supports enterprise architecture traceability across domains.

For the Simple Online Store, a C4 container view is usually the better first diagram when the team wants to understand the web application, API, database and external payment provider. ArchiMate becomes useful when the store is part of a wider enterprise transformation involving capabilities, operating model, applications, fulfilment facilities and migration states.

For Horizon Bank, both may be needed. ArchiMate can show how Customer Onboarding capability, business services, application services and platforms fit into the target enterprise architecture. C4 can then zoom into the Customer Onboarding Platform and explain its containers and components.

## ArchiMate versus BPMN

ArchiMate and BPMN also overlap, but they answer different process questions.

BPMN is stronger when the reader needs process sequence, gateways, events, timers, pools, lanes and message flows. Chapter 6 used BPMN to show onboarding and payment repair behaviour.

ArchiMate is stronger when the reader needs to place a business process in a wider architecture context. It can show that Customer Onboarding is part of Customer Management, realises a business service, uses Customer Profile Management from the Party and Customer Platform, and is constrained by screening requirements.

Use BPMN when process flow and exception behaviour are the focus. Use ArchiMate when process content needs to connect to capabilities, services, applications, technology and change.

## Common mistakes

The first mistake is creating a one-page enterprise map that shows everything. A diagram with every capability, process, application, database, network and project usually answers no question well.

The second mistake is using ArchiMate as decoration. If every relationship is a generic association, the diagram may look formal while saying very little. Choose relationships that express dependency, realisation, serving, access or flow.

The third mistake is mixing abstraction levels. A view that combines "Customer Management capability", "click Submit", "Customer table column" and "Kubernetes pod" is probably not a coherent architecture view.

The fourth mistake is treating ArchiMate as a replacement for specialist notations. Use BPMN for detailed business process flow, C4 for software structure and UML when its software or behavioural notation is the better fit.

The fifth mistake is ignoring motivation and migration. Enterprise architecture views should often show why the design exists and how change will happen, not only the target boxes.

The sixth mistake is inventing local meanings for standard symbols without explanation. If a team uses a simplified subset, document that subset and keep it consistent.

## Chapter cheat sheet

| Area | Plain question | Typical elements | Watch out for |
|---|---|---|---|
| Strategy | What abilities and direction matter? | Capability, resource, value stream, course of action | Do not turn process steps into capabilities |
| Business | What business behaviour and services are involved? | Actor, role, process, service, object | Do not replace BPMN detail when flow is the question |
| Application | Which applications provide which services? | Application component, service, interface, data object | Do not confuse with C4 component level |
| Technology | Which technology supports the applications? | Node, technology service, network, artefact | Do not model every infrastructure detail |
| Physical | Which real-world facilities or equipment matter? | Facility, equipment, material | Use only when physical context affects the decision |
| Motivation | Why is change needed? | Stakeholder, driver, goal, requirement, constraint | Avoid vague goals |
| Migration | How does architecture change over time? | Plateau, gap, work package, deliverable | Do not turn it into a project schedule |

## Key takeaways

- ArchiMate is an enterprise architecture modelling language for connecting business, application, technology, motivation and change.
- TOGAF is a framework and method; ArchiMate is a language that can represent selected architecture content.
- Use ArchiMate when the architecture question crosses domains and needs traceability.
- Use BPMN for detailed process flow and C4 for software architecture views.
- Capabilities describe organisational abilities, not task sequences.
- Relationship choice and direction are essential in ArchiMate.
- Motivation and migration views help explain why a target architecture exists and how the organisation can move towards it.
- Keep each view scoped to one audience and one decision.

## Practical exercise

Horizon Bank wants to reduce duplicate customer capture across retail products. It plans to introduce a Customer Onboarding Platform and a Party and Customer Platform while retaining the Core Deposit System during the first transition.

Create a small ArchiMate modelling plan before drawing:

1. Which capability or capabilities are in scope?
2. Which business service should be visible to the customer or channel?
3. Which application components support the change?
4. Which motivation elements explain the change?
5. Which migration states should be shown?

Suggested answer:

- Scope Customer Management and Customer Onboarding as capabilities. Avoid modelling every retail banking capability in the first view.
- Show a business service such as Open Customer Profile or Open Current Account, depending on the chosen scope.
- Include Customer Onboarding Platform, Party and Customer Platform, Financial Crime Platform, Horizon Digital Channels and retained Core Deposit System where they are relevant.
- Use drivers such as duplicate customer databases and slow product launches, with goals such as trusted customer view and improved straight-through processing.
- Show Current State, Transition State and Target State as plateaus if the question is migration. Keep delivery tasks and dates outside the first architecture view.

## Review checklist

- [ ] The view has a stated purpose, audience and architecture question.
- [ ] Business, application and technology elements are not mixed without a clear relationship.
- [ ] Capabilities describe abilities, not process steps.
- [ ] Application components and services are named consistently with the repository examples.
- [ ] Relationship types and directions are meaningful.
- [ ] Motivation elements explain why the architecture exists.
- [ ] Migration views distinguish current, transition and target states.
- [ ] The view does not replace BPMN, C4 or UML where those notations answer the question better.
- [ ] Diagram specifications are author-approved before source files are created.
- [ ] Terminology, link, diagram-register and manuscript checks pass.

## References and further reading

Chapter source notes are maintained in the repository under `research/archimate/` and registered in `SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index once the appendix is completed.

- `[OPEN-GROUP-ARCHIMATE-3.2]`: The Open Group ArchiMate 3.2 Specification.
