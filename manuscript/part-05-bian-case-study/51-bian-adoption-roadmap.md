---
title: "APIs, Events, Commands, Batch, Files, Workflow and External Networks"
chapter: 51
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 51. APIs, Events, Commands, Batch, Files, Workflow and External Networks

## Chapter purpose

Explain how Horizon Bank selects and governs interaction styles across a full-service-bank estate. The chapter distinguishes synchronous Application Programming Interfaces (APIs), commands, events, messages, batch, files, workflow hand-offs and external-network exchanges, then connects each style to semantics, security, failure, reconciliation and operations.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- select an interaction style from the needs of the business exchange rather than platform preference;
- distinguish a command, event and general asynchronous message;
- define the minimum contract for APIs, events, batch, files and workflow;
- adapt Banking Industry Architecture Network (BIAN) semantics without copying a specification into an unsuitable implementation;
- model external networks as trust, timing and operating boundaries; and
- trace failure, duplicate, correction, recovery and reconciliation behaviour.

## Prerequisites and dependencies

- Chapter 18: Modelling Integration and Runtime Behaviour
- Chapter 34: Full Bank Application and Integration Landscape
- Chapter 46: Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting
- Chapter 49: BIAN Mapping Method and Full-Stack Traceability
- Chapter 50: BIAN-Aligned Application, Software-Service and Team Boundaries

## Required models and artefacts

- `examples/horizon-bank/interfaces.md`
- `examples/horizon-bank/external-networks.md`
- Logical application and information-authority catalogues
- Accounting-event, reconciliation, control and critical-operation catalogues
- Versioned API or message contracts and operational ownership records

## Worked examples

- Interaction trace for `HB-SCN-02 Execute Cross-Border Payment`

## Source requirements

BIAN, OpenAPI, CloudEvents and AsyncAPI claims use official sources. Horizon Bank contracts, interfaces and external networks are fictional author models. The catalogue records logical exchanges and does not assert membership of a named scheme, provider or market infrastructure [BIAN-14-MAPPING-PV49-52] [OPENAPI-3.2-PV51] [EVENT-CONTRACTS-PV51].

## The question this architecture answers

This architecture answers: **How should two responsibilities exchange a request, fact, data set or work item so that meaning, authority and failure remain controlled?**

The answer begins with the business interaction. It then chooses a style and transport. Starting with `we use APIs` or `we are event driven` skips questions about completion, consistency, time, volume, evidence and recovery.

## Who uses interaction models

Business and domain owners define the meaning and outcome. Integration and solution architects select the style and boundaries. Developers and platform engineers implement and test contracts. Security, data, control, reconciliation and operations owners verify protection, lineage, financial completeness, monitoring and repair. External-network relationship owners confirm participant and support assumptions.

## Interaction style is a design decision

An interface is a governed point of interaction. Its style describes how information or control crosses a boundary. Horizon Bank uses the controlled interface types `API`, `Command`, `Event`, `Message`, `Batch`, `File` and `Workflow`.

| Style | Meaning | Typical reason to use it | Horizon Bank example |
|---|---|---|---|
| API | A caller requests information or behaviour and receives an immediate protocol response | Interactive validation, enquiry or bounded action | `HB-INT-015 Payment Entitlement Decision` |
| Command | A directed request asks one owner to perform an action | The receiver owns whether and how the action occurs | `HB-INT-036 Accepted Payment Command` |
| Event | A producer publishes a fact that has occurred | Several consumers may react without controlling the producer | `HB-INT-066 Intraday Settlement Position Event` |
| Message | An asynchronous exchange that is not classified as a pure command or event | Bilateral processing, protocol exchange or mixed request/status flow | `HB-INT-105 Cross-Border Financial Message` |
| Batch | A scheduled or grouped processing exchange | Periodic high-volume calculation, reporting or ledger work | `HB-INT-082 Subledger Journal Batch` |
| File | A governed file transfer with receipt and evidence | External submissions, bulk exchange or retained file contracts | `HB-INT-088 Regulatory Return Submission` |
| Workflow | A work or case hand-off between responsibilities | Human investigation, evidence gathering and variable path | `HB-INT-067 Correspondent Investigation Exchange` |

