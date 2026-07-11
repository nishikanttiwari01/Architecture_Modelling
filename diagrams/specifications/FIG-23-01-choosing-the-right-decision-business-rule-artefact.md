# FIG-23-01: Choosing the Right Decision and Business-Rule Artefact

## Purpose

Help beginner architects select a first artefact from the decision or rule question.

## Audience

Architects, business analysts, process designers, product and policy owners, developers, risk and operations reviewers.

## Question answered

Which decision or business-rule artefact should a modeller try first?

## Notation

PlantUML activity-style selection guide with explicit directional, labelled arrows. The author authorised specification creation and source/export production without an approval pause on 2026-07-11. This authorisation permits production, not approval.

## Production history correction

An initial draft PlantUML source and export were generated before this specification file was completed because of a workflow error on 2026-07-11. The specification was subsequently completed and reviewed against the chapter, register and repository diagram rules. The source and exports will be regenerated from this completed specification after the specification correction is committed. This record is transparent remediation of the sequence error; it does not approve the figure.

## Required elements

- Start point labelled `Start with the decision question`.

## Required relationships

- Authority to policy statement or Knowledge Source.
- Condition combinations to decision table.
- Ordered questions to decision tree.
- Decision dependencies to DMN DRD.
- Work before or after result to BPMN process view.
- Architecture rationale to ADR.
- Alternative comparison to trade-off matrix.
- Fallback to clarification of decision, audience and evidence.

## Main flow or structure

A left-to-right guide connects the starting question to seven focused first choices through labelled arrows.

## Alternative and exception flows

When several questions apply, create separate linked artefacts. When no question fits, clarify the decision, audience and evidence.

## Scope

Decision authority, logic, dependency, surrounding process, architecture rationale and comparison.

## Exclusions

This is a first filter. It does not reproduce formal notation, contain executable rules, replace governance, or imply that one artefact answers every concern.

## Accessibility requirements

- Text carries all meaning; colour is supporting only.
- Arrows are directional and labelled.

## Review criteria

- SVG and PNG must have no clipping, overlap, unreadable text, excessive crossings or ambiguous direction.
- Caption, accessibility text and terminology must agree with Chapter 23.
- Register status reaches no higher than `Review`.

## Source references

- OMG-DMN-1.5
- OMG-BPMN
- NYGARD-ADR-2011
