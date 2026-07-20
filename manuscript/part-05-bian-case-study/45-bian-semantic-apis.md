---
title: "Treasury, Markets, Funding, Liquidity, ALM and Capital"
chapter: 45
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 45. Treasury, Markets, Funding, Liquidity, ALM and Capital

## Chapter purpose

Show how to model the part of a full-service bank that manages funding, liquidity, market positions, balance-sheet structure and capital. The chapter separates business decisions from transaction execution, independent risk oversight, accounting and settlement, then traces those responsibilities through Horizon Bank's governed catalogues.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- explain funding, liquidity, markets, asset and liability management and capital in plain language;
- distinguish treasury ownership from payments, finance and independent risk ownership;
- model treasury decisions from governed positions, assumptions and limits through execution and evidence;
- identify the applications, data authorities, interfaces, accounting events, controls and reconciliations needed for a credible treasury landscape;
- trace a liquidity-shortfall scenario using exact Horizon Bank identifiers; and
- recognise where a BIAN mapping is still unverified rather than inventing a Service Domain equivalence.

## Prerequisites and dependencies

- Chapter 36: Horizon Bank Technology, Security, Resilience and Operations Architecture
- Chapter 41: Payments, Clearing, Settlement, Correspondent Banking and Foreign Exchange
- Chapter 46: Finance, Accounting, General Ledger, Reconciliation, Tax and Reporting

## Required models and artefacts

- Governed treasury domain, capability, process, organisation and application records
- Position, interface, accounting-event, reconciliation, control and resilience trace
- Scenario trace for `HB-SCN-15 Manage a Treasury Liquidity Shortfall`

## Worked examples

- Horizon Bank treasury and liquidity-shortfall scenario

## Source requirements

Current treasury and BIAN claims use official primary sources. Horizon Bank structures are identified as an author model, and jurisdiction-specific thresholds remain deferred.

## The question this architecture answers

Treasury architecture answers: **How does the bank understand and change its financial position while keeping decisions, trades, cash movements, risk limits and accounting evidence consistent?**

In plain language, treasury makes sure the bank can meet its obligations, obtains funding, manages exposures created by the balance sheet and executes approved market activity. It does not own every cash movement or every risk measure. Payment operations settle customer and bank transactions. Finance maintains the books. Independent risk challenges exposures and limits. Treasury brings those views together to decide and act.

Asset and liability management (ALM) is the coordinated management of the balance sheet. It considers matters such as maturity, repricing, currency and liquidity differences between assets and liabilities. Capital management considers whether the bank has sufficient and appropriately allocated financial resources for its risks and plans. These are related analytical responsibilities, but neither is the same as daily cash management or trading.

The Basel Committee describes liquidity as the ability to fund asset growth and meet obligations as they fall due without unacceptable loss. Its principles connect risk tolerance, cash-flow measurement, stress testing, contingency funding, intraday liquidity, collateral and liquid-asset buffers [BCBS-LIQUIDITY-RISK-2008]. The precise regulatory calculations and thresholds depend on a bank's jurisdictions. Horizon Bank therefore models the responsibilities and evidence without fabricating ratios or limits.

## Scope and responsibility boundaries

Horizon Bank groups the area under `HB-DOM-100 Treasury, Markets, Funding, Liquidity, ALM and Capital`. Its four Level 2 domains prevent the word *treasury* from becoming an uncontrolled bucket.

| Governed domain | Responsibility | Important boundary |
|---|---|---|
| `HB-DOM-101 Funding and Liquidity` | Funding plans, cash positions, buffers and intraday liquidity | Payment engines execute instructions; independent risk oversees liquidity risk |
| `HB-DOM-102 Asset and Liability Management and Capital` | Balance-sheet structure, interest-rate risk, capital planning and allocation | Finance owns accounting policy and authoritative books |
| `HB-DOM-103 Markets and Trading` | Trade capture, positions, pricing, execution and lifecycle oversight | Market Risk independently measures and challenges exposure |
| `HB-DOM-104 Treasury Operations` | Confirmation, settlement, collateral and transaction control | Trading authority is kept separate from confirmation and settlement control |

