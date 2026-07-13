---
title: "Enterprise Information and Data Architecture"
chapter: 35
part: "part-05-bian-case-study"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-13"
---

# 35. Enterprise Information and Data Architecture

## Chapter purpose

Establish Horizon Bank's bank-wide information concepts, authority decisions and data movement before the domain chapters add detail.

## Reader outcomes

By the end of this chapter, the reader should be able to distinguish conceptual, logical and physical models; identify major banking data domains; qualify a system-of-record decision; and trace data from an operational event to accounting, risk and reporting.

## Prerequisites and dependencies

- Chapter 34: Full Bank Application and Integration Landscape

## Required models and artefacts

- Data-domain catalogue, system-of-record matrix, lineage and reconciliation specifications

## Worked examples

- Horizon Bank deposit-interest and cross-border-payment data lineage

## Source requirements

- Use official risk-data, provenance, security and BIAN sources; qualify all authority decisions as Horizon Bank decisions.

## Planned chapter structure

The following sections establish bank-wide information authority and movement.

## Data is part of the bank's control system

Bank data represents customers, rights, obligations, transactions, balances, positions, decisions and evidence. A data error can become a customer, financial, risk or regulatory error. Data architecture therefore covers meaning, authority, quality, lineage, access and retention, not merely storage technology.

## Model levels

A **conceptual model** identifies important business concepts and relationships. A **logical model** adds attributes, identifiers, cardinality and rules without committing to one storage product. A **physical model** describes implementation structures such as tables, messages, indexes or document layouts.

BIAN information concepts can inform semantic comparison. They do not replace Horizon Bank's bank-owned models or mandate a physical schema. [BIAN-SERVICE-LANDSCAPE-14]

## Data domains

| Domain | Principal information |
|---|---|
| Party and customer | Persons, organisations, relationships, segments and due-diligence status |
| Product and pricing | Product definitions, features, rates, fees and eligibility references |
| Agreement and entitlement | Contracts, mandates, consent, access rights and authorised parties |
| Account and balance | Accounts, status, balances, holds and interest conditions |
| Transaction and payment | Instructions, transactions, clearing, settlement and status |
| Credit | Applications, decisions, facilities, loans, schedules and exposure |
| Collateral and limit | Assets, valuations, liens, limits and utilisation |
| Card and merchant | Cards, tokens, authorisations, disputes, merchants and terminals |
| Trade | Instruments, documents, obligations, guarantees and presentations |
| Investment and securities | Instruments, orders, trades, portfolios, positions and corporate actions |
| Treasury and market | Deals, curves, prices, funding, liquidity and risk positions |
| Finance | Accounting events, journals, subledgers, general ledger and reports |
| Risk and control | Assessments, limits, alerts, controls, evidence and issues |
| Case, document and communication | Cases, tasks, records, documents, messages and retention |
| Reference and organisation | Legal entities, branches, currencies, calendars, countries and roles |

Domain ownership does not mean one database. It establishes accountable meaning and decision rights.

## Data categories

Master data identifies relatively stable subjects such as parties and products. Reference data provides controlled codes and classifications. Transactional data records activity. Event data communicates completed facts. Analytical data is organised for analysis. Document data preserves content and evidence.

The categories overlap. A customer document can be evidence in an operational case and a retained record, while extracted attributes may become governed customer data.

## Systems of record and authoritative sources

`System of record` is too vague unless qualified. Horizon Bank records authority by entity or attribute scope, legal entity, lifecycle state and time.

| Information | Candidate authority | Qualification |
|---|---|---|
| Party identity and relationships | Party and Customer Platform | Target authority; migration and local exceptions to be catalogued |
| Product definition | Product Catalogue | Product terms and lifecycle, not account balances |
| Deposit account and balance | Core Deposit System | Retained operational authority during transition |
| Payment instruction and status | Payments Platform | Payment lifecycle; posting authority remains with account processor |
| Screening alert and case | Financial Crime Platform | Control case and evidence, not customer master |
| Accounting journal and ledger balance | Finance application family | Application names and subledger boundaries still to be catalogued |

A **source record** is where information originates for a particular event. A **golden record** is a governed consolidated view. A golden record can still preserve provenance and may not be authorised to overwrite every source attribute.

