---
title: "Modelling Integration and Runtime Behaviour"
chapter: 18
part: "part-03-diagram-selection"
status: "Ready for Author Approval"
author: "Nishikant Tiwari"
last_updated: "2026-07-08"
---

# 18. Modelling Integration and Runtime Behaviour

## Chapter purpose

Help beginner and practising architects choose the right view when the main concern is
how systems exchange information and behave together at runtime.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain why integration modelling needs more than one view.
- Choose between integration context views, application programming interface (API)
  interaction views, message-flow views, Unified Modeling Language (UML) sequence
  diagrams, C4 dynamic views, event-flow views, data-flow views and interface
  catalogues.
- Distinguish synchronous request-response, asynchronous messaging, event publication,
  queues, retries, timeout handling and later status updates.
- Use the Simple Online Store and Horizon Bank examples to select useful integration
  views.
- Review integration and runtime behaviour models for ownership, direction, failure
  behaviour, data responsibility and operational risk.

## Prerequisites and dependencies

- Chapter 4: UML: Unified Modeling Language
- Chapter 5: The C4 Model
- Chapter 6: BPMN: Business Process Model and Notation
- Chapter 8: Data Modelling
- Chapter 10: Domain and Event Modelling
- Chapter 16: Modelling Software Structure
- Chapter 17: Modelling User and System Interaction

## Required models and artefacts

This chapter uses one original selection-guide specification and one manuscript
selection table:

- FIG-18-01: Choosing the Right Integration and Runtime Behaviour View.
- Integration and runtime behaviour view selection table.

`FIG-18-01` is specified and registered, but source and SVG export are deferred until
the author approves the diagram specification, as required by the repository diagram
workflow.

## Worked examples

- Simple Online Store checkout, payment and delivery integration.
- Horizon Bank payment submission, screening, posting, status update and event
  publication.

## Source requirements

- `[OMG-UML]` supports UML sequence diagram terminology reused from Chapter 4.
- `[C4-OFFICIAL]` supports C4 dynamic diagram terminology reused from Chapter 5.
- `[OMG-BPMN]` supports BPMN message-flow terminology where business-process
  collaboration is discussed.
- `[CNCF-CLOUDEVENTS-1.0.2]` supports CloudEvents envelope terminology reused from
  Chapter 10.
- `[ASYNCAPI-3.1.0]` supports message-driven API contract terminology reused from
  Chapter 10.
- Existing source notes are sufficient for this chapter; no new source note is required.

## From interaction to integration behaviour

Chapter 17 looked at interaction from the user's and participant's point of view. It
helped the reader choose between use cases, journeys, screen flows, sequence diagrams,
Business Process Model and Notation (BPMN) collaborations, state machines and API
interaction views. Chapter 18 continues that thread, but it moves the question deeper
into the architecture.

The integration question is: **how do systems exchange information, depend on each
other and recover when runtime behaviour is not the happy path?**

That question cannot be answered by one diagram. A system context view can show that the
Online Store uses the Payment Provider System, but it does not show the request, the
response, the timeout or the later refund event. A sequence diagram can show one order
submission path, but it is not an interface catalogue. An event-flow view can show that
`PaymentPosted` is published, but it does not define every payload field or consumer
contract. A data-flow diagram can show information movement, but it should not pretend
to be a runtime message sequence.

Good integration modelling separates the views. Start with the integration question,
choose the smallest view that answers it, then add companion views only when the next
decision requires them.

## Start with the integration question

Before drawing anything, write the question in plain language. A useful question names
the systems, the runtime behaviour and the decision the audience needs to make.

Examples:

- Which systems are involved when the Online Store accepts an order?
- Which API call creates an order, and what response does the Web App receive?
- What messages pass between the Payments Platform, Financial Crime Platform and Core
  Deposit System?
- Which parts of the payment flow are synchronous, and which are asynchronous?
- What event is published when a payment is posted?
- Which queue absorbs work when a downstream system is unavailable?
- What happens when screening is slow, a posting call times out or a duplicate message
  arrives?
- Which interfaces exist, who owns them and which consumers use them?

The wording points to the view. System involvement points to an integration context or
landscape. Ordered runtime collaboration points to a sequence diagram or C4 dynamic
view. Business participant hand-off points to BPMN collaboration. Event publication
points to an event-flow view or event catalogue. Information movement points to a data
flow. Interface ownership points to an interface catalogue. Failure behaviour points to
a retry, timeout, compensation or exception view.

