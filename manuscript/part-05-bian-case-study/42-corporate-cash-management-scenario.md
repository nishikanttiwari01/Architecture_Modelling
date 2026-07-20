---
title: "Cards and Merchant Acquiring"
chapter: 42
part: "part-05-bian-case-study"
status: "Under Review"
author: "Nishikant Tiwari"
last_updated: "2026-07-20"
---

# 42. Cards and Merchant Acquiring

## Chapter purpose

A card purchase joins two customer relationships. An issuer serves the cardholder, while an acquirer serves the merchant. Between them, processing and network responsibilities carry authorisation, clearing, settlement and dispute information. This chapter shows how to model those responsibilities without treating `Cards` as one product or one application.

The central architecture question is: **who owns the cardholder, merchant, transaction and financial states from credential issuance to final settlement and dispute resolution?** The Horizon Bank catalogue is a fictional author model. Card-network participation, licences, rules and deadlines remain unverified.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- distinguish card issuing, card processing and merchant acquiring;
- trace authorisation, presentment, clearing, settlement, fraud and disputes;
- assign data authority without storing every card concern in one system;
- connect applications to interfaces, accounting events, controls, reconciliations and resilience classes;
- explain why a scheme or processor boundary is not automatically a bank application boundary; and
- identify the models needed for card product, behaviour, data and operational decisions.

## Prerequisites and dependencies

- Chapter 37, for party onboarding and customer due diligence.
- Chapter 38, for deposit accounts used by debit cards and merchant settlement.
- Chapter 41, for payment clearing and settlement concepts.

## Required models and artefacts

- Governed card product hierarchy, capability and process records.
- Issuer, processor, acquirer, interface and external-network catalogues.
- Card-state, data-authority, accounting-event and reconciliation views.
- Fraud, dispute, security and resilience control records.

The governed operating trace assigns proposition accountability to `HB-ORG-112 Cards Portfolio Owner Role`. `HB-ORG-28 Payment and Card Operations` performs card clearing, settlement, disputes and merchant funding. `HB-ORG-14 Compliance, Financial Crime and Conduct` provides independent fraud and conduct oversight, while `HB-ORG-12 Finance, Accounting, Tax and Reporting` owns accounting and financial control. Issuer and acquirer profit accountability remains a recorded organisational gap.

No new diagram source is required in this drafting pass. A later visual must follow the specification-first approval workflow.

## Worked examples

- Horizon Bank card purchase from authorisation through a later dispute.
- Horizon Bank merchant onboarding and funding lifecycle.

## Source requirements

Card-data-security claims use official PCI Security Standards Council material. Banking Industry Architecture Network (BIAN) claims use the governed BIAN 14.0 note. Scheme membership, transaction rules, deadlines and legal duties remain unverified Horizon Bank assumptions.

## What is the card and acquiring domain?

The governed Level 1 domain is `HB-DOM-060 Cards and Merchant Acquiring`. It supports three separate product records:

| Product | Customer or consumer | Principal concern |
|---|---|---|
| `HB-PRD-11 Card Issuing` | Retail, small and medium-sized enterprise (SME), and corporate cardholders | Card and credential lifecycle |
| `HB-PRD-12 Merchant Acquiring` | SME and corporate merchants | Acceptance, acquiring and merchant funding |
| `HB-PRD-13 Card Processing Services` | Internal or shared processing consumers | Authorisation, switching, clearing and settlement preparation |

All three belong to the Level 1 family `HB-PRD-08 Cards and Merchant Services`. The hierarchy matters. Issuing and acquiring have different customers, agreements and accountable owners. Processing can be shared and may have no direct customer-segment applicability.

The Level 1 capability `HB-CAP-060 Card and Merchant-Acquiring Management` and process `HB-PROC-08 Issue, Process and Acquire Cards` connect the family. They do not claim that one team or platform performs every activity.

## Issuing and credential lifecycle

