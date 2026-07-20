---
title: "Wealth, Investments, Securities, Custody and Asset Servicing"
chapter: 44
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 44. Wealth, Investments, Securities, Custody and Asset Servicing

## Chapter purpose

An investment journey does not end when an order is executed. The bank must preserve the client mandate, suitability evidence, order and allocation, settlement obligation, custody holding, income and corporate-action outcome. This chapter separates those responsibilities so that a portfolio view cannot be mistaken for the authoritative securities position.

The central architecture question is: **which responsibility owns each client, order, position and entitlement state from advice through safekeeping and asset servicing?** Horizon Bank is fictional. Jurisdictional advice duties, client-asset rules, market memberships and custody chains remain explicit assumptions.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish advice, portfolio management, order management, securities processing, custody and asset servicing;
- model client mandate and suitability evidence separately from execution;
- trace orders, allocations, settlement, holdings and corporate actions across applications and external parties;
- identify authoritative records, accounting events, reconciliations and controls;
- explain why client-asset protection and operational resilience require more than a portfolio screen; and
- treat BIAN mappings as verified candidates rather than assumed software boundaries.

## Prerequisites and dependencies

- Chapter 37, for party, relationship and customer due diligence.
- Chapter 41, for cash settlement, foreign exchange and external networks.
- Chapter 43, for complex mandates and external document flows.
- Chapter 45, for treasury market data and liquidity dependencies.

## Required models and artefacts

- Governed wealth, investment, securities, custody and asset-servicing records.
- Client-mandate, order-state, position-authority and entitlement views.
- Logical applications, typed interfaces and market-network boundaries.
- Accounting-event, reconciliation, control, critical-operation and resilience records.

The governed operating trace assigns wealth, investment and custody propositions to `HB-ORG-10 Wealth, Investments and Securities`. `HB-ORG-114 Securities Director Role` is accountable for custody, settlement and asset-servicing outcomes. `HB-ORG-30 Trade, Treasury and Securities Operations` performs post-trade and asset-servicing work, while `HB-ORG-14 Compliance, Financial Crime and Conduct` provides independent conduct oversight. `HB-ORG-12 Finance, Accounting, Tax and Reporting` owns the resulting financial records.

No new diagram source is required in this drafting pass. A later visual must follow the specification-first approval workflow.

## Worked examples

- Horizon Bank advice and investment-order lifecycle through settlement.
- Horizon Bank custody holding and corporate-action lifecycle.

## Source requirements

Suitability and client-asset claims use official International Organisation of Securities Commissions (IOSCO) material. Payment and securities settlement terminology uses Committee on Payments and Market Infrastructures (CPMI) material. Banking Industry Architecture Network (BIAN) statements use the governed BIAN 14.0 note. Jurisdiction, market, custody-chain and tax duties remain unverified Horizon Bank assumptions.

## Two related domains, not one application

The Horizon catalogue separates wealth and investment management from securities and custody operations:

| Domain | Purpose |
|---|---|
| `HB-DOM-080 Wealth and Investments` | Advice, portfolio, orders and client reporting |
| `HB-DOM-090 Securities, Custody and Asset Servicing` | Settlement, custody accounts, positions and asset events |

Both support `HB-PRD-10 Investment, Advisory and Custody` and `HB-VS-06 Safeguard and Service Assets`, but their ownership and evidence differ. `HB-DOM-080` focuses on the client's mandate and investment outcome. `HB-DOM-090` focuses on settling, safeguarding and servicing the assets.

This separation does not require two legal entities or vendors. It provides clear accountability when an investment order is executed but not settled, a portfolio view differs from a custody holding, or a corporate-action entitlement is disputed.

## Advice, suitability and portfolio responsibility

`HB-CAP-081 Advice and Suitability Management` captures goals, constraints, product characteristics and a governed recommendation or warning. `HB-PROC-132 Provide Advice and Determine Suitability` creates the behavioural record. Suitability and appropriateness depend on the service, product, client classification and jurisdiction. `Private and Institutional` is Horizon's segment scope, not a legal classification.

