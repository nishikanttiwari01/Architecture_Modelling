# FIG-24-01: Discovery Evidence and Recommended Model Set

## Purpose

Show how focused discovery views turn evidence into a governed readiness decision without implying a mandatory linear method, in a portrait layout readable at normal book-page width.

## Audience

Beginner architects, business analysts, sponsors, product owners and reviewers.

## Question answered

Which small set of models helps a team define a problem and decide what to do next?

## Notation

PlantUML activity-style flow with labelled, directional arrows. The author authorised specification, source and export production without an approval pause on 2026-07-11. This authorisation permits production, not approval.

## Required elements

- Problem, outcome and evidence starting point.
- Stakeholder and concerns, current-state context, capability assessment, process discovery, and constraints and assumptions views.
- Synthesis of findings, gaps and candidate directions.
- Readiness decision with proceed, loop, narrow, pause or stop outcomes.

## Required relationships

- Starting evidence connects to each focused discovery view.
- Each focused view contributes labelled evidence to synthesis.
- Synthesis leads to the readiness decision.
- Feedback from unresolved uncertainty to renewed evidence gathering.

## Main flow or structure

A top-to-bottom portrait flow branches from the starting evidence to five separate, vertically stacked focused-view nodes. Each node shows its discovery question and view name, and each contributes separately to synthesis before the readiness decision.

## Alternative and exception flows

When uncertainty remains, the feedback arrow returns the team to framing and evidence gathering. Teams select only the views their concerns require.

## Scope

The figure is a discovery model-set guide.

## Exclusions

It is not a prescribed project method, detailed notation example, requirements model or solution architecture.

## Accessibility requirements

- Text carries all meaning; colour is supporting only.
- All arrows are directional and labelled.
- Layout remains readable at book-page width.
- Export width should be approximately 800 pixels or less, with source text remaining readable when displayed at 700 to 750 pixels wide.

## Review criteria

- No clipping, overlap, unreadable font, excessive crossings or ambiguous direction.
- Caption, accessibility text and chapter terminology agree.
- Figure status reaches no higher than `Review`.

## Production review

The first exported layout was 1520 pixels wide and was not suitable for normal single-page text width. A later 717-pixel layout met page width but incorrectly aggregated the five required view nodes into one box. The next separate-node version omitted relationship labels. On 2026-07-11 the figure was rerendered with `informs` on all five evidence-to-view arrows and `contributes` on all five view-to-synthesis arrows. The final PNG is 735 by 656 pixels and the SVG view is 735 by 657. Inspection at native intended width confirmed every label is readable, with no clipping, overlap or excessive crossings, clear arrow direction and sufficient contrast. This correction does not constitute author approval.

## Source references

- ISO-42010
- C4-OFFICIAL
- OPEN-GROUP-BIZARCH-GUIDES-2022
- OMG-BPMN
