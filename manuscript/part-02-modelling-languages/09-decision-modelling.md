---
title: "Decision Modelling and DMN"
chapter: 9
part: "part-02-modelling-languages"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-06-30"
---

# 9. Decision Modelling and DMN

## Chapter purpose

Show how business decisions and rules can be separated from process flow and modelled transparently.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain why repeatable business decisions should often be modelled separately from process flow.
- Read a simple decision table, decision tree and Decision Model and Notation (DMN) decision requirements view.
- Distinguish a business rule, a decision, input data, a business knowledge model and a process task.
- Explain the role of hit policies in decision tables.
- Decide when to use DMN with Business Process Model and Notation (BPMN).
- Apply decision modelling to a simple product eligibility example and Horizon Bank credit or payment examples.
- Avoid common decision modelling mistakes, especially hiding process sequence inside decision logic.

## Prerequisites and dependencies

- Chapter 8: Data Modelling

## Required models and artefacts

- Decision table, planned, specification pending.
- Decision tree, planned, specification pending.
- DMN Decision Requirements Diagram (DRD), planned, specification pending.

## Worked examples

- Product eligibility
- Credit approval
- Payment routing

## Source requirements

- `[OMG-DMN-1.5]` is the current formal Object Management Group source for Decision Model and Notation (DMN) terminology and notation.
- OMG currently lists later beta material, but beta material is informational and not the formal compliance baseline for this chapter.
- Chapter guidance must distinguish official DMN terminology from the author's practical beginner recommendations.
- Diagrams and examples must be original teaching material and must not reproduce OMG specification diagrams.

## Planned chapter structure

## Why model decisions separately

Decision modelling answers: **what rule-based or judgement-based decision must be made, what information does it need and how is the answer derived?**

Processes and decisions are related, but they are not the same thing. A process model shows the order of work: receive an application, check identity, assess eligibility, notify the customer. A decision model shows the logic used at a decision point: is the customer eligible, which product terms apply, should the payment be routed normally or referred for review?

Separating them helps beginners avoid crowded diagrams. If a BPMN model contains every policy threshold, exception condition and scoring rule, the process becomes hard to read. If a decision model contains every human task and hand-off, the decision logic becomes hard to govern. The practical rule is simple: use process models for flow and responsibility, and use decision models for repeatable logic.

Decision modelling is useful when the organisation needs transparency. A team can review why an order is eligible for free delivery, why a loan application needs manual review, or why a payment instruction is routed to enhanced screening. The model does not remove accountability. It makes the logic visible enough for business, risk, compliance and technology people to discuss.

In the Simple Online Store, a decision might determine whether an order qualifies for express delivery. In Horizon Bank, a decision might determine whether a payment can proceed, needs repair, needs financial-crime review or must be rejected.

## Decision tables

A decision table answers: **which output applies for a combination of input conditions?**

It is a table of rules. Columns usually describe inputs, conditions and outputs. Rows describe rule cases. For example, an online store might decide delivery option from order value, product availability and destination region.

| Order value | All items in stock? | Destination | Delivery decision |
|---|---|---|---|
| GBP 50 or more | Yes | Domestic | Offer free standard delivery |
| Any value | Yes | Domestic | Offer paid standard delivery |
| Any value | No | Any | Wait for stock or split shipment |
| Any value | Yes | International | Offer international delivery quote |

The table is easy to review because each rule is visible. A business stakeholder can ask whether the GBP 50 threshold is correct. A tester can derive test cases. A developer can implement the logic without discovering the rules from scattered prose.

Decision tables are especially useful when the decision depends on several inputs and must be explainable. They are less useful when the real issue is a long sequence of activities, negotiation, exception handling or human investigation. In those cases, use a process model for the flow and a decision table only for the repeatable decision inside the flow.

For Horizon Bank, a payment routing decision table might use amount band, currency, screening result, account status and cut-off time to decide whether the payment proceeds, waits for repair, routes to manual review or is rejected. The table should not describe the operational steps taken after that outcome. Those steps belong in BPMN or another process view.

## Decision trees

A decision tree answers: **which path through a set of questions leads to a decision?**

It represents the logic as a branching sequence. Each branch asks a question or checks a condition. Each leaf gives an outcome. A tree can be easier than a table when the decision has a natural order, such as "is the customer known?", then "is identity verified?", then "is the product available in this jurisdiction?"

For a beginner, the main benefit of a decision tree is readability. It can show the story of the decision. The main risk is that a tree can hide duplicated or inconsistent logic when it grows large. If several branches repeat the same condition, a decision table or DMN model may be easier to govern.

A simple online-store eligibility tree might first ask whether the basket contains restricted products. If yes, it checks destination restrictions. If no, it checks stock availability. The outcome may be "eligible", "eligible with restricted delivery" or "not eligible".

In Horizon Bank, a first-pass credit decision tree might ask whether mandatory customer information is complete, whether identity verification passed, whether affordability checks pass and whether the requested product is available to that customer segment. This is a teaching example, not a credit-risk policy. Real banking decisions require governed policy, validation, audit and regulatory review.

## Introduction to DMN

