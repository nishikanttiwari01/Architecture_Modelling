---
title: "Domain and Event Modelling"
chapter: 10
part: "part-02-modelling-languages"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-06-30"
---

# 10. Domain and Event Modelling

## Chapter purpose

Introduce domain-driven design, bounded contexts, EventStorming and event-driven architecture models as practical ways to understand a business domain before choosing software, data or integration structures.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain domain models, Domain-Driven Design (DDD), bounded contexts, domain events and event-driven architecture in plain language.
- Identify the architecture question answered by a domain model, context map, EventStorming board, event flow and event catalogue.
- Distinguish a domain event from a command, technical notification, integration event and database change.
- Use simple examples to identify entities, value objects, aggregates, commands, events, policies and read models.
- Recognise when event-driven architecture helps and when it adds unnecessary complexity.
- Review domain and event models for unclear language, missing ownership, weak boundaries and over-technical detail.

## Prerequisites and dependencies

- Chapter 9: Decision Modelling and DMN

## Required models and artefacts

- FIG-10-01: Online Store Order Domain Model, specification created; source and export deferred pending author approval of the specification.
- FIG-10-02: Online Store Bounded Context Map, specification created; source and export deferred pending author approval of the specification.
- FIG-10-03: Horizon Bank Payment EventStorming Board, specification created; source and export deferred pending author approval of the specification.
- FIG-10-04: Horizon Bank Payment Event Flow, specification created; source and export deferred pending author approval of the specification.

## Worked examples

- Simple Online Store order domain.
- Horizon Bank payment and fraud domains.

## Source requirements

- `[DDD-REFERENCE-2015]` is the primary source for DDD vocabulary used in this chapter.
- `[EVENTSTORMING-BRANDOLINI-2026]` is the primary source for EventStorming provenance and method framing.
- `[CNCF-CLOUDEVENTS-1.0.2]` is the verified CloudEvents source for event envelope terminology.
- `[ASYNCAPI-3.1.0]` is the verified AsyncAPI source for message-driven application programming interface (API) contract terminology.
- Chapter guidance distinguishes primary terminology, official specifications and the author's practical beginner recommendations.

## Why domain and event modelling matter

Domain and event modelling answers: **what does this part of the business mean, what changes over time and which boundaries should shape the solution?**

Many architecture problems start badly because the team jumps straight to screens, databases, APIs or message topics. Those things matter, but they are not the business problem itself. Before designing a solution, a team needs shared language for orders, payments, shipments, accounts, fraud alerts and customer records.

A **domain** is the area of knowledge or activity being modelled. In the Simple Online Store, the order domain includes baskets, orders, payments and shipments. In Horizon Bank, the payment domain includes payment instructions, screening, posting, cut-off times, repairs and status updates.

A **domain model** describes the important concepts, rules and relationships in that area. It is not the same thing as a database schema. It may later influence classes, tables, APIs and events, but its first job is shared understanding.

Event modelling adds time. It asks what happened and why that occurrence matters. `OrderPlaced`, `PaymentAuthorised`, `ShipmentDispatched` and `PaymentScreeningFailed` are examples of business-significant events. Events help teams understand lifecycles, integration points, audit trails and eventual consistency.

## Domain models

A domain model answers: **which business concepts are important, how do they relate and what language should the team use?**

For a beginner, a domain model is a map of meaning. It names the business things that matter and shows the most important relationships between them. It should be understandable to domain experts, analysts, architects and developers. If only database specialists can read it, it is probably too technical for an early domain model.

In the Simple Online Store, a first order-domain model might include:

| Concept | Plain meaning | Example rule |
|---|---|---|
| Customer | A person who places orders. | A customer may place many orders. |
| Basket | A temporary collection of intended purchases. | A basket becomes an order only when checkout is completed. |
| Order | A confirmed request to buy products. | An order has one or more order lines. |
| Payment | A payment attempt or result for an order. | An order is not ready for fulfilment until payment is authorised or the chosen payment method allows deferred settlement. |
| Shipment | The delivery of ordered products. | One order may require more than one shipment. |

FIG-10-01 is specified as the Online Store Order Domain Model. It will show these concepts and selected relationships at a conceptual level after the figure specification is approved. The figure is not yet rendered because this repository requires author approval of diagram specifications before source creation.