The style does not necessarily determine the wire protocol. A command may be sent through an API or durable queue. A file can be transferred interactively or on a schedule. The catalogue type expresses the business interaction; the detailed contract records transport and runtime behaviour.

## A minimum governed contract

Every material interface needs enough information for designers, consumers, control owners and operators to reach the same interpretation.

### Business meaning

State the purpose, trigger, expected outcome, producer, consumer and authoritative state. Define whether the exchange is a request, acceptance, completion, rejection, correction or fact. Use governed information terms rather than local field names alone.

### Identity and authority

Record the calling service or external participant, authentication method, access-authorisation policy, customer or employee context where required, and delegated authority. A valid service credential does not prove that a customer may approve a corporate payment.

### Information protection

Classify the information, minimise the payload and define encryption, integrity, retention, logging and privacy rules. The catalogue uses `Internal`, `Confidential` and `Restricted`. The physical contract must define how that classification is enforced.

### Timing and completion

State response expectations, business cut-off, expiry, timeout and how later completion is observed. A Hypertext Transfer Protocol (HTTP) success response can mean `request accepted`, not `funds settled`. The contract should expose the difference.

### Delivery and duplicates

State retry responsibility, delivery expectation, idempotency key, duplicate window and what happens after uncertain outcome. A transport may deliver a message more than once. The business effect must still occur no more than intended.

### Correlation and traceability

Use stable business, request, message and causation identifiers. Preserve enough lineage to connect a customer instruction to processing, settlement, accounting, reconciliation and incident evidence without copying sensitive payloads into telemetry.

### Version and compatibility

Record contract version, schema version, effective date, compatibility policy, deprecation period and consumers. A new optional field, changed enumeration or altered business rule can affect consumers differently. Test meaning as well as syntax.

### Failure and operations

Define rejected input, unavailable dependency, timeout, partial completion, poison message, failed file, replay and manual repair. Name the monitoring signal, owner, escalation and reconciliation. A dead-letter queue without an owner is delayed data loss.

## Synchronous APIs

Use a synchronous API when the caller needs an immediate answer and the receiver can provide a bounded response within the business tolerance. Common cases include authentication, entitlement, price retrieval and account enquiry.

`HB-INT-015 Payment Entitlement Decision` lets `HB-APP-034 Payment Orchestration` ask `HB-APP-010 Customer Entitlement and Mandate Service` whether the current identity and mandate permit an action. The response is an entitlement result with rationale and rule reference. It is not payment settlement or business approval.

An API contract should define resources or operations, request and response schemas, validation errors, authorisation scopes, idempotency where an effect may be repeated, rate and capacity controls, timeout and later-status behaviour. The OpenAPI Specification (OAS) can describe HTTP APIs in a machine-readable, language-neutral form, but it does not assign business ownership, choose security policy or make the implementation resilient [OPENAPI-3.2-PV51].

Do not create a long synchronous chain across every domain step. Each dependency adds latency and another failure mode. If a caller only needs durable acceptance, a command followed by status or event may express the behaviour more accurately.

## BIAN Semantic APIs require adaptation

A BIAN Semantic API provides useful banking vocabulary and operation semantics associated with a Service Domain. It is a reference contract, not a production endpoint that every bank should expose unchanged [BIAN-14-MAPPING-PV49-52].

Before adopting one, verify the BIAN 14.0 Service Domain mapping, select only the relevant business behaviour, map BIAN information to governed Horizon Bank concepts, define local identifiers and authority, and add security, privacy, errors, idempotency, versioning and operational objectives. Record differences rather than claiming conformance from similar path names.

`HB-APP-075 API Management Platform` publishes, secures, throttles and observes APIs. It does not own the business semantics behind them. `HB-INT-093 Governed Rule Execution`, for example, exposes a rule result through managed access, while the rule owner and consuming credit application retain their responsibilities.

## Commands

