# Chapter 5 Quality Gate: The C4 Model

## Metadata

- **Chapter:** 5, The C4 Model
- **Review date:** 2026-06-28
- **Reviewer:** Codex
- **Status recommendation:** Approved by author
- **Author verdict:** Chapter 5 passes as the prototype chapter at `9.1/10`. It is approved as the structural and writing model for subsequent chapters. Diagrams remain `Review` until SVG visual inspection in VS Code is complete.

## Quality scores

| Area | Score | Notes |
|---|---:|---|
| Scope coverage | 9.3 | Covers C4 context, container, component, code, dynamic, deployment and system landscape views, plus UML comparison, mistakes, exercise and review checklist. |
| Beginner clarity | 9.2 | Starts with the zoom idea, explains plain-language terms before formal detail and uses the online store before the banking example. |
| Technical accuracy | 9.2 | Corrects the official C4 component meaning, keeps C4 containers distinct from Docker containers and keeps deployment nodes separate from logical containers. |
| Expert depth | 8.9 | Gives practical architecture guidance across software, enterprise and deployment views. Deeper C4 governance and tooling patterns remain appropriate for later chapters. |
| Logical flow | 9.1 | Moves from vocabulary to C4 levels, then supporting views, Horizon Bank application and comparison with UML. |
| Examples and exercises | 9.2 | Uses Simple Online Store and Horizon Bank consistently, with context, container, component, dynamic, deployment and landscape coverage. |
| Diagram quality | 9.0 | Eight diagram specifications, PlantUML sources, SVG exports and PNG previews exist. The longer deployment and landscape views are readable, with final page-layout scaling still worth checking. |
| Source quality | 8.9 | Uses official C4, Structurizr and local C4-PlantUML source notes. The C4-PlantUML local extraction records version `2.9.0`, but not the upstream release date. |
| Consistency with rest of book | 9.1 | Follows the repository examples, glossary terms, diagram workflow and author-only approval rules. |
| Writing and editorial quality | 9.2 | British English, concise paragraphs, no reader-facing drafting headings and no em dashes detected in the chapter text. |

**Average score:** 9.1

## Review perspectives

### Beginner reader

The chapter explains C4 as levels of zoom and introduces one concept at a time. The online store example makes context, container and component views concrete before the reader reaches the more complex Horizon Bank material.

### Solution architect

The chapter now provides usable guidance for context, container, component, dynamic and deployment views. The component section is technically sharper because it explains that components sit inside one deployable container.

### Enterprise architect

The system landscape figure and explanation show how C4 can support wider estate conversations without turning C4 into capability mapping, BIAN modelling or process modelling.

### Technical editor

The reader-facing draft scaffolding has been removed. The references section preserves source keys and connects source presentation to Appendix H.

### Diagram reviewer

All eight Chapter 5 diagrams have specifications, PlantUML source, SVG exports and PNG review previews. Visual inspection found no clipped text, no unreadable labels and no incorrect arrow direction. `FIG-05-07` and `FIG-05-08` are long horizontal figures, so they should be checked again during final page-layout production.

### Source and copyright checker

Official and primary C4-related sources are recorded in `research/c4/` and `SOURCE_REGISTER.md`. The chapter paraphrases source material and does not reproduce official diagrams or long copyrighted text.

### Consistency reviewer

The chapter uses existing Simple Online Store and Horizon Bank names and keeps software structure, runtime interaction, deployment and enterprise landscape concerns separate.

## Open issues

- Chapter 4 is still a stub, so the C4 versus UML section should receive another consistency pass after Chapter 4 is drafted.
- The local C4-PlantUML library records version `2.9.0`, but the local extracted file does not record its upstream release date.
- Long horizontal figures should be checked again during final page-layout review.

## Gate decision

The corrected chapter meets the quality-gate threshold: average score is at least 9.0 and no category is below 8.5. The author approved Chapter 5 as the prototype structural and writing model. Chapter 5 diagrams remain `Review` until SVG visual inspection in VS Code is complete.