Issuing establishes and services the cardholder relationship. `HB-CAP-061 Card Issuing` covers approval and fulfilment. `HB-CAP-062 Card and Credential Lifecycle Management` covers activation, controls, replacement, renewal, suspension and closure. `HB-PROC-124 Issue and Service Cards and Credentials` describes their lifecycle.

`HB-APP-040 Card Issuing Management` is authoritative for the issuer-managed card status, controls and cardholder relationship through `HB-SOR-10 Card Product and Credential Authority`. It references credentials and tokens but is not automatically the authority for authentication secrets or network token details. A card can also be linked to a deposit account or credit account whose balance authority remains outside this application.

A physical card and a virtual card are different presentations of a governed credential relationship. The model should record form, status, effective dates and permitted uses without assuming that the physical card number, virtual credential and token are one value. A personal identification number (PIN) has its own secure lifecycle for creation, delivery or selection, retry control, reset and block. It must not be stored as ordinary card data or copied into servicing applications.

Tokenisation replaces a sensitive account reference in a defined context with a token whose mapping and lifecycle have a separate authority. Provisioning, suspension, replacement and deletion must therefore link the token to the issuer decision without exposing the underlying value. Horizon Bank has not yet catalogued the token or PIN authority, so solution designs must retain this as a gap rather than assign it to `HB-APP-040` by default.

Activation, renewal, replacement, temporary block, permanent closure and compromised-credential response are distinct transitions. Closing a credential does not automatically close the linked deposit or credit account, and replacing a physical card need not end every valid token. A state model should show these relationships explicitly.

The mobile channel uses `HB-INT-031 Card Servicing for Mobile`. That interface should disclose only the information and actions needed for the journey. It is not an invitation to copy the entire issuer record into the mobile application.

## Authorisation is a decision, not settlement

When a transaction arrives, `HB-APP-041 Card Authorisation` evaluates issuer controls, account or credit availability and applicable limits. `HB-APP-043 Card Fraud Decisioning` supplies a governed fraud decision through `HB-INT-044 Card Fraud Decision`. The processing exchange uses `HB-INT-042 Card Authorisation Message` across `HB-EXT-006 Card Scheme Network`.

For e-commerce, strong customer authentication (SCA) and 3-D Secure (3DS) are jurisdiction- or scheme-dependent examples of additional authentication and data exchange. They are not universal approval steps. A design must state who requested authentication, which credential or token was presented, what result and exemption evidence was returned, and whether the issuer still authorised the transaction. The current interface catalogue has no separate 3DS contract, so that interaction remains pending.

`HB-CTRL-18 Card Authorisation and Fraud Decision` requires the request, card and account state, rule or model version, outcome and reason to remain traceable. An approval reserves or permits activity under issuer policy. It does not prove that a later clearing presentment will arrive or that settlement has completed.

Stand-in processing illustrates why boundaries matter. A network or processor might respond when the issuer is unavailable, but only under an approved policy covering authority, limits, evidence and reconciliation. `HB-CRIT-06 Authorise and Control Card Activity` leaves those decisions pending rather than implying that availability always overrides control.

## Processing, presentment, clearing and settlement

`HB-APP-042 Card Processing and Clearing` switches messages and records presentments, clearing adjustments and settlement preparation. Its capabilities are `HB-CAP-063 Card Authorisation`, `HB-CAP-064 Card Transaction Processing` and `HB-CAP-065 Card Clearing and Settlement`. The Level 2 process is `HB-PROC-125 Authorise, Process and Settle Card Transactions`.

The lifecycle commonly includes an authorisation request and response, optional reversal, later presentment, clearing, settlement and issuer or merchant posting. Actual message profiles and deadlines depend on the selected scheme and agreement. The Horizon model does not invent them.

`HB-SOR-11 Card Authorisation and Clearing Authority` deliberately splits authority. `HB-APP-041` owns issuer decisions, while `HB-APP-042` owns accepted clearing items. External scheme records still require reconciliation. `HB-REC-017 Card Authorisation to Presentment` exposes approved authorisations without matching presentments, presentments without expected authorisations, duplicates and timing differences. `HB-REC-018 Card Clearing and Settlement` compares scheme positions with issuer, acquirer, merchant and finance postings.

