# FIG-19-01: Choosing the Right Data Architecture View

## Purpose

Help beginner architects choose a data architecture view based on the question they
need to answer about meaning, structure, implementation, movement, lineage, ownership,
lifecycle or governed shared data.

## Audience

Beginner and practising architects, data architects, business analysts, developers,
data owners, data stewards, integration teams, security and privacy reviewers, reporting
teams and risk reviewers.

## Question answered

Which data architecture view should an architect try first for the current question?

## Notation

PlantUML decision guide using simple shapes and labelled branches. Source and export are
authorised for production using the repository's shared PlantUML style.

## Production authorisation

- **Authorisation date:** 2026-07-11
- **Authorisation:** The author explicitly instructed Codex to produce and integrate the
  Chapter 19 diagram without waiting for a separate approval step.
- **Status effect:** This authorises source creation and rendering. It does not grant
  final approval; the rendered figure proceeds to `Review`.

## Required elements

- A start point labelled `Start with the data question`.
- Eight concise question prompts.
- One first-choice view for each prompt.
- A reminder to state audience, boundary and abstraction level.
- A fallback directing the reader to clarify the decision before drawing.

## Required relationships

- Business meaning points to a conceptual information view.
- Precise technology-independent structure points to a logical ERD.
- Storage implementation points to a physical data model.
- Movement, transformation and stores point to a DFD.
- Origin, transformation and downstream use point to a lineage view.
- Accountability and stewardship point to an ownership matrix.
- Creation through disposal points to a lifecycle view.
- Shared subjects, classifications and controlled values point to a master/reference
  data catalogue.

## Main flow or structure

The reader starts with the data question, scans grouped concerns and follows the first
matching branch to a suggested view. The guide is a compact first filter; the Chapter 19
selection table provides fuller audience, element and companion-view guidance.

## Alternative and exception flows

If more than one concern applies, the guide advises separate linked views using stable
names and identifiers. If no concern fits, it directs the reader to clarify the data
boundary, audience, level and architecture decision.

## Scope

The figure covers conceptual information views, logical ERDs, physical data models,
DFDs, lineage views, ownership matrices, lifecycle views and master/reference data
catalogues.

## Exclusions

The figure does not teach ERD or DFD notation, define database products, prescribe a
universal data governance operating model, state jurisdiction-specific privacy or
retention rules, or replace detailed metadata and contract specifications.

## Accessibility requirements

- Colour may support grouping, but labels must carry the meaning.
- Text must remain readable at normal book-page width.
- Direction must be visible through arrows and branch labels.
- The SVG must avoid clipped text, overlapping labels and dense crossings.
- The figure must be understandable with the Chapter 19 prose and caption without
  relying on colour.

## Source references

The figure is an original selection guide derived from Chapter 19. Its source context is:

- CHEN-ER-1976
- CODD-RELATIONAL-1970
- DEMARCO-STRUCTURED-ANALYSIS-1979
- W3C-PROV-DM-2013
- DAMA-DMBOK2-2017

## Review criteria

- Production authorisation is recorded before diagram source creation.
- PlantUML source renders to SVG after sign-off.
- The SVG exists under `diagrams/exported/svg/` after rendering.
- The diagram register points to source and SVG paths after rendering.
- Chapter 19 references the figure with a meaningful caption after rendering.
- The figure remains readable at intended page width and passes visual inspection.
- The register status moves only to `Review` after rendering and inspection; final
  approval remains an author-only action.

## Production and visual review record

- **Production date:** 2026-07-11
- **Editable source:** `diagrams/source/plantuml/FIG-19-01-choosing-the-right-data-architecture-view.puml`
- **Publication export:** `diagrams/exported/svg/FIG-19-01-choosing-the-right-data-architecture-view.svg`
- **Review preview:** `diagrams/exported/png/FIG-19-01-choosing-the-right-data-architecture-view.png`
- **Arrowed-layout rerender:** 2026-07-11, replacing the original mind-map layout.
- **Rendered SVG size:** 783 × 1180 pixels; the PNG review preview is 782 × 1179
  pixels.
- **Visual result:** Pass for `Review`. Every route uses visible arrowheads. The `yes`
  and `no` labels make branch direction explicit. No clipped text, overlapping labels,
  connector crossings or unreadable fonts were found. Contrast is sufficient,
  terminology matches Chapter 19, and the portrait layout remains readable at intended
  page width.
- **Approval boundary:** Production and visual review do not constitute final author
  approval.
