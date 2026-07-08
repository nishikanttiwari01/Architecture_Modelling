# FIG-18-01: Choosing the Right Integration and Runtime Behaviour View

## Purpose

Help beginner architects choose an integration or runtime behaviour view based on the
question they are trying to answer, not on the integration technology a team happens to
prefer.

## Audience

Beginner architects, practising architects, integration architects, solution architects,
developers, testers, application owners, platform teams, operations teams and risk
reviewers.

## Question answered

Which integration or runtime behaviour view should an architect try first when the
question is about system dependency, API behaviour, message order, C4 runtime
collaboration, event publication, queues, failure behaviour, interface governance or
data movement?

## Notation

PlantUML decision guide, using simple shapes and labelled branches. Source and export
are deferred until author sign-off on this specification.

## Required elements

- A clear start point: "Start with the integration question".
- A compact sequence of question prompts that act as a first filter.
- One view recommendation for each prompt.
- Short labels that remain readable at book-page width.
- A concise caption matching the Chapter 18 text.

## Required relationships

- The guide should separate broad dependency, API, message-order, runtime
  collaboration, event, queue, failure, catalogue and data-movement questions.
- Each matching branch should point to a suggested view.
- Related questions should remain close enough for the reader to compare them.
- The data-movement branch should point towards Chapter 19 rather than re-teach data
  architecture.
- The final fallback should guide the reader to clarify system boundary, ownership and
  runtime decision if none of the questions fit.

## Main flow or structure

Start with the integration question, scan the grouped concerns, and choose the view
linked to the first matching concern. The map covers integration context views, API
interaction views, message-flow views, UML sequence diagrams, C4 dynamic diagrams,
event-flow views, queue or asynchronous processing views, error and retry views,
interface catalogues and data-flow views.

## Alternative and exception flows

If none of the listed concerns fits, the figure directs the reader to clarify the
system boundary, integration ownership, runtime behaviour and review decision before
choosing a notation. Detailed notation-specific alternatives remain in the chapter table
and in the referenced UML, C4, BPMN, domain-event and data-modelling chapters.

## Scope

The figure covers the Chapter 18 selection choices:

- integration context view
- API interaction view
- message-flow view
- UML sequence diagram
- C4 dynamic diagram
- event-flow view
- queue or asynchronous processing view
- error and retry view
- interface catalogue
- data-flow view

The figure does not teach UML, C4, BPMN, CloudEvents or AsyncAPI syntax.

## Exclusions

The figure excludes detailed API contract specification, full event schema design,
physical network topology, detailed infrastructure placement, security threat modelling,
data modelling beyond the view-selection boundary, product-specific integration
platform configuration and operational runbook procedures.

## Accessibility requirements

- Colour may support grouping, but labels must carry the meaning.
- All shapes must have readable text.
- Direction must be clear from arrows and branch labels.
- The SVG must avoid clipped text, overlapping labels and dense crossings.
- The figure must remain readable when scaled to a normal manuscript page width.

## Source references

The figure is an original selection guide derived from Chapter 18. It uses the
registered source context for integration and runtime behaviour:

- OMG-UML
- C4-OFFICIAL
- OMG-BPMN
- CNCF-CLOUDEVENTS-1.0.2
- ASYNCAPI-3.1.0

## Review criteria

- The author has signed off this specification before diagram source is created.
- The PlantUML source renders to SVG after sign-off.
- The SVG exists under `diagrams/exported/svg/` after rendering.
- The diagram register points to the source and SVG export after rendering.
- Chapter 18 references the figure with the required caption after rendering.
- The figure status is set to `Review` in the diagram register after rendering and
  inspection.