The model should stay at the right level. `Order` and `Payment` belong in the conceptual view. `orders.order_id`, `payment_gateway_response_code` and `idx_order_customer_id` belong later in logical or physical data modelling. Chapter 8 covers those levels.

## Domain-Driven Design vocabulary

DDD answers: **how can a team keep software design closely connected to the business domain and its language?**

DDD is an approach to software and architecture design associated with Eric Evans. The DDD Reference provides pattern summaries and vocabulary for concepts such as domain, model, ubiquitous language, bounded context, entity, value object, aggregate and domain event [DDD-REFERENCE-2015]. It is not a standards-body notation like Unified Modeling Language (UML), Business Process Model and Notation (BPMN) or Decision Model and Notation (DMN).

The practical idea is straightforward: the model should use the language of the business area it represents. If operations staff say "payment repair", risk staff say "screening alert" and developers say "exception queue", the team must decide whether those are three names for one concept or three different concepts. DDD calls the shared language within a context the **ubiquitous language**.

Ubiquitous language does not mean one word must have the same meaning everywhere in the organisation. In Horizon Bank, `customer` might mean a legal party in the Party and Customer Platform, a product relationship in a lending context and a channel user in Horizon Digital Channels. The architecture should expose those differences rather than hide them.

Use DDD vocabulary when domain language and boundaries influence design. Do not use it as decoration. A model is not more useful because every box uses a DDD label. It is useful when the labels reveal ownership, rules and change boundaries.

## Subdomains and bounded contexts

Subdomains and bounded contexts answer: **where should one model stop and another model begin?**

A **subdomain** is a part of the wider business domain. It is a problem-area distinction. In the Simple Online Store, ordering, payment, fulfilment and customer support may be different subdomains. In Horizon Bank, payments, financial crime, customer data, account processing and operations case management may be different subdomains.

A **bounded context** is a boundary within which a particular model and language are consistent [DDD-REFERENCE-2015]. It is a design boundary, not automatically a microservice, database, team or deployment unit. A bounded context may be implemented by one service, several services or a module inside a larger system, depending on design constraints.

This distinction matters. A team may identify the payments subdomain as important, but still split the implementation into a Payment Initiation context, Payment Screening context and Payment Posting context. Another organisation may keep those responsibilities together if volume, risk, ownership and change frequency justify it.

For the Online Store, a simple context split might be:

| Bounded context | Main language | Main responsibility |
|---|---|---|
| Catalogue | Product, price, availability | Present products for sale. |
| Ordering | Basket, order, order line | Capture and confirm a purchase. |
| Payment | Payment request, authorisation, settlement | Take and track payment. |
| Fulfilment | Shipment, carrier, delivery status | Dispatch and deliver goods. |
| Support | Return, refund request, case | Handle post-order issues. |

The same word may cross contexts with changed meaning. `Available` in Catalogue may mean visible for sale. `Available` in Fulfilment may mean physically pickable in a warehouse. A good model makes those differences reviewable.

FIG-10-02 is specified as the Online Store Bounded Context Map. It will show the five contexts above and the main relationships between them after specification approval.

## Context maps

A context map answers: **how do bounded contexts relate, depend on each other and exchange meaning?**

A context map is useful when one model is not enough. It shows relationships between contexts, not the internal details of each context. The aim is to expose dependency, translation and ownership.

For beginners, start with plain relationship labels. Examples include:

| Relationship | Plain meaning | Example |
|---|---|---|
| Provides product information to | One context supplies information another context needs. | Catalogue provides product information to Ordering. |
| Requests payment authorisation from | One context asks another to perform a business action. | Ordering requests payment authorisation from Payment. |
| Publishes event to | One context records something happened for other contexts to use. | Payment publishes `PaymentAuthorised` to Fulfilment. |
| Translates terms for | A boundary protects one model from another model's language. | Enterprise Integration Platform translates legacy account status for Payments Platform. |

DDD literature includes named context-map relationship patterns [DDD-REFERENCE-2015]. Those names can be valuable for experienced teams, but a beginner should first understand the dependency itself. Which context owns the term? Which context is downstream? Where is translation needed? Which relationship creates the greatest change risk?