`HB-ACC-17 Issuer Card Purchase Cleared` represents the accounting consequence for a cleared purchase, withdrawal, refund or reversal. It does not hard-code whether the customer side is a deposit posting or receivable. That depends on the card and account product.

## Billing, statements and revolving credit

A debit-card purchase normally affects a linked deposit account under its own balance authority. A credit-card purchase can instead increase a receivable that is later billed. Billing groups cleared activity, adjustments, fees, interest and payments into a governed statement period. A statement is evidence of the period and presentation, not the only transaction record.

`HB-APP-022 Statement and Correspondence Management` can compose and retain a card statement, but the catalogue does not yet assign a dedicated credit-card receivable, billing-cycle or minimum-payment authority. That gap prevents this chapter from pretending `HB-APP-040` is a complete credit-card ledger.

Where revolving credit is offered, the architecture needs statement balance, minimum payment, due date, payment allocation, grace treatment, interest calculation, fees, delinquency and correction rules. Each must be effective-dated and linked to the agreement and applicable accounting policy. Rewards are another liability and fulfilment lifecycle: earn, pending, available, redeemed, expired and reversed should not be inferred from transaction status alone. Horizon Bank currently has no governed rewards application or accounting event, so rewards remain a product and catalogue gap.

## Fraud, customer claims and disputes

Fraud monitoring and dispute processing overlap but are not the same. `HB-CAP-066 Card Fraud Management` detects and decides suspicious activity. It can block or challenge a transaction and create an alert. `HB-CAP-067 Card Dispute and Chargeback Management` manages a claim after the cardholder or merchant contests an outcome.

`HB-PROC-126 Prevent Fraud and Resolve Card Disputes` connects the work while retaining distinct evidence. `HB-INT-045 Card Fraud Case Handover` creates a dispute or investigation case in `HB-APP-044 Card Disputes and Chargebacks`. The case records evidence, deadlines, representment and disposition. The card-processing record remains the transaction authority.

`HB-CTRL-19 Card Clearing, Dispute and Chargeback Control` links unmatched presentments, case stages, evidence, deadlines and financial adjustments. `HB-REC-019 Card Dispute and Chargeback` checks that the internal case, external scheme state and financial effects agree. `HB-ACC-19 Card Dispute or Chargeback Adjusted` records the governed adjustment, but provisional credit, liability and write-off rules remain pending.

A case state model is useful here. Candidate states might include received, evidence pending, submitted, represented, decided, adjusted and closed. These names must be aligned to the chosen scheme before becoming controlled values.

## Merchant acquiring is a separate lifecycle

Merchant acquiring begins before a purchase. `HB-CAP-068 Merchant Onboarding and Servicing` covers due diligence, contract, outlet and acceptance configuration. `HB-CAP-069 Merchant Acceptance and Settlement` covers acquired transactions, merchant proceeds and settlement. `HB-PROC-127 Onboard, Service and Settle Merchants` connects both.

`HB-APP-045 Merchant Acquiring Management` owns merchant agreements, pricing, reserves, service state and funding instructions. `HB-APP-046 Merchant Transaction Gateway` accepts merchant messages, minimises sensitive data and routes authorisation traffic. The gateway is a processor, not the final authority for every acquired transaction or merchant balance.

A merchant can have several outlets, terminals and e-commerce acceptance points. Terminal identity, configuration, keys, software state and ownership require an asset and security boundary distinct from the merchant agreement. The catalogue records that boundary as pending. Merchant onboarding must also govern settlement account, pricing, reserve, accepted transaction types and restricted uses before activity is released.

`HB-INT-046 Merchant Transaction Submission` transfers accepted activity into acquiring management. `HB-INT-104 Merchant Acceptance Network Exchange` represents the logical merchant-side boundary. `HB-INT-070 Card Clearing and Acquiring Exchange` carries acquiring authorisations, presentments and settlement information through the logical card network.