The Level 1 capability is `HB-CAP-100 Treasury, Markets and Balance-Sheet Management`. Its Level 2 capabilities are `HB-CAP-101 Funding Management`, `HB-CAP-102 Liquidity Management`, `HB-CAP-103 Asset and Liability Management`, `HB-CAP-104 Capital Management`, `HB-CAP-105 Markets Trading`, `HB-CAP-106 Market Valuation and Risk Analytics`, `HB-CAP-107 Counterparty Exposure Management` and `HB-CAP-108 Treasury Transaction Operations`.

This capability view says what the bank must be able to do. The process view says how work progresses. `HB-PROC-11 Manage Treasury and Financial Position` is the Level 1 process, supported by:

- `HB-PROC-139 Plan and Execute Funding and Liquidity`;
- `HB-PROC-140 Manage Balance-Sheet Structure and Capital`;
- `HB-PROC-141 Trade and Manage Market Positions`; and
- `HB-PROC-142 Confirm, Settle and Control Treasury Transactions`.

The organisation view assigns accountability. `HB-ORG-11 Treasury and Markets` and `HB-ORG-30 Trade, Treasury and Securities Operations` are different units. `HB-ORG-106 Treasurer Role` owns treasury direction. `HB-ORG-13 Enterprise and Financial Risk` provides independent risk oversight, while `HB-ORG-12 Finance, Accounting, Tax and Reporting` owns financial control and books. A process model that places all these activities in one swimlane hides necessary challenge and segregation.

## Model the four connected lifecycles

### Funding and liquidity

Funding management forecasts needs, evaluates sources, executes approved funding and monitors maturities and concentration. Liquidity management adds current cash and collateral positions, expected inflows and outflows, intraday obligations, stress assumptions and contingency actions. A balance alone is not a liquidity position because availability, currency, time, legal entity and encumbrance matter.

The architecture must retain the assumptions behind a forecast. A forecast generated at 09:00 from incomplete settlement data is not interchangeable with an updated position at 12:00. Store effective time, source cut-off, scenario, currency, legal entity and quality state with the result.

Funding instruments have different timing and risk effects. Illustrative money-market activity includes overnight unsecured borrowing, short-term deposits, secured borrowing and repurchase transactions. A short maturity does not make an instrument interchangeable with cash. The model must retain counterparty, currency, principal, rate, maturity, collateral, settlement and legal-entity scope.

Two prudential views commonly needed in liquidity architecture are the **Liquidity Coverage Ratio (LCR)** and **Net Stable Funding Ratio (NSFR)**. At a conceptual level, the LCR concerns resilience to a short-term stressed outflow horizon, while the NSFR concerns a more stable funding profile over a longer horizon. Their applicable calculation rules, factors and thresholds are jurisdictional requirements, not values to invent for Horizon Bank. Architecture must preserve the source positions, classifications, encumbrance, currency, legal entity, rule version, adjustments and approval supporting either measure.

### ALM and capital

ALM compares assets and liabilities by characteristics such as repricing and maturity. It uses behavioural assumptions where contractual behaviour does not describe likely cash flows. Examples include how non-maturity deposits may behave or when customers may prepay loans. These assumptions are governed inputs, not hidden spreadsheet constants.

Interest rate risk in the banking book (IRRBB) is one ALM concern. The Basel Committee's 2024 recalibration shows that prescribed shock assumptions can change [BCBS-IRRBB-2024]. The architectural lesson is to version models, parameters and results and to record which version supported a decision. This chapter does not reproduce the regulatory calibration or assert its local applicability.

Capital management consumes approved exposures, financial plans, earnings and risk results. It produces plans, allocations and management actions. It should not overwrite the General Ledger or become a second authoritative source for product balances.

**Funds transfer pricing (FTP)** is an internal management method for attributing funding and liquidity effects to products or business units. `HB-APP-057` may calculate governed FTP results from curves, behavioural assumptions and product cash flows. FTP is not a customer rate, a cash settlement or a General Ledger balance. Its methodology, effective date, allocation dimensions and approval must remain traceable.

