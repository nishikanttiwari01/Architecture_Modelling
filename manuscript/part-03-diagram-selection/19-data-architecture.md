---
title: "Modelling Data Architecture"
chapter: 19
part: "part-03-diagram-selection"
status: "Ready for Author Approval"
author: "Nishikant Tiwari"
last_updated: "2026-07-10"
---

# 19. Modelling Data Architecture

## Chapter purpose

Help beginner and practising architects choose views that explain data meaning,
structure, movement, ownership and governance without forcing every concern into one
diagram.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish conceptual, logical and physical data views;
- choose between an entity relationship diagram (ERD), data flow diagram (DFD), data
  lineage view, lifecycle view, ownership matrix and catalogue;
- explain how master data and reference data differ from ordinary transaction data;
- make ownership, stewardship, privacy, retention and data-quality implications visible;
- combine a small set of views for the Simple Online Store and Horizon Bank; and
- review a data architecture model for clarity, traceability and appropriate detail.

## Prerequisites and dependencies

- Chapter 8: Data Modelling
- Chapter 10: Domain and Event Modelling
- Chapter 18: Modelling Integration and Runtime Behaviour

## Required models and artefacts

This chapter uses one original selection-guide specification and one manuscript
selection table:

- FIG-19-01: Choosing the Right Data Architecture View.
- Data architecture view selection table.

`FIG-19-01` is specified and registered, but source and Scalable Vector Graphics (SVG)
export are deferred until the author approves the diagram specification, as required by
the repository diagram workflow.

## Worked examples

- Simple Online Store order data.
- Horizon Bank payment and party data.

## Source requirements

- `[CHEN-ER-1976]` supports the entity, relationship and attribute foundation.
- `[CODD-RELATIONAL-1970]` supports separation of logical structure from physical
  storage concerns.
- `[DEMARCO-STRUCTURED-ANALYSIS-1979]` supports the established use of DFDs to show
  data movement and transformation.
- `[W3C-PROV-DM-2013]` supports provenance concepts used in lineage guidance.
- `[DAMA-DMBOK2-2017]` provides practitioner context for data architecture, ownership,
  metadata, quality and lifecycle concerns.

Existing source notes are sufficient. This chapter applies the techniques introduced in
Chapter 8 and does not introduce a new normative notation or version-sensitive claim.

## Start with the data question

Chapter 18 asked how systems exchange information and behave together at runtime.
Chapter 19 changes the emphasis. Its central question is: **what data matters, what does
it mean, where does it move, who is responsible for it and what rules govern it?**

No single diagram answers all of that. An ERD can show that an Order contains Order
Lines, but not which system sends payment information to a provider. A DFD can show
movement between systems, but not the complete attributes and cardinalities of an
Order. A lineage view can trace a report value to its sources, but it is not a retention
schedule. An ownership matrix can name accountable roles, but it does not define a
database schema.

Start by writing the question and audience. Business stakeholders may need agreement on
Party, Customer and Account. Developers may need keys and constraints. Integration and
security reviewers may need movement, stores and sensitive fields. Data owners may need
lineage, quality controls and retention responsibilities. Choose the smallest view that
answers the immediate question, then connect it to companion views through controlled
names and identifiers.

## Conceptual information architecture

A conceptual information view answers: **which business information concepts matter,
and how are they related in broad terms?**

It uses familiar business names and a small number of relationships. It normally avoids
attributes, database tables, data types and integration mechanisms. This makes it useful
for business architects, domain experts, data architects and product owners who need to
agree meaning before implementation detail dominates the discussion.

For the Simple Online Store, the view might contain Customer, Product, Basket, Order,
Payment and Shipment. A Customer places an Order; an Order contains Products; a Payment
settles an Order; a Shipment fulfils an Order. The purpose is shared understanding, not
database design.

For Horizon Bank, a conceptual view might contain Party, Customer Relationship,
Agreement, Account and Payment Instruction. This prevents a common mistake: treating
Party and Customer as synonyms. A person or organisation can be known to the bank as a
party and play several roles, while a customer relationship has a more specific business
meaning. The conceptual view should make such distinctions discussable.

