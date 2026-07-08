# Chapter 18 Quality Gate Review

- **Chapter:** 18, Modelling Integration and Runtime Behaviour
- **Review date:** 2026-07-08
- **Reviewer:** Codex
- **Status:** Ready for Author Approval

## Review summary

Chapter 18 is drafted as a Part III selection chapter. It helps readers choose between
integration context views, API interaction views, message-flow views, UML sequence
diagrams, C4 dynamic diagrams, event-flow views, queue and asynchronous processing
views, error and retry views, interface catalogues and data-flow views. It reuses
established source notes from UML, C4, BPMN, CloudEvents and AsyncAPI rather than
re-teaching those notations.

`FIG-18-01` is registered and specified. Source and export are intentionally deferred
until author approval of the diagram specification, following the repository diagram
workflow.

## Review passes

| Review area | Result | Notes |
|---|---|---|
| Technical accuracy | Pass | Source keys reuse recorded UML, C4, BPMN, CloudEvents and AsyncAPI notes. The chapter distinguishes synchronous request-response, asynchronous messaging, queues, events and data-flow concerns. |
| Beginner comprehension | Pass | Each section begins with the plain-language question before formal terminology. The examples use the Simple Online Store and Horizon Bank. |
| Educational flow | Pass | The chapter moves from integration question, through view types, to selection table, worked examples, mistakes, checklist and exercise. |
| Terminology and cross-chapter consistency | Pass | Uses controlled names from `examples/` and cross-references Chapters 4, 5, 6, 10, 17 and 19. New glossary terms were added for integration-specific concepts. |
| Diagram quality and accessibility | Deferred | `FIG-18-01` has a complete specification, but source/export are pending author approval. No rendered diagram exists yet. |
| Source and copyright verification | Pass | No standards text or diagrams are copied. Source keys point to existing source notes and `SOURCE_REGISTER.md`. |
| Copy-editing | Pass | British English used. No em dashes intentionally introduced. |

## Open author decisions

- Review and approve or revise the `FIG-18-01` diagram specification before Codex creates
  diagram source.
- Accept, revise or reject proposed scope decision `DEC-026`.

## Quality-gate checklist

- [x] Required sections are complete.
- [x] Claims requiring sources have citations or source notes.
- [x] Required diagram is registered and explicitly deferred pending author approval of
  the specification.
- [x] Terminology is aligned with the glossary and example files.
- [x] Simple Online Store and Horizon Bank examples are consistent with repository
  naming.
- [x] Common mistakes are concrete and actionable.
- [x] Practical exercise includes suggested answers and review criteria.
- [x] Open issues are documented.