Client segmentation determines the Horizon service model, not a universal legal category. An investment profile should record objectives, time horizon, liquidity needs, knowledge and experience, financial circumstances, risk appetite, capacity for loss and relevant restrictions under the applicable regime. The source, effective date and reviewer matter because a profile can become stale.

Suitability asks whether an advice or portfolio decision is appropriate for the client and service under applicable rules. Appropriateness can be a different assessment for a non-advised service. The architecture must not use one Boolean flag for both or infer either from wealth segment alone.

IOSCO, the international association of securities regulators, provides guidance on complex financial products that illustrates why customer classification, product complexity, assessment and management oversight need retained evidence [IOSCO-CLIENT-ASSETS-SUITABILITY]. A real bank must use the applicable jurisdictional rule, not apply the report as a universal decision table.

`HB-APP-049 Portfolio and Advisory Management` owns the client mandate, suitability evidence, recommendation and governed portfolio view through `HB-SOR-14 Wealth Mandate and Portfolio Authority`. It consumes market data through `HB-INT-074 Portfolio Market Data Feed`. A price feed supports valuation and advice but does not become the authority for a client's custody position.

`HB-CAP-082 Portfolio Management` establishes mandate constraints, allocation and rebalancing. `HB-CAP-084 Investment Product Administration` maintains holdings, valuations, fees and product information. `HB-PROC-133 Establish and Manage Investment Portfolios` joins them. The portfolio is a governed investment-management view, not necessarily the legal record of safekept assets.

A model portfolio is a governed target allocation or strategy, not the client's actual holding. Applying it requires a current mandate, restrictions, suitability, available cash, tax and transaction-cost considerations and an approved deviation process. Discretionary management permits authorised decisions within a mandate. An advisory service requires the client decision defined by the applicable arrangement. These operating models need different evidence.

Investment product governance identifies the intended client population, product characteristics, risks, costs, distribution conditions, restrictions and review triggers. A product that is approved for the bank is not automatically suitable for this client. Restricted instruments need an effective-dated rule and reason, such as client, jurisdiction, mandate, concentration or conduct constraint.

## Order capture, execution and allocation

An approved recommendation or discretionary decision becomes `HB-INT-049 Approved Investment Order`, a command from `HB-APP-049` to `HB-APP-050 Investment Order Management`. The order application validates, routes, tracks, cancels and allocates orders. `HB-SOR-15 Investment Order Authority` assigns it authority for the accepted internal order lifecycle.

`HB-CAP-083 Investment Order Management` and `HB-PROC-134 Execute Investment Orders and Report to Clients` cover capture through execution and reporting. The external exchange `HB-INT-075 Investment Venue Order Exchange` crosses `HB-EXT-008 Securities Trading Venue Connectivity`. The record does not assert a venue, broker relationship or membership.

An order, execution and allocation are separate states. One order may receive several fills; one execution may be allocated across portfolios; a cancellation can race with an external fill. The model must retain identifiers, quantities, timestamps, venue evidence, allocation status and corrections rather than overwrite everything with `Executed`.

`HB-REC-023 Investment Order, Execution and Contract` compares orders and allocations with external executions, confirmations and client-contract records. `HB-CTRL-22 Wealth Suitability and Order Approval` requires current mandate, customer classification, suitability evidence and approval before a governed order is released.

Pre-trade controls test mandate, restriction, available cash or position, concentration, authority and required approval before release. Market or product surveillance can later test conduct patterns, allocation fairness, best-execution evidence or prohibited activity. An alert is not a confirmed conduct breach. It needs an owner, evidence and disposition. Horizon Bank has no separate wealth-surveillance application or interface, so that responsibility remains a governed gap rather than an implied feature of order management.

## Securities processing and settlement

`HB-APP-051 Securities Processing` receives executed allocations through `HB-INT-050 Executed Investment Allocation`. It books the securities trade and manages confirmation, settlement and position updates. `HB-CAP-092 Securities Settlement` and `HB-PROC-136 Settle Securities Transactions` cover validation, matching, instruction, settlement and failed-item repair.

