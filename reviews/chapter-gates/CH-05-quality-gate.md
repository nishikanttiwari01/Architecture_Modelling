# Chapter 5 Quality Gate: The C4 Model

## Metadata

- **Chapter:** 5, The C4 Model
- **Review date:** 2026-06-28
- **Reviewer:** Codex
- **Status recommendation:** Ready for Author Approval

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.3 | Covers all planned C4 topics: context, container, component, code, dynamic, deployment, system landscape, UML comparison and mistakes. |
| Beginner clarity | 9.1 | Starts with zoom metaphor, then introduces formal C4 terms and simple examples. |
| Technical accuracy | 9.0 | Uses official C4 concepts and avoids the C4 container versus Docker mistake. |
| Expert depth | 8.8 | Good architecture guidance, with deeper C4 governance deferred to later chapters. |
| Logical flow | 9.1 | Moves from concept to online store to Horizon Bank and then comparison. |
| Examples and exercises | 9.0 | Simple Online Store and Horizon Bank examples are consistent with repository examples. |
| Diagram quality | 8.9 | Five rendered diagrams are readable; dynamic view has a dense but numbered interaction path. |
| Source quality | 8.7 | Uses official C4 and Structurizr sources; C4-PlantUML local extraction records version but not release date. |
| Consistency with rest of book | 9.0 | Uses glossary terms and preserves the distinction between software structure, process and deployment. |
| Writing and editorial quality | 9.1 | British English, no em dashes, clear headings and concise paragraphs. |

**Average score:** 9.0

## Review perspectives

### Beginner reader

The chapter introduces C4 through a simple zoom metaphor before formal terms. The online store example appears before Horizon Bank, which keeps the learning curve manageable.

### Solution architect

The chapter gives practical guidance on choosing context, container, component, dynamic and deployment views. It clearly separates software structure from business process and infrastructure detail.

### Enterprise architect

The system landscape section and Horizon Bank example connect C4 to broader enterprise modelling without overstretching C4 into business capability or BIAN modelling.

### Technical editor

The chapter avoids em dashes, unexplained jargon and marketing language. Acronyms are defined where first used in the chapter.

### Diagram reviewer

All five diagram specifications exist. PlantUML source and SVG exports exist. PNG previews were generated for visual review. The figures are readable and use text labels rather than colour alone.

### Source and copyright checker

Official and primary sources are recorded in `research/c4/` and `SOURCE_REGISTER.md`. No official diagrams or standards text are copied.

### Consistency reviewer

The chapter uses existing Simple Online Store and Horizon Bank names. It preserves the repository rule that a C4 container is not automatically Docker.

## Open issues

- Chapter 4 is still a stub, so the C4 versus UML section may need a later consistency pass after Chapter 4 is drafted.
- The local C4-PlantUML library records version `2.9.0`, but the local extracted file does not record its release date.
- The dynamic view should be revisited during final page-layout review because long horizontal figures may need scaling.

## Gate decision

No critical findings remain. Chapter 5 can move to `Ready for Author Approval`. The chapter and diagrams must not be marked `Approved` without explicit author action.