A command asks a particular owner to do something. Use an imperative name such as `ExecutePayment` in a detailed contract. The receiver may accept, reject or defer the request. A command is not a fact merely because it is delivered asynchronously.

`HB-INT-036 Accepted Payment Command` directs `HB-APP-034 Payment Orchestration` to accept coordination responsibility for an instruction submitted by `HB-APP-033 Payment Initiation Service`. The contract should include payment reference, accepted version, requested action, idempotency key, legal entity, priority and expiry. A transport acknowledgement proves receipt by the messaging layer. A business acceptance proves that the receiver has taken responsibility. Clearing and settlement remain later outcomes.

Commands should have one logical owner. Multiple competing consumers can be used as runtime instances of that owner, but two different business responsibilities should not race to decide who owns the action.

## Events

An event records a fact. Use a past-tense business name such as `SettlementPositionChanged`. The producer owns the truth of the event and its relationship to authoritative state. Consumers decide what the fact means for their own responsibilities.

`HB-INT-066 Intraday Settlement Position Event` tells `HB-APP-056 Funding and Liquidity Management` that a governed settlement position changed. The event should state event identity, source, type, subject, occurrence time, effective business time, schema version and position reference. It also needs ordering scope, duplicate handling, correction rules, retention, replay and access controls.

CloudEvents 1.0.2 standardises common event context such as `id`, `source`, `specversion` and `type`. It does not define the business payload or prove that the producer published the fact atomically with its state change [EVENT-CONTRACTS-PV51].

Use an outbox or another controlled publication mechanism when the state change and publication must not drift apart. Consumers should be idempotent. If ordering matters, state the key and bounded scope, for example `within one settlement account`, rather than promising total order across the bank.

AsyncAPI can describe message-driven APIs, channels, operations and messages. It helps contract tooling, but ownership, retention, privacy, reconciliation and recovery still need governance [EVENT-CONTRACTS-PV51].

## General asynchronous messages

Some exchanges are neither a pure event nor a simple command. Payment-network protocols can contain instructions, acknowledgements, status, returns and investigation messages. The catalogue type `Message` preserves that broader interaction.

`HB-INT-105 Cross-Border Financial Message` exchanges payment, agent, remittance, status and investigation information between `HB-APP-035` and `HB-APP-038` through `HB-EXT-004`. A detailed model should classify each message role. It should not turn a network status into final settlement unless the governing rule and system of record support that interpretation.

`HB-APP-077 Enterprise Messaging Platform` provides durable delivery, retries and dead-letter handling. It is authoritative for transport evidence, not payment status.

## Batch and file exchange

Batch is appropriate where work is naturally periodic or grouped, or where source and consumer operate on different processing schedules. Files remain important for bulk exchange, external submission and coexistence with systems that do not offer record-level services.

`HB-INT-082 Subledger Journal Batch` posts balanced journals from `HB-APP-058 Product Subledger Platform` to `HB-APP-059 General Ledger`. The contract needs legal entity, accounting period, currency, source, journal balance, control totals, batch identity and correction semantics. Partial acceptance must be forbidden or explicitly designed.

`HB-INT-088 Regulatory Return Submission` sends an approved return through `HB-APP-078 Managed File Transfer Platform` to `HB-EXT-015 Prudential and Conduct Reporting Gateway`. The transfer requires file identity, version, checksum or integrity evidence, encryption, approval, transmission receipt, regulator acknowledgement and resubmission rules. Receipt by the transfer platform is not acceptance by a regulator.

For batch and files, define:

- business date, cut-off and timezone;
- manifest, record count and control totals;
- schema and filename conventions;
- encryption, signing and key ownership;
- duplicate and rerun behaviour;
- whole-file and record-level rejection;
- acknowledgement levels;
- late, missing and corrupt-file handling; and
- reconciliation and retention.

`HB-APP-079 Enterprise Batch Scheduler` coordinates dependency and execution state. It does not own ledger balances or regulatory content.

## Workflow hand-offs