`HB-SOR-12 Merchant and Acquiring Authority` separates merchant configuration, accepted messages and reconciled settlement. `HB-REC-020 Merchant Funding and Acquiring Settlement` compares acquired transactions, pricing, fees, reserves, refunds and chargebacks with merchant funding. `HB-ACC-18 Merchant Settlement Payable Recognised` records the payable only under approved funding and accounting rules.

Interchange, scheme fees, acquirer charges and merchant service fees are different economic items even when one net amount is funded. Their payer, beneficiary, basis, timing, tax and reversal treatment depend on the applicable agreements and network. `HB-ACC-18` leaves interchange and tax rules pending, so a solution must preserve gross components and not treat an unexplained net settlement as sufficient accounting evidence.

## Information and security boundaries

`HB-DATA-09 Cards and Merchant Acquiring` covers card product, credential reference, authorisation, presentment, dispute, merchant, reserve and funding information. It is related to, but distinct from, `HB-DATA-03 Account and Transaction`, `HB-DATA-05 Finance and Accounting` and `HB-DATA-06 Case, Document and Evidence`.

The Payment Card Industry Data Security Standard (PCI DSS) provides technical and operational requirements intended to protect payment account data. Its stated audience includes merchants, processors, acquirers, issuers and service providers in scope [PCI-DSS-4.0.1]. An architecture review should therefore show where relevant account data is stored, processed or transmitted and which parties can affect its security. A catalogue relationship is not evidence of compliance, and applicability must be assessed for the real implementation.

Token references can reduce unnecessary exposure, but the token, underlying account data and mapping have different authorities. The Horizon catalogue intentionally leaves token authority pending. A diagram that labels every protected value `card number` would conceal that distinction.

## Controls and resilience

Three controls form the chapter's minimum chain:

- `HB-CTRL-18` protects authorisation and fraud decisions.
- `HB-CTRL-19` governs clearing, disputes and chargebacks.
- `HB-CTRL-20 Merchant Onboarding, Acceptance and Funding Control` protects merchant approval, configuration, reserves and funding.

`HB-TECH-011 Card Issuing and Processing Classification` and `HB-TECH-012 Merchant Acquiring Classification` keep recovery concerns separate. Issuer authorisation may require a tightly controlled real-time response. Merchant funding can be delayed rather than estimated when clearing evidence is incomplete, subject to approved treatment. Both require complete replay, duplicate and reconciliation design.

`HB-CRIT-07 Process Card Clearing and Merchant Funding` defines the business outcome, not a recovery target. Scheme calendars, exception capacity, impact tolerance, Recovery Time Objective (RTO) and Recovery Point Objective (RPO) remain gaps. A realistic design records those missing decisions instead of assigning unsupported numbers.

## BIAN alignment and model selection

The current BIAN mapping register has no controlled card or merchant-acquiring candidate. That is a governed gap requiring integration-owner action. This chapter does not invent exact BIAN 14.0 Service Domains from memory. Any future mapping must record source, confidence, verification status and a many-to-many rationale.

Use different models for different questions:

| Model | Card question answered |
|---|---|
| Product hierarchy | Which issuing, processing and acquiring offers are distinct? |
| Capability map | Which abilities need accountable owners? |
| Sequence view | What happens during the time-sensitive authorisation? |
| State machine | Which card, transaction or dispute transitions are permitted? |
| Data-flow view | Where does protected payment account data cross boundaries? |
| Reconciliation matrix | Which issuer, scheme, acquirer and merchant populations must agree? |
| Resilience view | What can degrade safely and what evidence must be restored? |

Do not combine these into one unreadable diagram. No diagram source is created in this pass.

## Worked traceability: purchase and later dispute

`HB-SCN-10 Authorise, Clear and Dispute a Card Purchase` begins when a cardholder presents an active tokenised credential to an e-commerce merchant. The merchant acceptance point sends the request through `HB-APP-046` and `HB-INT-070` to `HB-APP-042`, which uses `HB-INT-042` with `HB-APP-041`. Any applicable SCA or 3DS result is linked as pending external authentication evidence because no dedicated interface is registered. `HB-APP-043` supplies the fraud result over `HB-INT-044`. The issuer response is approved or declined with reasons and evidence.

