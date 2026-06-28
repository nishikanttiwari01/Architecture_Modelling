# FIG-05-01: C4 levels of zoom

## Purpose

Introduce the four main C4 levels as a progressive zoom from broad context to implementation detail.

## Audience

Beginners who are meeting C4 for the first time.

## Question answered

How does C4 help a reader move from a whole software system to more detailed design views?

## Notation

C4 explanatory diagram using PlantUML.

## Required elements

- System Context
- Container
- Component
- Code
- Short description for each level

## Required relationships

- A visual zoom relationship from System Context to Container to Component to Code.
- No runtime or dependency arrows.

## Main flow or structure

Show four labelled boxes from left to right. Each box states the level name and the main question it answers.

## Alternative and exception flows

None.

## Scope

Conceptual explanation of C4 levels.

## Exclusions

Do not include Horizon Bank or online store details. Do not imply that every project needs all four levels.

## Accessibility requirements

Use text labels inside each level. Do not rely on colour alone. Keep font sizes readable at book-page width.

## Source references

- `[C4-OFFICIAL]`

## Review criteria

- The four levels are in the correct order.
- The labels are concise.
- The diagram does not look like a runtime sequence.
- The caption and chapter text explain that Code level is optional for many architecture discussions.

## Authorisation note

The author instructed Codex to proceed with the Chapter 5 prototype on 2026-06-28. This authorises prototype production but does not grant final figure sign-off.
