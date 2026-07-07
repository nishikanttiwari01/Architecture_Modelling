# FIG-17-01: Choosing the Right User and System Interaction View

## Purpose

Help beginner architects choose an interaction view based on the question they are trying to answer, not on personal notation preference or the diagram a team already has.

## Audience

Beginner architects, practising architects, product owners, analysts, developers, testers, process reviewers and technical reviewers who need a quick selection guide for user and system interaction views.

## Question answered

Which interaction view should an architect try first when the question is about actor goals, user experience, visible screen flow, message order, runtime collaboration, business hand-offs, workflow logic, lifecycle states or API behaviour?

## Notation

PlantUML mind-map selection guide used as an original selection figure.

## Required elements

- A clear start point: "Start with the interaction question".
- A compact sequence of question prompts that act as a first filter.
- One view recommendation for each prompt.
- Short labels that remain readable at book-page width.
- A concise caption matching the chapter text.

## Required relationships

- The mind map should group actor, user-centred, screen, sequence, process, workflow, state and API interaction questions.
- Each matching branch should point to a suggested view.
- Related questions should remain close enough for the reader to compare them.
- The API interaction branch should show the boundary where the question moves towards Chapter 18 integration detail.
- The final fallback should guide the reader to clarify the modelling purpose if none of the questions fit.

## Main flow or structure

Start with the interaction question, scan the grouped concerns, and choose the view linked to the first matching concern. The map covers actor goals and customer experience, visible interface flow, runtime message order, C4 dynamic collaboration, business process hand-offs, action flow, lifecycle state and API interaction behaviour.

## Alternative and exception flows

If none of the listed concerns fits, the figure directs the reader to clarify the actor, boundary and decision before choosing a notation. Detailed notation-specific alternatives remain in the chapter tables and the referenced UML, C4 and BPMN chapters.

## Scope

The figure covers the Chapter 17 selection choices:

- use case diagram
- user journey
- service blueprint
- wireframe or screen flow
- UML sequence diagram
- C4 dynamic view
- BPMN collaboration
- activity diagram
- state machine
- API interaction view

The figure does not teach UML, C4 or BPMN notation syntax.

## Exclusions

The figure excludes detailed user interface design, complete service-design artefacts, full BPMN notation, full UML syntax, API contract specification, event choreography detail, data modelling, security modelling, infrastructure topology and implementation procedures.

## Accessibility requirements

- Colour may support grouping, but labels must carry the meaning.
- All shapes must have readable text.
- Direction must be clear from arrows and branch labels.
- The SVG must avoid clipped text, overlapping labels and dense crossings.
- The figure must remain readable when scaled to a normal manuscript page width.

## Source references

The figure is an original selection guide derived from Chapter 17. It uses the registered source context for interaction-related modelling:

- OMG-UML
- C4-OFFICIAL
- OMG-BPMN

## Review criteria

- The PlantUML source renders to SVG.
- The SVG exists under `diagrams/exported/svg/`.
- The diagram register points to the source and SVG export.
- Chapter 17 references the figure with the required caption.
- The figure status is set to `Review` in the diagram register after rendering and inspection.
