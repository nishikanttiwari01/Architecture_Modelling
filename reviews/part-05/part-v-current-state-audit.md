# Part V Current-State Audit

**Audit date:** 2026-07-13
**Baseline branch:** `main`, four commits ahead of `origin/main`
**Baseline commit:** `5dd7730a0f215f7ed0e989af81471a3d2262097c`
**Scope:** Chapters 31 to 56, Horizon Bank controlled artefacts, Part V diagrams, research notes and registers

## Executive finding

Part V is a coherent set of chapter outlines, but it is not yet the promised integrated architecture of a full-service bank. All 26 chapters are planning stubs. They identify useful topics and repeatedly state sound BIAN cautions, but they do not provide governed catalogues, full-bank traceability, domain depth, accounting mechanics, systems-of-record decisions, or an enterprise-wide control and resilience model.

The existing material should be treated as an idea bank for the redesign, not as a structure to preserve. No bulk prose drafting or diagram production should begin until the proposed chapter structure and controlled catalogues receive author review.

## Repository baseline and inventory

- Chapters inspected: all files from `31-introduction-to-bian.md` through `56-bian-quick-reference.md`.
- Chapter state: every file is an outline stub with purpose, outcomes, planned headings, completion checklist and drafting notes. `STATUS.md` previously listed all as `Planned`.
- Controlled Horizon Bank files: `README.md`, `actors.md`, `capabilities.md` and `system-landscape.md`.
- Part V figure register: only `FIG-31-01`, status `Planned`, with pending source and export.
- Part V specifications, sources and exports: none.
- BIAN research: `research/bian/README.md` only. No BIAN 14.0 source notes were found.
- Banking research: `research/banking/README.md` only. No substantive banking source notes were found.
- Baseline working tree: the supplied master instruction was untracked. No tracked user changes were overwritten.

## Existing material worth preserving

The following ideas are useful and should be migrated into the new structure:

| Existing material | Preserve in redesigned chapter(s) | Reason |
|---|---|---|
| Chapter 31 hierarchy, scenarios, Service Operations, Business Object Model and adoption cautions | 31 and 49 | Essential BIAN orientation and mapping method |
| Chapter 32 comparisons with ArchiMate, BPMN, C4, UML, data and security models | 31 and 49 | Useful explanation of complementary viewpoints |
| Chapters 33 to 36 operating model, process, value-stream and scenario concepts | 32, 33 and 49 | Sound enterprise-baseline concepts, but currently selective |
| Customer onboarding and account-opening material | 37 and 38 | Reusable scenarios within broader domain chapters |
| Cross-border payment material | 41 and 56 | Strong candidate for an integrated front-to-back scenario |
| Consumer loan origination | 39 and 56 | Useful lifecycle scenario, expanded to mortgage, SME and corporate lending |
| Card fraud investigation | 42, 47 and 56 | Connects cards, fraud, cases, controls and accounting |
| Corporate cash management | 43 and 56 | Useful corporate transaction-banking scenario |
| Application mapping and service-boundary cautions | 34, 49 and 50 | Necessary separation of BIAN reference concepts from implementation boundaries |
| API and event guidance | 51 | Reusable after adding batch, files, workflow and external networks |
| Data ownership, canonical/local models, lineage, privacy and retention | 35 | Correct foundations requiring full-domain authority decisions |
| Security, deployment, operations and migration headings | 36, 52 and 53 | Useful seeds, but insufficiently connected to critical operations |
| Governance, measures, mistakes, review checklist and quick reference | 54, 55 and 56 | Appropriate consolidation material |

## Repetition to consolidate

The same caution appears across Chapters 31, 32, 36, 43, 44, 45, 47, 49, 50, 52, 54 and 56 in slightly different forms: BIAN is a reference, a Service Domain is not automatically a microservice, and BIAN does not replace other architecture views. State this clearly in Chapter 31, turn it into a mapping rule in Chapter 49, apply it in Chapter 50, and retain only a short reminder in the practitioner reference.

Repeated generic structures such as benefits, common mistakes, review questions, completion checklists and tool comparisons should be retained only where they teach a domain-specific lesson. The redesign should avoid repeating cautions in place of modelling the bank.

## Stub assessment

All Chapters 31 to 56 are stubs rather than drafted chapters. They contain useful headings, but none meets the `Drafting`, `Under Review` or `Ready for Author Approval` exit criteria. The most developed outlines are Chapters 31, 33, 34, 37 to 42 and 47 to 50. Even these lack sourced prose, governed artefacts and required diagrams.

## Banking-domain gaps

Coverage is absent or shallow for product and pricing governance; mortgages; small and medium-sized enterprise and corporate credit; collateral, limits, exposure, collections and recovery; merchant acquiring; trade finance; wealth, investments, securities, custody and asset servicing; treasury, markets, funding, liquidity, asset and liability management and capital; finance, tax, regulatory and management reporting; enterprise operations; legal; audit; procurement; human resources; facilities; and third-party management.

The existing scenarios are isolated. They do not form complete domain architectures or show dependencies among customer, deposits, lending, payments, cards, trade, wealth, treasury, finance and risk.

