---
title: "Modelling Business Strategy and Capabilities"
chapter: 14
part: "part-03-diagram-selection"
status: "Revision Required"
author: "Nishikant Tiwari"
last_updated: "2026-07-04"
---

# 14. Modelling Business Strategy and Capabilities

## Chapter purpose

Show how to choose and combine models that connect business strategy to the stable abilities an organisation needs. Part II introduced the notations. This chapter, the first in Part III, helps a reader select the right model when the architecture question is about goals, stakeholders, capabilities, value and investment, rather than software structure or runtime behaviour.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Separate plain-language strategy words from the formal ArchiMate concepts they map to.
- Record drivers, goals and genuinely measurable outcomes, keeping a goal distinct from its outcome.
- Read a capability map, use capability levelling, and explain why a capability is not a process, an organisation unit, an application or a project.
- Cross-map a value stream to the capabilities that enable each stage.
- Keep strategic importance, current condition, current funding and proposed priority as separate ideas on a heat map.
- Trace a driver through a goal, outcome and capability to a funded change, using stable identifiers.
- Select and combine strategy and capability models for a realistic situation, and review them critically.

## Prerequisites and dependencies

- Chapter 2: Model, View and Viewpoint
- Chapter 3: How to Read Architecture Diagrams
- Chapter 7: ArchiMate
- Chapter 13: Other Useful Modelling Approaches

## Required models and artefacts

The reader meets two figures specified for this chapter, plus figures reused from earlier chapters:

- FIG-14-01: Horizon Bank Strategy-to-Capability Traceability View, an ArchiMate-informed teaching view of the driver-to-work-package thread.
- FIG-14-02: Horizon Bank Onboarding Value Stream to Capability Cross-Map, a capability-by-stage matrix.
- Reused for reference: FIG-07-01 capability map, FIG-07-05 motivation view, FIG-13-02 onboarding value stream and FIG-13-05 capability heat map.

## Worked examples

- Simple Online Store strategy for a single goal, its enabling capability and one change.
- Horizon Bank onboarding and payments strategy traced from four drivers through goals, measurable outcomes and capabilities to two funded work packages.

## Source requirements