`HB-INT-076 Securities Settlement Exchange` crosses `HB-EXT-009 Securities Depository and Custody Connectivity`. The logical boundary can represent a depository, market infrastructure, agent or sub-custodian relationship. It does not assert that Horizon Bank connects directly.

**Delivery versus payment (DvP)** is a settlement arrangement that links delivery of securities to payment. It reduces principal risk where applicable, but the exact model, settlement asset and finality depend on the infrastructure [CPMI-PAYMENT-GLOSSARY-2016]. Horizon's catalogue therefore records settlement states and evidence without claiming universal DvP.

`HB-ACC-22 Investment Trade Settled` records the client cash, security position, fee and settlement consequence after governed settlement. Principal-versus-agent treatment, currency, fees and failed settlement remain accounting-policy gaps.

## Custody and safekeeping

Custody begins with an agreement and account structure, not with the first trade. `HB-CAP-091 Custody Account Management` and `HB-PROC-135 Establish and Service Custody Accounts` establish accounts, locations and restrictions. `HB-CAP-093 Safekeeping and Position Management` maintains positions, asset locations and movements.

`HB-APP-052 Custody and Safekeeping` is authoritative for accepted internal custody accounts and positions through `HB-SOR-16 Custody Holding Authority`. That authority is qualified. External depository and sub-custodian evidence must be reconciled before internal acceptance. Omnibus structures also require controlled allocation to underlying clients.

IOSCO's client-assets recommendations support explicit records, status, responsibilities and reconciliation where assets are placed with third parties [IOSCO-CLIENT-ASSETS-SUITABILITY]. Applicability and implementation vary by jurisdiction. The chapter therefore does not claim a universal segregation structure.

`HB-REC-024 Portfolio Position and Custody Holding` compares the investment-management view with custody or external holdings. `HB-REC-025 Securities Cash and Position Settlement` compares trades with position and cash movements. The first catches portfolio-to-custody differences; the second catches settlement breaks. Combining them would obscure the cause and owner.

Broker or venue execution evidence, internal order and allocation records, settlement instructions, cash movements and custody positions form different populations. `HB-REC-023` checks order, execution and contract, while `HB-REC-025` checks securities and cash settlement. A broker confirmation cannot replace the later depository or custodian evidence.

Tax-lot or cost-basis records associate acquisitions, disposals and adjustments for a stated reporting purpose. Their method and authority depend on jurisdiction and product. They are not interchangeable with market value, accounting carrying value or custody quantity. The current catalogue has no dedicated tax-lot authority, so any physical design must record this gap and retain lineage to trades and corporate actions.

## Corporate actions and asset servicing

Securities continue to generate events after settlement. An issuer may announce income, redemption, reorganisation or another corporate action. Eligible holders may need information, a choice and a deadline. `HB-CAP-094 Corporate Action Management` covers notice, eligibility, election and outcome. `HB-CAP-095 Securities Income and Tax Processing` covers income allocation and associated tax information.

`HB-PROC-137 Process Corporate Actions, Income and Tax` begins with an issuer or market event and ends with processed entitlements and client reporting. `HB-APP-053 Corporate Actions and Asset Servicing` owns elections, entitlement calculations and servicing-event state through `HB-SOR-17 Corporate Action and Entitlement Authority`.

`HB-INT-077 Corporate Action Exchange` carries announcements, elections and confirmations across the custody network. The bank must govern notice-source precedence, position snapshot, election cut-off, default action, tax inputs, proceeds and fractional entitlements. These detailed rules remain pending.

`HB-ACC-23 Securities Income Entitlement Recognised` represents dividends, coupons, redemptions or other cash entitlements. `HB-REC-026 Corporate Action and Entitlement` compares announcements and eligible positions with elections, receipts and client allocations. `HB-CTRL-24 Corporate Action Entitlement and Election Control` preserves provenance, calculation and exception evidence.

## Information authority and lineage

`HB-DATA-10 Wealth, Advice and Portfolio` includes mandate, suitability, recommendation, portfolio, order, allocation, performance and reporting information. `HB-DATA-11 Securities, Custody and Asset Servicing` includes security, trade, settlement, custody account, holding, corporate action, election and entitlement.