Hedging changes a defined risk exposure through an approved instrument or relationship. For example, an interest-rate swap may reduce repricing sensitivity, while a foreign-exchange swap may change currency liquidity across value dates. The hedge decision, executed trade, independent valuation, accounting treatment and effectiveness assessment are separate concerns. The architecture should never infer that a position is hedged merely because an offsetting trade exists.

### Markets and trading

A treasury trade lifecycle includes an authorised decision, execution, capture, independent confirmation, valuation, position update, settlement, accounting and reconciliation. Not every product follows an identical path, but each trade needs a stable identity and traceable lifecycle state.

Front-office execution and position management should not silently perform independent confirmation or approve its own valuation exception. The separation can be organisational, technical or both. What matters is that the model shows who may create, confirm, amend, value, settle and approve an exception.

The markets model must work for more than one instrument family. A money-market borrowing creates principal and interest cash flows. A fixed-income purchase creates trade, security, price, accrued-interest, settlement and position records. A derivative such as an interest-rate swap or foreign-exchange swap creates contractual cash flows, valuation changes, counterparty exposure and, where applicable, margin obligations. Instrument-specific detail belongs in product and trade models, while common trade identity, authority, confirmation, valuation, settlement and accounting relationships belong in the enterprise architecture.

Profit and loss (P&L) reporting connects trading activity and valuation to explainable financial effects. Realised trading results, unrealised valuation changes, accrued interest, fees, funding effects and authorised adjustments must not be collapsed into one unexplained number. Treasury can analyse P&L, but Finance owns the governed accounting view. `HB-APP-063 Management Reporting and Performance` consumes `HB-INT-089 Management Reporting Dataset` from `HB-APP-081 Enterprise Analytical Data Platform`; it does not calculate authoritative trade state or replace the General Ledger.

### Treasury operations

Treasury operations turns an executed trade into controlled obligations and evidence. It confirms terms, manages settlement instructions, monitors failures, coordinates collateral and margin where relevant and resolves breaks. It connects markets to `HB-VS-04 Execute and Settle Transaction` and finance to `HB-VS-09 Record, Reconcile and Report` without transferring ownership of those value streams to the trading desk.

## Applications and authoritative information

A credible landscape separates applications when responsibility, authority or operational behaviour differs.

| Application | Primary responsibility | Authority or limitation |
|---|---|---|
| `HB-APP-054 Treasury Trading and Position Management` | Treasury trades, positions, valuations and lifecycle events | Authority for treasury trades and positions |
| `HB-APP-055 Market and Counterparty Risk` | Market, counterparty and valuation exposure measurement | Derived risk measurement, not trade authority |
| `HB-APP-056 Funding and Liquidity Management` | Cash forecasts, funding plans, liquidity positions and actions | Authority for funding plans and derived liquidity positions |
| `HB-APP-057 Asset Liability and Capital Management` | Balance-sheet, IRRBB, capital and transfer-pricing analysis | Analytical results, not transaction authority |
| `HB-APP-036 Settlement and Nostro Management` | Settlement-account and correspondent positions | Payment and settlement responsibility |
| `HB-APP-058 Product Subledger Platform` | Product-level accounting entries and balances | Target subledger authority, not trade execution |
| `HB-APP-059 General Ledger` | Approved legal-entity journals, periods and balances | `HB-SOR-04 General Ledger Authority` |

The core information domain is `HB-DATA-12 Treasury, Markets, Funding, Liquidity and Capital`. Treasury also consumes `HB-DATA-03 Account and Transaction`, `HB-DATA-05 Finance and Accounting` and `HB-DATA-15 Reference and Market Data`. `HB-SOR-18 Treasury Trade and Position Authority` identifies the authoritative source boundary. Analytical copies may be useful, but they must retain lineage to that authority.

A position is a calculated view at a defined point or interval. A balance is an amount associated with an account or ledger dimension. A cash-flow forecast is a time-distributed expectation. Treating these as synonyms leads to false reconciliation and poor decisions.

