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

Explain enterprise architecture modelling across strategy, business, application, technology and transformation domains.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain what ArchiMate is and where it helps enterprise architecture work.
- Read basic ArchiMate 4 notation across strategy, business, application, technology, motivation and migration views.
- Distinguish ArchiMate from The Open Group Architecture Framework (TOGAF), C4 and Business Process Model and Notation (BPMN).
- Reuse the same ArchiMate model concepts across several stakeholder views.
- Apply ArchiMate ideas to the Simple Online Store and Horizon Bank examples.
- Avoid common ArchiMate mistakes, especially over-large diagrams, mixed abstraction and weak relationship semantics.

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
- Horizon Bank customer onboarding architecture

## Source requirements

- `[OPEN-GROUP-ARCHIMATE-4]` supports the current ArchiMate 4 version, terminology and public release changes.
- `[OPEN-GROUP-ARCHIMATE-3.2]` remains a historical source note only and is not the current normative source for this chapter.
- Chapter guidance is the author's practical interpretation for beginner architecture work.
- Diagrams are planned as original teaching examples and must not reproduce The Open Group specification diagrams.

## What ArchiMate is

ArchiMate is a modelling language for enterprise architecture. In plain language, it helps architects show how business needs, capabilities, processes, applications, data, technology and change work relate to each other.

It answers questions such as: **which capability is in scope, which business service is needed, which application service supports it, which application component provides that service, and which technology support is required?** That is a different question from "what are the steps in this process?" or "what classes are inside this component?"

The current official specification is ArchiMate 4, released by The Open Group in April 2026 [OPEN-GROUP-ARCHIMATE-4]. ArchiMate 4 changes some terminology from earlier versions. The most important beginner change is that the formal word **domain** replaces the older habit of speaking only about layers. Many practitioners still say business layer, application layer and technology layer in conversation, but this chapter uses **domain** when it refers to ArchiMate 4 formally.

ArchiMate is useful when a team needs traceability across architecture domains. A single model might connect Customer Onboarding capability, Open Customer Profile service, Customer Onboarding process, Customer Profile Management application service, Party and Customer Platform, and the technology services that host or support it.

ArchiMate is not a process notation, a user-interface design tool or a replacement for detailed software design. It is strongest when the question crosses business, application, technology, motivation and migration concerns at enterprise architecture level.

## ArchiMate and TOGAF

ArchiMate and TOGAF are related, but they are not the same thing. TOGAF is an enterprise architecture framework and method. ArchiMate is a modelling language that can be used to describe selected architecture content.

A practical way to remember the distinction is this: TOGAF helps structure the work, while ArchiMate helps represent selected results of the work. TOGAF may guide a team through baseline architecture, target architecture, migration planning and governance. ArchiMate can then show the baseline landscape, target capabilities, motivation for change and transition plateaus.

An organisation can use ArchiMate without adopting the full TOGAF method. It can also use TOGAF and choose other notations for some work products. The two are compatible, but one does not force the other.

For beginners, the important point is to choose ArchiMate because it answers a question. Do not draw ArchiMate symbols only because a governance template asks for an enterprise architecture model. A useful ArchiMate view still needs a title, purpose, audience, scope, legend and clear exclusions.

## Models, views and reuse

Chapter 2 explained that one model may support several views. ArchiMate makes that idea practical for enterprise architecture.

The model is the organised set of concepts and relationships: Customer Onboarding capability, Retail Customer actor, Open Customer Profile service, Customer Onboarding process, Party and Customer Platform, Customer Record and Transition State. A diagram is a view that selects some of those concepts for a stakeholder concern.

This matters because the same concept should be reused across views. If Customer Onboarding appears in a capability map, a layered view, an application cooperation view and a migration view, it should refer to the same model concept unless the diagram says otherwise. The diagrams are not unrelated copies. They are views over a shared enterprise model.

Reusing model concepts helps reviewers ask better questions:

| Reused concept | Appears in | Consistency question |
|---|---|---|
| Customer Onboarding capability | Capability map and layered view | Does the business process support the same capability that the map shows? |
| Customer Profile Management service | Layered and application cooperation views | Is the same application service used consistently? |
| Party and Customer Platform | Application, technology and migration views | Does the migration path explain how this component is introduced? |
| Trusted customer view goal | Motivation and migration views | Do the work packages and deliverables support the stated goal? |

If a diagram uses a different name, the reader may assume a different concept. That may be correct, but the model must say so.

## How to read ArchiMate notation

A beginner should read an ArchiMate diagram in three passes: identify element kinds, read relationship meaning and check the legend.

