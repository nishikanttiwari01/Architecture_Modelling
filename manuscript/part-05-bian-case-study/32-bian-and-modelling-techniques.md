---
title: "How a Full-Service Bank Works"
chapter: 32
part: "part-05-bian-case-study"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-13"
---

# 32. How a Full-Service Bank Works

## Chapter purpose

Give readers the commercial and operational foundation needed to understand the architecture of Horizon Bank.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- describe the main customer segments, product families and enterprise functions of a full-service bank;
- explain, at a conceptual level, how interest, fees, capital, liquidity and risk affect architecture;
- distinguish customer, product, transaction, case, accounting and reporting lifecycles;
- explain why channels, processors, customer, risk, finance, integration and data platforms have different responsibilities;
- identify critical operations and their people, technology and third-party dependencies.

## Prerequisites and dependencies

- Chapter 31: BIAN Essentials and the Case-Study Method

## Required models and artefacts

- Full-service bank operating model and lifecycle views, specified before diagram production

## Worked examples

- Horizon Bank interest posting and time-critical payment

## Source requirements

- Use official banking, accounting, prudential and resilience sources; qualify jurisdiction-specific claims.

## Planned chapter structure

The following sections implement the approved Chapter 32 full-service bank foundation.

## Horizon Bank scope and assumptions

Horizon Bank is a fictional full-service bank. It serves retail, small and medium-sized enterprise (SME), commercial, corporate, private-banking and institutional customers. It provides deposits, lending, payments, cards, cash management, trade finance, wealth services and treasury products.

The case study uses one banking group with country entities and shared group services. It does not claim one jurisdiction's legal or regulatory rules apply universally. Quantitative capital, liquidity, recovery and service targets are deliberately omitted until evidence exists.

## Why a bank exists

A bank connects customers who need to store, move, borrow or invest money with a controlled financial and operational infrastructure. It accepts and manages obligations, transforms maturities, provides credit, executes transactions, safeguards assets and supplies information and advice. These activities expose the bank to credit, market, liquidity, operational, conduct, legal and other risks.

Stakeholders include customers, employees, shareholders, boards, regulators, central banks, payment and market infrastructures, suppliers, counterparties, auditors and communities. Architecture must therefore consider safety, service, control and evidence as well as speed and cost.

## Customer segments and needs

| Segment | Typical needs | Architectural consequences |
|---|---|---|
| Retail | Everyday accounts, payments, cards, savings, mortgages and personal credit | High volumes, accessible channels, fraud controls and simple servicing |
| SME | Accounts, payments, lending, cards and cash-flow support | Business ownership, mandates, limits and mixed digital-assisted service |
| Commercial and corporate | Liquidity, bulk payments, credit, trade and foreign exchange | Complex legal structures, approvals, files, host connectivity and relationship management |
| Private banking | Advice, investments, credit and consolidated reporting | Suitability, confidentiality, portfolio and relationship views |
| Institutional | Markets, custody, settlement and financing | Market infrastructure, positions, collateral, high-value controls and resilience |

Segments influence service design but do not create separate copies of every capability. Shared party, product, identity, finance and control services may support several segments.

## Product families and business lines

Products define commercial terms and customer promises. Business lines organise accountability and performance. Legal entities hold contracts, assets, liabilities and regulatory responsibilities. These are different views.

Horizon Bank's product families include current and savings accounts, term deposits, consumer and mortgage lending, SME and corporate credit, domestic and cross-border payments, cards, cash management, trade instruments, investments, custody and treasury products. Each needs an owner, lifecycle, eligibility, pricing, accounting treatment, controls and servicing model.

## Front, middle and back office

The **front office** engages customers and counterparties, originates business and provides advice or service. The **middle office** independently assesses or monitors risks, limits, valuation and controls where separation is appropriate. The **back office** confirms, settles, records, reconciles and services transactions.

This is a responsibility pattern, not a universal organisation chart. A digital transaction may be straight-through while still crossing these control responsibilities. Manual exceptions may involve operations, compliance, risk, finance and customer service.

## Revenue, costs and the balance sheet

A simplified bank balance sheet has assets such as cash, securities and loans, and liabilities such as customer deposits and wholesale funding. Equity absorbs losses and supports the business. The two sides must remain balanced through accounting entries.

Interest income arises when the bank earns interest on assets. Interest expense arises when it pays for deposits or funding. The difference contributes to net interest income. Fees may arise from payments, cards, accounts, advice, custody, trade services or commitments. Costs include people, technology, premises, suppliers, losses and regulatory or control activity.

Architecture affects these mechanics. A pricing engine, product processor, subledger, general ledger and profitability platform answer different questions. Combining them without clear authority makes it difficult to explain a customer's charge or reconcile financial results.

## Capital, liquidity and risk

Capital provides loss-absorbing capacity. Liquidity concerns the ability to meet obligations when due. Profit does not guarantee liquidity, and a liquid position does not guarantee solvency. Risk limits, collateral, funding, settlement timing and legal-entity boundaries influence whether a transaction can proceed.

