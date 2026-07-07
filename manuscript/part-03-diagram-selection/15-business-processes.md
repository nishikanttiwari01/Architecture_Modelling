---
title: "Modelling Business Processes"
chapter: 15
part: "part-03-diagram-selection"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-07"
---

# 15. Modelling Business Processes

## Chapter purpose

Select and combine Business Process Model and Notation (BPMN), Unified Modeling Language (UML) activity diagrams, swimlane-style responsibility views and value streams when the architecture question is about business process.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain the difference between a value stream, a process architecture, a process model and a system behaviour flow.
- Choose between a BPMN process diagram, a BPMN collaboration diagram, a UML activity diagram, a responsibility view and a value stream.
- Select the right level of process detail for strategy, architecture, analysis and operational review.
- Show responsibility, hand-offs, exceptions, controls and metrics without turning one diagram into everything.
- Trace process models back to capabilities and forward to software, data, integration and decision models.
- Review a process model critically for scope, audience, ownership, abstraction, exceptions and common misuse.

## Prerequisites and dependencies

- Chapter 4: UML: Unified Modeling Language
- Chapter 6: BPMN: Business Process Model and Notation
- Chapter 9: Decision Modelling and DMN
- Chapter 13: Other Useful Modelling Approaches
- Chapter 14: Modelling Business Strategy and Capabilities

## Required models and artefacts

This chapter uses a mixed notation selection guide as a manuscript table. It reuses existing figures rather than introducing new Chapter 15 diagram source:

- FIG-06-01: Online Store order fulfilment BPMN process.
- FIG-06-02: Horizon Bank customer onboarding BPMN collaboration.
- FIG-06-03: Horizon Bank payment repair BPMN exception collaboration.
- FIG-04-05: Horizon Bank payment validation activity diagram.
- FIG-09-04: BPMN and DMN Responsibility Split.
- FIG-13-02: Horizon Bank Customer Onboarding Value Stream.

## Worked examples

- Simple Online Store return handling and order fulfilment.
- Horizon Bank onboarding, payment repair and payment validation.

## Source requirements