Authority follows purpose:

- `HB-APP-049` owns mandate and advice evidence.
- `HB-APP-050` owns accepted order and allocation state.
- `HB-APP-051` owns internal trade and settlement state.
- `HB-APP-052` owns reconciled internal custody position.
- `HB-APP-053` owns processed corporate-action and entitlement state.

No single `golden portfolio` can replace all five. Client reporting may assemble them, but the report remains a derived view with lineage to authoritative records and effective times.

Client fees can arise from advice, management, execution, custody, transactions or assets under management. The basis, period, currency, waiver and tax treatment must be effective-dated and reconciled. Performance reporting must state valuation sources, cash-flow treatment, period, benchmark and fee basis. A client statement brings together derived portfolio, cash and custody information with lineage. It does not become the authority for the underlying positions. Horizon Bank has no separately governed wealth-statement interface, which remains a catalogue gap.

Reference and market data is another dependency. `HB-DATA-15 Reference and Market Data` and `HB-EXT-010 Market and Reference Data Connectivity` provide instruments, prices and calendars. Source hierarchy, licences and redistribution rules remain pending. A stale or unlicensed price can affect advice, valuation and reporting even when order processing is healthy.

## Controls and operational resilience

Three controls protect the principal lifecycle:

- `HB-CTRL-22` protects advice and order approval.
- `HB-CTRL-23 Custody Position and Asset-Segregation Control` protects holdings, restrictions, allocations and breaks.
- `HB-CTRL-24` protects notices, elections, entitlements, tax and client allocation.

`HB-CRIT-12 Safeguard Client Assets and Positions` states that client assets must remain identifiable, controlled and traceable through disruption. `HB-CRIT-13 Settle Securities and Service Entitlements` focuses on settlement and deadline-sensitive asset events. These outcomes require different recovery priorities.

`HB-TECH-015 Wealth and Portfolio Management Classification` may permit resumable advisory work under controlled restriction. `HB-TECH-016 Securities, Custody and Asset Servicing Classification` protects time-sensitive settlement, positions and elections. Neither record invents a Recovery Time Objective (RTO), Recovery Point Objective (RPO) or impact tolerance. Market deadlines, downstream cash and third-party recovery must be known first.

A degraded process might stop new orders while still accepting time-critical corporate-action elections. It must preserve the decision, cut-off basis, queued work, customer communication and subsequent reconciliation.

## BIAN alignment and software boundaries

The BIAN mapping register currently has no governed wealth, investment, custody or asset-servicing candidate. This is a shared foundation gap. The chapter does not infer exact BIAN 14.0 Service Domain names.

When candidates are added, mappings will be many-to-many. Advice, portfolio, orders, settlement, custody and corporate actions have distinct functional patterns, but this does not mean each candidate must become one application, microservice, database or team. Physical boundaries require separate reasoning about transaction consistency, ownership, data, security, scale, latency, recovery and retained platforms.

## Choosing the right models

| Model | Wealth or securities question |
|---|---|
| Client journey | What does the client experience from need to reporting? |
| Capability map | Which durable abilities and owners are required? |
| State machine | Which order, settlement or election states are permitted? |
| Sequence view | How do applications and external venues interact at runtime? |
| Position and lineage model | Which portfolio, custody and external positions exist at an effective time? |
| Reconciliation matrix | Which records must agree, and who owns a break? |
| Dependency and resilience view | Which market, identity, data and cash services support the critical outcome? |

Do not show advice steps, application components, custody accounts and deployment nodes as though they were one notation. No diagram source is created in this pass.

## Worked traceability: advice through settlement

`HB-SCN-13 Advise and Execute an Investment` begins with an eligible client and current mandate. `HB-APP-049` records suitability and recommendation under `HB-CTRL-22`. An approved order crosses `HB-INT-049` to `HB-APP-050`, which routes it through `HB-INT-075` and records fills and allocation.

Before release, the order is checked against the client's objectives, risk appetite, mandate, current restrictions and available position or cash. Any suitability exception or restricted instrument stops or refers the order under the authorised policy. The external response retains broker or venue evidence for `HB-REC-023`.

