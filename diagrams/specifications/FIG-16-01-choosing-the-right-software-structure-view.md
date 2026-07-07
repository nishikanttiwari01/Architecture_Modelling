# FIG-16-01: Choosing the Right Software Structure View

## Purpose

Help beginner architects choose a software-structure view based on the question they are trying to answer, not on personal notation preference or the diagram a team already has.

## Audience

Beginner architects, practising architects, technical leads, developers, reviewers and delivery teams who need a quick selection guide for software-structure views.

## Question answered

Which software-structure view should an architect try first when the question is about a wider system landscape, one system boundary, runnable parts, internal components, code packages, important classes, dependencies or runtime placement?

## Notation

Mermaid flowchart used as an original decision guide.

## Scope

The figure covers the Chapter 16 selection choices:

- system landscape
- system context
- container view
- component view
- package view
- class view
- dependency view
- deployment view as the boundary case when the question has moved from logical software structure to runtime placement

The figure does not teach C4 or Unified Modeling Language (UML) notation syntax.

## Required elements

- A clear start point: "Start with the architecture question".
- A compact sequence of question prompts that act as a first filter.
- One model recommendation for each prompt.
- Short labels that remain readable at book-page width.
- A concise caption matching the chapter text.

## Required relationships

- The decision path should move from broad estate and boundary questions to narrower internal design questions.
- Each matching branch should point to a suggested view.
- Each non-matching branch should continue to the next question.
- The deployment branch should show the logical-to-physical boundary rather than mixing runtime placement into the structural views.
- The final fallback should guide the reader to clarify the modelling purpose if none of the questions fit.

## Main flow or structure

Start with the architecture question, test the structural concern in order, and choose the view linked to the first matching concern. The path moves from enterprise system landscape and system context through container and component structure, then into code-level package, class and dependency concerns. Runtime placement is treated as a boundary case that points to a deployment view instead of overloading a software-structure diagram.

## Alternative and exception flows

If none of the listed concerns fits, the figure directs the reader to clarify the modelling purpose before choosing a notation. Detailed notation-specific alternatives remain in the chapter tables and the referenced C4 and UML chapters.

## Exclusions

The figure excludes C4 notation details, UML syntax, business process flow, data modelling, security modelling, infrastructure topology, implementation procedures and complete codebase documentation.

## Accessibility requirements

- Colour may support grouping, but labels must carry the meaning.
- All shapes must have readable text.
- Direction must be clear from arrows and labels.
- The SVG must avoid clipped text, overlapping labels and dense crossings.
- The figure must remain readable when scaled to a normal manuscript page width.

## Source references

The figure is an original selection guide derived from Chapter 16. It uses the registered source context for software-structure modelling:

- C4-OFFICIAL
- OMG-UML

## Review criteria

- The Mermaid source renders to SVG.
- The SVG exists under `diagrams/exported/svg/`.
- The diagram register points to the source and SVG export.
- Chapter 16 references the figure with the required caption.
- The figure status is set to `Review` in the diagram register after rendering and inspection.