The case study treats these concepts qualitatively. Later chapters must not invent ratios or thresholds. They should show where decisions, data, controls and evidence belong.

## From business event to general ledger

Consider interest credited to a deposit account. A business event triggers product rules, the deposit processor updates the account, accounting logic produces balanced entries, a subledger retains product detail and summarised postings reach the general ledger. Reconciliations compare positions and movements across these records.

The general pattern is:

```text
business event
→ product or transaction processing
→ accounting event
→ subledger entry
→ general ledger posting
→ reconciliation
→ financial, management and regulatory reporting
```

A straight-through flow still needs exception handling. Invalid mappings, late files, rejected postings and unmatched balances require repair, ownership and evidence.

## Dates and the banking day

The **booking date** records when an entry is recognised by a system. The **value date** affects when financial value or interest takes effect. The **settlement date** records when obligations are exchanged or discharged. These dates may differ.

End-of-day and intraday processing can include cut-offs, accruals, fees, interest, settlement, reconciliation, batch controls and opening the next business date. Architecture diagrams that show only a real-time API miss these operational responsibilities.

## Connected lifecycles

| Lifecycle | Starts with | Typical outcome |
|---|---|---|
| Customer | Prospect or party identified | Relationship established, serviced or exited |
| Product | Idea or market need | Product launched, changed and retired |
| Agreement | Offer accepted | Rights and obligations created, amended and closed |
| Transaction | Instruction or market event | Accepted, processed, settled, posted or rejected |
| Case or exception | Alert, complaint or failed step | Decision, repair, redress or closure with evidence |
| Accounting | Business event | Balanced, reconciled financial records |
| Reporting | Reporting requirement | Approved information delivered and retained |

These lifecycles intersect. Onboarding creates party and agreement information. A payment uses an account agreement, creates transactions and accounting entries, may create a screening case and contributes to reporting.

## Why banks use different application families

- **Channels** manage interaction and presentation.
- **Journey and workflow platforms** coordinate multi-step work.
- **Customer and party platforms** manage identity and relationships.
- **Product processors** apply product rules, maintain balances or positions and execute lifecycle behaviour.
- **Risk and control systems** provide independent assessment, monitoring, limits, alerts and evidence.
- **Finance systems** maintain accounting authority and reporting.
- **Integration platforms** connect systems without becoming the owner of every business rule.
- **Data platforms** support governed analytics and reporting without silently replacing operational authority.

Separation is justified by responsibility and control, not by a desire to maximise the number of systems.

## Three lines and independent assurance

Horizon Bank uses an illustrative three-lines model. Business and operational management own and manage risk. Independent risk and compliance functions set frameworks and challenge or monitor. Internal audit provides independent assurance. Exact responsibilities vary by organisation and jurisdiction, so catalogues must name the accountable owner instead of relying on the label alone.

## Group, country, shared service and outsourcing

Group functions may define standards, shared platforms and consolidated reporting. Country entities retain local contractual, operational and regulatory responsibilities. Shared-service centres can perform common work, while outsourced providers can supply technology or operations. Accountability does not disappear when work is centralised or outsourced.

Every shared or external dependency therefore needs a service owner, data and control responsibilities, failure and exit arrangements, and a clear legal-entity scope.

## Critical operations

A critical operation is modelled from an important customer or market outcome through the people, process, applications, information, facilities, technology and third parties needed to deliver it. Operational resilience is the ability to deliver critical operations through disruption. [BCBS-OPERATIONAL-RESILIENCE-2021]

For example, `Make a time-critical payment` depends on customer access, identity, payment initiation, screening, account balance and posting, clearing connectivity, liquidity, settlement, customer communication and repair operations. A resilient design tests the whole chain, including degraded operation, rather than only the availability of the Payments Platform.

## Common mistakes

- Treating a business line as a capability or legal entity.
- Modelling the customer journey without accounting, settlement or exceptions.
- Assuming real-time channels remove batch and business-day controls.
- Treating the data platform as authoritative for every operational datum.
- Describing outsourcing without retained accountability and exit planning.
- Assigning numerical service targets without evidence.

## Key takeaways

- A bank connects customer outcomes to controlled financial obligations and records.
- Customer, product, transaction, case, accounting and reporting lifecycles are distinct but connected.
- Product processors, risk systems and finance systems have different authorities.
- Legal entity, group and shared-service responsibilities must be explicit.
- Critical operations include people, data and third parties as well as applications.

## Practical exercise

Trace a retail card purchase through customer interaction, authorisation, clearing, settlement, account posting, reconciliation and reporting. Mark which stages may occur on different dates and identify one exception path.

## Review checklist

- [x] Major customer segments and product families are introduced.
- [x] Revenue, cost, balance-sheet and accounting mechanics are explained conceptually.
- [x] The principal lifecycles and application families are distinguished.
- [x] Critical operations include end-to-end dependencies.
- [ ] Enterprise figure specifications require author approval before source creation.

## References and further reading

- [BCBS-OPERATIONAL-RESILIENCE-2021]

## Drafting notes

- Add further primary-source support for accounting, capital and liquidity before formal source review.