## Integration context

An integration context view answers: **which systems exchange information, and through
which broad integration mechanisms?**

Use it when the audience needs a first map of dependencies before discussing individual
operations, events, payloads or infrastructure. It is useful for enterprise architects,
solution architects, application owners, integration teams and risk reviewers. It often
looks like a focused system landscape: systems are boxes, relationships are labelled
with integration style, and the boundary of the change is explicit.

For the Simple Online Store, an integration context view can show Web App, Online Store,
Payment Provider System and Delivery Partner System. The relationship labels might say
`order API`, `payment authorisation API`, `shipment booking API` and `delivery status
event`. This is enough to discuss dependency direction and ownership. It is not enough
to implement the API.

For Horizon Bank, a payment integration context can show Horizon Digital Channels,
Payments Platform, Financial Crime Platform, Core Deposit System, Enterprise Integration
Platform, Event Platform and Enterprise Data Platform. Relationship labels might say
`payment initiation API`, `screening request`, `posting request`, `payment status
event` and `payment reporting feed`. This view makes the integration landscape visible
without mixing in every retry rule or message field.

The common mistake is to leave every line labelled `integrates with`. That label hides
the important decisions. Is it a synchronous API, an asynchronous message, a published
event, a file, an adapter or a replicated data feed? Who owns it? Which direction does
the dependency run? If the line cannot answer those questions, the view is not yet an
integration model.

## API interactions

An API interaction view answers: **which caller invokes which API operation, what
response is expected and what later behaviour may follow?**

The plain-language idea is simple: one system asks another system to do something or
provide something through a defined interface. The formal term often used is
request-response. The caller sends a request and waits for a response. In many
architectures this is synchronous: the caller expects the response before it can
continue.

For the Simple Online Store checkout, the Web App may call `POST /orders` on the Online
Store API Application. The Online Store then calls the Payment Provider System for
payment authorisation and returns an order confirmation or a refusal to the Web App.
An API interaction view should show direction, operation name, immediate response and
important error responses.

For Horizon Bank, Horizon Digital Channels may submit a payment instruction to the
Payments Platform. The immediate response may be `accepted for processing` with a
payment reference rather than `money moved`. That distinction is critical. If screening
and posting happen later, the channel needs status polling, a notification, an event or
another mechanism for later state change.

Do not make the API diagram promise more than the runtime design provides. A successful
HTTP response from a payment API may only mean that the instruction was accepted, not
that screening, posting, customer notification and reconciliation have all completed.
The view should make that contract visible.

## Message flows

A message-flow view answers: **which messages move between participants or systems, in
what direction and for what purpose?**

In BPMN, a message flow has a formal meaning: it shows communication between separate
participants, usually separate pools [OMG-BPMN]. In integration architecture, teams also
use message-flow views more generally to show messages between systems, adapters,
queues and platforms. Be explicit about which meaning you are using.

Use a BPMN collaboration when the question is business-process responsibility: which
participant waits, responds, escalates or owns the hand-off? Use an integration
message-flow view when the question is technical exchange: which system sends a
screening request, which system returns a result, which platform routes the message and
which queue buffers work?

For the Simple Online Store, a message-flow view might show Online Store sending
`Authorise Payment` to Payment Provider System, receiving `Payment Authorised`, sending
`Book Shipment` to Delivery Partner System and later receiving `Delivery Status
Updated`. The view should say whether each message is synchronous, queued, event-based
or file-based.

For Horizon Bank, a message-flow view can show Payments Platform requesting screening
from Financial Crime Platform, requesting posting from Core Deposit System and
publishing payment status through Event Platform. That is different from a BPMN
collaboration about operations ownership, and different again from an event catalogue
that defines event meaning and consumers.

The review question is not "are there arrows?" The review question is: do the arrows
explain direction, ownership, delivery expectation and business meaning?

## Sequence diagrams

A UML sequence diagram answers: **for one scenario, which participant sends which
message, and in what order?**

Use it when message order matters. UML sequence diagrams are interaction diagrams with
lifelines and ordered messages [OMG-UML]. In architecture work, they are especially
useful for one selected path: submit order, authorise payment, create shipment; or
submit payment, screen, post, publish status.

For the Simple Online Store, a checkout sequence can show Customer, Web App, Online
Store API Application, Payment Provider System, Order Database and Delivery Partner
System. It can include a small alternative for payment accepted and payment rejected.
It should not include every fulfilment, refund, warehouse and customer-support path in
the same drawing.