In Horizon Bank, the Payments Platform should not silently adopt every internal term from the Core Deposit System. It may need an adapter or translation layer so payment concepts remain stable while legacy account-processing terms are contained. That is a modelling decision before it is a coding decision.

## Aggregates, entities and value objects

Aggregates, entities and value objects answer: **which domain objects have identity, which are defined by values and where must consistency be protected?**

An **entity** is a domain object with an identity that matters over time [DDD-REFERENCE-2015]. An `Order` remains the same order even if its status changes. A Horizon Bank `Payment Instruction` remains identifiable as it moves from received to screened, posted, repaired or rejected.

A **value object** is defined by its values rather than a long-running identity. A delivery address may be treated as a value object in the Online Store order context. If the customer changes the address before dispatch, the order now contains a different address value.

An **aggregate** is a consistency boundary around related objects [DDD-REFERENCE-2015]. It protects rules that must be enforced together. In the Online Store, `Order` may be the aggregate root for order lines and order status. A rule might say an order cannot be submitted without at least one order line and a selected delivery option.

Do not turn aggregate modelling into a database exercise too early. An aggregate is not automatically one table, one object-relational mapping class, one API resource or one microservice. It is a domain consistency boundary. Implementation choices come later.

For Horizon Bank, a `Payment Instruction` aggregate might protect rules about status transitions, repair information and idempotent submission. But sanctions screening, fraud case investigation and account posting may belong to other contexts. Combining all of them into one large aggregate would create a model that is hard to own and hard to change.

## Domain events

A domain event answers: **what meaningful thing happened in the domain that other work may need to know about?**

A domain event records an occurrence. It should be named in the past tense because it is a fact, not a request. Good examples include `OrderPlaced`, `PaymentAuthorised`, `ShipmentDispatched`, `PaymentInstructionReceived`, `PaymentScreeningFailed` and `FraudCaseOpened`.

A **command** is different. A command asks for something to happen, such as `PlaceOrder`, `AuthorisePayment` or `ScreenPayment`. A command may be accepted, rejected or ignored. An event says that something has happened.

| Item | Plain meaning | Naming pattern | Example |
|---|---|---|---|
| Command | Request to do work. | Imperative verb phrase. | `SubmitPaymentInstruction` |
| Domain event | Business-significant fact. | Past-tense phrase. | `PaymentInstructionSubmitted` |
| Technical notification | System-level signal. | Operational phrase. | `FileTransferCompleted` |
| Database change event | Record that data changed. | Table or record oriented. | `payment_row_updated` |

A technical notification or database change can be useful, but it is not automatically a domain event. `payment_row_updated` tells a consumer that a row changed. It does not tell the consumer whether a payment was authorised, repaired, rejected or posted. A domain event should carry business meaning.

Domain events are also not always integration events. A team may use domain events inside one bounded context. If an event crosses a system or organisational boundary, the team may publish an **integration event** with a stable contract, security classification and versioning policy. That integration event may be derived from one or more internal domain events.

CloudEvents defines a common way to describe event data across services, platforms and transports [CNCF-CLOUDEVENTS-1.0.2]. Its metadata is useful for event envelopes, such as event identifier, source, type and time. It does not define the business meaning of `PaymentAuthorised`; the team still needs a domain model and event catalogue.

## EventStorming

EventStorming answers: **what happens in this business process or domain, and what do people disagree about?**

EventStorming is a collaborative modelling technique originated by Alberto Brandolini and associated with DDD and collaborative modelling [EVENTSTORMING-BRANDOLINI-2026]. In a workshop, participants place domain events on a timeline and then add related commands, actors, policies, external systems, questions and problems.

The important feature is not the sticky notes. The important feature is shared discovery. Domain experts, architects, developers, testers, operations and risk people can see the same sequence and challenge unclear assumptions.

For an Online Store order flow, a workshop might identify:

- `BasketCheckedOut`
- `OrderPlaced`
- `PaymentAuthorised`
- `OrderReadyForFulfilment`
- `ShipmentDispatched`
- `DeliveryConfirmed`
- `ReturnRequested`

