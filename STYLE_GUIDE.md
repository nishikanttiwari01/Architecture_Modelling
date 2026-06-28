# Style Guide

## Voice

Write like an expert teacher helping a capable beginner. Be precise, practical and calm. Avoid sounding like a standards document, marketing brochure or generated summary.

## Core teaching sequence

1. Begin with a plain-language explanation.
2. State the question the model answers.
3. Introduce formal terminology.
4. Explain the minimum essential notation.
5. Show a simple example.
6. Show a banking or enterprise example.
7. Compare it with nearby alternatives.
8. Explain mistakes and review criteria.

## Language

- Use British English: `modelling`, `organisation`, `authorisation`, `licence` as a noun.
- Do not use em dashes.
- Prefer direct sentences and concrete verbs.
- Define acronyms at first use in every chapter that may be read independently.
- Avoid filler such as `simply`, `obviously`, `clearly`, `basically` and `as we all know`.
- Avoid unexplained jargon.
- Avoid anthropomorphising systems unless it aids a beginner example and remains accurate.

## Paragraphs and headings

- Keep most paragraphs between two and five sentences.
- Use one idea per paragraph.
- Use descriptive headings that reveal the question or topic.
- Do not skip heading levels.
- Avoid heading-only sections with no explanatory text.

## Definitions

Use this pattern where useful:

> **Term:** A concise explanation in plain language, followed by any important formal nuance.

Distinguish:

- Standard or official definition
- Practical interpretation
- Author recommendation

## Examples

- Use the simple online store for first exposure.
- Use Horizon Bank for realistic architecture application.
- Maintain consistent names from the example files.
- Explain what the example deliberately omits.
- Never imply that one sample design is universally correct.

## Tables

Use tables for comparison, selection, mapping and checklists. Do not use tables for long narrative explanations. Keep cell content concise and explain the most important conclusions in prose.

## Lists

Use lists for true sets, sequences or checklists. Do not replace connected reasoning with excessive bullet points.

## Code and notation

- Use fenced code blocks with a language identifier when possible.
- Text diagrams may use `text`, Mermaid or PlantUML.
- Explain diagrams in surrounding prose; never rely on the image alone.
- Use stable identifiers for figures, tables and decisions.

## Figure captions

Use:

`Figure FIG-05-02. C4 container view of the online store. It shows the major executable units and their responsibilities, not individual classes.`

A caption should state what the figure communicates and any essential limitation.

## Comparisons

Comparisons should explain differences in purpose, abstraction and audience. Avoid declaring one notation universally better.

## Chapter endings

Every substantive chapter should end with:

- Key takeaways
- A short practical exercise
- A review checklist or self-test
- References or source notes where applicable

## Forbidden shortcuts

- Do not copy official diagrams.
- Do not present BIAN Service Domains as deployable services without qualification.
- Do not call a C4 container a Docker container unless it is actually implemented as one.
- Do not call every business activity a capability.
- Do not mix process sequence with structural decomposition without explaining the viewpoint.