For Horizon Bank, a payment submission sequence can show Horizon Digital Channels,
Payments Platform, Financial Crime Platform, Core Deposit System and Event Platform. It
can show that the channel submits a payment, the Payments Platform validates the
instruction, requests screening, requests posting, records status and publishes a
payment event.

Sequence diagrams are weak when teams use them as interface inventories. They show
order for a scenario, not the complete catalogue of operations, versions, owners,
service-level expectations and consumers. Use them to understand behaviour, then record
stable contracts elsewhere.

## C4 dynamic diagrams

A C4 dynamic diagram answers: **how do known C4 elements collaborate at runtime for one
scenario?**

The C4 model includes dynamic diagrams as supplementary views for showing runtime
collaboration between people, software systems, containers or components [C4-OFFICIAL].
They work best after the relevant system context, container or component structure is
already understood.

For the Simple Online Store, a C4 dynamic view can show the Web App, API Application,
Database, Payment Provider System and Delivery Partner System collaborating to place an
order. The same scenario could be shown as a UML sequence diagram. The C4 dynamic view
is usually more comfortable for architecture audiences who are already using C4
structure views.

For Horizon Bank, a C4 dynamic view can reuse structural elements from the payment
platform context: Horizon Digital Channels, Payments Platform, Financial Crime Platform,
Core Deposit System, Event Platform and Enterprise Data Platform. It can show a single
numbered path without re-drawing all internal classes or deployment nodes.

The common mistake is to use a dynamic view without a known structure view. If the
audience does not know what the systems, containers or components are, the dynamic view
becomes a loose message sketch. Establish the structural boundary first, then show the
runtime collaboration.

## Events and queues

An event-flow view answers: **what significant event is published, by whom, and who may
react to it?**

A queue or asynchronous message view answers a related but different question: **where
can work wait so that the sender and receiver do not have to proceed at the same time?**

Events are facts about something that has happened. Chapter 10 introduced domain
events, integration events, event catalogues, CloudEvents and AsyncAPI. CloudEvents
standardises event envelope and context metadata, not the business meaning of the
payload [CNCF-CLOUDEVENTS-1.0.2]. AsyncAPI can describe message-driven APIs in a
machine-readable, protocol-agnostic way [ASYNCAPI-3.1.0].

For the Simple Online Store, `OrderPlaced` may be published after an order is accepted.
The Delivery Partner System, analytics pipeline or customer-notification component may
consume it. The event-flow view should show producer, event name, event platform or
topic, consumers and any ordering or duplicate-handling expectations.

For Horizon Bank, the Payments Platform may publish `PaymentInstructionReceived`,
`PaymentScreeningCompleted` and `PaymentPosted`. Consumers may include Horizon Digital
Channels, Enterprise Data Platform, operational dashboards and reconciliation services.
The event-flow view should not imply that every consumer may change the payment. The
producer owns the meaning of the event, and consumers react within their own
responsibilities.

Queues are useful when a receiver may be slow or temporarily unavailable. They can
absorb work, smooth peaks and decouple processing time. They also introduce design
questions: ordering, duplicate delivery, poison messages, replay, retention and
operational ownership. Do not draw a queue as a magic reliability box. State what it
guarantees, what it does not guarantee and who monitors it.

## Error and retry behaviour

An error and retry view answers: **what happens when the runtime path does not complete
as expected?**

This is one of the most valuable integration views because many integration failures are
not discovered in the happy-path diagram. A caller may time out. A downstream service
may reject a request. A message may be delivered twice. A queue may contain a poison
message that cannot be processed. A payment may be screened successfully but fail during
posting. A customer may see a pending status while the back-end process is still
recovering.

For the Simple Online Store, payment authorisation might time out after the Online
Store has already created a pending order. The model should show whether the order is
cancelled, retried, marked pending or reconciled later. The customer-facing message
should match the real state. Do not show `Order confirmed` if the payment result is
unknown.

For Horizon Bank, a posting request to Core Deposit System may time out. The Payments
Platform needs to know whether it can safely retry, whether the operation is
idempotent, whether reconciliation is required and what status Horizon Digital Channels
will show. A retry loop without idempotency can create duplicate business effects.

Useful error and retry views often include:

- timeout and retry limits
- idempotency keys or duplicate-detection rules
- dead-letter or exception queues
- manual repair or reconciliation paths
- customer-visible status behaviour
- alerting and ownership for stuck work