`HB-INT-050` transfers the allocation to `HB-APP-051`. Settlement crosses `HB-INT-076`; `HB-REC-023` checks order and execution, while `HB-REC-025` checks securities and cash. `HB-ACC-22` records the governed financial consequence, and positions flow to custody and the portfolio view with effective-time lineage.

The example deliberately leaves the applicable advice regime, venue, execution policy, settlement mechanism, fees and failed-item rules pending.

## Worked traceability: corporate action

`HB-SCN-14 Safekeep Securities and Process a Corporate Action` begins with an external notice for a held security. `HB-APP-053` validates the notice, while `HB-APP-052` supplies the eligible position. The asset-servicing application records any client election and sends it through `HB-INT-077`.

When proceeds or securities arrive, `HB-CTRL-24` validates the outcome, `HB-ACC-23` records the entitlement and `HB-REC-026` compares the notice, position, election, receipt and allocation. A missing response remains an exception with an owner rather than becoming a silent default.

## Current-to-target considerations

The portfolio, order, securities-processing, custody and asset-servicing applications are current. The target need is governed authority, market connectivity and reconciliation across them, not forced consolidation into one wealth platform.

A safe transition begins with common client, portfolio, order, instrument, account and position identifiers. It then versions product and restriction rules, establishes market-data precedence, parallel-reconciles executions, cash and positions, and moves client reporting only after lineage is proven. Custody or broker migration must preserve historical cost and tax-lot evidence, open settlement fails, pending elections and external account relationships. A new portfolio screen must not become authoritative merely because it is introduced first.

## When should this model set be used?

Use it for wealth-platform change, order-management replacement, custody sourcing, client-asset review, market expansion, corporate-action improvement and recovery planning. It is especially useful when several systems display a position but only one is authoritative for a stated purpose and time.

Do not use it as investment advice, a custody agreement, a market rulebook, a legal segregation opinion or proof of regulatory compliance.

## Common mistakes

- Treating an investment recommendation as an executable order.
- Treating an execution as completed securities settlement.
- Calling the portfolio view the authoritative custody holding.
- Ignoring partial fills, allocation changes and settlement fails.
- Storing corporate-action notices without source precedence or eligible-position time.
- Treating external custody records as accepted internal books without reconciliation.
- Assuming every client or asset uses the same suitability, custody or tax rules.
- Mapping a BIAN candidate directly to a microservice or team.

## Key takeaways

- Advice, portfolio, order, settlement, custody and asset servicing are distinct responsibilities.
- Data authority changes by lifecycle, purpose and effective time.
- Client-asset protection depends on records, controls, third-party responsibilities and reconciliation.
- Corporate actions require notice, position, election, proceeds and allocation traceability.
- Operational priorities differ between advisory work, settlement and market deadlines.
- BIAN mappings must be verified and must not dictate physical boundaries.

## Practical exercise

Trace one investment order from recommendation to custody position, then add a later dividend event. For each stage, record the capability, process, application, source of record, interface, control, accounting event and reconciliation.

**Suggested review criteria:** The answer must use full governed IDs, distinguish execution from settlement, distinguish portfolio from custody, include an external-network boundary, and leave jurisdiction and market rules explicit.

## Review checklist

- [x] Advice, portfolios, orders, securities, custody and asset servicing are separated.
- [x] Authoritative records and effective-time concerns are explicit.
- [x] Accounting events, controls and reconciliations use governed IDs.
- [x] Client-asset, market and jurisdiction assumptions remain visible.
- [x] Resilience is tied to business outcomes and deadlines.
- [ ] Add governed BIAN 14.0 candidates for wealth and securities after verification.
- [ ] Diagram production remains deferred pending author-approved specifications.

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14]
- [CPMI-PAYMENT-GLOSSARY-2016]
- [IOSCO-CLIENT-ASSETS-SUITABILITY]

## Drafting notes

- Before formal review, verify exact BIAN 14.0 candidates and applicable advice, client-asset, market, custody and tax obligations.