## Interfaces, accounting and reconciliation

Interfaces are contracts between responsibilities, not lines drawn for decoration.

- `HB-INT-068 Treasury Foreign Exchange Booking` connects approved foreign-exchange activity to treasury booking.
- `HB-INT-078 Market Risk Position Feed` transfers positions and valuations from `HB-APP-054` to `HB-APP-055`.
- `HB-INT-079 Treasury Liquidity Position Event` transfers position changes to `HB-APP-056`.
- `HB-INT-080 Balance-Sheet Analytical Feed` supplies governed balances and cash flows to `HB-APP-057`.
- `HB-INT-081 Treasury Accounting Event` transfers treasury lifecycle effects to `HB-APP-058`.
- `HB-EXT-010 Market and Reference Data Connectivity` represents external market and reference data connectivity without naming an unsupported vendor.

Treasury accounting events include `HB-ACC-24 Treasury Trade Settled`, `HB-ACC-25 Treasury Valuation Changed` and `HB-ACC-26 Funding Interest Accrued`. `HB-ACC-16 Foreign-Exchange Deal Recognised` may also participate where a foreign-exchange deal is in scope. An accounting event states the economically relevant occurrence. It is not the journal itself. Finance applies governed accounting rules and chart mappings before posting.

Three reconciliations provide different evidence:

- `HB-REC-027 Treasury Trade Confirmation` compares internal capture with a counterparty or venue confirmation;
- `HB-REC-028 Treasury Position, Cashflow and Ledger` compares positions and valuations with settlement, product-control and ledger records; and
- `HB-REC-029 Liquidity Position and Cash Availability` compares liquidity positions with settlement accounts, nostro balances, funding trades and expected cash flows.

Combining them into one `treasury reconciliation` would hide different populations, timing, owners and break actions.

## Controls, risk and resilience

`HB-CTRL-25 Treasury Dealing Authority and Confirmation` controls who may deal and ensures confirmation is independent. `HB-CTRL-26 Market Data and Valuation Control` governs sources, valuation methods and exceptions. `HB-CTRL-27 Liquidity Position and Funding Decision Control` connects data quality, limits, decision authority and evidence. The general `HB-CTRL-03 Ledger Reconciliation` still applies to the finance boundary.

Market and counterparty exposure measurement in `HB-APP-055` supports treasury decisions, but `HB-DOM-122 Financial Risk Oversight` and capabilities `HB-CAP-123 Market Risk Oversight` and `HB-CAP-124 Liquidity Risk Oversight` remain independently accountable. Independent oversight should be able to reproduce results, challenge assumptions and see breaches without editing treasury's trade record.

`HB-TECH-017 Treasury and Markets Classification` groups the recovery and technology concerns for this estate. It is linked to `HB-CRIT-14 Manage Intraday Liquidity and Funding`. A useful resilience model includes market-data connectivity, identity and dealing authority, trade and position authority, settlement dependencies, accounting-event delivery and post-recovery reconciliation. It should not invent a recovery time objective (RTO) or recovery point objective (RPO) before business impact analysis and owner approval.

## Worked trace: liquidity shortfall

`HB-SCN-15 Manage a Treasury Liquidity Shortfall` starts when a governed indicator identifies an actual or emerging shortfall. Its outcome is not merely `dashboard updated`. An authorised action must restore or protect liquidity, or the matter must be escalated with explicit restrictions and evidence.

A catalogue-backed trace is:

1. `HB-APP-054` supplies governed trade and position changes through `HB-INT-079`.
2. `HB-APP-036` contributes settlement and cash availability through `HB-INT-066 Intraday Settlement Position Event`.
3. `HB-APP-056` aggregates positions in `HB-DATA-12`, records source timing and evaluates the shortfall.
4. Treasury applies `HB-CTRL-27`, checks approved limits and evaluates funding or restriction options.
5. `HB-ORG-106 Treasurer Role` or a delegated authority approves the action; independent liquidity risk retains challenge rights.
6. An approved trade is captured in `HB-APP-054`, exchanged through the relevant market connection and later creates `HB-ACC-24` or `HB-ACC-26` as applicable.
7. `HB-REC-027`, `HB-REC-028` and `HB-REC-029` test confirmation, position, cash and ledger consistency.
8. The scenario remains open if settlement fails, the forecast uses stale data, a limit is breached or required evidence is missing.

