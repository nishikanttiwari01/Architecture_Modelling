# FIG-07-01: Retail Banking Capability Map

## Purpose

Show a simple ArchiMate-style capability map for retail banking.

## Audience

Beginners, business architects, enterprise architects and transformation sponsors.

## Question answered

Which stable retail banking abilities are in scope before the team discusses processes, applications or projects?

## Abstraction level

Strategy and capability overview. It shows abilities, not process order, organisation structure or system design.

## Notation

ArchiMate-style capability map using a small subset of strategy elements.

## Required elements

- Capability: Retail Banking
- Child capabilities: Customer Management, Account Management, Payments, Cards, Lending, Customer Support, Financial Crime Management
- Optional grouping cue for core customer-facing capabilities and control/support capabilities

## Required relationships

- Retail Banking is composed of the child capabilities.
- Financial Crime Management supports or serves relevant retail capabilities where shown.

## Main flow or structure

Use a map layout rather than a sequence. Put Retail Banking as the parent scope and arrange child capabilities in readable rows.

## Alternative and exception flows

Not applicable. This is a structural capability view, not a process view.

## Scope

Retail banking capabilities used as a beginner example for ArchiMate strategy concepts.

## Exclusions

No detailed value streams, BPMN process steps, application components, database entities, BIAN Service Domains or technology nodes.

## Accessibility requirements

Use high contrast, readable labels and no colour-only meaning. The figure must remain readable at book-page width.

## Source references

- `[OPEN-GROUP-ARCHIMATE-3.2]` for ArchiMate strategy concepts and relationships.
- `examples/horizon-bank/README.md` for Horizon Bank business lines and starting problems.

## Review criteria

- Capabilities read as abilities, not activities.
- The map does not imply detailed process sequence.
- Relationship meaning is clear from the caption and labels.
- Terminology matches `GLOSSARY.md`.
