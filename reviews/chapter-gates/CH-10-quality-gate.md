# Chapter 10 Quality Gate: Domain and Event Modelling

## Gate summary

- **Chapter:** 10, Domain and Event Modelling
- **Manuscript:** `manuscript/part-02-modelling-languages/10-domain-event-modelling.md`
- **Status:** Approved
- **Current gate:** Chapter 10 has complete prose, source notes, registered source keys, corrected diagram specifications, PlantUML sources, SVG exports, PNG previews, glossary updates, register updates, repository checks and author approval.
- **Final quality score:** 9.1
- **Diagram status:** `FIG-10-01` through `FIG-10-04` remain `Review`, not `Approved`.

## Scorecard

| Category | Score | Evidence |
|---|---:|---|
| Scope coverage | 9.2 | Covers domain models, strategic DDD, tactical DDD, subdomain types, context maps, aggregates, aggregate roots, repositories, domain services, domain events, EventStorming, event-driven architecture, runtime guidance, Event Sourcing, CQRS, tooling and event catalogues. |
| Technical accuracy | 9.1 | Uses `[DDD-REFERENCE-2015]`, `[EVENTSTORMING-BRANDOLINI-2026]`, `[CNCF-CLOUDEVENTS-1.0.2]`, `[ASYNCAPI-3.1.0]` and `[DOMAIN-EVENT-TOOL-GUIDANCE-2026]`; corrects CloudEvents required attributes and replaces the earlier screening event name with `PaymentScreeningCompleted`. |
| Beginner comprehension | 9.0 | Uses Simple Online Store and Horizon Bank examples, clear command-event distinctions, reading guidance, accessibility text, comparison tables and a practical exercise. |
| Educational flow | 9.0 | Moves from domain meaning to strategic DDD, tactical DDD, events, discovery, event flow, runtime concerns, catalogue governance, tooling and review checks. |
| Diagram quality | 9.0 | Four figures render to SVG and PNG, avoid clipped text, use labelled direction, distinguish commands and events, and keep ownership boundaries visible. Wider event figures remain marked for final page-layout review. |
| Source and copyright discipline | 9.2 | Uses official or primary sources, paraphrases source material and uses original teaching diagrams. |
| Repository tracking | 9.2 | `BOOK_PLAN.md`, `STATUS.md`, `RESUME.md`, `CHANGELOG.md`, `SOURCE_REGISTER.md`, `DIAGRAM_REGISTER.md`, `GLOSSARY.md` and this gate file are updated. |

Average score: 9.1

No category is below 8.5.

## Required gate checks

| Check | Result | Evidence |
|---|---|---|
| Required sections complete | Pass | Chapter includes purpose, outcomes, prerequisites, artefacts, examples, source requirements, main sections, checklist and references. |
| Strategic DDD coverage | Pass | Chapter covers subdomains, bounded contexts, ubiquitous language and context maps. |
| Tactical DDD coverage | Pass | Chapter covers entities, value objects, aggregates, aggregate roots, repositories, domain services and domain events. |
| Subdomain types present | Pass | Core, supporting and generic subdomains are explained. |
| Context-map guidance strengthened | Pass | Upstream/downstream, Customer/Supplier, Conformist, Anti-Corruption Layer, Open Host Service, Published Language and Separate Ways are covered. |
| FIG-10-01 corrected | Pass | Figure stays within Ordering, includes Basket Item, Order Line, Product Snapshot, Delivery Address and external Payment Attempt and Shipment references with required cardinalities. |
| FIG-10-02 corrected | Pass | Figure shows relationship direction, translation boundaries and context-map pattern legend without implying microservice mapping. |
| FIG-10-03 corrected | Pass | Figure uses the requested command-event-policy chain and `PaymentScreeningCompleted`. |
| FIG-10-04 corrected | Pass | Figure distinguishes commands or synchronous requests, responses and published events; Event Platform is an intermediary, not owner. |
| Old screening event name removed | Pass | Search confirms the old event name no longer appears in manuscript, specifications or diagram source. |
| Runtime guidance present | Pass | Chapter covers at-least-once delivery, duplicates, idempotent consumers, ordering, correlation, causation, retries, dead letters, replay safety, schema compatibility, eventual consistency and privacy. |
| Event-driven architecture versus Event Sourcing and CQRS | Pass | Chapter distinguishes the three techniques. |
| CloudEvents correction present | Pass | Chapter states that `id`, `source`, `specversion` and `type` are required in CloudEvents 1.0.2 and `time` is optional. |
| Tool guidance present | Pass | Chapter covers Context Mapper, Miro or physical boards, PlantUML, diagrams.net, AsyncAPI Studio, AsyncAPI CLI and EventCatalog. |
| `PaymentPosted` event-catalogue entry present | Pass | Entry includes ownership, business meaning, trigger, producer, consumers, version, CloudEvents type, classification, retention, replay, compatibility, correlation, causation, ordering and support owner. |
| Diagrams registered | Pass | `DIAGRAM_REGISTER.md` includes `FIG-10-01` through `FIG-10-04` at `Review`. |
| Diagrams rendered | Pass | SVG and PNG outputs exist for all four Chapter 10 figures. |
| Diagram visual review | Pass | PNG previews inspected for clipping, overlapping labels, causal direction, command/event distinction, ownership boundaries, colour dependence and page-width readability. |

## Figure review notes

`FIG-10-01` stays within the Ordering bounded context. Payment Attempt and Shipment are external references. Basket to Basket Item and Order to Order Line are one or more; Order to Payment Attempt and Shipment are zero or more.

`FIG-10-02` uses short relationship IDs on arrows and a legend to prevent label overlap. Relationship direction, upstream/downstream dependency and translation boundaries are explicit.

`FIG-10-03` uses commands, events and policy labels. `PaymentScreeningCompleted` is the screening event. The board is an original teaching synthesis, not BPMN or a copied workshop board.

`FIG-10-04` uses sequence-style arrow labels to distinguish commands or synchronous requests, responses and published events. The Core Deposit System response is labelled as posting confirmed. Events originate from owning producers, and the Event Platform distributes events without owning their meaning.

## Render and visual validation record

| Figure ID | SVG export | PNG preview | Visual result |
|---|---|---|---|
| `FIG-10-01` | Present | Present | Pass, clear Ordering boundary and external references. |
| `FIG-10-02` | Present | Present | Pass, no label overlap after relationship-ID layout correction. |
| `FIG-10-03` | Present | Present | Pass, command/event/policy distinction is readable. |
| `FIG-10-04` | Present | Present | Pass, arrow types and event ownership are readable. |

## Remaining risks

- Final book-page layout review remains pending for all Chapter 10 diagrams, especially wider event-oriented figures.
- Later integration and BIAN event chapters should reuse the Chapter 10 command/event vocabulary consistently.

## Gate decision

Chapter 10 is `Approved` by the author. The final quality score is 9.1, no category is below 8.5, all four figures render to SVG and PNG, source versions are recorded, the requested review corrections are implemented and repository checks pass. `FIG-10-01` through `FIG-10-04` remain at `Review`.