This trace crosses domains, but it does not imply that one orchestrator owns every state. The scenario view shows coordination. The application and data views preserve authority.

### Required trace: short-term funding plus a foreign-exchange swap

Assume `HB-APP-056` identifies a same-day shortfall in one currency and a near-term surplus in another. Treasury considers short-term borrowing for the immediate need and a foreign-exchange swap to manage the currency profile across agreed value dates.

1. `HB-APP-036` publishes settlement obligations and cash-position changes to `HB-APP-056` through `HB-INT-066`.
2. `HB-APP-054` publishes treasury cash, funding and maturity changes to `HB-APP-056` through `HB-INT-079`.
3. `HB-APP-056` preserves the currency, legal entity, maturity, source time, quality and stress context, then applies `HB-CTRL-27 Liquidity Position and Funding Decision Control`.
4. `HB-ORG-106 Treasurer Role` or a valid delegate approves the funding and foreign-exchange actions. `HB-CAP-124 Liquidity Risk Oversight` retains independent challenge.
5. The approved borrowing and swap are booked in `HB-APP-054`. The interface catalogue currently has no governed treasury-to-market execution interface, so the external execution hand-off remains an explicit gap rather than being mislabelled as `HB-INT-068`, which carries customer foreign-exchange bookings from `HB-APP-039` to `HB-APP-054`.
6. `HB-INT-081` carries treasury accounting events from `HB-APP-054` to `HB-APP-058`. Relevant governed events can include `HB-ACC-16 Foreign-Exchange Deal Recognised`, `HB-ACC-24 Treasury Trade Settled` and `HB-ACC-26 Funding Interest Accrued`.
7. `HB-REC-027`, `HB-REC-028` and `HB-REC-029` test confirmation, position, cash, liquidity and ledger consistency. Settlement failure, a stale position or an unapproved limit breach keeps the scenario open.
8. Management receives a lineage-controlled view through `HB-INT-089`, while authoritative trades remain under `HB-SOR-18 Treasury Trade and Position Authority` and approved ledger balances remain under `HB-SOR-04 General Ledger Authority`.

The trace separates the liquidity decision, market execution, trade authority, settlement, accounting and management view. It also exposes a real catalogue gap instead of drawing an invented integration.

## BIAN alignment without invented precision

BIAN announced Service Landscape 14.0 in March 2026 [BIAN-SERVICE-LANDSCAPE-14-PV45-48]. The current Horizon Bank BIAN mapping register contains proposed author-model candidates for deposits, payments, credit and trade finance. Their exact BIAN 14.0 objects and verification remain pending. The register contains no governed treasury mapping record.

Therefore this chapter does not assign a Service Domain name from memory. A future mapping must inspect the specific 14.0 artefacts, compare the complete Horizon responsibility with the candidate Service Domain purpose and control record, record source and confidence, and obtain review. A BIAN Service Domain would remain a logical reference boundary. It would not automatically equal `HB-APP-054`, a microservice, a database or `HB-ORG-11`.

## Current-to-target considerations

The catalogue records `HB-APP-054` to `HB-APP-057` as current applications, while `HB-INT-080` and `HB-INT-081` represent target governed feeds. This mix is realistic. A target-state programme should not replace current systems merely to make a picture uniform.

A defensible transition sequence is to establish trade and position identifiers, govern market-data and model versions, expose position and accounting contracts, automate high-risk reconciliations, then reduce duplicate analytical stores. Each step needs parallel-run criteria, break ownership and a rollback path. The target is improved authority and traceability, not a fashionable platform shape.

## When to use each model

Use a capability map to agree responsibilities, a process model to examine hand-offs and approvals, an application cooperation view to show system interactions, a data-lineage view to test source and transformation, and a scenario trace to examine one outcome across all layers. Do not use a balance-sheet chart to explain application ownership, or an application landscape to specify trade-state transitions.