- `[OMG-BPMN]` supports BPMN 2.0.2 terminology for process, collaboration, events, activities, gateways, sequence flows, message flows, pools and lanes.
- `[OMG-UML]` supports UML 2.5.1 activity diagram terminology at the diagram-type level reused from Chapter 4.
- `[OMG-DMN-1.5]` supports the separation of repeatable decision logic from process flow when the chapter discusses BPMN with Decision Model and Notation (DMN).
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]` supports the value-stream framing reused from Chapters 13 and 14.
- Chapter guidance is the author's practical interpretation for beginner architecture work.
- Existing source notes are sufficient for this draft; no new source note is required.

## Planned chapter structure

## Process architecture

Process architecture answers: **which business processes exist, how they relate, who owns them and which processes need more detailed modelling?**

It is tempting to start by drawing the first process someone mentions. A better first step is to understand the process landscape. A process landscape is the map of major business processes at a level where a sponsor, process owner or architect can see the whole area before zooming into one flow.

For the Simple Online Store, the process landscape might include `Place order`, `Fulfil order`, `Handle return`, `Respond to customer enquiry` and `Resolve payment exception`. For Horizon Bank, it might include `Onboard customer`, `Open account`, `Initiate payment`, `Repair payment`, `Investigate fraud alert` and `Handle customer service case`.

A process architecture is not the same as a capability map. A capability says what the organisation must be able to do, such as `Identity Verification` or `Payment Screening`. A process says how work happens over time, such as capture application, request screening, wait for result, review exception and notify the customer. Chapter 14 used capabilities and value streams to decide where change matters. This chapter shows how to model the operational flow once the team needs sequence, responsibility and exceptions.

The first process-architecture question is often not "which BPMN symbols do we need?", but "which process deserves a detailed model?" Choose the process where decisions will be made: a high-risk exception path, a hand-off that causes delay, a control that must be evidenced, or a customer journey stage where ownership is unclear.

At this level, a table is often better than a diagram:

| Process | Trigger | Outcome | Owner | Why model it now? |
|---|---|---|---|---|
| Handle return | Customer requests return | Return approved, rejected or escalated | Customer Support Agent | Clarify eligibility, refund and collection hand-offs |
| Onboard customer | Retail Customer submits application | Customer relationship ready or application rejected | Relationship Manager | Connect onboarding roles, screening and exception review |
| Repair payment | Payment posting fails | Payment resubmitted, cancelled or timed out | Operations Analyst | Make exception ownership and customer response timing visible |

The process architecture gives the reader a controlled list. The detailed process model then zooms into one selected process instead of trying to cover the whole bank or store on one page.

## Process levels

Process levels answer: **how much detail should this process model show?**

Beginners often mix levels without noticing. A diagram might show `Open account`, `Click submit`, `Check sanctions list`, `Create customer record` and `Send API request` as if these were equivalent activities. They are not. Some are business outcomes, some are user-interface actions, some are control checks and some are implementation steps.

Use four practical levels:

| Level | Question | Typical model | Example activity |
|---|---|---|---|
| Level 0: Process landscape | Which processes exist and relate? | Process catalogue or high-level map | Customer onboarding |
| Level 1: End-to-end process | What major stages and outcomes occur? | Value stream or high-level BPMN | Application received to services ready |
| Level 2: Operational process | Who does what, in what order, with what exceptions? | BPMN process or collaboration | Request screening and review possible match |
| Level 3: Procedure or automation detail | Which fields, screens, service calls or engine steps occur? | Procedure, workflow design or technical sequence | Validate mandatory fields and call screening API |

Architecture work usually lives around levels 1 and 2. Level 0 helps select the scope. Level 3 becomes useful when implementation, workflow configuration, test design or operational procedure is the actual question. Do not force level 3 detail into a chapter whose audience is trying to understand process ownership and architecture implications.

For Horizon Bank onboarding, FIG-13-02 shows value stages. It does not show tasks. FIG-06-02 then zooms into a BPMN collaboration where Horizon Bank requests screening and waits for a result. A later implementation chapter might add API contracts, event schemas or workflow-engine details, but those belong to different views.

## BPMN selection

BPMN selection answers: **when is BPMN the right model for the process question?**

Business Process Model and Notation (BPMN) is the strongest choice in this chapter when the reader needs to see process order, participants, responsibility, events, gateways, messages and exceptions [OMG-BPMN]. It is especially useful when the process crosses organisational or system boundaries and when the exception path matters as much as the happy path.

Use a BPMN process diagram when the work stays inside one process owner or participant. FIG-06-01 does this for Online Store order fulfilment. It shows the main order fulfilment flow inside the Online Store, with stock availability and fulfilment outcomes. It deliberately avoids payment-provider internals, delivery-provider internals and software component design.

Use a BPMN collaboration diagram when multiple participants exchange messages. FIG-06-02 does this for Horizon Bank customer onboarding. The Retail Customer and Financial Crime Platform are separate participants; Horizon Bank does not own their internal processes. Message flows cross participant boundaries, while sequence flows stay inside the Horizon Bank process.

Use a focused BPMN exception view when the problem is waiting, timeout, escalation, repair or rejection. FIG-06-03 shows payment repair after posting failure. The event-based gateway matters because it records that the process waits for whichever event happens first: customer correction or timeout.

BPMN is not the best choice for every flow. A UML activity diagram may be enough when the flow is internal system logic. A value stream is better when the question is how stakeholder value progresses before operational detail is known. A DMN decision table is better when the question is the repeatable logic behind a decision result. A C4 dynamic diagram or UML sequence diagram is better when the question is message order between software parts.

The selection rule is simple: use BPMN when the process behaviour itself is the subject, not when the process is merely background context for a software, data, deployment or decision model.

## Swimlanes and responsibilities

Swimlanes and responsibility views answer: **who performs or owns each part of the work?**

The word swimlane is used broadly for any horizontal or vertical partition that shows responsibility. In BPMN, the formal terms are pool and lane. A pool represents a participant, such as an organisation, major process owner or black-box external party. A lane partitions responsibility inside a pool [OMG-BPMN].

Responsibility modelling is often the reason a process diagram is needed. A flow can look simple until the modeller shows that a customer, customer support, operations, compliance, a platform team and an external provider all touch it. Lanes reveal hand-offs, and hand-offs reveal delay, control gaps and ownership questions.

For the Simple Online Store return process, a useful first split might be:

| Responsibility | Example work |
|---|---|
| Customer | Submit return request and provide requested evidence |
| Customer Support Agent | Check policy exception and communicate with the customer |
| Online Store fulfilment | Confirm dispatch status and arrange return collection |
| Payment Provider System | Receive refund request and return refund status |
| Delivery Partner System | Receive collection request and return collection status |

Do not create a lane for every job title or application by habit. A lane should answer a responsibility question. If the model becomes wide and unreadable, group responsibilities and explain the more detailed operating model in a supporting table.

For Horizon Bank onboarding, lanes might separate Digital Channels, Onboarding Operations and Compliance inside the Horizon Bank pool, with Financial Crime Platform shown as a separate pool. This distinction is important: a lane inside Horizon Bank means Horizon Bank owns the flow. A separate pool means the participant has its own behaviour and communicates by messages.

When a responsibility view is needed but BPMN notation is too heavy for the audience, a simple responsibility matrix may be better. For example:

| Process activity | Retail Customer | Relationship Manager | Operations Analyst | Compliance Officer |
|---|---|---|---|---|
| Submit application | Performs | Informed | | |
| Validate application completeness | | Accountable | Supports | |
| Review possible screening match | | Informed | Supports | Accountable |
| Notify outcome | Receives | Accountable | Supports | Informed |

This table is not a BPMN diagram. It is a responsibility view. Use it when ownership is the question and sequence is secondary.

## Exceptions and controls

Exceptions and controls answer: **what happens when the normal path cannot continue, and how is important work governed?**

The normal path is rarely enough for architecture review. A process model that says "screen customer, open account" hides the cases that usually matter: missing evidence, possible sanctions match, timeout, failed posting, rejected refund, system outage or manual override.

For beginner process modelling, show at least the important exception paths:

| Exception type | Process modelling question | Example |
|---|---|---|
| Missing information | How does the process request and wait for correction? | Customer must provide identity evidence |
| Business rejection | How is the negative outcome recorded and communicated? | Return request outside policy |
| Control exception | Who reviews a risk or compliance concern? | Possible financial-crime screening match |
| Technical failure | What business process starts when automation fails? | Payment posting failure creates repair case |
| Timeout | What happens when a response does not arrive in time? | Customer correction deadline reached |
| Escalation | When does another role or process intervene? | Compliance Officer reviews unresolved match |

BPMN has useful notation for these cases, including boundary events, intermediate events, event-based gateways, escalations and alternative end events [OMG-BPMN]. The chapter does not need to re-teach every symbol from Chapter 6. The selection point is this: choose BPMN when these exception behaviours must be visible and reviewable.

Controls should be modelled with care. A control is not just another box labelled "check". The model should say what is controlled, who performs or owns it, what evidence is produced and what happens if the control fails. For Horizon Bank screening, the process should show the screening request, the received result, the review of a possible match and the outcome. A separate decision model or control table can hold the detailed rule logic and evidence requirements.

Do not overload a BPMN model with every control detail. Use the process model to show where the control occurs and how its result affects the flow. Use a Decision Model and Notation (DMN) model for repeatable decision logic, a security control map for security evidence or an audit table for control ownership when those questions require more precision.

## Process metrics

Process metrics answer: **how will the organisation know whether the process is working well enough?**

A process diagram explains flow. It does not automatically explain performance. Metrics make the model useful for improvement, but only if they are tied to the process question. Avoid attaching every possible measure to the diagram. Pick the few measures that reveal whether the process outcome, customer experience, risk control or operational health is acceptable.

Useful process metrics include:

| Metric type | Question | Example |
|---|---|---|
| Cycle time | How long does the process take end to end? | Median time from application submitted to services ready |
| Waiting time | Where does work sit idle? | Time waiting for customer correction |
| Rework | How often must work be corrected or repeated? | Percentage of returns needing extra evidence |
| Exception rate | How often does the process leave the normal path? | Percentage of payments entering repair |
| Straight-through processing | How often does the process complete without manual intervention? | Percentage of clear onboarding cases completed without operations review |
| Control evidence | Can required reviews be evidenced? | Percentage of screening decisions with retained evidence |
| Outcome quality | Did the process produce the intended result? | Percentage of orders dispatched correctly first time |

Straight-through processing means a process completes without manual intervention for the scope being measured. It is not automatically good in every case. A high-risk payment or a possible screening match may need manual review. The useful question is not "how do we maximise automation?", but "which cases should flow straight through, and which should deliberately stop for review?"

Metrics should be placed at the level where they can be acted on. A sponsor may care about end-to-end onboarding time. An operations lead may care about exception queue age. A compliance reviewer may care about retained evidence. A solution architect may care about whether the process needs events, status tracking or workflow state to measure those metrics accurately.

In Chapter 14, OUT-14-01 used median onboarding time as an illustrative outcome measure. Chapter 15 connects that outcome to process modelling: the team now needs to see where onboarding waits, which exceptions interrupt it, and which roles can act.

## Process-to-capability traceability

Process-to-capability traceability answers: **which stable business abilities does this process use, and where does process detail start to affect architecture choices?**

Capabilities and processes are different, but they should not drift apart. A capability map gives stable language for business abilities. A process model shows how work happens. Traceability connects them so the team can say, for example, that the onboarding process uses `Document Capture`, `Identity Verification`, `Financial Crime Screening`, `Risk Assessment`, `Party Management`, `Account Opening` and `Notification Management`.

This traceability matters because process changes often lead to architecture changes. If a process waits for screening results, the architecture may need a status event, a case record, an integration contract and evidence retention. If a process relies on party data, the architecture may need a trusted party record. If a process has many payment repair cases, the architecture may need better validation, routing decisions or operational tooling.

For Horizon Bank onboarding:

| Process segment | Capabilities used | Architecture questions raised |
|---|---|---|
| Capture application | Digital Servicing, Document Capture | Which channel captures evidence, and where is it retained? |
| Verify identity and eligibility | Identity Verification, Risk Assessment | Which data and decision inputs are required before proceeding? |
| Screen customer | Financial Crime Screening | How are requests, results, possible matches and evidence retained? |
| Establish relationship | Party Management, Account Opening | Which systems create party, customer and account records? |
| Notify and enable service | Notification Management, Account Servicing | Which status events and customer messages are needed? |

The process model should not pretend that a capability is a step. `Financial Crime Screening` is a capability. `Request screening`, `Receive screening result` and `Review possible match` are process activities or events. Keeping that distinction protects the Chapter 14 capability work and makes Chapter 16 software structure easier to connect later.

## Selection table

The selection table answers: **which model should a beginner reach for when the process question changes?**

| Question | Best first model | Main audience | Use it for | Avoid using it for |
|---|---|---|---|---|
| Which major processes exist? | Process catalogue or process architecture table | Sponsors, process owners and architects | Scope selection and ownership | Detailed task sequence |
| How does stakeholder value progress? | Value stream | Business architects, product owners and sponsors | Value stages and capability alignment | Roles, timers, message flows and exceptions |
| What is the ordered business flow inside one owner? | BPMN process diagram | Analysts, process owners and architects | Activities, gateways, events and outcomes | Software component structure |
| Which participants exchange messages? | BPMN collaboration diagram | Analysts, architects and control reviewers | Cross-boundary hand-offs and ownership | Internal application design |
| What happens when the normal path fails? | Focused BPMN exception view | Operations, risk, compliance and architects | Repair, timeout, escalation and rejection paths | Full procedure manuals |
| Who is responsible for each activity? | BPMN lanes or responsibility matrix | Process owners and operating teams | Hand-offs and accountability | Detailed timing or system internals |
| What compact flow happens inside a system or service? | UML activity diagram | Architects, developers and testers | Algorithm-like or system-level behaviour | Multi-participant business collaboration |
| What repeatable decision logic chooses an outcome? | DMN decision table or DRD | Business, risk, compliance and technology teams | Rules, inputs, decisions and authorities | Human task sequence |
| Which software parts interact during one scenario? | UML sequence or C4 dynamic view | Architects, developers and testers | Runtime message order | Business responsibility and process ownership |

No model is universally better. The right model is the smallest one that answers the current question without misleading the audience. If the discussion moves from value stages to operational work, move from value stream to BPMN. If the discussion moves from process flow to rule logic, split out DMN. If the discussion moves from business work to software responsibilities, move to Chapter 16.

## Worked example

The Simple Online Store return process starts with a customer request. The first architecture question is modest: which model helps the team agree the flow without turning it into software design?

A process architecture table names `Handle return` as the selected process. A value stream might be too high level if the problem is eligibility, refund and collection hand-offs. A BPMN collaboration is a good fit if the store needs to show messages between Customer, Online Store, Payment Provider System and Delivery Partner System. A responsibility matrix may be enough if the only argument is whether Customer Support Agent or Fulfilment owns the eligibility exception. A UML activity diagram could be enough if the team is only explaining eligibility logic inside the Online Store.

A first BPMN collaboration for returns might include these steps in prose before drawing:

1. Customer submits return request.
2. Online Store checks return eligibility.
3. If eligible, Online Store requests refund from Payment Provider System.
4. If collection is required, Online Store requests collection from Delivery Partner System.
5. If outside policy, Customer Support Agent reviews the exception.
6. Customer receives approval, rejection or request for more information.

The diagram should deliberately exclude payment-settlement internals, delivery-provider routing, warehouse stock adjustment, user-interface screens and database tables. Those details may be modelled later, but they are not needed to agree the process.

Horizon Bank shows the same selection logic at enterprise scale. Chapter 14 identified onboarding speed, screening traceability and payment transparency as strategic concerns. Chapter 15 asks how the work actually happens.

For customer onboarding, use the Chapter 13 value stream first when the question is stakeholder value and enabling capabilities. Use FIG-06-02 when the question becomes process collaboration: customer application, bank-owned onboarding flow, screening request, screening result, compliance review and final outcome. Use DMN when the question becomes the screening or eligibility decision logic. Use Chapter 16 software structure views when the question becomes which platforms and components support capture, screening, party creation and notification.

For payment repair, use FIG-06-03 because the exception path is the point. A payment posting failure creates a repair situation. Operations reviews the exception, may request customer correction, waits for either corrected information or a timeout, and then resubmits or closes the case. A happy-path payment sequence would hide the behaviour that operations and risk reviewers need to see.

For payment validation inside the Payments Platform, FIG-04-05 is a UML activity diagram. That is suitable because the scope is internal system behaviour: receive instruction, validate fields, check limits, request screening, decide whether to continue, post payment and publish status. It is not a complete business process. It deliberately excludes customer service, operations repair, compliance casework and external participant collaboration.

The architecture skill is knowing when to switch models. A value stream says where value is created. BPMN says how the work happens. DMN says how a repeatable decision is derived. UML activity says how internal behaviour flows. C4 and UML structure views say which software parts support the process. Keeping those viewpoints separate makes the final architecture easier to review.

## Common mistakes

The first mistake is turning a value stream into a process model. Value stages are not BPMN activities. They describe stakeholder value, not detailed sequence, roles, timers or exceptions.

The second mistake is using BPMN to show software structure. A BPMN pool is not a C4 container, and a lane is not automatically an application component.

The third mistake is mixing process levels. A readable model does not combine "open account", "click button", "call API" and "complete regulatory review" as if all are the same kind of activity.

The fourth mistake is hiding exceptions. The path that fails, waits, rejects or escalates is often the path architecture reviewers need most.

The fifth mistake is using too many swimlanes. Lanes should clarify responsibility, not reproduce the organisation chart.

The sixth mistake is copying decision logic into BPMN gateways when a governed DMN model should own the rules.

The seventh mistake is treating process metrics as decorative labels. A metric should have a definition, owner and use in review.

The eighth mistake is breaking traceability between process activities and capabilities. A process uses capabilities; it should not rename them casually or turn them into task lists.

## Key takeaways

- Start with the process question before choosing BPMN, UML activity, value stream, DMN or a responsibility view.
- A process architecture names and scopes the processes before one detailed flow is drawn.
- Value streams show stakeholder value stages; BPMN shows operational process behaviour.
- BPMN is strongest when order, participants, messages, events, gateways, exceptions and hand-offs matter.
- UML activity diagrams are useful for compact internal behaviour, especially inside one system or service.
- Swimlanes and lanes should clarify responsibility, not reproduce every role or application.
- Important exception, timeout, repair, rejection and escalation paths should be shown or explicitly excluded.
- Process metrics and capability traceability connect the model to architecture decisions, not just documentation.

## Practical exercise

Horizon Bank wants to improve the customer onboarding process. The sponsor cares about reducing the time from application submission to usable services. Compliance cares about screening evidence. Operations cares about possible match review and customer correction.

Choose the first model for each question:

1. Which model should show the value stages from customer need to services ready?
2. Which model should show the operational flow, participants, screening request, screening result and possible match review?
3. Which model should show the detailed decision logic for whether an application is clear, needs review or should be rejected?
4. Which model should show the internal validation flow inside the Customer Onboarding Platform?
5. Which table or model should connect onboarding activities to `Document Capture`, `Identity Verification`, `Financial Crime Screening`, `Risk Assessment`, `Party Management` and `Account Opening`?
6. Name two exception paths that the process model should not hide.

Suggested answer:

- Use a value stream for stakeholder value stages.
- Use a BPMN collaboration diagram for the operational process and participant message exchange.
- Use a DMN decision table or DRD for repeatable decision logic.
- Use a UML activity diagram if the scope is internal validation behaviour inside one system.
- Use a process-to-capability traceability table.
- Show possible screening match review and missing customer evidence or timeout. Other valid exception paths include application rejection, technical failure in screening request, or account-opening failure.

## Review checklist

- [ ] The process question is explicit before a notation is selected.
- [ ] The audience and abstraction level are clear.
- [ ] Process architecture, value stream, BPMN process, BPMN collaboration, UML activity and DMN are distinguished.
- [ ] Formal terms are introduced after a plain-language explanation.
- [ ] Sequence, responsibility, messages, exceptions and controls are modelled only where they serve the question.
- [ ] Important exceptions, timeouts, escalations and rejection paths are shown or explicitly excluded.
- [ ] Process metrics have definitions and do not imply unsupported performance claims.
- [ ] Process activities trace to stable capability names where capability alignment matters.
- [ ] The Simple Online Store and Horizon Bank examples are consistent with repository example files.
- [ ] Comparisons do not imply that one notation is universally superior.
- [ ] Required sources and reused diagrams are registered.
- [ ] Terminology, link and word-count checks pass.

## References and further reading

Chapter source notes are maintained under `research/bpmn/`, `research/uml/`, `research/dmn/` and `research/other-modelling/`, and registered in `SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index.

- `[OMG-BPMN]`: Object Management Group BPMN 2.0.2 specification.
- `[OMG-UML]`: Object Management Group UML 2.5.1 specification.
- `[OMG-DMN-1.5]`: Object Management Group DMN 1.5 formal specification.
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`: The Open Group TOGAF Series Guides for Business Capabilities and Value Streams.

## Drafting notes

- Target length: 2,000 to 4,000 words unless the chapter scope justifies more.
- Draft uses existing official source notes and reuses existing figures. No Chapter 15 diagram specification, source or export has been created.
- Keep this file as the canonical manuscript source for the chapter.
- Do not mark this chapter `Approved` without explicit author approval.
