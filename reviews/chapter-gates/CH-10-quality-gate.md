# Chapter 10 Quality Gate: Domain and Event Modelling

## Gate summary

- **Chapter:** 10, Domain and Event Modelling
- **Manuscript:** `manuscript/part-02-modelling-languages/10-domain-event-modelling.md`
- **Status:** Under Review
- **Current gate:** Chapter 10 has complete prose, source notes, registered source keys, diagram specifications and diagram-register entries. Diagram source and exports are deferred until author approval of `FIG-10-01` through `FIG-10-04` specifications.
- **Interim quality score:** 8.5
- **Diagram status:** `FIG-10-01` through `FIG-10-04` are `Planned`, not `Review` or `Approved`.

## Scorecard

| Category | Score | Evidence |
|---|---:|---|
| Scope coverage | 9.0 | Covers domain models, DDD vocabulary, subdomains, bounded contexts, context maps, aggregates, entities, value objects, domain events, EventStorming, commands, events, policies, read models, event-driven architecture diagrams and event catalogues. |
| Technical accuracy | 8.8 | Uses `[DDD-REFERENCE-2015]`, `[EVENTSTORMING-BRANDOLINI-2026]`, `[CNCF-CLOUDEVENTS-1.0.2]` and `[ASYNCAPI-3.1.0]`; distinguishes DDD and EventStorming from standards-body notations. |
| Beginner comprehension | 8.8 | Uses plain-language explanations, Simple Online Store and Horizon Bank examples, comparison tables, a practical exercise and command-versus-event naming guidance. |
| Educational flow | 8.7 | Moves from purpose and domain meaning to DDD terms, boundaries, events, event discovery, event architecture and governance. |
| Diagram readiness | 7.0 | Four diagram specifications exist and are registered, but no source files or rendered exports may be created until author approval of specifications. |
| Source and copyright discipline | 8.9 | Uses paraphrased source guidance and original planned diagrams; no standards text or external diagrams are copied. |
| Repository tracking | 8.8 | `BOOK_PLAN.md`, `STATUS.md`, `RESUME.md`, `CHANGELOG.md`, `DIAGRAM_REGISTER.md` and this gate file are updated. |

Average score: 8.5

Diagram readiness is below final approval level because the repository's specification-first gate intentionally prevents source creation until author approval.

## Required gate checks

| Check | Result | Evidence |
|---|---|---|
| Required sections complete | Pass | Chapter includes purpose, outcomes, prerequisites, artefacts, examples, source requirements, main sections, checklist and references. |
| DDD source basis present | Pass | Chapter uses `[DDD-REFERENCE-2015]` and states that DDD is not a standards-body notation. |
| EventStorming source basis present | Pass | Chapter uses `[EVENTSTORMING-BRANDOLINI-2026]` and treats EventStorming as a collaborative method rather than formal notation. |
| CloudEvents scope correct | Pass | Chapter uses CloudEvents for envelope metadata and avoids implying that it defines business event meaning. |
| AsyncAPI scope correct | Pass | Chapter uses AsyncAPI for message-driven API contracts and distinguishes it from discovery methods. |
| Bounded context caution present | Pass | Chapter states that a bounded context is not automatically a microservice, database, team or deployment unit. |
| Command and event distinction present | Pass | Chapter distinguishes imperative command names from past-tense event names. |
| Event catalogue governance present | Pass | Chapter records ownership, producer, consumers, schema, classification, retention and compatibility concerns. |
| Diagram specifications created | Pass | Specifications exist for `FIG-10-01` through `FIG-10-04`. |
| Diagram register updated | Pass | `DIAGRAM_REGISTER.md` includes the four Chapter 10 planned figures and asset details. |
| Diagram source created | Deferred | Source creation awaits author approval of the specifications. |
| Diagram exports created | Deferred | SVG and PNG exports await source creation. |

## Figure review notes

`FIG-10-01` is specified as a conceptual domain model for the Simple Online Store order domain. It must avoid database and implementation detail.

`FIG-10-02` is specified as a context map for the Simple Online Store. It must not imply that one bounded context equals one microservice.

`FIG-10-03` is specified as an EventStorming-style teaching illustration for Horizon Bank payment handling. It must use original content and avoid presenting workshop conventions as a formal standard.

`FIG-10-04` is specified as an event-flow architecture view for Horizon Bank payments. It must distinguish commands or requests from published events and must not turn into a deployment topology.

## Remaining risks

- Author approval of the Chapter 10 diagram specifications is required before diagram source files can be created.
- The final chapter score cannot reach the Chapter 5 prototype target until figures are rendered, visually reviewed and integrated into the chapter.
- Event-driven architecture examples should be rechecked during later integration chapters to avoid duplication or contradiction.

## Gate decision

Chapter 10 is suitable to remain at `Under Review`. The prose draft and diagram specifications are complete, but the chapter is not ready for author approval until the four diagram specifications are approved, source files and exports are created, visual review is completed and repository checks pass after those assets are added.