Entity–relationship modelling has long separated entities, relationships and attributes
from later physical implementation [CHEN-ER-1976]. At conceptual level, use only the
precision needed to settle business meaning. If a debate is about column types or
indexes, the conversation has moved to a different view.

## Logical and physical models

A logical data model answers: **what entities, attributes, identifiers, relationships,
cardinalities and optionalities are required, independently of a particular storage
product?**

An ERD is a common way to present this view. For the Online Store, it can show that one
Order contains one or more Order Lines, each Order Line refers to one Product, and an
Order may have zero or more Payments or Shipments. Optionality matters because an order
can exist before payment or fulfilment is complete.

A physical data model answers: **how will this data be implemented in a chosen storage
technology?** It may contain table or collection names, columns, data types, primary and
foreign keys, indexes, constraints, partitions and storage-specific choices. It is aimed
at developers, database specialists, security reviewers and operations teams making or
reviewing implementation decisions.

The relational model's separation of logical representation from physical storage is a
useful foundation for this distinction [CODD-RELATIONAL-1970]. The practical lesson is
not that every solution must use a relational database. It is that a business concept is
not automatically a table, and a table does not by itself explain business meaning.

For Horizon Bank, a logical model may define Payment Instruction, debtor and creditor
roles, amount, currency, requested execution date and payment status. A physical model
for the Payments Platform may then show its chosen persistence structures. The
Enterprise Data Platform may use a different physical model for analytics. Those
implementations can differ while remaining mapped to the same controlled concepts.

Do not combine conceptual, logical and physical detail merely to claim one complete
model. Label the level. State the intended audience. Maintain traceability between
levels where it supports a real decision.

## Data flows and stores

A DFD answers: **where does data enter, move, change and rest within a stated scope?**

Its common elements are external entities, processes, data stores and labelled,
directional flows. DFDs are an established structured-analysis technique for separating
data movement and transformation from program structure [DEMARCO-STRUCTURED-ANALYSIS-1979].
They remain useful architecture views even when teams use informal visual styling.

For the Online Store, a DFD can show Customer order details entering the Online Store,
payment authorisation data moving to and from the Payment Provider System, order data
being written to the Order data store, and shipment information moving to and from the
Delivery Partner System. Each arrow should name the information, not merely say `data`.

For Horizon Bank, a payment DFD can show the Payment Instruction passing from Horizon
Digital Channels to the Payments Platform, screening information exchanged with the
Financial Crime Platform, posting information exchanged with the Core Deposit System,
payment status published through the Event Platform and governed reporting data supplied
to the Enterprise Data Platform.

A DFD is not a runtime sequence diagram. It need not promise precise timing or message
order. It is also not an ERD: a data store symbol does not define every entity, field or
constraint. If runtime order, retry or timeout is the decision, use Chapter 18 guidance.
If structure is the decision, use an ERD.

## Data lineage

A lineage view answers: **where did a data item come from, what transformed it, who or
what was involved, and where is it used?**

Lineage is especially valuable for reports, risk measures, customer communications,
reconciliation and regulatory outputs. A line from `source` to `report` is rarely
enough. Useful lineage identifies source data, transformations, validation or quality
controls, intermediate products, responsible systems and downstream uses.

The World Wide Web Consortium (W3C) PROV Data Model describes provenance using entities,
activities and agents involved in producing or influencing things [W3C-PROV-DM-2013].
This chapter does not require formal PROV notation. It applies the underlying discipline:
record origin, transformation, responsibility and use.

At Horizon Bank, a reported payment status may derive from the original Payment
Instruction, a screening result, a posting result and a consolidated status event. A
lineage view helps a reviewer ask which source is authoritative at each stage, which
rule transformed a status, and which reports consume it. This is different from a DFD,
which maps movement, and from a logical model, which defines structure.

Lineage should also indicate granularity. System-level lineage can support an early
architecture decision. Field-level lineage may be necessary for a critical measure or
regulatory report. Do not promise field-level completeness with a diagram that only
shows systems.

## Ownership and stewardship

An ownership view answers: **who is accountable for the meaning and acceptable use of
data, and who performs its day-to-day stewardship?**