ArchiMate element kinds can be understood as a small set of questions:

| Kind | Plain question | Examples in this chapter |
|---|---|---|
| Active structure | Who or what can perform behaviour? | Actor, Role, Application Component, Technology Node, System Software |
| Behaviour | What does something do? | Process, Function, Event |
| Passive structure | What is used, produced or stored? | Business Object, Data Object, Artifact |
| Service | What externally visible behaviour is offered? | Open Customer Profile, Customer Profile Management, API Gateway Service |
| Strategy | What ability or direction matters? | Capability, Value Stream, Course of Action |
| Motivation | Why is this needed or constrained? | Stakeholder, Driver, Assessment, Goal, Outcome, Requirement, Principle |
| Implementation and migration | How does the architecture change? | Work Package, Deliverable, Plateau, Event |

Relationships carry the meaning. Read them before trusting the diagram:

| Relationship | Plain meaning | Direction to check |
|---|---|---|
| Composition | Strong whole-to-part structure | From whole to part |
| Aggregation | Weaker grouping | From grouping to member |
| Assignment | An active element performs behaviour | From performer to behaviour |
| Realisation | One element fulfils another | From realising element to realised element |
| Serving | One element provides behaviour to another | From provider to consumer |
| Access | Behaviour uses, reads or writes passive structure | From behaviour to passive structure |
| Flow | Something is transferred | From source to target |
| Triggering | One behaviour starts or follows another | From trigger to triggered behaviour |
| Influence | One motivation element affects another | From influencing element to influenced element |
| Association | A weak or general relationship | Direction may be absent or non-semantic |

Direction matters. A service serving a process is different from a process serving a service. A component assigned to a function is different from a function assigned to a component.

Nesting can be used to show containment or grouping, but it must not hide relationship meaning. If a diagram nests capabilities inside Retail Banking, the caption or legend should say whether this means composition, aggregation or only visual grouping.

Colour can help separate domains, but it must not be the only carrier of meaning. A reader should still understand the diagram from labels, legends, relationship types and surrounding prose.

## Strategy domain

The strategy domain answers: **what abilities and strategic direction does the organisation need?**

Common strategy elements include Capability, Resource, Value Stream and Course of Action [OPEN-GROUP-ARCHIMATE-4]. A capability describes an ability the organisation has or needs, such as Customer Onboarding, Payment Processing or Fraud Investigation. A value stream describes stages that deliver value to a stakeholder. A course of action describes an approach or direction, such as "consolidate customer identity across products".

For Horizon Bank, a retail banking capability map might include Customer Management, Account Management, Payments, Lending, Cards, Customer Support and Financial Crime Management. This is not a process model. It does not show the order of onboarding tasks. It shows stable abilities that the bank must manage, improve and govern.

Use strategy elements when capability ownership, investment planning or transformation scope is the main question. Do not use them to describe detailed workflow steps.

## Business domain

The business domain answers: **which business actors, roles, behaviour, services and business objects are involved?**

An **actor** is an entity capable of performing behaviour. It may be a person, organisation or organisational unit. A **role** is a responsibility that an actor performs. One actor may perform several roles, and the same role may be performed by different actors.

For example, Horizon Bank is a business actor. The same bank actor may perform the Account Provider role and the Payment Service Provider role. A Customer Support Agent role may be performed by different employees, teams or outsourced operations actors, depending on the organisation. This distinction matters because a role describes responsibility, while an actor identifies who or what can perform behaviour.

Common business-domain elements include Actor, Role, Process, Function, Event, Service and Business Object. In a Horizon Bank onboarding view, Retail Customer may be an actor, Applicant may be a role, Customer Onboarding may be a process, Open Customer Profile may be a business service and Identity Evidence may be a business object.

This domain overlaps with BPMN, but the purpose is different. BPMN is better for detailed process flow, gateways, timers, pools and message exchange. ArchiMate is better when the process needs to connect upward to capabilities and downward to application and technology support.

## Application domain

The application domain answers: **which application components perform behaviour, realise services and use data?**

The beginner pattern to learn is explicit:

```text
Application Component
→ assigned to Application Function or Process
→ realises Application Service
→ serves another element
```

In ArchiMate 4, behaviour concepts are streamlined across domains, so the phrase "Application Function or Process" should be read as a function or process placed in the application domain. The modelling pattern is still useful because it prevents a common shortcut: drawing an application component directly to every consumer without explaining the behaviour and service it provides.

For Horizon Bank:

- Party and Customer Platform is an Application Component.
- Customer Profile Management Function is behaviour assigned to that component.
- Customer Profile Management is an Application Service realised by that function.
- The service serves the Customer Onboarding process and other consuming application behaviour.

This explicit chain is better for teaching than a single derived relationship from component to business process. A derived shortcut may be acceptable in a simplified view, but the diagram or caption should say that the service and function are implied.

Do not confuse an ArchiMate Application Component with a C4 component. A C4 component sits inside one container. An ArchiMate Application Component is an enterprise architecture element and may represent a larger application or a modular part of an application estate.

## Technology domain

The technology domain answers: **which technology active structure, services and artifacts support the applications?**

A **Technology Node** is a technology active structure element that can host, process, store or execute technology behaviour. A node may represent a server, runtime environment, platform node or other execution environment at the chosen abstraction level.

**System Software** is software that provides an environment for applications or technology behaviour, such as an operating system, database management system, application server or container platform. It is not the same as the business application being described.

A **Technology Service** is technology behaviour exposed for use by applications or other technology elements. Examples include API Gateway Service, Messaging Service, Runtime Hosting Service and Database Service.

An **Artifact** is a deployable or stored technology item, such as an application package, configuration file, database schema artifact or deployable container image. Do not confuse an artifact with a business object or application data object.

Deployment or hosting is usually shown by assigning or placing artifacts on nodes, and by showing technology services serving application components or application behaviour. Be precise: a managed database service is not automatically a Technology Node. It may be modelled as a Technology Service when the concern is consumption of database capability, or as a node plus system software when the concern is hosting or runtime structure.

For Horizon Bank, Customer Onboarding Platform may depend on a Runtime Hosting Service. Party and Customer Platform may use a Database Service. The Customer Profile Service Package may be an Artifact deployed to an Application Runtime Node. Choose the representation that answers the reader's concern.

## Physical domain

The physical domain answers: **which physical facilities, equipment, distribution networks or materials matter to the architecture?**

Many digital architecture models do not need physical elements. They become useful when the architecture depends on branches, cash machines, devices, warehouses, telecommunications equipment, production facilities or material movement.

For a retail bank, a physical view might show branch locations, cash devices and network connectivity at a high level. For the Simple Online Store, physical elements might matter if the architecture discussion includes fulfilment centres, packing stations or delivery hand-off points.

Use the physical domain only when physical reality affects the design decision. Do not add it just because the language provides the elements.

## Motivation elements

Motivation elements answer: **why does this architecture need to change, and what goals or requirements shape it?**

Common motivation elements include Stakeholder, Driver, Assessment, Goal, Outcome, Principle and Requirement [OPEN-GROUP-ARCHIMATE-4]. They connect architecture views to reasons rather than treating diagrams as neutral pictures.

For Horizon Bank, drivers might include slow product launches, duplicate customer databases and limited end-to-end process visibility. Assessments might state that customer data is fragmented and onboarding is duplicated across products. Goals might include improved straight-through processing and a trusted party and customer view. Requirements might include reusable customer identity services, auditability of screening decisions and integration with retained core systems.

Motivation views are useful in review meetings because they expose the logic behind the design. If the target application view does not support the stated goals, the inconsistency is visible.

Avoid vague goal labels. A goal such as "be digital" is too vague. A goal such as "reduce duplicate customer capture across retail products" gives the architecture team something to trace.

## Implementation and migration elements

Implementation and migration elements answer: **how does the architecture move from current state to target state?**

Common elements include Work Package, Deliverable, Plateau and Event [OPEN-GROUP-ARCHIMATE-4]. A plateau represents a relatively stable architecture state, such as Current State, Transition State or Target State. A work package represents a unit of change work. A deliverable represents an output of that work. ArchiMate 4 uses the generic Event element rather than a separate Implementation Event.

Earlier ArchiMate versions included a Gap element. ArchiMate 4 removed it, so this chapter does not use Gap as current notation. If the team needs to describe the difference between current and target states, use prose, assessment, outcome, deliverables or labelled relationships rather than drawing a Gap element.

For Horizon Bank, a migration view might show a current plateau with product-specific onboarding and duplicate customer stores, a transition plateau where Customer Onboarding Platform and Party and Customer Platform are introduced for new retail products, and a target plateau where onboarding services are reused across retail and small business channels.

This view helps keep transformation realistic. It shows that enterprise architecture is not only a target picture. It must also describe sequencing, dependency, risk and temporary coexistence.

## Core relationships

ArchiMate diagrams are only useful when relationships carry meaning. Boxes without clear relationships are inventory, not architecture.