Workflow represents an assignment, case transfer or evidence-bearing hand-off where human work and variable paths matter. It should identify case, task, role, due date, evidence, disposition and return path.

`HB-INT-067 Correspondent Investigation Exchange` connects `HB-APP-038 Correspondent Banking Management` with `HB-APP-037 Payment Investigations and Exceptions` and `HB-EXT-005`. A correspondent enquiry can wait for external information, require manual evidence and return through several states. A synchronous API alone would hide that lifecycle.

`HB-APP-071 Enterprise Workflow Platform` can coordinate tasks, but the payment applications retain payment authority. Workflow completion must be idempotent and auditable. Recovery must preserve timers, assignments and already-completed external actions.

## External networks

An external network is more than an arrow leaving the bank. It introduces a separate identity, contract, operating calendar, message profile, cut-off, finality rule, incident route and legal or commercial dependency.

Horizon Bank models logical network classes such as:

- `HB-EXT-001 High-Value Payment Network`;
- `HB-EXT-004 Cross-Border Financial Messaging Network`;
- `HB-EXT-006 Card Scheme Network`;
- `HB-EXT-009 Securities Depository and Custody Connectivity`;
- `HB-EXT-016 Trade Finance Messaging Network`; and
- `HB-EXT-017 Open Banking and Ecosystem Connectivity`.

These records do not claim that Horizon Bank is a member of a named scheme or uses a particular provider. A physical design must add participant identity, endpoint, certification, credentials, permitted message profiles, availability, contingency method, support contact and jurisdiction. External adapters should translate formats and protect credentials without taking ownership of the business state.

## Worked interaction trace: cross-border payment

`HB-SCN-02 Execute Cross-Border Payment` begins with an authorised customer instruction and ends in a governed settled, rejected, returned or investigation state.

1. A channel submits the instruction through `HB-INT-023 Retail Payment Initiation` or `HB-INT-025 Corporate Payment Initiation` to `HB-APP-033`.
2. `HB-APP-034` requests `HB-INT-015 Payment Entitlement Decision` from `HB-APP-010`. A denial ends the requested action; it is not a technical retry.
3. `HB-INT-026 Transaction Sanctions Screening` obtains a screening result from `HB-APP-018 Name and Sanctions Screening`. A referral creates controlled work rather than an automatic success.
4. If foreign exchange is needed, `HB-INT-038 Foreign Exchange Quote` requests a governed quote from `HB-APP-039`.
5. `HB-APP-033` issues `HB-INT-036 Accepted Payment Command` to `HB-APP-034`. Durable acceptance and business completion are distinct.
6. After the required controls permit release, `HB-APP-034` sends `HB-INT-037 Payment Clearing Instruction` to `HB-APP-035`.
7. `HB-APP-035` exchanges `HB-INT-105 Cross-Border Financial Message` with `HB-APP-038` through `HB-EXT-004`.
8. `HB-APP-038` sends `HB-INT-065 Correspondent Settlement Instruction` to `HB-APP-036` through `HB-EXT-005` where applicable.
9. Settlement-position facts such as `HB-INT-066` inform `HB-APP-056` without transferring settlement authority.
10. Timeout, return or enquiry enters `HB-APP-037` through a governed investigation path.
11. `HB-REC-012`, `HB-REC-014` and `HB-REC-015` compare instruction, processing, settlement, ledger and correspondent evidence.

The trace includes APIs, a command, messages, an event, external networks and workflow. Using one integration style for every step would make the model less accurate.

## Choosing the style

| Need | Prefer | Check before deciding |
|---|---|---|
| Immediate bounded decision or enquiry | API | Latency, dependency failure, authorisation and timeout |
| Directed durable action | Command | Single owner, acceptance, idempotency and expiry |
| Publish a completed fact | Event | Authority, atomic publication, ordering, replay and privacy |
| Bilateral protocol or mixed asynchronous flow | Message | Message roles, correlation, status semantics and repair |
| Scheduled grouped processing | Batch | Cut-off, dependency, totals, partial failure and restart |
| Bulk or external document exchange | File | Integrity, encryption, acknowledgement and retention |
| Human assignment or case transfer | Workflow | Evidence, due date, escalation, return path and recovery |