Keep this view concrete. "Handle errors" is not a design. State the failure, the
runtime response, the owner and the evidence the team will monitor.

## Interface catalogue

An interface catalogue answers: **which interfaces exist, what do they expose, who owns
them, who consumes them and what governance information is needed?**

It is usually a table or repository record rather than a diagram. It complements
runtime views by recording stable facts that would clutter a drawing. It is useful for
application owners, integration architects, developers, testers, operations teams,
security reviewers and governance forums.

A beginner-friendly interface catalogue might include:

| Field | Purpose |
|---|---|
| Interface name | Stable name used by architecture and delivery teams |
| Provider | System or team accountable for the interface |
| Consumers | Known systems, channels or external parties that use it |
| Style | API, event, queue, file, adapter or data feed |
| Direction | Who calls, publishes, subscribes, sends or receives |
| Business meaning | What outcome or information the interface represents |
| Contract reference | OpenAPI, AsyncAPI, schema, file specification or other contract |
| Version | Current supported contract version |
| Security classification | Handling need for data crossing the boundary |
| Failure behaviour | Timeout, retry, duplicate handling, dead-letter or repair expectation |
| Operational owner | Team that monitors and supports the interface |

For the Simple Online Store, the catalogue might contain `Create Order API`, `Payment
Authorisation API`, `Shipment Booking API` and `OrderPlaced Event`. For Horizon Bank,
it might contain `Payment Initiation API`, `Screening Request Interface`, `Posting
Request Interface`, `Payment Status Event` and `Payment Reporting Feed`.

The catalogue should not become a dumping ground. Keep it tied to real interfaces and
decisions. If an entry has no owner, no consumers and no contract reference, it is a
risk, not a completed record.

## How to choose the right integration view

`FIG-18-01` is the planned visual selection guide for this chapter. Its specification is
registered, but the figure source and export are deferred until the author approves the
specification. Until the figure is produced, use the selection table below as the
working guide.

| View | Main question | Best audience | Best time to use | Common mistake |
|---|---|---|---|---|
| Integration context view | Which systems exchange information, and by what broad integration style? | Enterprise architects, solution architects, application owners and risk reviewers | Early integration scope and dependency discussion | Labelling every line `integrates with` |
| API interaction view | Which caller invokes which API operation, and what response or later status follows? | Architects, developers, testers and API owners | Channel-to-service or service-to-service design | Treating accepted-for-processing as completed business outcome |
| Message-flow view | Which messages move between systems, platforms or participants? | Integration architects, developers, operations and process analysts | When direction, routing and delivery expectation matter | Hiding synchrony, ownership and delivery expectation |
| UML sequence diagram | What ordered messages occur in one runtime scenario? | Architects, developers and testers | When order, alternatives and responsibility need precision | Turning one scenario into a complete interface inventory |
| C4 dynamic diagram | How do known C4 elements collaborate at runtime? | Architects and technical reviewers | After structure views identify systems, containers or components | Using it without a known structural boundary |
| Event-flow view | What event is published, by whom, and who reacts? | Integration architects, data teams, developers and operations | When event ownership and consumer reaction matter | Treating event publication as shared write ownership |
| Queue or asynchronous processing view | Where can work wait, and how is delayed processing handled? | Integration, platform and operations teams | When systems must decouple processing time or absorb peaks | Drawing a queue without ordering, retry or monitoring rules |
| Error and retry view | What happens when calls, messages or events fail? | Architects, developers, testers, operations and risk reviewers | Before implementation and operational readiness review | Saying "retry" without idempotency or reconciliation |
| Interface catalogue | Which interfaces exist, who owns them and what contracts govern them? | Application owners, architects, developers, testers and governance forums | When interfaces must be governed, tested and operated | Treating a diagram as the complete contract |
| Data-flow view | What information moves, transforms or is stored across boundaries? | Data architects, integration architects and risk reviewers | When data meaning, movement or lineage is the concern | Using data flow as a runtime sequence diagram |

The table is not a maturity ladder. A simple interface catalogue can be more valuable
than a beautiful dynamic diagram if the real problem is ownership. A sequence diagram
can be more useful than a broad landscape if the decision depends on timeout or retry
order. Choose the view that answers the question.

## Worked example: Simple Online Store

The Online Store checkout is a small enough example to show the differences between
integration views.

If the question is "which systems are involved?", start with an integration context
view. Show Web App, Online Store, Payment Provider System and Delivery Partner System.
Label relationships as order API, payment authorisation API, shipment booking API and
delivery status event. This view helps the team agree scope and dependency direction.