The repository uses ownership in its ordinary governance sense. A data owner is the
accountable business role for decisions about a defined data area. A data steward is a
role that helps maintain definitions, quality rules, issue handling and appropriate use.
Exact titles and authorities vary by organisation, so the model should state the local
governance arrangement rather than imply a universal standard.

A compact matrix often works better than a network diagram. Rows can represent data
concepts or products, while columns record business owner, steward, authoritative
system, producer, main consumers, quality rules and escalation route. The matrix should
distinguish ownership of meaning from application ownership and technical custody.

For the Online Store, a product manager may own Product definitions while an operations
role stewards catalogue quality. The Online Store remains the authoritative system for
placed Order data, while the Payment Provider System is authoritative for its payment
authorisation result.

For Horizon Bank, the Party and Customer Platform supports a trusted party and customer
view, but naming the platform does not settle business accountability. The view should
identify who can approve a definition change, who investigates duplicate party records,
which systems may update specific facts and how quality issues are escalated.

## Master data, reference data and transaction data

These categories answer: **which data should be shared and governed for reuse, which
values provide controlled classifications, and which records capture business events or
activities?**

Master data describes relatively stable, shared business subjects such as Party or
Product. Reference data provides controlled values used to classify or constrain other
data, such as currency codes or payment-status codes. Transaction data records business
activity, such as an Order, Payment or Payment Instruction.

The boundaries depend on scope. Product can be master data for the Online Store, while a
product price change may be recorded as a separate event or effective-dated record.
Currency can be reference data, while a payment amount and currency together form part
of a transaction. A model should explain the chosen classification and governance
implication instead of treating the labels as self-evident.

For Horizon Bank, Party and Product are candidates for governed master data. Currency,
country and payment-status value sets are candidates for reference data. Payment
Instructions and postings are transaction data. This classification helps select
authoritative sources, distribution mechanisms and change controls. It does not mean
all master data must be stored in one database or that every consuming system must use
one physical schema.

Use a catalogue or ownership matrix to record classification, definition, owner,
authoritative source, quality expectations and consumers. Use a conceptual or logical
model to show how the concepts relate.

## Privacy, retention and data quality

A governance view answers: **what handling obligations and quality expectations apply
to data throughout its lifecycle?**

Begin with the data lifecycle: create or receive, validate, use, update, share, retain,
archive and dispose. Then add the concerns that affect architecture decisions. These may
include sensitivity classification, permitted use, access responsibility, retention
rule, disposal trigger, quality rule and evidence of control. Applicable legal and
regulatory requirements must be verified for the organisation and jurisdiction. A
generic architecture diagram is not a substitute for legal advice or an approved
records schedule.

For the Online Store, customer contact details and order history may have different
purposes, access needs and retention rules. Payment data should not be labelled simply
`sensitive`; the view should say which data is stored by the Online Store, which remains
with the Payment Provider System, and which role owns the handling decision.

For Horizon Bank, Party, Account and Payment Instruction data can support service,
screening, reconciliation, reporting and audit. A lifecycle view should identify when
data becomes authoritative, where copies are created, which controls apply, how quality
issues are resolved and what approved retention or disposal rule governs each copy.

Quality statements should be testable. `High quality` is vague. `Payment status is
present for every posted payment`, `currency uses the controlled value set`, and
`reporting status is reconciled to the authoritative posting result` are reviewable
rules. Record the owner, measurement point and response when a rule fails.

## Choosing the right view

Use this table as a first filter. Several views may be needed, but each should keep one
primary question.

| Architecture question | Start with | Useful elements | Main audience | Common companion |
|---|---|---|---|---|
| Which information concepts matter? | Conceptual information view | Concepts and broad relationships | Business and domain stakeholders | Glossary or catalogue |
| What structure and business rules are required? | Logical ERD | Entities, attributes, keys, cardinality and optionality | Data architects, analysts and developers | Conceptual view |
| How will data be stored? | Physical data model | Tables or collections, types, constraints and indexes | Developers and database specialists | Logical ERD |
| Where does data move and change? | DFD | Sources, processes, stores and labelled flows | Solution, integration and security reviewers | Integration view |
| How was a value produced? | Lineage view | Origin, transformation, control, responsibility and use | Data, risk, audit and reporting teams | Data catalogue |
| Who is accountable? | Ownership matrix | Owner, steward, authoritative source and escalation | Business and data governance | Catalogue |
| What happens to data over time? | Lifecycle view | Create, use, share, retain, archive and dispose | Data, security, privacy and records roles | Ownership matrix |
| Which shared values and subjects are governed? | Master/reference data catalogue | Definition, classification, source, version and consumers | Data governance and application teams | Logical model |