This chapter uses a beginner subset of the ArchiMate 4 relationship types: composition, aggregation, assignment, realisation, serving, access, flow, triggering, influence and association [OPEN-GROUP-ARCHIMATE-4].

Some practical interpretations are:

| Relationship | Plain meaning | Example |
|---|---|---|
| Composition | This thing is made of these parts | Retail Banking capability is composed of Customer Management and Payments capabilities |
| Aggregation | This thing groups related parts | Onboarding Transformation groups several work packages |
| Assignment | This active element performs behaviour | Party and Customer Platform is assigned to Customer Profile Management Function |
| Realisation | This element fulfils another | Customer Profile Management Function realises Customer Profile Management Service |
| Serving | This element provides behaviour to another | Customer Profile Management Service serves Customer Onboarding Process |
| Access | This behaviour uses or changes information | Customer Profile Management Function accesses Customer Record |
| Flow | Something passes from one element to another | Screening Request flows to Financial Crime Platform |
| Triggering | One behaviour starts or follows another | Application Submitted Event triggers Customer Onboarding Process |
| Influence | One motivation element affects another | Duplicate customer data influences the Trusted Customer View goal |
| Association | A weak or general relationship | Use only when a more precise relationship is not justified |

Relationship direction matters. If the arrow direction is wrong, the model can imply the wrong dependency. Label relationships when the meaning is not obvious to the audience.

## Common viewpoints

An ArchiMate viewpoint is a reusable way to select content for a concern. The important beginner question is: **which view will help this audience make a decision?**

Useful early viewpoints include:

| Viewpoint | Question answered | Typical audience |
|---|---|---|
| Capability map | What abilities does the organisation need or improve? | Business architects, sponsors and portfolio teams |
| Layered or domain traceability view | How do business, application and technology concepts connect? | Enterprise and solution architects |
| Application cooperation view | How do application components collaborate through services and data? | Solution architects and application owners |
| Technology view | What technology services, nodes and artifacts support the applications? | Platform, infrastructure and operations teams |
| Motivation view | Why is the change needed and what requirements shape it? | Sponsors, architects and reviewers |
| Implementation and migration view | What changes between current, transition and target states? | Transformation, delivery and governance teams |

Do not put every element in every view. A capability map should not include database tables. A technology view should not include every business goal. A migration view should show meaningful architecture states, not a detailed Gantt chart.

## ArchiMate versus C4

ArchiMate and C4 can both show systems and relationships, but they serve different levels of discussion.

C4 is strongest for software architecture communication. It helps teams explain a software system, its containers, components, dynamic interactions and deployment. It is compact and familiar to developers.

ArchiMate is stronger when the view must connect strategy, business services, application services, technology services, motivation and migration. It supports enterprise architecture traceability across domains.

For the Simple Online Store, a C4 container view is usually the better first diagram when the team wants to understand the web application, API, database and external payment provider. ArchiMate becomes useful when the store is part of a wider enterprise transformation involving capabilities, operating model, applications, fulfilment facilities and migration states.

For Horizon Bank, both may be needed. ArchiMate can show how Customer Onboarding capability, business services, application services and platforms fit into the target enterprise architecture. C4 can then zoom into the Customer Onboarding Platform and explain its containers and components.

## ArchiMate versus BPMN

ArchiMate and BPMN overlap around business behaviour, but they answer different process questions.

BPMN is stronger when the reader needs process sequence, gateways, events, timers, pools, lanes and message flows. Chapter 6 used BPMN to show onboarding and payment repair behaviour.

ArchiMate is stronger when the reader needs to place a business process in a wider architecture context. It can show that Customer Onboarding belongs to Customer Management capability, realises or supports a business service, uses Customer Profile Management from the Party and Customer Platform, and is shaped by screening requirements.

Use BPMN when process flow and exception behaviour are the focus. Use ArchiMate when process content needs to connect to capabilities, services, applications, technology and change.

## Common mistakes

The first mistake is creating a one-page enterprise map that shows everything. A diagram with every capability, process, application, database, network and project usually answers no question well.

The second mistake is using ArchiMate as decoration. If every relationship is a generic association, the diagram may look formal while saying little. Choose relationships that express composition, assignment, realisation, serving, access, flow or influence.

The third mistake is mixing abstraction levels. A view that combines "Customer Management capability", "click Submit", "Customer table column" and "Kubernetes pod" is probably not a coherent architecture view.

The fourth mistake is skipping the application realisation chain. A component-to-consumer shortcut may hide the behaviour and service that actually explain the dependency.