Decision Model and Notation (DMN) answers: **how can a business decision be modelled with standard concepts for decision requirements and decision logic?**

DMN is an Object Management Group standard for modelling repeatable business decisions [OMG-DMN-1.5]. The current formal version used by this chapter is DMN 1.5. OMG also lists later beta material, but the beta material is informational rather than the formal compliance baseline for this book.

In plain language, DMN gives teams a standard way to separate decision logic from process flow. A BPMN task may say "Assess application". A DMN model can show which decision is being made, which input data it needs, which supporting knowledge it uses and, where appropriate, the decision table or expression that produces the result.

DMN is most useful when the decision is repeatable, reviewable and important enough to govern. Product eligibility, pricing rules, routing choices, risk bands, benefit entitlement and policy decisions are common examples. It is less useful for one-off expert judgement, creative design choices or informal conversations where the rules are not stable enough to model.

This chapter uses DMN as a beginner architecture technique. It does not teach every DMN expression feature. The goal is to help readers understand what belongs in a decision model, how it relates to BPMN, and how to review it critically.

## Decision Requirements Diagrams

A Decision Requirements Diagram (DRD) answers: **which decisions depend on which other decisions, input data and knowledge?**

In DMN, a decision requirements view can show the dependencies around a decision. The useful beginner elements are:

| Element | Plain meaning | Example |
|---|---|---|
| Decision | A question that produces an answer | Determine payment route |
| Input data | Information supplied to the decision | Payment amount, currency, customer risk rating |
| Business knowledge model | Reusable decision logic or function | Payment routing rules |
| Knowledge source | Authority for the logic | Payments policy, sanctions screening policy |

The diagram should not be used as a process sequence. It does not show which team performs work first or how long a task waits. It shows logical dependency: this decision needs this input, this decision uses this reusable knowledge, and this policy authority shapes the model.

For Horizon Bank, a DRD for payment routing might show `Determine Payment Route` depending on `Payment Instruction`, `Account Status`, `Screening Result` and `Payment Cut-Off Status`. It might use a business knowledge model called `Payment Routing Rules` and cite a knowledge source called `Payments Operations Policy`.

The DRD helps a review meeting ask better questions. Are all required inputs available at the point of decision? Is the policy authority known? Are reused rules named once instead of copied into several places? Does the process call the decision at the right time?

## Inputs, decisions and knowledge models

Inputs, decisions and knowledge models answer: **what information is known, what answer is needed and what reusable logic supports it?**

An **input data** element represents information supplied to the decision. It might be an order value, customer segment, payment amount, country, account status or identity verification result.

A **decision** represents a question that produces an output. Good decision names are phrased around the answer being produced, such as `Determine delivery option`, `Assess product eligibility` or `Determine payment route`.

A **business knowledge model** represents reusable decision logic. It may contain a decision table, formula or other expression. Use it when the same logic is shared, or when naming the logic separately makes governance clearer.

A **knowledge source** represents an authority behind the decision logic. It might be a policy, regulation, product rulebook, risk appetite statement or operations standard. This matters because decision logic often changes when policy changes. A model that names the authority is easier to govern than one that hides the policy inside code or prose.

Keep the modelling level consistent. Do not mix raw database columns, senior policy goals and low-level implementation functions unless the view explains why. A beginner DRD should usually show business-level inputs and decisions first, then leave implementation mapping to later design work.

## Hit policies

A hit policy answers: **what should happen when one or more decision-table rules match the same inputs?**

This is important because a decision table may have overlapping rules. If a payment is both high value and international, more than one rule might apply. The model must state whether only one rule is expected to match, whether the first matching rule wins, whether several outputs are collected, or whether matching several rules is an error.

DMN defines formal hit-policy notation for decision tables [OMG-DMN-1.5]. For beginner architecture work, the most important lesson is not to leave the policy implicit. Reviewers should be able to see whether the table expects a single result or allows multiple applicable rules.

For example:

| Situation | Practical hit-policy concern |
|---|---|
| Product eligibility | Usually one clear eligibility outcome should be produced. |
| Discount selection | The table may need to choose the highest, first or combined discount, depending on policy. |
| Payment routing | More than one risk flag may apply, so the model must say how conflicts are resolved. |

If the hit policy is unclear, the implementation may behave differently from the business expectation. One system may stop at the first rule. Another may apply the strictest rule. A third may combine results. The decision model should remove that ambiguity before implementation.

## DMN with BPMN

DMN with BPMN answers: **where does process flow call decision logic, and what happens with the result?**

BPMN is useful for activities, participants, events, gateways, messages and exceptions. DMN is useful for repeatable decision logic. They work well together when the process needs a decision result but should not carry all the rule detail inside the process diagram.

A BPMN process might include a business rule task called `Determine Payment Route`. That task can refer to a DMN decision model. The process then uses the output, such as `Proceed`, `Repair`, `Manual Review` or `Reject`, to choose the next process path.

This separation keeps both models readable. The BPMN model shows who does the work and what happens next. The DMN model shows how the decision result is derived. Reviewers can inspect process ownership separately from decision logic.