A combination is often correct. The design should minimise semantic ambiguity, not the number of technologies.

## Current-to-target considerations

`HB-APP-077`, `HB-APP-078` and `HB-APP-079` are current integration platforms. `HB-APP-075` and `HB-APP-076` are proposed target platforms. Introducing them does not require every interface to change style.

Migrate contracts by business value and risk. Preserve stable references, translate at controlled boundaries and operate old and new paths with explicit ownership. Avoid publishing events reconstructed from incomplete legacy tables unless their authority and occurrence semantics are proven. Chapter 53 covers transition and decommissioning.

## Common mistakes

- Choosing the platform before defining the interaction.
- Calling every message an event.
- Treating a transport acknowledgement as business completion.
- Retrying a non-idempotent action without a stable key.
- Promising global event ordering without evidence.
- Using an API gateway as the business owner.
- Sending full sensitive records when a governed reference is sufficient.
- Omitting file manifests, totals and acknowledgement levels.
- Treating workflow completion as product-state authority.
- Naming a provider or scheme without verified membership.
- Leaving dead-letter, late-file and replay work without an owner.
- Describing a BIAN API as implemented because paths look similar.

## Chapter summary

Interaction design begins with meaning, authority and completion. APIs support immediate bounded exchanges; commands request action; events publish facts; general messages support broader asynchronous protocols; batch and files handle grouped work; workflow coordinates variable human work; and external networks introduce independent operating boundaries. Horizon Bank combines these styles in one payment scenario and governs each with security, versioning, failure, reconciliation and ownership.

## Key takeaways

- Select style from the business exchange, not platform fashion.
- Separate receipt, acceptance, completion and settlement.
- Give commands one logical owner and events one authoritative producer.
- Design idempotency, correlation and correction explicitly.
- Treat batch and files as first-class governed interfaces.
- Keep workflow separate from product authority.
- Model external networks as trust and operating boundaries.
- Adapt BIAN semantics to the bank's governed implementation.

## Practical exercise

Design the interfaces for `HB-SCN-16 Close the Books and Submit a Regulatory Return` from product subledger through regulator acknowledgement.

### Suggested answer criteria

A strong answer uses `HB-INT-082` for balanced subledger journals, `HB-INT-083` for ledger reconciliation, `HB-INT-085` for a governed reconciliation command, `HB-INT-087` for the regulatory dataset and `HB-INT-088` for submission through `HB-EXT-015`. It distinguishes batch completion, file transfer receipt, reporting approval and regulator acknowledgement. It includes legal entity, business date, totals, lineage, corrections, resubmission, security, operational owner and `HB-REC-030` plus `HB-REC-033`.

## Review checklist

- [ ] Purpose, producer, consumer and authoritative state are explicit.
- [ ] The interaction type matches its business meaning.
- [ ] Receipt, acceptance and completion are distinct.
- [ ] Identity, access authorisation and classification are defined.
- [ ] Idempotency, correlation, timeout and duplicate behaviour are defined.
- [ ] Version, compatibility and deprecation are governed.
- [ ] Events have authoritative producers and correction rules.
- [ ] Batch and files have totals, integrity and acknowledgement levels.
- [ ] Workflow has assignment, evidence, escalation and return behaviour.
- [ ] External-network assumptions and memberships are explicit gaps.
- [ ] Failure, recovery and reconciliation have owners.
- [ ] BIAN semantics are verified and adapted rather than copied blindly.

## References and source notes

- [BIAN-14-MAPPING-PV49-52]
- [OPENAPI-3.2-PV51]
- [EVENT-CONTRACTS-PV51]

## Deferred work

No diagram source is created in this pass. Physical protocols, endpoints, contract repositories, consumer inventories, message schemas, external participant memberships, cryptographic profiles, service objectives and jurisdiction-specific network rules remain governed gaps. Interface records should later link to versioned contract artefacts and test evidence.