If the question is "what happens when the customer places the order?", use a sequence
diagram or C4 dynamic view. Show Customer, Web App, Online Store API Application, Order
Database, Payment Provider System and Delivery Partner System. Keep it to one scenario:
valid basket, payment authorised and shipment requested. Add a small alternative for
payment rejected if that is important to the decision.

If the question is "what happens after the order is accepted?", use an event-flow view.
Show `OrderPlaced` being published by the Online Store and consumed by customer
notification, delivery coordination or reporting consumers. State whether the event is a
domain event, integration event or technical notification, and who owns its meaning.

If the question is "what happens when payment is uncertain?", use an error and retry
view. Show payment timeout, pending order state, retry or reconciliation, customer
message and support ownership. This view often prevents the common user-facing mistake:
telling the customer that the order is confirmed when the payment result is unknown.

If the question is "what stable interfaces must be governed?", use an interface
catalogue. Record Create Order API, Payment Authorisation API, Shipment Booking API and
OrderPlaced Event with provider, consumers, contract reference, version, security
classification, failure behaviour and operational owner.

The checkout feature does not need every view at the start. It needs the first view
that matches the next decision, then additional views when design risk becomes visible.

## Worked example: Horizon Bank

Horizon Bank payment submission is more complex because business risk, financial crime
screening, legacy posting and status visibility all matter.

If the question is "what integration landscape surrounds payment submission?", use an
integration context view. Show Horizon Digital Channels, Payments Platform, Financial
Crime Platform, Core Deposit System, Enterprise Integration Platform, Event Platform
and Enterprise Data Platform. Label relationships with integration styles such as
payment initiation API, screening request, posting request, payment status event and
payment reporting feed.

If the question is "what runtime path occurs for one payment submission?", use a UML
sequence diagram or C4 dynamic view. Show Horizon Digital Channels submitting the
payment instruction, Payments Platform validating it, Financial Crime Platform returning
screening status, Core Deposit System accepting or rejecting posting, and Event
Platform distributing the later status event.

If the question is "what should the channel tell the customer?", model the API
interaction and status behaviour. The response from Payments Platform may be `accepted
for processing`, not `posted`. Horizon Digital Channels then needs a way to show
`received`, `screening`, `processing`, `posted`, `rejected` or `failed`, depending on
the payment lifecycle. That status model connects to Chapter 17 state-machine guidance
and Chapter 19 data ownership.

If the question is "how do downstream consumers learn about payment progress?", use an
event-flow view and event catalogue entries. `PaymentInstructionReceived`,
`PaymentScreeningCompleted` and `PaymentPosted` should have clear producer ownership,
business meaning, version, consumers and duplicate-handling expectations. CloudEvents
may help standardise envelope metadata, and AsyncAPI may help document message-driven
contracts, but neither replaces business ownership [CNCF-CLOUDEVENTS-1.0.2]
[ASYNCAPI-3.1.0].

If the question is "what happens when Core Deposit System times out?", use an error and
retry view. State whether the Payments Platform can retry safely, which identifier
supports idempotency, how reconciliation detects uncertain posting, which queue or case
captures failed work, which team receives alerts and what the customer sees during the
uncertain period.

If the question is "what must be governed over time?", use an interface catalogue. The
catalogue can record Payment Initiation API, Screening Request Interface, Posting
Request Interface, Payment Status Event and Payment Reporting Feed. It should name
provider, consumers, style, direction, contract, version, classification, failure
behaviour and operational owner.

The bank should avoid one enormous payment integration diagram. The better approach is
a small set of connected views, each with a clear question and audience.

## Common mistakes

The first mistake is labelling every relationship `integrates with`. Integration views
need direction, style, meaning and ownership.

The second mistake is treating a system landscape as an interface catalogue. A landscape
shows selected relationships; a catalogue records governed interface facts.

The third mistake is using a sequence diagram for every integration question. Sequence
diagrams are strong for one scenario and message order, but weak as contract
repositories.

The fourth mistake is hiding asynchronous behaviour behind synchronous language.
`Accepted` may mean accepted for processing, not completed.

The fifth mistake is drawing event publication without ownership. An event has a
producer, meaning, version and consumers. Consumers should not infer write authority
from the fact that they receive an event.

The sixth mistake is assuming a queue solves failure by itself. Queues also need
ordering, retry, duplicate handling, dead-letter handling, retention, monitoring and
support ownership.