The common mistake is to duplicate the same decision in both places. If the BPMN gateway says "amount over GBP 10,000 and non-domestic and customer high risk", while the DMN table says something slightly different, the architecture now has two competing sources of truth. Prefer a gateway that branches on the named decision result, not on a copied version of the full rule logic.

## Decision governance

Decision governance answers: **who owns the decision logic, how is it changed and how can it be audited?**

Decision models often sit between business policy and software implementation. That makes ownership important. A product owner may own commercial eligibility rules. A risk team may own risk scoring policy. Operations may own routing thresholds. Compliance may own controls that must not be changed without review.

Good governance records:

- The decision name and purpose.
- The policy or knowledge source behind it.
- The owner who can approve changes.
- The inputs required and where they come from.
- The output values and their meaning.
- The tests or examples used to validate the model.
- The implementation or service that executes the decision, if any.

For Horizon Bank, a payment routing decision should have traceability from policy to model to implementation and test cases. If the cut-off time changes, the team should know which decision table, process path, API contract and operational procedure are affected.

Governance should be proportionate. A small internal reporting filter may not need a formal DMN model. A credit, fraud, payment, pricing or eligibility decision that affects customers, risk or compliance usually deserves stronger traceability.

## Common mistakes

The first mistake is hiding decision logic inside a process diagram. The process becomes unreadable and the rules become hard to govern.

The second mistake is modelling every judgement as if it were a stable rule. Some decisions rely on expert assessment, negotiation or incomplete evidence. Those may need guidance and audit trails rather than a rigid decision table.

The third mistake is leaving hit policies implicit. If several rules can match, the table must say how the result is chosen or combined.

The fourth mistake is copying the same rules into BPMN gateways, code, spreadsheets and policy documents without traceability. Duplicate rules drift apart.

The fifth mistake is naming inputs too technically too early. A decision model for business review should usually say `Customer risk rating`, not `cust_rsk_cd`, unless the purpose is implementation mapping.

The sixth mistake is ignoring data availability. A decision may require an input that the process does not yet have. The DRD and BPMN model should agree on when the input becomes available.

The seventh mistake is treating DMN as only an automation tool. DMN can support automation, but it is also useful as a communication, review and governance technique.

## Chapter cheat sheet

| Technique | Question answered | Useful for | Watch out for |
|---|---|---|---|
| Decision table | Which output applies for these input conditions? | Explainable rules and test cases | Unclear hit policy or duplicated rules |
| Decision tree | Which path through questions leads to the outcome? | Branching logic that has a natural order | Large trees with repeated conditions |
| DMN DRD | Which decisions depend on which inputs and knowledge? | Decision dependencies and governance | Treating it as process sequence |
| Business knowledge model | Which reusable logic supports decisions? | Shared or governed rule logic | Hiding unclear policy behind a formal box |
| Knowledge source | Which authority shapes the logic? | Policy and compliance traceability | Citing vague or outdated sources |
| BPMN plus DMN | Where does a process call a decision? | Separating flow from rule logic | Duplicating rules in gateways and tables |

## Key takeaways

- Decision models explain repeatable decision logic; process models explain flow and responsibility.
- Decision tables make rules reviewable, testable and easier to govern.
- Decision trees are useful for ordered branching logic but can become difficult to maintain when they grow.
- DMN provides standard concepts for decisions, input data, business knowledge models, knowledge sources and decision requirements.
- A DRD shows decision dependencies, not process sequence.
- Hit policies must be explicit when more than one rule might match.
- BPMN and DMN work well together when process tasks call governed decision logic.
- Decision governance connects policy, ownership, inputs, outputs, tests and implementation.

## Practical exercise

Horizon Bank wants to decide how to route an outgoing payment instruction. The routing outcome can be `Proceed`, `Repair`, `Manual Review` or `Reject`. The available inputs are payment amount, currency, account status, screening result and cut-off-time status.

Before drawing, choose the right model for each question:

1. Which model would show the rules that map input conditions to the routing outcome?
2. Which model would show that `Determine Payment Route` depends on account status, screening result and cut-off-time status?
3. Which model would show the operational steps after the routing outcome is known?
4. What must be stated if two routing rules could match the same payment?
5. Which detail should be excluded from the first business-level decision model?

Suggested answer:

- Use a decision table for the routing rules.
- Use a DMN DRD to show decision dependencies and policy knowledge sources.
- Use BPMN for operational steps after the decision result.
- State the hit policy so rule conflicts are resolved deliberately.
- Exclude low-level database column names, user-interface screens, network routing and detailed exception handling from the first business-level decision model.

## Review checklist

- [ ] The question answered by each model is explicit.
- [ ] The audience and abstraction level are clear.
- [ ] Formal terms are introduced after a plain-language explanation.
- [ ] The simple and banking examples are consistent with repository example files.
- [ ] Comparisons do not imply that one notation is universally superior.
- [ ] Common mistakes are concrete and actionable.
- [ ] Required sources and diagrams are registered.
- [ ] Terminology, link and word-count checks pass.

## Drafting notes

- Target length: 2,000 to 4,000 words unless the chapter scope justifies more.
- Keep this file as the canonical manuscript source for the chapter.
- Do not mark this chapter `Approved` without explicit author approval.
