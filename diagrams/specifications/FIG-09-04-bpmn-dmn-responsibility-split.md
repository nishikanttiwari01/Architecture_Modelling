# FIG-09-04: BPMN and DMN Responsibility Split

## Purpose

Show how BPMN process flow and DMN decision logic have different responsibilities when a process calls a decision.

## Audience

Beginners, process analysts, architects and implementation reviewers.

## Question answered

What should be shown in BPMN, what should be shown in DMN, and where does vendor-specific invocation configuration sit?

## Notation

PlantUML teaching illustration using separate BPMN and DMN responsibility areas. It is not a formal BPMN or DMN XML model.

## Required elements

- BPMN responsibility area.
- DMN responsibility area.
- Business Rule Task: Determine Payment Route.
- DMN decision: Determine Payment Route.
- Result-driven BPMN gateway.
- Note that technical binding is platform-specific.

## Required relationships

- BPMN task invokes the DMN decision with the label `invoke decision, platform-specific`.
- DMN decision returns a route result with the label `payment route result`.
- BPMN gateway branches on the result.

## Main flow or structure

Capture payment instruction, call the decision, return the route, then branch on the named result.

## Alternative and exception flows

The diagram shows the named result flowing back to the BPMN process. Detailed proceed, repair, manual review and rejection paths are outside the figure.

## Scope

Teaching view for Chapter 9 BPMN and DMN integration.

## Exclusions

Engine configuration, API protocols, retries, queues, BPMN XML, DMN XML and detailed payment operations workflow.

## Accessibility requirements

Use clear labels, readable relationship text and surrounding prose explaining the split.

## Source references

- `[OMG-DMN-1.5]`
- `[OMG-BPMN]`
- `[CAMUNDA-DMN-1.3-DOCS-2026]`

## Review criteria

- Does not claim OMG standardises direct executable binding.
- BPMN process responsibilities and DMN decision responsibilities are visually separate.
- The diagram status remains `Review`.

## Authorisation

The author authorised source creation through the Chapter 9 completion request on 2026-06-30.
