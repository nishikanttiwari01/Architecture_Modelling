# FIG-22-01: Choosing the Right Transformation and Migration View

## Purpose

Help beginner architects select a first transformation or migration view from the question they need to answer.

## Audience

Architects, transformation leads, sponsors, delivery, operations, data, security, risk and service owners.

## Question answered

Which transformation or migration view should an architect try first?

## Notation

PlantUML activity-style decision guide with explicit directional, labelled arrows. The author authorised specification creation and source/export production without an approval pause on 2026-07-11. This authorisation permits production, not approval.

## Required elements

- Start point labelled `Start with the transformation question`.
- Nine concise questions and one first-choice view for each.
- Fallback asking for scope, state, audience and decision to be clarified.

## Required relationships

- Current evidence to current-state baseline.
- Intended state to target architecture.
- Differences to gap analysis.
- Viable intermediate operation to transition architecture.
- Ordering constraints to dependency map.
- Grouping and timing to roadmap or migration-wave view.
- Service or data movement to cutover or parallel-operation view.
- Retirement evidence to decommission view.
- Outcomes or uncertainty to benefit map or risk view.

## Main flow or structure

A left-to-right guide connects one starting question to nine focused first choices through labelled arrows.

## Alternative and exception flows

When several questions apply, create separate linked views and reuse stable identifiers. When no question fits, clarify scope, state, audience and decision before drawing.

## Scope

Current, target and transition states, gaps, dependencies, sequencing, movement, retirement, benefits and risks.

## Exclusions

The figure is a first filter. It does not prescribe a programme method, guarantee dates or benefits, replace detailed design or runbooks, or combine every concern into one view.

## Accessibility requirements

- Text carries all meaning; colour is supporting only.
- Arrows are directional and labelled.

## Review criteria

- The figure must render to SVG and PNG with no clipping, overlap, unreadable text, excessive crossings or ambiguous direction.
- Caption, accessibility text and terminology must agree with Chapter 22.
- Register status reaches no higher than `Review`.

## Source references

- OPEN-GROUP-ARCHIMATE-4