- `[OPEN-GROUP-ARCHIMATE-4]` supports the motivation and strategy concept names used here (driver, goal, outcome, capability, course of action and work package) and the removal of the former `Constraint` element. It does not support formal relationship semantics in this book, because the licensed specification text is out of scope for this AI-assisted drafting; see the research note.
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]` supports capability maps and value streams as business architecture elements used for planning.
- `[AUTHOR-HEAT-MAP-CONVENTIONS-2026]` records the local heat-map scoring and legend convention reused here.
- `[ISO-42010]` supports the stakeholder and concern vocabulary from Chapter 2.
- Controlled names come from `examples/horizon-bank/capabilities.md`, `examples/horizon-bank/actors.md` and `examples/simple-online-store/README.md`.

## Why this chapter exists

Chapter 13 introduced capability maps, value streams, heat maps and Wardley maps at an introductory level. This chapter answers a more practical question: when the discussion is about strategy and capability, which model should you reach for, and how do these models fit together?

Strategy models are easy to get wrong. A team draws a colourful capability map, a value stream and a heat map, but nobody can say which goal the pictures serve or which change they justify. The discipline in this chapter is to keep a visible thread from why the organisation wants to change, through what it must be able to do, to what it will actually fund.

The thread has a consistent shape. A driver or a stakeholder concern raises a goal. The goal sets a measurable outcome. The outcome needs one or more capabilities to improve. A value stream shows where those capabilities create value for a stakeholder. A heat map exposes where attention and money might go. A funded change lifts the chosen capabilities. Traceability keeps each link navigable so a reviewer can challenge it.

## Plain language and formal ArchiMate concepts

This section answers: **which everyday strategy words map to which formal ArchiMate concepts, and when does the difference matter?**

Everyday strategy language and formal modelling language are not the same, and mixing them carelessly is a common source of confusion. The table below maps the plain words used in this chapter to the ArchiMate concept each one corresponds to.

| Plain-language concept | ArchiMate concept or treatment |
|---|---|
| Strategic pressure | Driver |
| Strategic intention | Goal |
| Measurable result | Outcome |
| Enduring organisational ability | Capability |
| Chosen strategic approach | Course of Action |
| Funded change initiative | Work Package, when formal ArchiMate implementation notation is used |

The word `initiative` is useful business language, and this chapter still uses it in prose. It is not, however, a substitute for a formal ArchiMate element. When a figure claims formal notation, the funded change should be shown as a `Work Package` (with the familiar initiative name as its label), not as a box simply captioned "initiative".

One honest limitation shapes the whole chapter. The exact ArchiMate 4 relationship types, their allowed element pairs and their directions are defined in the licensed specification text, which this book does not incorporate into AI-assisted drafting because of the specification's usage restriction. This book can therefore use the ArchiMate concept names above, and can avoid the removed `Constraint` element, but it does not assert formal ArchiMate relationship semantics. For that reason, FIG-14-01 is presented as an **ArchiMate-informed strategy traceability teaching view**, and its connectors are simplified, directional teaching links, not formal ArchiMate relationship notation. The research note `research/archimate/open-group-archimate-4.md` records this decision.

## Goals, drivers and outcomes

This section answers: **how do you record why an architecture needs to change, in a form precise enough to steer design?**

Strategy work often begins with vague ambition, such as "be more digital". A motivation model turns that ambition into named elements that can be traced and reviewed. The most useful for a beginner are the driver, the goal, the outcome, the principle and the requirement [OPEN-GROUP-ARCHIMATE-4].

> **Driver:** An external or internal force that creates a need to change, such as a regulatory expectation or a cost pressure.
>
> **Goal:** A stated intention, such as "reduce time to usable banking services".
>
> **Outcome:** A measurable end state that shows the goal is met, such as "median onboarding time is reduced against an agreed baseline".
>
> **Principle:** A general rule that guides many decisions, such as "prefer governed reuse over point-to-point integration".
>
> **Requirement:** A specific need a design must satisfy, such as "publish governed payment-status events for approved consumers".

The distinction beginners miss most often is goal versus outcome. A goal is an intention; an outcome is the observable result you would measure. Keeping them separate stops a model from claiming success it cannot demonstrate. ArchiMate 4 removed the earlier `Constraint` element, so this book does not use it; where a limit matters, express it as a principle, a requirement or an outcome target [OPEN-GROUP-ARCHIMATE-4].

For Horizon Bank, four drivers raise four goals, each with a target outcome. The drivers, goals and outcomes carry stable identifiers so the rest of the chapter can refer to them precisely.

| Driver | Goal | Target outcome |
|---|---|---|
| DRV-14-01 Customer expectation for fast account access | GOAL-14-01 Reduce time to usable banking services | OUT-14-01 Median onboarding time reduced |
| DRV-14-02 Regulatory scrutiny of financial crime | GOAL-14-02 Strengthen screening traceability | OUT-14-02 Every screening decision evidenced |
| DRV-14-03 Cost of legacy integration | GOAL-14-04 Reduce integration cost and fragility | OUT-14-04 Fewer point-to-point interfaces |
| DRV-14-04 Competition from digital-first banks | GOAL-14-03 Improve payment transparency | OUT-14-03 Payment status available promptly |

### Making outcomes measurable

Calling an outcome measurable is not the same as measuring it. A directional phrase such as "reduced" or "promptly" becomes decision-ready only when the metric, baseline, target, scope and time horizon are known. The table below gives each outcome a complete measurement definition. The baselines and targets are illustrative placeholders for teaching; they are not commitments by any real bank, and they are marked as values to be established or agreed.

| Outcome ID | Outcome statement | Metric | Baseline | Target | Scope | Time horizon | Measure owner | Evidence source |
|---|---|---|---|---|---|---|---|---|
| OUT-14-01 | Median onboarding time is reduced | Median elapsed time from application start to services ready to use | Illustrative baseline, to be established | Illustrative target, to be agreed | Retail onboarding via Horizon Digital Channels | Planning horizon to be agreed | Executive Sponsor | Onboarding platform records |
| OUT-14-02 | Every in-scope screening decision has retained evidence | Percentage of screening decisions with complete retained evidence | Illustrative baseline, to be established | Illustrative target, to be agreed | Onboarding and payment screening | Planning horizon to be agreed | Compliance Officer | Financial Crime Platform case records |
| OUT-14-03 | Payment status is available to customers promptly after each status change | Time from payment status change to customer-visible status | Illustrative baseline, to be established | Illustrative target, to be agreed | Outgoing retail payments | Planning horizon to be agreed | Product Manager | Event Platform and channel telemetry |
| OUT-14-04 | Fewer bespoke point-to-point interfaces remain in payment integration | Count of bespoke point-to-point payment interfaces in scope | Illustrative baseline, to be established | Illustrative target, to be agreed | Payment integration estate | Planning horizon to be agreed | Platform Engineer | Integration inventory |

## Stakeholder concerns

This section answers: **whose interests decide whether a strategy model is any good?**

Chapter 2 introduced stakeholders and concerns, where a concern is an interest a description should address for a stakeholder [ISO-42010]. Strategy modelling makes that concrete: every goal belongs to someone, and every strategy view that cannot be traced to a stakeholder concern is decoration. The stakeholders below use controlled roles from `examples/horizon-bank/actors.md`, including the Executive Sponsor role introduced for this chapter.

| Stakeholder | Primary concern | Model that addresses it |
|---|---|---|
| Executive Sponsor | Is the investment justified by strategic value? | Goals, outcomes and capability investment heat map |
| Relationship Manager | Can customers be onboarded quickly and well? | Onboarding value stream and enabling capabilities |
| Compliance Officer | Is screening effective and evidenced? | Goals, principles and screening capabilities |
| Product Manager | Which capabilities support the product roadmap? | Capability map and traceability to work packages |
| Platform Engineer | Is reuse governed and operable? | Principles, requirements and work-package scope |

Two disciplines keep this honest. Name concerns as questions, because a question can be answered and reviewed. And do not promise that one model serves every stakeholder: the Executive Sponsor and the Platform Engineer need different views of the same strategy.

## Capability maps

This section answers: **what must the organisation be able to do, independent of how it is currently organised or built?**

Chapter 13 introduced the capability map. Here the concern is using it for planning. A capability is a stable ability, such as `Identity Verification`. It does not change every time the process is redesigned or the software is replaced, which is why it is a good backbone for strategy [OPEN-GROUP-BIZARCH-GUIDES-2022].

For planning, two properties matter. The first is levelling. A capability map is shown at levels, with a small number of high-level capabilities decomposed into more specific ones. The controlled example in `examples/horizon-bank/capabilities.md` records that `Customer Onboarding` (level one) decomposes into `Document Capture`, `Identity Verification` and `Risk Assessment` (level two). Levelling lets a sponsor discuss investment coarsely while an architect works finely, without drawing two unrelated maps. Three ideas must be kept apart: decomposition (a parent and its children), contribution (a capability that enables a value stage without being a child of that stage's headline capability), and dependency (one capability relying on another). For example, `Financial Crime Screening` contributes to onboarding but is a level-one peer of `Customer Onboarding`, not a child of it. To avoid double counting, `Financial Crime Screening` and `Payment Screening` are kept as separate level-one peers scoped to different control points, customer and onboarding screening for the first and payment-instruction screening for the second.

The second property is stability of naming. The same capability must mean the same thing on the map, the value stream, the heat map and the traceability view, which is why the names are controlled and reused. The distinctions below are the ones a capability map exists to protect.

| A capability is not | Example of the confusion | Why it matters |
|---|---|---|
| A process step | Calling "Check documents" a capability | Steps change with each redesign; capabilities should stay stable |
| An organisation unit | Treating `Relationship Management` as the sales team | Reorganisations should not rewrite the map |
| An application | Treating `Party Management` as the Party and Customer Platform | Systems are replaced; the ability remains |
| A project | Treating `Payment Screening` as the screening programme | Initiatives are temporary; capabilities are enduring |
| A BIAN Service Domain | Mapping one capability to one Service Domain automatically | The partitions use different criteria and need separate justification |

## Value streams

This section answers: **where along the path to stakeholder value do the capabilities contribute?**

A capability map says what the organisation can do. A value stream says how value accumulates for a stakeholder, stage by stage, from a triggering need to a usable outcome [OPEN-GROUP-BIZARCH-GUIDES-2022]. Combined as a cross-map, they answer a planning question neither answers alone: for a given journey, which capabilities carry the value, and where would an improvement help most?

FIG-14-02 renders this as a matrix for the Horizon Bank onboarding journey. The rows are unique capabilities, the columns are the five value stages from the FIG-13-02 value stream, and each cell marks a primary enabler (P) or a supporting enabler (S). A blank cell means no material contribution in this teaching view. The final column rates strategic importance assessed specifically against GOAL-14-01, reduce time to usable banking services, not against every possible strategy. The level-one parent `Customer Onboarding` is represented by its level-two children rather than as a separate row, so the matrix does not double count.

| Capability | S1 Need understood | S2 Application established | S3 Identity and eligibility confirmed | S4 Banking relationship established | S5 Services ready to use | Strategic importance for GOAL-14-01 |
|---|---|---|---|---|---|---|
| Digital Servicing | P | | | | P | M |
| Relationship Management | S | | | | | L |
| Document Capture | | P | | | | M |
| Identity Verification | | | P | | | H |
| Risk Assessment | | | P | | | H |
| Financial Crime Screening | | | P | | | H |
| Party Management | | | | P | | M |
| Account Opening | | | | P | | M |
| Product Management | | | | S | | L |
| Notification Management | | | | | S | L |
| Account Servicing | | | | | S | L |

Reading down the importance column tells a planner where the speed goal lands: on the identity-and-eligibility stage, and specifically on `Identity Verification`, `Financial Crime Screening` and `Risk Assessment`. That is more precise than "improve onboarding", and it points effort at named capabilities.

A value stream is not a process model. It shows value stages, not sequence flows, roles, message flows, timers or exceptions, and it is not a customer journey map, a Lean value-stream map, an application landscape or an interface model. When the discussion turns to how the work is performed, Chapter 15 moves to BPMN.

## Heat maps and the investment question

This section answers: **given a stable capability structure, how do you frame an investment question without pretending it is already a funding decision?**

A heat map overlays a rating onto a stable structure. Chapter 13 introduced it. For investment, the common mistake is to collapse several different ideas into one colour and then read that colour as though it shows what is being funded. It does not. These are separate facts and judgements, and a useful heat map keeps them apart:

- Strategic importance: how strongly a capability matters to the strategy.
- Current health or pain: the present condition of the capability.
- Current investment status: what is already funded or committed.
- Proposed priority: a portfolio recommendation, not a decision.
- Delivery constraint: difficulty, dependency or uncertainty.
- Final funding: a governance decision made elsewhere.

The example below keeps these dimensions in separate columns and computes no composite score. The values are illustrative teaching values, recorded with a scoring basis, date, owner and version in line with the heat-map convention [AUTHOR-HEAT-MAP-CONVENTIONS-2026]. Use `H`, `M` and `L` text as well as any colour, so the meaning survives in greyscale.

| Capability | Strategic importance | Current health or pain | Current investment status | Proposed priority | Delivery constraint | Rationale |
|---|---|---|---|---|---|---|
| Identity Verification | H | M | Partly funded | H | M | Gates onboarding speed and drop-out |
| Financial Crime Screening | H | M | Partly funded | H | M | Regulatory scrutiny and evidence needs |
| Payment Screening | H | M | Funded | M | M | Important, partly addressed by existing controls |
| Account Servicing | H | M | Not funded in scope | L | H | Change gated by legacy risk |
| Event Governance | M | M | Not yet funded | H | M | Enables reuse the payment goals depend on |

The value is the conversation the separation forces. `Account Servicing` is strategically important yet low proposed priority, because change is gated by legacy risk; `Event Governance` is only moderately important yet high proposed priority, because other goals depend on it. A proposed priority is a recommendation to a governance forum. It is not proof that funding exists, and the heat map should never be read as though it were.

## Traceability to initiatives

This section answers: **how do you connect a strategic driver to the change you fund, so each can be defended?**

This is the thread that turns strategy models into decisions. A driver raises a goal; the goal sets an outcome; the outcome needs named capabilities to improve; a funded change, shown formally as a `Work Package`, lifts those capabilities using a chosen `Course of Action`. Traceability records these links so a reviewer can walk from any driver to its work package, or back again.

The single table below is the complete strategy thread for the Horizon Bank example, and it is the dataset FIG-14-01 draws. Nothing in the figure needs to be inferred from separate paragraphs.

| Driver | Goal | Outcome | Capabilities | Course of Action | Work Package | Stakeholder owner | Open assumption or decision |
|---|---|---|---|---|---|---|---|
| DRV-14-01 | GOAL-14-01 | OUT-14-01 | Identity Verification, Financial Crime Screening, Risk Assessment | COA-14-01 Streamline identity and screening within onboarding | WP-14-01 Onboarding Uplift | Executive Sponsor | Baseline and target to be established |
| DRV-14-02 | GOAL-14-02 | OUT-14-02 | Financial Crime Screening, Payment Screening, Data Governance | COA-14-01 and COA-14-02 | WP-14-01 Onboarding Uplift and WP-14-02 Payment Modernisation | Compliance Officer | Evidence-retention scope to be agreed |
| DRV-14-04 | GOAL-14-03 | OUT-14-03 | Payment Initiation, Event Governance, Notification Management | COA-14-02 Modernise payments through governed reuse and events | WP-14-02 Payment Modernisation | Product Manager | Latency target to be agreed |
| DRV-14-03 | GOAL-14-04 | OUT-14-04 | Event Governance, Data Governance | COA-14-02 Modernise payments through governed reuse and events | WP-14-02 Payment Modernisation | Platform Engineer | Interface-count baseline to be established |

Two properties make the thread useful. First, a capability can appear under more than one goal: `Financial Crime Screening` serves both speed and traceability, so an improvement there has more than one justification, and GOAL-14-02 is deliberately served by both work packages. Second, a work package should trace to at least one goal.

A goal with no linked work package is a review finding, not automatically an invalid goal. The absence may mean the goal is unfunded, deliberately deferred, delivered through business-as-usual change, answered by a policy or operating-model response rather than a project, or exposed as an ownership or portfolio gap; occasionally it means the goal is obsolete and should be challenged. Each reading leads to a different action, so the reviewer investigates rather than assumes. For the same reason, do not imply that every capability improvement must be delivered by a project; some improve through routine operational change. Chapter 13's Architecture Decision Record technique complements this thread by recording why a course of action was chosen over the alternatives.

## Recommended notation combinations

This section answers: **which of these models should be drawn together, and in what order?**

No single notation covers strategy and capability well. Draw a small, ordered set of views that share controlled names, and only the views a stakeholder concern requires.

| Question in focus | Lead model | Typical order |
|---|---|---|
| Why are we changing? | Motivation model with a stakeholder and concern table | First; it anchors everything else |
| What must we be able to do? | Capability map with controlled, levelled names | Second; reuse stable names |
| Where does value accrue? | Value stream and its capability cross-map | Third; connect stages to capabilities |
| Where might we invest? | Capability investment heat map | Fourth; overlay separated ratings |
| What will we fund? | Strategy traceability view linking drivers to work packages | Last; keep the thread navigable |

The combination works because each model reuses the same capability names. ArchiMate can express the whole chain in one language when integrated traceability and tool support matter [OPEN-GROUP-ARCHIMATE-4]. A lighter mix of a motivation table, a capability map, a cross-map and a heat map is easier for a sponsor to read. Neither is universally better: choose ArchiMate when integrated traceability is the priority, and the lighter mix when accessibility to non-architects is the priority.

## Selection table

This section answers: **for a specific strategy or capability question, which model should you reach for?**

| Question | Reach for | Main audience | Why |
|---|---|---|---|
| Why does this change matter? | Motivation model | Executive Sponsor and architects | Records drivers, goals and measurable outcomes |
| Whose interests are at stake? | Stakeholder and concern table | Executive Sponsor and architects | Ties every view to a named concern |
| What enduring abilities do we need? | Capability map with levelling | Business architects and portfolio teams | Separates ability from process, unit, system and project |
| Which capabilities carry a journey? | Value stream to capability cross-map | Business and enterprise architects | Points investment at specific capabilities per stage |
| Where might we invest first? | Capability investment heat map | Portfolio teams and Executive Sponsor | Keeps importance, condition, funding and priority separate |
| Which goal does this change serve? | Strategy traceability view | Executive Sponsor, architects and reviewers | Keeps driver, goal, capability and work-package links navigable |
| Why did we choose this approach? | Architecture Decision Record | Architects and governance reviewers | Records rationale and consequences (Chapter 13) |

The safest habit is the one from Chapter 13: use the smallest model that answers the question, and add another view only when it removes confusion or supports a real decision.

## Worked example

The Simple Online Store shows the thread at its smallest. The driver is rising customer expectation for a trustworthy checkout. The goal is to remove card-data handling from the store; the outcome is that no full card details are stored in the Online Store. The enabling capability is `Take payment`, delivered by delegating to the Payment Provider System. One change is enough, and drawing a five-view pack here would be over-modelling.

Horizon Bank shows the thread at realistic size, reusing every controlled name and the identifiers defined earlier. The motivation model records four drivers, four goals and the four measured outcomes OUT-14-01 to OUT-14-04. The capability map supplies the stable abilities, levelled so onboarding's children are not double counted with their parent. The onboarding cross-map (FIG-14-02) shows the speed goal landing on the identity-and-eligibility stage. The investment heat map keeps importance, condition, current funding and proposed priority separate, so the Executive Sponsor can see where strategic value and funding agree and disagree. The traceability table then closes the thread into two work packages: WP-14-01 Onboarding Uplift lifts identity, screening and risk-assessment capabilities, and WP-14-02 Payment Modernisation lifts payment initiation, event and data governance. A reviewer can start at DRV-14-03 and arrive at WP-14-02, or start at WP-14-01 and arrive at two goals, without a gap. That navigability, not the diagrams themselves, is the point.

The example deliberately omits detail that belongs elsewhere: onboarding sequence, roles and exceptions (BPMN, Chapter 15); system structure (C4, Chapter 16); and dates, budgets and staffing (programme concerns, not architecture).

## Common mistakes

The first mistake is drawing capability and strategy models with no visible thread to a decision. If no driver, concern, goal or work package is served, the pack is decoration.

The second mistake is confusing a capability with a process, an organisation unit, an application, a project or a BIAN Service Domain, or double counting a parent capability together with its children.

The third mistake is merging goals and outcomes, or calling an outcome measurable without a metric, baseline, target, scope and time horizon.

The fourth mistake is turning a value stream into a process model. Sequence, roles, message flows and exceptions belong in BPMN.

The fifth mistake is a heat map that collapses importance, condition, funding and priority into one colour, and is then read as proof of funding.

The sixth mistake is assuming a goal with no work package is invalid. It is a finding to investigate, because the cause may be deferral, business-as-usual delivery, a policy response or a portfolio gap.

The seventh mistake is inconsistent capability names across views, which quietly breaks the shared vocabulary that holds the pack together.

## Key takeaways

- Strategy and capability models are only useful when a visible thread runs from why the organisation is changing to what it will fund.
- Everyday words such as driver, goal, outcome, capability and initiative map to ArchiMate concepts; when a figure claims formal notation, a funded change is a Work Package, not a box labelled "initiative".
- This book uses ArchiMate concept names but not formal ArchiMate relationship semantics, because the licensed specification text is out of scope for AI-assisted drafting; FIG-14-01 is therefore a labelled teaching traceability view.
- An outcome is measurable only when its metric, baseline, target, scope and time horizon are stated; a goal is not the same as its outcome.
- A capability is a stable ability, levelled to avoid double counting, and is not a process, unit, application, project or BIAN Service Domain.
- A value-stream-to-capability cross-map points investment at named capabilities per stage.
- On a heat map, strategic importance, current condition, current funding and proposed priority are separate ideas; a priority is a recommendation, not proof of funding.
- A goal with no work package is a review finding to investigate, not automatically an invalid goal.

## Practical exercise

Horizon Bank wants to reduce onboarding drop-out and strengthen screening evidence, while keeping legacy change risk under control.

1. Write one driver, one goal and one outcome for the drop-out concern, and give the outcome a metric, a placeholder baseline and a placeholder target.
2. Name three capabilities from `examples/horizon-bank/capabilities.md` that most affect that outcome, and justify each in one line.
3. Place those three capabilities on the onboarding cross-map. Which value stage do they cluster in?
4. On the heat map, give each capability a strategic importance and a proposed priority, and state separately whether it is currently funded.
5. Name one work package that lifts these capabilities, and write the single sentence tracing driver to goal to outcome to capability to work package.

Suggested answer:

- Driver DRV-14-01; goal GOAL-14-01; outcome OUT-14-01, metric "median time from application start to services ready", baseline and target marked illustrative and to be agreed.
- `Identity Verification`, `Financial Crime Screening` and `Risk Assessment`, because they gate whether an applicant can proceed.
- They cluster in the identity-and-eligibility stage (S3).
- Importance is typically high for identity and screening; proposed priority high; current funding is a separate fact, here partly funded, and is not implied by the priority.
- Work package WP-14-01 Onboarding Uplift. Thread: DRV-14-01 raises GOAL-14-01, which sets OUT-14-01, which needs identity, screening and risk-assessment capabilities, which WP-14-01 lifts.

## Review checklist

- [ ] Every strategy view traces to a named stakeholder concern.
- [ ] Plain-language words are mapped to ArchiMate concepts, and formal notation is claimed only where it is used.
- [ ] Goals and measurable outcomes are separate, and each outcome has a metric, baseline, target, scope and time horizon.
- [ ] Capabilities are stable, levelled abilities, not processes, units, applications, projects or Service Domains, and parents are not double counted with children.
- [ ] Capability names are consistent across the map, cross-map, heat map and traceability view, and match `examples/horizon-bank/capabilities.md`.
- [ ] The value-stream cross-map stays at value-stage level and does not drift into process detail.
- [ ] The heat map keeps importance, condition, funding and priority separate, states its basis, and does not rely on colour alone.
- [ ] Every work package names the goal it serves and the capabilities it lifts, and a goal with no work package is treated as a finding, not an error.
- [ ] Comparisons do not imply that one notation is universally superior.
- [ ] Required source notes and diagram specifications are registered, and figures are produced only after author approval of the specifications.
- [ ] Terminology, link and word-count checks pass.

## References and further reading

Chapter source notes are maintained under `research/archimate/` and `research/other-modelling/`, with related architecture-description vocabulary under `research/fundamentals/`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index.

- `[OPEN-GROUP-ARCHIMATE-4]`: The Open Group, ArchiMate 4 Specification.
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`: The Open Group, TOGAF Series Guides for Business Capabilities and Value Streams.
- `[AUTHOR-HEAT-MAP-CONVENTIONS-2026]`: Repository-local heat-map scoring and legend convention.
- `[ISO-42010]`: ISO/IEC/IEEE 42010:2022, Architecture description.