## Application gaps

The controlled landscape contains only 11 broad systems. Missing families include branch and contact-centre platforms; customer relationship management and sales; pricing; deposit product processors beyond the core placeholder; loan origination, collateral, limits, collections and recovery; payment gateways, clearing adapters, sanctions screening, reconciliation and investigations; card issuing, authorisation, clearing, disputes and merchant acquiring; trade finance; wealth, order management, portfolio, custody and corporate actions; treasury trading, market data, liquidity and asset and liability management; general ledger, subledgers, tax and regulatory reporting; document, correspondence, workflow and case platforms; identity, privileged access, security operations, observability, configuration and service management; and enterprise support systems.

Application ownership, lifecycle, vendor status, interfaces, criticality and authoritative-data responsibilities are not governed.

## Data and systems-of-record gaps

No controlled data-domain catalogue or systems-of-record register exists. Missing authority decisions include party identity, customer relationship, product, pricing, agreement, account, balance, transaction, payment, loan, collateral, limit, card, merchant, trade instrument, security, portfolio, position, market data, accounting entry, general ledger balance, risk, control, case, document, consent, entitlement and regulatory-reporting data.

The current files do not define identifier ownership, attribute-level authority, reference data, golden-source qualification, lineage, quality rules, retention or operational-to-analytical movement.

## Accounting and reconciliation gaps

The outlines do not model product-to-subledger-to-general-ledger flows; debit and credit teaching examples; accruals, interest and fee posting; value date and booking date; suspense and repair; settlement accounting; nostro reconciliation; card clearing and settlement reconciliation; loan principal, interest, impairment and write-off; collateral and limit exposure; trade-finance contingent obligations; securities positions and cash reconciliation; treasury valuation and profit and loss; intercompany; tax; close; or regulatory-reporting controls.

## Control and critical-operation gaps

There is no control catalogue, control ownership model or evidence model. Missing areas include segregation of duties, maker-checker, customer due diligence, sanctions, transaction monitoring, fraud, credit approval, limit control, privileged access, privacy, financial controls, reconciliation, model risk, third-party risk, audit trail and retention.

No critical-operation catalogue or dependency map links customer outcomes to people, applications, data, facilities, technology and third parties. Impact tolerances, degraded modes, recovery classes, recovery time, recovery point, batch windows and cut-offs are not defined.

## BIAN items requiring 14.0 verification

Every intended Business Area, Business Domain, Service Domain, Service Operation, Business Scenario and Business Object Model reference must be re-verified. The current stubs mostly name BIAN object types rather than exact objects, so they cannot support conformance or mapping claims. Verification must record the official 14.0 source, exact spelling, version, mapping rationale, confidence and unresolved ambiguity. No existing name should be grandfathered into the mapping register.

## Links and figures affected

The chapter titles and purposes for 31 to 56 change substantially. `BOOK_PLAN.md`, the table of contents, chapter cross-references, `STATUS.md`, build ordering where title-sensitive, and future links into Part V will require synchronisation during Phase 2. Existing filenames can initially remain stable to avoid premature link breakage, but their titles and eventual rename policy need author approval.

`FIG-31-01` is the only existing Part V figure ID. Its concept remains relevant, but its title, purpose and chapter placement must be reconsidered against the redesigned Chapter 31. The new programme requires many additional figure IDs. No source may be created until its specification is author-approved.

## Restructuring risks

- Renaming all files at once would create avoidable broken links and noisy history.
- Drafting before catalogue agreement would produce inconsistent names and duplicated sources of truth.
- Treating the master instruction’s candidate BIAN mappings as verified would risk false BIAN 14.0 claims.
- Assigning numerical non-functional targets without evidence would create fictional precision.
- Producing enterprise diagrams before controlled catalogue and author-approved specification work would breach repository policy.
- Expanding breadth without explicit exclusions could create shallow catalogue dumps rather than teachable architecture.

## Decisions requiring author approval

1. Accept the proposed Chapter 31 to 56 structure and old-to-new migration map.
2. Decide whether chapter filenames are renamed in one controlled change or retained while titles change.
3. Accept the controlled artefact model and the proposed Horizon Bank architecture principles.
4. Approve each diagram specification before source creation, beginning with the enterprise baseline figures.
5. Decide the legal-entity and geographical scope assumptions used for regulatory examples.
6. Confirm whether illustrative classifications may be used where quantitative service levels are unavailable.

## Recommended migration sequence

1. Approve structure, scope assumptions and controlled artefact ownership.
2. Research and record BIAN 14.0 and primary banking sources.
3. Expand Horizon Bank business, capability, process, role, application, data, interface, accounting, control, critical-operation and technology catalogues.
4. Build and validate the master coverage matrix.
5. Synchronise `BOOK_PLAN.md`, chapter purposes/outcomes/outlines, links and statuses.
6. Register and seek approval for enterprise diagram specifications.
7. Draft Chapters 31 to 36.
8. Draft domain Chapters 37 to 48 in Groups A to D with cross-domain reviews.
9. Draft implementation and transformation Chapters 49 to 56.
10. Run the full-bank coverage and quality audit before seeking author approval.
