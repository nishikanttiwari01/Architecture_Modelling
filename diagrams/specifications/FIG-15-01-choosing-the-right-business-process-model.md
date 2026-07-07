# FIG-15-01: Choosing the Right Business Process Model

## Purpose

Help beginner architects choose a process-related model based on the question they are trying to answer, not on personal notation preference.

## Audience

Beginner architects, practising architects, reviewers and delivery teams who need a quick selection guide for business process modelling views.

## Question answered

Which process-related model should an architect try first when the question is about process landscape, value progression, hand-offs, flow, exceptions, responsibility, decision logic, system behaviour or software interaction?

## Notation

Mermaid flowchart used as an original decision guide.

## Scope

The figure covers the Chapter 15 selection choices:

- process architecture
- value stream
- BPMN process
- BPMN collaboration
- focused BPMN exception view
- responsibility matrix or swimlanes
- DMN decision model
- UML activity
- UML sequence or C4 dynamic view

The figure does not teach BPMN, UML, DMN or C4 notation syntax.

## Required elements

- A clear start point: "Start with the question".
- A compact sequence of question prompts that act as a first filter.
- One model recommendation for each prompt.
- Short labels that remain readable at book-page width.
- A concise caption matching the chapter text.

## Required relationships

- The decision path should move from broad process landscape questions to narrower interaction and behaviour questions.
- Each matching branch should point to a suggested model.
- Each non-matching branch should continue to the next question.
- The final fallback should guide the reader to discuss the modelling purpose if none of the questions fit.

## Main flow or structure

Start with the architecture question, test the process concern in order, and choose the model linked to the first matching concern. The path moves from business process landscape and value progression through collaboration, exception, responsibility and decision concerns, then into system behaviour and software interaction concerns.

## Alternative and exception flows

If none of the listed concerns fits, the figure directs the reader to clarify the modelling purpose before choosing a notation. Detailed notation-specific alternatives remain in the chapter tables and referenced notation chapters.

## Exclusions

The figure excludes BPMN syntax, DMN table structure, UML activity syntax, C4 notation details, process procedure steps, service design and implementation flow.

## Accessibility requirements

- Colour may support grouping, but labels must carry the meaning.
- All shapes must have readable text.
- Direction must be clear from arrows and labels.
- The SVG must avoid clipped text, overlapping labels and dense crossings.
- The figure must remain readable when scaled to a normal manuscript page width.

## Source references

The figure is an original selection guide derived from Chapter 15. It uses the registered source context for business process and decision modelling:

- OMG-BPMN
- OMG-UML
- OMG-DMN-1.5
- OPEN-GROUP-BIZARCH-GUIDES-2022

## Review criteria

- The Mermaid source renders to SVG.
- The SVG exists under `diagrams/exported/svg/`.
- The diagram register points to the source and SVG export.
- Chapter 15 references the figure with the required caption.
- The figure status is set to `Review` in the diagram register after rendering and inspection.