The seventh mistake is adding retries without idempotency. A repeated request or
message can duplicate a business effect unless the receiver can recognise and handle
the duplicate safely.

The eighth mistake is mixing integration, data architecture, infrastructure and
security detail in one view without stating the reason. A focused companion view is
usually clearer.

## Review checklist

- [ ] The integration question is explicit before the view is selected.
- [ ] System boundaries and ownership are clear.
- [ ] Relationship labels state integration style, direction and meaning.
- [ ] Synchronous, asynchronous and event-driven behaviour are distinguished.
- [ ] API responses do not overstate completed business outcomes.
- [ ] Sequence diagrams and C4 dynamic views stay focused on one scenario or selected
  path.
- [ ] BPMN message flows are used only when business-process participants and hand-offs
  are the concern.
- [ ] Event-flow views name producer, event meaning, consumers and ownership.
- [ ] Queue and asynchronous views include retry, ordering, duplicate, dead-letter and
  monitoring considerations where relevant.
- [ ] Error and retry behaviour includes timeout, idempotency, reconciliation and
  customer-visible status where relevant.
- [ ] Interface catalogue entries include provider, consumers, contract, version,
  classification, failure behaviour and operational owner.
- [ ] Data-flow views are kept separate from runtime sequence unless the viewpoint
  explicitly explains the combination.
- [ ] The Simple Online Store and Horizon Bank examples use controlled names from the
  repository.
- [ ] Source keys are registered and no unsupported standard wording is copied.

## Key takeaways

- Integration modelling is about runtime information exchange, dependency and recovery
  behaviour.
- Start with the integration question, then choose the smallest view that answers it.
- Integration context views show systems and broad integration styles.
- API interaction views must distinguish accepted-for-processing from completed
  business outcomes.
- Sequence diagrams and C4 dynamic views are good for one selected runtime scenario.
- Event-flow views need producer ownership, event meaning, consumers and delivery
  expectations.
- Queues and retries require idempotency, duplicate handling, dead-letter handling and
  monitoring.
- Interface catalogues govern stable interface facts that should not be hidden inside a
  diagram.

## Practical exercise

Horizon Bank is improving payment submission from Horizon Digital Channels. A Retail
Customer submits a payment. The Payments Platform validates it, requests screening from
Financial Crime Platform, requests posting from Core Deposit System and publishes
status through Event Platform. Sometimes screening is slow, and sometimes the posting
request times out.

Choose the first view for each question:

1. Which systems exchange information during payment submission?
2. Which API call does Horizon Digital Channels make, and what immediate response does
   it receive?
3. What ordered messages occur in the normal successful payment path?
4. Which events tell downstream consumers about payment progress?
5. Where can work wait if screening or posting is delayed?
6. What happens if the posting request times out?
7. Which interfaces must be owned, versioned, tested and operated?
8. Which information moves into reporting or analytics after payment posting?

Suggested answer:

- Use an integration context view for the involved systems and broad integration
  styles.
- Use an API interaction view for the channel-to-payments request and immediate
  response.
- Use a UML sequence diagram or C4 dynamic view for the ordered successful runtime
  path.
- Use an event-flow view and event catalogue entries for payment-progress events.
- Use a queue or asynchronous processing view for delayed work and buffering.
- Use an error and retry view for timeout, idempotency, reconciliation, status and
  operational ownership.
- Use an interface catalogue for governed interfaces, contracts, versions, consumers
  and support ownership.
- Use a data-flow or lineage view for reporting and analytics movement, then continue
  into Chapter 19 for data architecture detail.

Good review criteria are: each selected view answers the stated question; the design
does not confuse immediate response with completed outcome; retry behaviour is tied to
idempotency and reconciliation; and every important interface has an owner.

## References and further reading

Chapter source notes are maintained in the repository under `research/uml/`,
`research/c4/`, `research/bpmn/` and `research/domain-event/`, and registered in
`SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md),
is the intended publication location for the final source-key index.

- `[OMG-UML]`: Object Management Group, Unified Modeling Language specification,
  version 2.5.1.
- `[C4-OFFICIAL]`: Official C4 model documentation.
- `[OMG-BPMN]`: Object Management Group BPMN 2.0.2 specification.
- `[CNCF-CLOUDEVENTS-1.0.2]`: CloudEvents specification, version 1.0.2.
- `[ASYNCAPI-3.1.0]`: AsyncAPI Specification, version 3.1.0.