For Horizon Bank, a payment workshop might identify:

- `PaymentInstructionReceived`
- `PaymentInstructionValidated`
- `ScreeningRequested`
- `ScreeningResultReceived`
- `PaymentRepairRequested`
- `PaymentPosted`
- `PaymentRejected`
- `FraudCaseOpened`

FIG-10-03 is specified as the Horizon Bank Payment EventStorming Board. It will show a readable teaching version of a workshop board, including events, commands, actors, policies, external systems and open questions. It is planned as an explanatory figure, not as a copied workshop artefact.

Avoid treating EventStorming as a formal publication notation. Colours and layout conventions are useful, but the method is a workshop approach rather than an Object Management Group style standard. The book will use original teaching diagrams to explain the idea.

## Commands, events, policies and read models

Commands, events, policies and read models answer: **what causes work, what records the result, what reacts to it and what view is built for reading?**

This vocabulary helps beginners separate concerns:

| Concept | Plain meaning | Online Store example | Horizon Bank example |
|---|---|---|---|
| Actor | Person or system that asks for work. | Customer | Retail Customer |
| Command | Request to perform an action. | `PlaceOrder` | `SubmitPaymentInstruction` |
| Event | Fact that something happened. | `OrderPlaced` | `PaymentInstructionReceived` |
| Policy | Rule that reacts to an event. | When payment is authorised, start fulfilment. | When screening fails, create a repair or investigation case. |
| Read model | A view optimised for query or display. | Order status page | Payment status view |

A policy is not the same thing as a governance policy in Chapter 9, although both express rules. In event modelling, a policy often means reactive behaviour: when this event happens and these conditions hold, issue this command or start this process.

Read models matter in event-driven designs because the data a user wants to see may be assembled from several events or contexts. The Online Store order status page may combine order, payment and shipment information. Horizon Bank's payment status view may combine validation, screening, posting and repair information.

Do not overuse this pattern. If the system is small and one transaction can reliably update the needed state, a direct request and response may be easier. Event-driven architecture is valuable when loose coupling, auditability, asynchronous processing, integration or independent scaling justifies the extra operational complexity.

## Event-driven architecture diagrams

An event-driven architecture diagram answers: **which producers publish events, which consumers use them and how event messages move through the architecture?**

Event-driven architecture is an architecture style in which systems publish and react to events. It can reduce point-to-point coupling, but it does not remove design responsibility. Someone still owns each event, schema, topic, retention rule, consumer contract and failure path.

At beginner level, distinguish four views:

| View | Question answered | Typical audience |
|---|---|---|
| Event flow | What happens, in what order, for one scenario? | Analysts, architects and developers |
| Event producer-consumer view | Who publishes and who consumes each event? | Integration architects and application owners |
| Event contract view | What does each event message contain? | Developers, testers and data governance |
| Operational event view | How are retries, dead letters, monitoring and recovery handled? | Platform and operations teams |

FIG-10-04 is specified as the Horizon Bank Payment Event Flow. It will show how selected payment events move between Horizon Digital Channels, Payments Platform, Financial Crime Platform, Core Deposit System, Event Platform and Enterprise Data Platform.

Keep event-flow diagrams separate from detailed BPMN process models unless the view states why both are shown. A BPMN model is better for human tasks, gateways and process responsibility. An event-flow model is better for publish-subscribe relationships and asynchronous reactions. A C4 or deployment model is better for software and runtime structure.

AsyncAPI describes message-driven APIs in a machine-readable, protocol-agnostic format, including applications, channels, operations and messages [ASYNCAPI-3.1.0]. It is useful when event contracts need documentation, governance or tooling. It should not be confused with EventStorming, which is used for discovery and shared understanding.

## Event catalogues

An event catalogue answers: **what events exist, who owns them, what they mean and who depends on them?**

Without a catalogue, event-driven systems become difficult to govern. Teams may publish similar events with different names, change schemas without warning, expose sensitive data or create consumers that nobody knows about.

A practical event catalogue should record:

| Field | Purpose |
|---|---|
| Event name | Stable business name, usually past tense. |
| Event type or identifier | Machine-readable event type used in contracts. |
| Owning context | The bounded context responsible for meaning and lifecycle. |
| Producer | The system or component that publishes the event. |
| Consumers | Known systems or teams that use the event. |
| Business meaning | Plain-language description of what happened. |
| Trigger | What causes the event to be produced. |
| Schema version | Version of the message structure. |
| Data classification | Privacy, security or regulatory sensitivity. |
| Retention and replay policy | How long the event is retained and whether replay is allowed. |
| Compatibility rules | What changes are allowed without breaking consumers. |

CloudEvents can help standardise envelope metadata. AsyncAPI can help document message-driven contracts. Neither replaces domain ownership. The catalogue should still answer the business question: what does this event mean, and who is allowed to change it?

For Horizon Bank, `PaymentInstructionReceived` should have an owner in the Payments Platform context, a clear relationship to payment submission, a schema version, privacy classification and a list of consumers such as Financial Crime Platform, Enterprise Data Platform and operations monitoring. It should not be a vague catch-all event containing every payment field simply because a consumer might need it one day.

## How domain and event modelling compare with nearby techniques

Domain and event models overlap with earlier chapters, but they answer different questions.

| Technique | Main question | Use it for | Do not use it for |
|---|---|---|---|
| Domain model | What concepts and rules matter in this business area? | Shared language and conceptual relationships | Physical database design |
| Context map | Where do model boundaries and dependencies sit? | Ownership, translation and upstream/downstream relationships | Detailed process sequence |
| EventStorming | What happens over time, and where are the disagreements? | Discovery workshops and lifecycle exploration | Formal publication notation |
| Event flow | Who publishes and consumes events in one scenario? | Asynchronous integration and reactions | Human task ownership |
| BPMN | What is the process flow and who performs work? | Tasks, gateways, events, message flows and exceptions | Message contract detail |
| DMN | How is a repeatable decision derived? | Decision logic and decision dependencies | Business object lifecycle |
| Data model | What information is stored, related and governed? | Conceptual, logical and physical data views | Runtime event sequencing |

The models should support each other. An EventStorming workshop may reveal domain events. A domain model may define the concepts those events refer to. A context map may show where the events cross boundaries. A BPMN model may show the operational process that reacts to a payment exception. A DMN model may define the payment routing decision that leads to `PaymentRepairRequested`.

## Common mistakes

The first mistake is treating a domain model as a database schema. A domain model should explain business meaning before physical storage.

The second mistake is forcing one language across all contexts. Shared enterprise terms are useful, but a bounded context exists because meaning can legitimately differ.

The third mistake is equating bounded context with microservice. A bounded context is a model boundary. Physical service boundaries require separate design reasoning.

The fourth mistake is naming commands as events. `ApprovePayment` is a request. `PaymentApproved` is a fact.

The fifth mistake is publishing technical changes as if they were business events. `payment_table_updated` rarely gives consumers the meaning they need.

The sixth mistake is drawing event flows without ownership. Every event needs a producer, owner, meaning, schema and compatibility rule.

The seventh mistake is hiding process logic inside event diagrams. If the concern is human workflow, responsibility, waiting, escalation or exception handling, BPMN is usually clearer.

The eighth mistake is assuming event-driven architecture is automatically better. It can improve loose coupling and auditability, but it also introduces eventual consistency, replay concerns, monitoring needs and contract governance.

The ninth mistake is using EventStorming output as final architecture without synthesis. Workshop boards are discovery artefacts. They need review, pruning and translation into appropriate models.

## Chapter cheat sheet

| Topic | Question answered | Useful for | Watch out for |
|---|---|---|---|
| Domain model | What concepts and rules matter? | Shared meaning | Turning it into a database design too early |
| Ubiquitous language | What words does this context use? | Reducing misunderstanding | Pretending one term means the same thing everywhere |
| Subdomain | Which business problem area is this? | Scope and business importance | Confusing problem areas with deployment units |
| Bounded context | Where is a model consistent? | Boundary design | Equating it with one microservice |
| Context map | How do contexts depend on each other? | Ownership and translation | Hiding internal context detail in the map |
| Entity | What has identity over time? | Lifecycles and rules | Treating every table as an entity |
| Value object | What is defined by values? | Small descriptive concepts | Giving it artificial identity |
| Aggregate | Where must consistency be protected? | Transaction and rule boundaries | Creating very large aggregates |
| Domain event | What meaningful thing happened? | Lifecycles and integration | Publishing vague technical updates |
| EventStorming | What happens over time? | Discovery and shared understanding | Treating workshop notation as a formal standard |
| Event catalogue | What events exist and who owns them? | Governance and reuse | Maintaining only a broker-topic list |