The planned `FIG-19-01` will provide a compact visual route through these choices after
its specification is author-approved. The table remains the fuller selection aid and
makes the chapter complete while production of the figure is deferred.

## Worked example

Horizon Bank wants to improve confidence in payment-status reporting. The architecture
question is: **how should the bank model payment-status meaning, movement, derivation and
accountability so that reporting and operational teams can trust the result?**

The audience includes payment operations, data owners and stewards, solution and data
architects, reporting teams, risk reviewers and the application teams responsible for
the participating systems. The scope begins when Horizon Digital Channels captures a
Payment Instruction and ends when the Enterprise Data Platform publishes the governed
payment reporting data product. It includes the Payments Platform, Financial Crime
Platform, Core Deposit System and Event Platform. It does not cover every payment type,
customer journey or downstream report.

The primary view is a lineage view. It traces the reported payment status back through
the consolidated status event, posting result, screening result and original Payment
Instruction. This view contributes the origin, important transformations, quality
controls, responsible systems and downstream use needed to test whether a reported
status is explainable.

The lineage view needs complementary views:

1. A conceptual information view defines Party, Account and Payment Instruction in
   business language so that participants agree what the traced data means.
2. A logical ERD defines selected payment attributes, debtor and creditor roles,
   identifiers, cardinalities and optionalities without choosing a database product.
3. A DFD shows payment-status movement and material stores across Horizon Digital
   Channels, Payments Platform, Financial Crime Platform, Core Deposit System, Event
   Platform and Enterprise Data Platform.
4. An ownership and lifecycle matrix records the status definition owner, steward,
   authoritative source at each stage, quality rule, escalation route and approved
   retention reference.

Together, these views answer related questions without mixing notation. Cross-reference
them through stable concept names, status definitions, data-product identifiers and
interface or event identifiers.

Deliberately omit physical table and index design, detailed application programming
interface payloads, Business Process Model and Notation (BPMN) gateways, message retry
timing, network zones and jurisdiction-specific retention periods. Those details belong
in physical data, integration, process, deployment or approved policy artefacts when a
separate decision requires them.

Review the set by asking:

- Can each reported status be traced to its source facts and transformations?
- Is the authoritative source clear at each lifecycle stage?
- Do the conceptual and logical views use the same controlled meanings as the lineage
  and DFD?
- Are the owner, steward, quality rule and escalation route explicit?
- Are material copies and intermediate stores included without adding unrelated
  infrastructure detail?
- Can each view be understood by its intended audience without relying on another view
  to explain its notation?

## Common mistakes

### Starting with tables

A technically tidy schema can encode the wrong business meaning. Agree the important
concepts before optimising storage.

### Leaving the model level unstated

Readers cannot tell whether an entity is a business concept, logical structure or
physical table. Label the level, audience and scope.

### Confusing structure, movement and sequence

Use an ERD for structure, a DFD for movement and a sequence or dynamic view for ordered
runtime interaction. Link them instead of blending their notation.

### Drawing lineage as one unexplained arrow

Show origin, meaningful transformations, controls, responsible systems and downstream
use. State whether the lineage is system-level or field-level.

### Treating application ownership as data ownership

The team operating a platform is not automatically accountable for business meaning.
Name owner, steward, authoritative source and technical custodian separately where the
distinction matters.

### Declaring one universal canonical model

Shared meaning can reduce confusion, but local models still serve local responsibilities
and constraints. Govern mappings and boundaries rather than forcing one physical model
on every system.

### Using vague governance labels

Labels such as `sensitive`, `retain` or `high quality` are not enough. State the rule,
owner, trigger, measurement and action, with jurisdiction-specific obligations verified
by the appropriate specialists.

### Ignoring copies and intermediate stores