The fifth mistake is treating a managed technology service as a node without asking the architecture question. If the concern is consumption, model a Technology Service. If the concern is hosting or execution, show the Technology Node, System Software and Artifact where needed.

The sixth mistake is using historical ArchiMate elements as if they were current ArchiMate 4 elements. Do not use removed elements such as Gap or Constraint in new Chapter 7 diagrams.

## Chapter cheat sheet

| Area | Plain question | Typical elements | Watch out for |
|---|---|---|---|
| Strategy domain | What abilities and direction matter? | Capability, Resource, Value Stream, Course of Action | Do not turn process steps into capabilities |
| Business domain | Who performs business behaviour and what service is visible? | Actor, Role, Process, Function, Event, Service, Business Object | Actor and Role are not the same concept |
| Application domain | Which applications perform behaviour and realise services? | Application Component, Process, Function, Service, Data Object | Do not skip the component to behaviour to service chain without saying so |
| Technology domain | Which technology hosts or supports the applications? | Technology Node, System Software, Technology Service, Artifact | A managed service is not automatically a node |
| Physical domain | Which real-world facilities or equipment matter? | Facility, Equipment, Material | Use only when physical context affects the decision |
| Motivation | Why is change needed? | Stakeholder, Driver, Assessment, Goal, Outcome, Requirement, Principle | Avoid vague goals |
| Migration | How does architecture change over time? | Work Package, Deliverable, Plateau, Event | Do not use the removed Gap element as current notation |

## Key takeaways

- ArchiMate is an enterprise architecture modelling language for connecting business, application, technology, motivation and change.
- ArchiMate 4 is the current normative version for this chapter.
- TOGAF is a framework and method; ArchiMate is a language that can represent selected architecture content.
- One ArchiMate model can support several views, and the same concept should be reused across those views.
- Use BPMN for detailed process flow and C4 for software architecture views.
- Actors perform behaviour; roles describe responsibilities performed by actors.
- Application services should usually be traced through behaviour assigned to application components.
- Relationship choice, direction, legend and scope are essential in ArchiMate.

## Practical exercise

Horizon Bank wants to reduce duplicate customer capture across retail products. It plans to introduce a Customer Onboarding Platform and a Party and Customer Platform while retaining the Core Deposit System during the first transition.

Create a small ArchiMate modelling plan before drawing:

1. Which capability or capabilities are in scope?
2. Which actor and role distinction matters?
3. Which application component to function to service chain should be visible?
4. Which motivation elements explain the change?
5. Which migration states should be shown without using a Gap element?

Suggested answer:

- Scope Customer Management and Customer Onboarding as capabilities. Avoid modelling every retail banking capability in the first view.
- Treat Horizon Bank as an actor and Account Provider or Customer Service Provider as possible roles, depending on the concern.
- Show Party and Customer Platform assigned to Customer Profile Management Function, which realises Customer Profile Management Service, which serves Customer Onboarding Process.
- Use drivers such as duplicate customer databases and slow product launches, assessments such as customer data fragmented, and goals such as trusted customer view and improved straight-through processing.
- Show Current State, Transition State and Target State as plateaus. Explain differences between states in prose, deliverables or assessment notes rather than drawing a Gap element.

## Review checklist

- [ ] The view has a stated purpose, audience, concern and scope.
- [ ] The model concepts are reused consistently across capability, layered, application, technology, motivation and migration views.
- [ ] Formal ArchiMate 4 terminology is used where the chapter refers to the current standard.
- [ ] Business actors and roles are not confused.
- [ ] Application services are traced through assigned application behaviour unless a derived shortcut is explicitly stated.
- [ ] Technology Node, System Software, Technology Service and Artifact are distinguished.
- [ ] Business, application and technology details are not mixed without clear relationships.
- [ ] Capabilities describe abilities, not process steps.
- [ ] Relationship types and directions are meaningful.
- [ ] Removed ArchiMate 3.2 elements are not used as current ArchiMate 4 notation.
- [ ] Diagram specifications are author-approved before source files are created.
- [ ] Terminology, link, diagram-register and manuscript checks pass.

## References and further reading

Chapter source notes are maintained in the repository under `research/archimate/` and registered in `SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index once the appendix is completed.

- `[OPEN-GROUP-ARCHIMATE-4]`: The Open Group ArchiMate 4 Specification, current normative source.
- `[OPEN-GROUP-ARCHIMATE-3.2]`: The Open Group ArchiMate 3.2 Specification, retained as a historical source note.