## Key takeaways

- Domain modelling starts with business meaning, not implementation structure.
- DDD provides useful vocabulary for language, boundaries and consistency, but it is not a standards-body notation.
- A bounded context is a consistency boundary for a model and language, not automatically a team, microservice or database.
- Domain events record meaningful facts in the past tense. Commands request action.
- EventStorming is useful for discovering events, commands, policies, actors and open questions with domain experts.
- Event-driven architecture needs ownership, contracts, versioning, observability and failure handling.
- CloudEvents helps with event envelope metadata; AsyncAPI helps with message-driven API contracts. Neither replaces domain modelling.
- Use BPMN, DMN, data models, context maps and event flows for different questions, and keep their viewpoints explicit.

## Practical exercise

Horizon Bank wants to improve outgoing retail payment handling. A Retail Customer submits a payment instruction through Horizon Digital Channels. The Payments Platform validates it, asks the Financial Crime Platform for screening, posts to the Core Deposit System when allowed, and publishes status updates through the Event Platform. Some payments require repair or fraud investigation.

Choose the right model for each question:

1. Which model would identify `Payment Instruction`, `Screening Result`, `Payment Repair` and `Fraud Case` as business concepts?
2. Which model would show that Payments Platform, Financial Crime Platform and Core Deposit System use different models and need translation at their boundaries?
3. Which workshop technique would help domain experts agree what happens from instruction receipt to posting or rejection?
4. Which model would show `PaymentInstructionReceived`, `ScreeningResultReceived`, `PaymentPosted` and `FraudCaseOpened` moving between systems?
5. Which artefact would record event owner, schema version, consumers, data classification and retention policy?
6. Which term describes `SubmitPaymentInstruction`: command or event?
7. Which term describes `PaymentInstructionSubmitted`: command or event?

Suggested answer:

- Use a domain model for the business concepts and their relationships.
- Use a context map for bounded contexts and translation boundaries.
- Use EventStorming for collaborative discovery of the timeline, events, commands, policies and open questions.
- Use an event flow for system-to-system event movement.
- Use an event catalogue for event ownership, contracts, consumers and governance.
- `SubmitPaymentInstruction` is a command because it requests work.
- `PaymentInstructionSubmitted` is an event because it records that something happened.

## Review checklist

- [ ] The question answered by each model is explicit.
- [ ] The audience and abstraction level are clear.
- [ ] DDD terms are introduced after plain-language explanations.
- [ ] DDD is not presented as a standards-body notation.
- [ ] Domain models are not reduced to database schemas.
- [ ] Bounded contexts are not equated with microservices, teams or databases.
- [ ] Commands and events are named distinctly.
- [ ] Domain events are distinguished from technical notifications and database changes.
- [ ] EventStorming is presented as a collaborative method, not a formal publication notation.
- [ ] CloudEvents and AsyncAPI are used only for their appropriate contract and metadata roles.
- [ ] Event-driven architecture guidance includes ownership, versioning, privacy, replay, monitoring and failure concerns.
- [ ] The simple and banking examples are consistent with repository example files.
- [ ] Required sources and diagram specifications are registered.
- [ ] Terminology, link, structure, diagram-register and word-count checks pass.

## References and further reading

Chapter source notes are maintained in the repository under `research/domain-event/` and registered in `SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index once the appendix is completed.

- `[DDD-REFERENCE-2015]`: Eric Evans / Domain Language, Domain-Driven Design Reference.
- `[EVENTSTORMING-BRANDOLINI-2026]`: Alberto Brandolini / Avanscoperta, official EventStorming book information page.
- `[CNCF-CLOUDEVENTS-1.0.2]`: CloudEvents specification, version 1.0.2.
- `[ASYNCAPI-3.1.0]`: AsyncAPI Specification, version 3.1.0.