## Common mistakes

- Treating treasury, finance and risk as one function because they use similar numbers.
- Treating the LCR and NSFR as dashboard labels without rule version, source classification and legal-entity scope.
- Treating FTP as an external price or an authoritative ledger balance.
- Claiming a hedge without linking the approved exposure, instrument, valuation and accounting treatment.
- Modelling a dashboard as the source of liquidity truth without showing sources and effective times.
- Hiding behavioural assumptions and model versions inside spreadsheets.
- Allowing the trading application to self-confirm trades or approve its own valuation exceptions.
- Treating settlement as complete before cash, position and accounting reconciliations finish.
- Using one `position` field for trade, cash, risk and ledger meanings.
- Claiming BIAN alignment without a versioned mapping record.
- Publishing invented limits, capital ratios, RTOs or RPOs for the fictional bank.

## Chapter summary

Treasury architecture connects decisions to positions, actions and evidence. Horizon Bank separates funding and liquidity, ALM and capital, markets and trading, and treasury operations while preserving interfaces to payments, finance and independent risk. Exact application, interface, accounting-event, reconciliation, control and resilience identifiers make the model testable. The remaining BIAN mapping is an explicit governance gap, not an invitation to guess.

## Key takeaways

- Liquidity is time-, currency-, entity- and availability-sensitive; it is not just a balance.
- ALM assumptions and regulatory scenarios must be versioned and traceable.
- Money-market, fixed-income and derivative lifecycles share control patterns but retain instrument-specific cash flows and risks.
- LCR, NSFR, FTP, hedging and P&L each answer a different management or prudential question.
- Trading, independent risk oversight, confirmation, settlement and accounting are distinct responsibilities.
- `HB-APP-054` to `HB-APP-057` form a realistic treasury application set with different authorities.
- Accounting events and reconciliations connect treasury activity to authoritative financial books.
- Resilience includes identity, market data, settlement and recovery reconciliation, not only application uptime.
- No treasury BIAN mapping is claimed until a version-specific candidate is governed and verified.

## Practical exercise

An intraday dashboard shows sufficient liquidity, but the latest correspondent statement has not arrived and a large treasury trade was amended after the last feed. Create a one-page scenario trace that names the relevant governed applications, interfaces, control and reconciliations. State whether the bank may act on the displayed position.

### Suggested answer criteria

A strong answer includes `HB-APP-036`, `HB-APP-054` and `HB-APP-056`; identifies `HB-INT-066` and `HB-INT-079`; flags source time and quality; applies `HB-CTRL-27`; and requires `HB-REC-027`, `HB-REC-028` and `HB-REC-029` as applicable. It does not treat the dashboard as authoritative. It either blocks the decision, applies an approved conservative fallback or escalates under an explicit policy.

## Review checklist

- [ ] Funding, liquidity, ALM, capital, markets and treasury operations have distinct definitions.
- [ ] Treasury, payments, finance and independent risk boundaries are explicit.
- [ ] Positions show source, effective time, currency, legal entity and quality.
- [ ] Applications and interfaces use exact governed identifiers.
- [ ] Accounting events are not confused with journals.
- [ ] Confirmation, cash, position and ledger reconciliations are separate.
- [ ] Decision authority and independent challenge are visible.
- [ ] Resilience includes external and downstream dependencies.
- [ ] Regulatory applicability and numeric thresholds are not invented.
- [ ] BIAN candidates remain unclaimed until versioned verification is recorded.

## References and source notes

- [BCBS-LIQUIDITY-RISK-2008]
- [BCBS-IRRBB-2024]
- [BIAN-SERVICE-LANDSCAPE-14-PV45-48]

## Deferred work

No diagram source is created in this pass. A future treasury position-and-control view requires an author-approved diagram specification. Horizon Bank still needs verified BIAN candidates, product coverage for markets activity, legal-entity decision rights, approved model inventory, market connectivity detail and owner-approved resilience objectives.