If approved activity is later presented, `HB-APP-042` records clearing state and `HB-REC-017` matches it to the authorisation. Settlement and customer posting create the `HB-ACC-17` consequence and are checked by `HB-REC-018`. A later claim transfers through `HB-INT-045` to `HB-APP-044`; the scheme exchange uses `HB-INT-071 Card Dispute Network File`. `HB-ACC-19` applies only after the governed case decision.

The scenario exposes, rather than conceals, the pending scheme rules for token data, stand-in authority, late presentment, deadlines and provisional credit.

## Current-to-target considerations

The principal issuing, authorisation, processing, fraud, dispute and acquiring applications are current. The target need is therefore clearer authority and controlled interfaces, not automatic platform replacement.

A defensible transition first identifies credential, token, card-account, merchant, terminal and transaction authorities. It then versions scheme adapters, separates card decisions from dispute cases, proves authorisation-to-presentment and settlement reconciliations, and introduces missing billing or rewards responsibilities only where the product scope requires them. Processor or scheme migration needs parallel message comparison, stand-in and cut-over authority, open-dispute retention and merchant-funding rollback. Token migration must not strand an active credential or expose the underlying account data.

## When should this model set be used?

Use it for issuer or acquirer platform change, processor sourcing, fraud redesign, payment-data scope assessment, dispute improvement, merchant-funding control and recovery planning. It is also useful when teams disagree about which application owns transaction status.

Do not use it as a scheme certification plan, detailed message specification, PCI DSS assessment, merchant contract or accounting policy. Those require authoritative implementation evidence.

## Common mistakes

- Calling issuing, processing and acquiring one product.
- Treating authorisation as clearing or settlement.
- Assuming the network owns the bank's internal customer balance.
- Putting fraud alerts and dispute cases in the transaction record without separate lifecycle authority.
- Funding merchants from estimated data without an approved hold and reconciliation policy.
- Copying protected account data into channels and case tools unnecessarily.
- Assuming a card scheme, processor, BIAN Service Domain, application and microservice are the same boundary.
- Ignoring reversals, partial presentments, late items, chargebacks and negative merchant funding.

## Key takeaways

- Card issuing, card processing and merchant acquiring have different owners and customers.
- Authorisation is a decision before later clearing and settlement states.
- Fraud decisions and dispute cases require linked but separate evidence.
- Merchant funding depends on governed acquiring, pricing, reserve and reconciliation data.
- Security scope follows data and service influence, not application labels.
- Resilience decisions must preserve safe authorisation, clearing and funding outcomes.
- Exact BIAN 14.0 card mappings remain a controlled gap.

## Practical exercise

Create three swimlanes for issuer, shared processing and acquirer responsibilities. Add a fourth lane for the logical card network. Place authorisation, reversal, presentment, settlement, dispute and merchant funding in the lane that owns each state. Then add the authoritative application and reconciliation ID.

**Suggested review criteria:** The result must use `HB-APP-040` to `HB-APP-046` where applicable, show that authorisation is not settlement, distinguish customer and merchant adjustments, and label scheme rules as pending.

## Review checklist

- [x] Issuing, processing and acquiring are separate products and responsibilities.
- [x] Fraud, disputes, clearing and merchant funding are explicit.
- [x] Data authorities, accounting events and reconciliations use governed IDs.
- [x] Security and resilience limitations are stated.
- [x] Scheme participation and deadlines are not fabricated.
- [ ] Add governed BIAN 14.0 candidates for cards and acquiring after verification.
- [ ] Diagram production remains deferred pending author-approved specifications.

## References and further reading

- [BIAN-SERVICE-LANDSCAPE-14]
- [CPMI-PAYMENT-GLOSSARY-2016]
- [PCI-DSS-4.0.1]

## Drafting notes

- Before formal review, verify scheme-specific lifecycles, PCI DSS applicability and exact BIAN 14.0 mappings for the selected legal entities.