Data may be cached, queued, replicated, exported or curated. These copies can change
privacy, retention, lineage and quality responsibilities. Include the copies material to
the decision.

## Chapter cheat sheet

| View | Question answered | Keep out |
|---|---|---|
| Conceptual information view | What business information matters? | Tables, types and indexes |
| Logical ERD | What precise structure and relationships are required? | Product-specific storage tuning |
| Physical data model | How is data implemented? | Unresolved business definitions |
| DFD | Where does data move, transform and rest? | Detailed message timing and table schemas |
| Lineage view | How was data produced and where is it used? | Unrelated process steps |
| Ownership matrix | Who decides, stewards and escalates? | Detailed data structures |
| Lifecycle view | What happens from creation to disposal? | Every business-process activity |
| Data catalogue | What is the controlled definition, classification and source? | Uncontrolled free-text synonyms |

## Key takeaways

- Start with the data question, audience, boundary and required decision.
- Conceptual, logical and physical views provide different levels of detail.
- ERDs show structure; DFDs show movement; lineage shows origin, transformation and use.
- Ownership of business meaning is not the same as application ownership or custody.
- Master, reference and transaction data need explicit definitions and governance.
- Privacy, retention and data quality become useful when rules, owners and lifecycle
  points are specific.
- Linked, focused views are clearer than a single mixed-concern diagram.

## Practical exercise

Horizon Bank wants to improve confidence in payment-status reporting. Horizon Digital
Channels captures a Payment Instruction. The Payments Platform validates and
orchestrates it. The Financial Crime Platform returns a screening result. The Core
Deposit System returns a posting result. The Event Platform distributes status events,
and the Enterprise Data Platform creates a reporting data product.

Choose a view for each question:

1. Which business concepts must stakeholders agree?
2. Which attributes, roles and cardinalities define a Payment Instruction?
3. Where does payment-status data move and where is it stored?
4. How did one reported status derive from instruction, screening and posting data?
5. Who owns the status definition, stewards quality and resolves discrepancies?
6. Which lifecycle, privacy and retention facts should be recorded without inventing a
   legal rule?

Suggested answer:

- Use a conceptual information view for Party, Account and Payment Instruction meaning.
- Use a logical ERD for attributes, identifiers, roles, cardinality and optionality.
- Use a DFD for movement and stores across the named Horizon Bank systems.
- Use a lineage view for origin, transformations, controls and reporting use.
- Use an ownership matrix for owner, steward, authoritative source, quality rule and
  escalation path.
- Use a lifecycle and governance view to record creation, use, sharing, approved
  retention reference and disposal trigger. Mark any unverified legal requirement as an
  open question for the appropriate legal, privacy or records specialist.

Review the result by asking whether every view has one primary question, uses controlled
system names, states its level and scope, and links to companion views without mixing
their notation.

## Review checklist

- [ ] The question answered by each view is explicit.
- [ ] The audience, boundary and abstraction level are clear.
- [ ] Conceptual, logical and physical models are not confused.
- [ ] ERDs, DFDs, lineage, lifecycle and ownership views remain distinct.
- [ ] Important flows, stores, transformations and copies are labelled.
- [ ] Owner, steward, authoritative source and technical custody are distinguished where
      relevant.
- [ ] Master, reference and transaction data classifications are explained in context.
- [ ] Privacy, retention and quality rules are specific and appropriately qualified.
- [ ] The Simple Online Store and Horizon Bank examples use controlled repository names.
- [ ] Common mistakes are concrete and actionable.
- [ ] Required sources and diagrams are registered or explicitly deferred.
- [ ] Terminology, link, diagram-register and word-count checks pass.

## References and further reading

Chapter source notes are maintained under `research/data/` and registered in
`SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md),
is the intended publication location for the final source-key index once completed.

- `[CHEN-ER-1976]`: Peter Pin-Shan Chen, entity–relationship modelling source.
- `[CODD-RELATIONAL-1970]`: E. F. Codd, relational model source.
- `[DEMARCO-STRUCTURED-ANALYSIS-1979]`: structured analysis and DFD source.
- `[W3C-PROV-DM-2013]`: W3C PROV Data Model Recommendation.
- `[DAMA-DMBOK2-2017]`: data-management practitioner reference.