## Identifiers and cross-references

Legal entity, party, customer relationship, agreement, account and transaction identifiers answer different questions. Reusing one identifier for all concepts hides lifecycle differences. Cross-reference management links local identifiers without destroying provenance.

Identifiers need an issuer, scope, uniqueness rule, lifecycle, privacy classification and resolution method. Display values such as account numbers may require additional protection and are not always suitable internal keys.

## Ownership and stewardship

The data owner is accountable for meaning, permitted use, quality and control. A steward maintains definitions and quality practices. A system owner operates technology. A producer creates data and a consumer uses it. These roles can be held by different teams.

Every business term should have a definition, owner, synonyms, valid values, related terms and source. Near-duplicates such as `client`, `customer`, `party` and `account holder` must either be distinguished or reconciled.

## Quality, lineage and reconciliation

Quality rules address dimensions such as accuracy, completeness, validity, consistency, uniqueness and timeliness. A rule needs a population, threshold or class, measurement point, owner, action and evidence. Numerical thresholds require business approval.

Lineage connects source event, transformations, stores and reports. BCBS 239 links governance, architecture, aggregation and risk reporting, and expects risk reports to be reconciled and validated. Its original scope is not assumed for every Horizon Bank entity, but its principles provide a strong architecture reference. [BCBS-239]

Reconciliation compares two independently meaningful records or control totals. It identifies breaks; it does not by itself decide which side is correct. Repair needs ownership, ageing, materiality and evidence.

## Operational and analytical data

Operational stores support current processing and control. A warehouse, lakehouse or data mart supports historical analysis, aggregation and reporting. The Enterprise Data Platform does not become operational authority merely because it contains a copy.

A governed data product is justified when it has a defined consumer outcome, owner, contract, quality measures, lineage and service expectations. Renaming an unmanaged extract as a data product adds no control.

## Transaction-to-report lineage

```text
customer or market event
→ operational validation and processing
→ authoritative transaction state
→ accounting event and subledger
→ general ledger and reconciliation
→ governed extraction and transformation
→ management, risk or regulatory report
→ approval and retained evidence
```

Late adjustments, rejected records and manual journals must remain visible in the lineage.

## Protection, retention and use

Horizon Bank classifies information as `Public`, `Internal`, `Confidential` or `Highly Restricted`. Classification influences access, encryption, masking, monitoring and sharing. Privacy and confidentiality are related but not identical.

Retention depends on record purpose, legal hold, contract and applicable law. Data residency and cross-border transfer decisions are recorded by legal entity and dataset. Purpose limitation asks whether data is being used compatibly with the reason and authority under which it was collected.

## Artificial intelligence and model data

Models require governed training, validation and production data, reproducible lineage, access control, quality monitoring and accountable decisions. Generated or inferred attributes must not silently overwrite authoritative facts. Model outputs are decisions or evidence only where governance explicitly assigns that role.

## Common mistakes

- Naming a data platform as the system of record for everything.
- Defining authority at whole-system level without attribute scope.
- Confusing a golden record with the source of every fact.
- Drawing lineage without adjustments, controls and report approval.
- Treating reconciliation breaks as technology errors without business ownership.
- Copying a reference information model into a physical schema.

## Key takeaways

- Data domains govern meaning; applications provide implementations.
- Authority must be qualified by information scope and lifecycle.
- Identifiers require explicit ownership and cross-reference rules.
- Quality, lineage and reconciliation are connected control mechanisms.
- Operational authority remains distinct from analytical copies.

## Practical exercise

For a cross-border payment, list party, agreement, account, payment, accounting and case data. Assign a candidate authority to each and identify two reconciliations. Mark all assumptions.

## Review checklist

- [x] Major data domains and categories are defined.
- [x] Authority, golden record and source record are distinguished.
- [x] Lineage includes accounting, reconciliation and reporting.
- [x] Protection, retention, residency and analytical use are covered.
- [ ] The full system-of-record matrix and data-domain catalogue remain controlled deliverables.

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14]
- [BCBS-239]
- [W3C-PROV-DM-2013]

## Drafting notes

- Complete attribute-scope authority, ownership and critical-data-element examples before formal review.
