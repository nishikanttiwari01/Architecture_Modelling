---
title: "Modelling Business Strategy and Capabilities"
chapter: 14
part: "part-03-diagram-selection"
status: "Drafting"
author: "Nishikant Tiwari"
last_updated: "2026-07-03"
---

# 14. Modelling Business Strategy and Capabilities

## Chapter purpose

Show how to choose and combine models that connect business strategy to the stable abilities an organisation needs. Part II introduced the notations. This chapter, the first in Part III, helps a reader select the right model when the architecture question is about goals, stakeholders, capabilities, value and investment, rather than software structure or runtime behaviour.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain goals, drivers, outcomes, stakeholders and concerns in plain language and say which model records each one.
- Read a capability map and explain why a capability is not a process, an organisation unit, an application or a project.
- Cross-map a value stream to the capabilities that enable it.
- Use a heat map to turn a stable capability structure into an explicit investment question.
- Trace a strategic goal through a capability to a change initiative, and explain why that thread matters.
- Select and combine strategy and capability models for a realistic situation, and review them critically.
- Apply the techniques to the Simple Online Store and to Horizon Bank.

## Prerequisites and dependencies

- Chapter 2: Model, View and Viewpoint
- Chapter 3: How to Read Architecture Diagrams
- Chapter 7: ArchiMate
- Chapter 13: Other Useful Modelling Approaches

## Required models and artefacts

- FIG-14-01: Horizon Bank Strategy-to-Capability Traceability View. Specification registered; source pending author approval before production.
- FIG-14-02: Horizon Bank Onboarding Value Stream to Capability Cross-Map. Specification registered; source pending author approval before production.
- Reused from Chapter 13 for reference: FIG-13-02 customer onboarding value stream and FIG-13-05 capability heat map.
- Reused from Chapter 7 for reference: FIG-07-01 capability map and FIG-07-05 motivation view.

## Worked examples

- Simple Online Store strategy for a single goal, its enabling capabilities and one initiative.
- Horizon Bank onboarding and payments strategy traced from drivers and goals through capabilities and a value stream to two change initiatives.

## Source requirements

- `[OPEN-GROUP-ARCHIMATE-4]` supports the motivation and strategy concepts, including stakeholder, driver, assessment, goal, outcome, principle, requirement, capability, resource, value stream and course of action.
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]` supports capability-map and value-stream practice as business architecture elements used for planning.
- `[ISO-42010]` supports the stakeholder and concern vocabulary reused from Chapter 2.
- The Horizon Bank capability names are controlled in `examples/horizon-bank/capabilities.md`. The Simple Online Store names are controlled in `examples/simple-online-store/README.md`.

## Why this chapter exists

Chapter 13 introduced capability maps, value streams, heat maps and Wardley maps as part of a wider modelling toolkit, and it deliberately kept each one at an introductory level. This chapter answers a different, more practical question: when the discussion is about strategy and capability, which model should you reach for, and how do these models fit together?

Strategy models are easy to get wrong. A team draws a colourful capability map, a value stream and a heat map, but nobody can say which goal the pictures serve or which project they justify. The models look like business architecture, yet they do not change a decision. The discipline in this chapter is to keep a visible thread from why the organisation wants to change, through what it must be able to do, to what it will actually fund.

The thread has a consistent shape. A driver or a stakeholder concern raises a goal. The goal names a measurable outcome. The outcome depends on one or more capabilities improving. A value stream shows where those capabilities create value for a stakeholder. A heat map exposes where attention and money should go. An initiative is the change that lifts the chosen capabilities. Traceability keeps each link navigable so a reviewer can challenge it.

## Planned chapter structure

The chapter follows that thread. It starts with goals, drivers and outcomes, then the stakeholders and concerns that anchor them. It then treats capability maps and value streams as planning tools, uses heat maps to frame the investment question, and connects the whole chain to change initiatives. It closes with recommended notation combinations, a selection table, a Horizon Bank worked example, common mistakes and the usual chapter endings.

## Goals, drivers and outcomes

This section answers: **how do you record why an architecture needs to change, in a form precise enough to steer design?**

Strategy work often begins with vague ambition, such as "be more digital" or "reduce risk". A motivation model turns that ambition into named elements that can be traced and reviewed. ArchiMate calls these motivation elements, and the most useful ones for a beginner are the driver, the assessment, the goal, the outcome, the principle and the requirement [OPEN-GROUP-ARCHIMATE-4].

> **Driver:** An external or internal force that creates a need to change, such as a regulatory expectation, a cost pressure or a competitor move.
>
> **Assessment:** A judgement about a driver, usually the result of analysis, such as "onboarding takes too long and customers drop out".
>
> **Goal:** A stated intention, such as "reduce time to usable banking services".
>
> **Outcome:** A measurable end state that shows the goal is met, such as "median onboarding time reduced against the current baseline".
>
> **Principle:** A general rule that constrains many decisions, such as "prefer governed reuse over point-to-point integration".
>
> **Requirement:** A specific need that a design must satisfy, such as "publish governed payment-status events for approved consumers".

The distinction that beginners miss most often is goal versus outcome. A goal is an intention. An outcome is the observable result you would measure. Keeping them separate stops a model from claiming success it cannot demonstrate. A second common slip is treating an assessment as a solution. "We need a new onboarding platform" is not an assessment; it is a decision that should come later, after the driver, assessment, goal and outcome are clear.

ArchiMate 4 removed the separate `Constraint` element that appeared in earlier versions, so this book does not use `Constraint` as current notation. Where a limit matters, express it as a principle, a requirement, an outcome target or plain prose [OPEN-GROUP-ARCHIMATE-4].

For the Simple Online Store, a small motivation chain is enough. A driver is rising customer expectation for a trustworthy checkout. The assessment is that storing card data raises avoidable risk. The goal is to remove card-data handling from the store. The outcome is that no full card details are stored in the Online Store. This single chain is already enough to justify delegating payment capture to the Payment Provider System, a decision the book uses from Chapter 4 onward.

Horizon Bank needs a broader set. The following drivers, assessments, goals and outcomes anchor the rest of the chapter.

| Driver | Assessment | Goal | Target outcome |
|---|---|---|---|
| Customer expectation for fast account access | Onboarding is slow and drops applicants | Reduce time to usable banking services | Median onboarding time reduced against baseline |
| Regulatory scrutiny of financial crime | Screening decisions are hard to evidence | Strengthen screening traceability | Every screening decision has retained evidence |
| Cost of legacy integration | Point-to-point links raise reconciliation effort | Reduce integration cost and fragility | Fewer bespoke point-to-point interfaces in scope |
| Competition from digital-first banks | Payment status visibility is poor | Improve payment transparency | Payment status available in near real time |

## Stakeholder concerns

This section answers: **whose interests decide whether a strategy model is any good?**

Chapter 2 introduced stakeholders and concerns from the architecture-description vocabulary, where a concern is an interest a description should address for a stakeholder [ISO-42010]. Strategy modelling makes that idea concrete. Every goal in the previous section belongs to someone, and every capability decision affects someone. If a capability map or value stream cannot be traced to a stakeholder concern, it is decoration.

A short stakeholder-and-concern table is often the most valuable page in a strategy pack, because it decides which views are worth drawing. Horizon Bank's relevant stakeholders come from the controlled actor list in `examples/horizon-bank/actors.md`.

| Stakeholder | Primary concern | Model that addresses it |
|---|---|---|
| Sponsor and executive | Is the investment justified by strategic value? | Goals, outcomes and capability investment heat map |
| Relationship Manager | Can customers be onboarded quickly and well? | Onboarding value stream and enabling capabilities |
| Compliance Officer | Is screening effective and evidenced? | Goals, principles and the Payment Screening capability |
| Product Manager | Which capabilities support the product roadmap? | Capability map and traceability to initiatives |
| Platform Engineer | Is reuse governed and operable? | Principles, requirements and initiative scope |

Two disciplines keep this honest. First, name concerns as questions, not as features, because a question can be answered and reviewed. Second, do not promise that one model serves every stakeholder. The sponsor and the Platform Engineer need different views of the same strategy, and forcing both onto one diagram usually serves neither.

## Capability maps

This section answers: **what must the organisation be able to do, independent of how it is currently organised or built?**

Chapter 13 introduced the capability map. Here the concern is using it for planning. A capability is a stable ability, such as `Identity Verification` or `Payment Screening`. It does not change every time the process is redesigned or the software is replaced, which is exactly why it is a good backbone for strategy. The Open Group's business-capabilities guide describes capability maps as a way to support business planning and align business architecture viewpoints [OPEN-GROUP-BIZARCH-GUIDES-2022].

For planning, two properties of capability maps matter. The first is levelling. A capability map is usually shown at levels, with a small number of high-level capabilities decomposed into more specific ones. A level-one capability such as `Customer Onboarding` might decompose into `Document Capture`, `Identity Verification` and `Risk Assessment`. Levelling lets a sponsor discuss investment at a coarse level while an architect works at a finer one, without drawing two unrelated maps.

The second property is stability of naming. The capability names must be nouns of ability, controlled and reused, not process verbs. The controlled Horizon Bank set lives in `examples/horizon-bank/capabilities.md`, and Chapter 7's FIG-07-01 shows a capability map using these ideas. The point of a controlled list is that the same capability means the same thing on the heat map, the value stream and the traceability view.

The distinctions below are the ones a capability map exists to protect. Keeping them clear is the single most useful skill in this chapter.

| A capability is not | Example of the confusion | Why it matters |
|---|---|---|
| A process step | Calling "Check documents" a capability | Steps change with each redesign; capabilities should stay stable |
| An organisation unit | Treating `Relationship Management` as the sales team | Reorganisations should not rewrite the capability map |
| An application | Treating `Party Management` as the Party and Customer Platform | Systems are replaced; the ability remains |
| A project | Treating `Payment Screening` as the screening programme | Initiatives are temporary; capabilities are enduring |
| A BIAN Service Domain | Mapping one capability to one Service Domain automatically | The partitions use different criteria and need separate justification |

## Value streams

This section answers: **where along the path to stakeholder value do the capabilities actually contribute?**

A capability map says what the organisation can do. A value stream says how value accumulates for a stakeholder, stage by stage, from a triggering need to a usable outcome [OPEN-GROUP-BIZARCH-GUIDES-2022]. On its own, each view is useful. Combined, they answer a planning question that neither answers alone: for a given journey, which capabilities carry the value, and where would an improvement help most?

The combination is a cross-map. Each value-stream stage is listed with the capabilities that enable it. This is the same Horizon Bank onboarding value stream shown as FIG-13-02 in Chapter 13, now read as a planning grid rather than an introduction. FIG-14-02 renders this cross-map; its content is the table below.

| Value stage | Stakeholder value produced | Enabling capabilities |
|---|---|---|
| Need understood | The customer's banking need is clear enough to act on | Digital Servicing, Relationship Management |
| Application established | Structured application information exists | Customer Onboarding, Document Capture |
| Identity and eligibility confirmed | The customer is assessed against identity, eligibility and financial-crime expectations | Identity Verification, Financial Crime Screening, Risk Assessment |
| Banking relationship established | Party and product records exist in authoritative systems | Party Management, Account Opening, Product Management |
| Services ready to use | The customer can use the selected channels and products | Digital Servicing, Notification Management, Account Servicing |

Reading across the grid tells a planner where a goal lands. The goal to reduce onboarding time depends most on the middle stages, and within them on `Identity Verification`, `Financial Crime Screening` and `Risk Assessment`. That is a more precise statement than "improve onboarding", and it points investment at specific capabilities rather than at a vague journey.

A value stream is not a process model. It shows value stages, not sequence flows, roles, message flows, timers or exceptions. When the discussion turns to how the work is actually performed, Chapter 15 moves to BPMN. Keeping the value stream at value-stage level is what makes it readable by a sponsor.

## Heat maps

This section answers: **given a stable capability structure, where should attention and money go first?**

A heat map overlays a rating onto a stable structure. Chapter 13 introduced it and rated capabilities by current pain, strategic importance and delivery risk. For strategy and investment, the most decision-relevant overlay pairs strategic importance with investment priority, so a sponsor can separate what matters from what is being funded. A capability that is highly important but low priority is a visible gap worth discussing.

The rating is only meaningful when its basis is written down. Use `H`, `M` and `L` labels as well as any colour, so meaning survives in greyscale and in print, and record the date, owner, version and scoring definitions on the figure. The values below are illustrative teaching values, not an assessment of a real bank.

| Capability | Strategic importance | Investment priority | Basis for attention |
|---|---|---|---|
| Identity Verification | H | H | Directly limits onboarding speed and drop-out |
| Financial Crime Screening | H | H | Regulatory scrutiny and evidence needs |
| Payment Screening | H | M | Important, but partly addressed by existing controls |
| Account Servicing | H | L | Important yet constrained by legacy change risk |
| Event Governance | M | H | Enables reuse the payment goal depends on |

The value of the heat map is the conversation it forces. Why is `Account Servicing` strategically important but low priority? Because change is gated by legacy risk, which is a roadmap and sequencing decision, not a reason to deny its importance. The heat map does not make that decision; it makes the decision visible. A heat map that hides its scoring, collapses several dimensions into one colour, or averages away disagreement is worse than no heat map, because it lends false confidence to a guess.

## Traceability to initiatives

This section answers: **how do you connect a strategic goal to the change you actually fund, so each can be defended?**

This is the thread that turns strategy models into decisions. A goal names an intention and an outcome. The outcome depends on named capabilities improving. An initiative is the funded change that lifts those capabilities. A course of action, in ArchiMate's strategy vocabulary, describes the approach the initiative takes [OPEN-GROUP-ARCHIMATE-4]. Traceability records these links so a reviewer can walk from any goal to its initiative, or from any initiative back to the goal that justifies it.

FIG-14-01 shows this thread for Horizon Bank. Its content is summarised below. Read each row as a sentence: a driver raises a goal, the goal targets an outcome, the outcome depends on capabilities, and an initiative lifts those capabilities through a course of action.

| Goal | Target outcome | Capabilities to lift | Initiative | Course of action |
|---|---|---|---|---|
| Reduce time to usable banking services | Median onboarding time reduced | Identity Verification, Financial Crime Screening, Risk Assessment | Onboarding Uplift | Streamline identity and screening within onboarding |
| Strengthen screening traceability | Every screening decision evidenced | Financial Crime Screening, Payment Screening, Data Governance | Onboarding Uplift and Payment Modernisation | Retain screening evidence per decision |
| Improve payment transparency | Payment status available in near real time | Payment Initiation, Event Governance, Notification Management | Payment Modernisation | Publish governed payment-status events |
| Reduce integration cost and fragility | Fewer point-to-point interfaces | Event Governance, Data Governance | Payment Modernisation | Prefer governed reuse over point-to-point links |

Two properties make this thread trustworthy. First, an initiative should trace to at least one goal, and a goal that no initiative serves is either not funded or not really a goal. Second, the same capability can appear under more than one goal, which is normal and useful: it shows that `Financial Crime Screening` serves both speed and compliance, so an improvement there has more than one justification. When a project cannot name the goal it serves or the capability it lifts, that is a finding, not a detail. Chapter 13's Architecture Decision Record technique complements this thread by recording why a particular course of action was chosen over the alternatives.

## Recommended notation combinations

This section answers: **which of these models should be drawn together, and in what order?**

No single notation covers strategy and capability well. The practical approach is a small, ordered set of views that share controlled names. Draw only the views that a stakeholder concern requires.

| Question in focus | Lead model | Supporting models | Typical order |
|---|---|---|---|
| Why are we changing? | Motivation model (drivers, goals, outcomes) | Stakeholder and concern table | Draw first; it anchors everything else |
| What must we be able to do? | Capability map | Controlled capability list | Draw second; reuse stable names |
| Where does value accrue? | Value stream | Value stream to capability cross-map | Draw third; connect to capabilities |
| Where do we invest? | Capability investment heat map | Capability map | Draw fourth; overlay ratings |
| What will we fund? | Strategy-to-capability traceability view | Roadmap, ADRs | Draw last; link goals to initiatives |

The combination works because each model reuses the same capability names. If the capability map, the value stream, the heat map and the traceability view disagree on what a capability is called, the pack loses its thread. A shared, controlled vocabulary is what lets five simple views behave like one coherent model.

ArchiMate can express this whole chain in one language, which is an advantage when formal traceability and tool support matter [OPEN-GROUP-ARCHIMATE-4]. Many teams instead use a lighter mix of a motivation table, a capability map, a value-stream grid and a heat map, which is easier for a sponsor to read. Neither is universally better. Choose ArchiMate when integrated traceability is the priority, and choose the lighter mix when accessibility to non-architects is the priority.

## Selection table

This section answers: **for a specific strategy or capability question, which model should you reach for?**

| Question | Reach for | Main audience | Why |
|---|---|---|---|
| Why does this change matter? | Motivation model | Sponsors and architects | Records drivers, goals and measurable outcomes |
| Whose interests are at stake? | Stakeholder and concern table | Sponsors and architects | Ties every view to a named concern |
| What enduring abilities do we need? | Capability map | Business architects and portfolio teams | Separates ability from process, unit, system and project |
| Where does value accumulate for a stakeholder? | Value stream | Business architects and product owners | Shows value stages before process detail |
| Which capabilities carry a given journey? | Value stream to capability cross-map | Business and enterprise architects | Points investment at specific capabilities |
| Where should we invest first? | Capability investment heat map | Portfolio teams and sponsors | Overlays explicit importance and priority |
| Which goal does this project serve? | Strategy-to-capability traceability view | Sponsors, architects and reviewers | Keeps goal, capability and initiative links navigable |
| Why did we choose this approach? | Architecture Decision Record | Architects and governance reviewers | Records rationale and consequences (Chapter 13) |

The safest habit is the same one from Chapter 13: use the smallest model that answers the question, and add another view only when it removes confusion or supports a real decision.

## Worked example

The Simple Online Store shows the thread at its smallest. The driver is rising customer expectation for a trustworthy checkout. The goal is to remove card-data handling from the store, with the outcome that no full card details are stored in the Online Store. The enabling capability is `Take payment`, delivered by delegating to the Payment Provider System. The initiative is a single checkout change. One driver, one goal, one outcome, one capability and one initiative are enough, and drawing a five-view pack for this would be over-modelling.

Horizon Bank shows the thread at a realistic size, reusing every controlled name from the example files. Start with motivation. The bank faces four drivers: customer expectation for fast access, regulatory scrutiny of financial crime, the cost of legacy integration, and competition from digital-first banks. These raise four goals with measurable outcomes, as set out in the goals-and-outcomes table earlier in the chapter.

Move to capability. The goals depend on a focused set of capabilities: `Identity Verification`, `Financial Crime Screening`, `Risk Assessment`, `Payment Initiation`, `Event Governance`, `Notification Management` and `Data Governance`. These are stable abilities, not the systems that deliver them, so the same map survives the platform changes described in Chapter 13's roadmap.

Add the value stream. The onboarding cross-map shows that the speed goal lands on the middle stages, and specifically on `Identity Verification`, `Financial Crime Screening` and `Risk Assessment`. This tells the Onboarding Uplift initiative where to focus.

Overlay investment. The heat map marks `Identity Verification` and `Financial Crime Screening` as high importance and high priority, `Payment Screening` as high importance but medium priority, and `Account Servicing` as high importance but low priority because legacy change risk gates it. The sponsor can now see, on one page, where strategic value and funding agree and disagree.

Close with traceability. Two initiatives absorb the work. Onboarding Uplift lifts identity, screening and risk-assessment capabilities to serve the speed and traceability goals. Payment Modernisation lifts payment initiation, event governance and data governance to serve the transparency and integration-cost goals. Every initiative names its goals, and every goal names an initiative. A reviewer can start at "reduce integration cost" and arrive at Payment Modernisation, or start at Payment Modernisation and arrive at two goals, without a gap in the thread. That navigability, not the diagrams themselves, is the point of the chapter.

The example deliberately omits detail that belongs elsewhere. It does not show onboarding sequence, roles or exceptions, which are BPMN concerns for Chapter 15. It does not show system structure, which is a C4 concern for Chapter 16. It does not set dates, budgets or staffing, which are programme concerns, not architecture concerns.

## Common mistakes

The first mistake is drawing capability and strategy models with no visible thread to a decision. If no goal, concern or initiative is served, the pack is decoration.

The second mistake is confusing a capability with a process, an organisation unit, an application, a project or a BIAN Service Domain. The capability map exists to protect these distinctions, and losing them makes every later view unstable.

The third mistake is merging goals and outcomes. Without a measurable outcome, a goal cannot be shown to be met.

The fourth mistake is turning a value stream into a process model. Sequence, roles, message flows and exceptions belong in BPMN, not in a value stream.

The fifth mistake is a heat map with a hidden scoring basis, colour-only meaning, or averaged-away disagreement. State the criteria, date, owner and version, and keep text labels.

The sixth mistake is an initiative that cannot name the goal it serves or the capability it lifts. That gap is a governance finding, not a formatting detail.

The seventh mistake is using inconsistent capability names across the map, value stream, heat map and traceability view, which quietly breaks the shared vocabulary that holds the pack together.

## Key takeaways

- Strategy and capability models are only useful when a visible thread runs from why the organisation is changing to what it will fund.
- A motivation model records drivers, assessments, goals, outcomes, principles and requirements, and it keeps goals separate from measurable outcomes.
- Every strategy view should trace to a named stakeholder concern, or it is decoration.
- A capability is a stable ability, not a process, an organisation unit, an application, a project or a BIAN Service Domain.
- Cross-mapping a value stream to its enabling capabilities points investment at specific capabilities rather than at a vague journey.
- A capability investment heat map turns a stable structure into an explicit, reviewable investment question, and only works when its scoring basis is stated.
- Traceability from goal to capability to initiative lets any project be defended, and any goal be checked for funding.
- Combine a small, ordered set of views that share controlled capability names; use the smallest set that answers the question.

## Practical exercise

Horizon Bank wants to reduce onboarding drop-out and strengthen screening evidence, while keeping legacy change risk under control.

1. Write one driver, one goal and one measurable outcome for the drop-out concern.
2. Name three capabilities from `examples/horizon-bank/capabilities.md` that most affect that outcome, and justify each in one line.
3. Place those three capabilities on the onboarding value stream. Which value stage do they cluster in?
4. Give each of the three capabilities a strategic-importance and an investment-priority rating, and state the basis in one line each.
5. Name one initiative that lifts these capabilities, and write the single sentence that traces goal to outcome to capability to initiative.

Suggested answer:

- Driver: customer expectation for fast account access. Goal: reduce time to usable banking services. Outcome: median onboarding time reduced against baseline.
- `Identity Verification`, `Financial Crime Screening` and `Risk Assessment`, because they gate whether an applicant can proceed.
- They cluster in the "Identity and eligibility confirmed" stage.
- Ratings are a matter of judgement, but identity and screening are typically high importance and high priority, with a stated basis of drop-out impact and regulatory scrutiny.
- Initiative: Onboarding Uplift. Thread: to reduce time to usable services (goal) and cut median onboarding time (outcome), Onboarding Uplift (initiative) lifts identity, screening and risk-assessment capabilities.

## Review checklist

- [ ] Every strategy view traces to a named stakeholder concern.
- [ ] Goals and measurable outcomes are stated separately.
- [ ] Capabilities are stable abilities, not processes, units, applications, projects or Service Domains.
- [ ] Capability names are consistent across the map, value stream, heat map and traceability view, and match `examples/horizon-bank/capabilities.md`.
- [ ] The value stream stays at value-stage level and does not drift into process detail.
- [ ] The heat map states its scoring basis, date, owner and version, and does not rely on colour alone.
- [ ] Every initiative names the goal it serves and the capabilities it lifts.
- [ ] Comparisons do not imply that one notation is universally superior.
- [ ] Common mistakes are concrete and actionable.
- [ ] Required source notes and diagram specifications are registered, and figures are produced only after author approval of the specifications.
- [ ] Terminology, link and word-count checks pass.

## References and further reading

Chapter source notes are maintained under `research/archimate/` and `research/other-modelling/`, with related architecture-description vocabulary under `research/fundamentals/`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index.

- `[OPEN-GROUP-ARCHIMATE-4]`: The Open Group, ArchiMate 4 Specification.
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`: The Open Group, TOGAF Series Guides for Business Capabilities and Value Streams.
- `[ISO-42010]`: ISO/IEC/IEEE 42010:2022, Architecture description.

## Drafting notes

- Status is `Drafting`: all planned sections contain coherent prose. The draft runs a little above the 2,000 to 4,000 word target (about 4,450 words), which the scope justifies because the chapter carries a full strategy-to-initiative thread and a worked example; a review pass may tighten it.
- Figures `FIG-14-01` and `FIG-14-02` are registered in `DIAGRAM_REGISTER.md` with specifications under `diagrams/specifications/`. Their editable sources and SVG exports are deliberately deferred until the author approves the specifications, per the diagram workflow. The chapter presents each figure's content as an inline table so it reads completely before production.
- This chapter deliberately references, rather than re-teaches, the Chapter 7 and Chapter 13 figures for capability maps, value streams, heat maps and motivation views.
- Do not mark this chapter `Approved` without explicit author approval, and do not mark any figure `Approved`.
