# FIG-07-01: Retail Banking Capability Map

## Purpose

Show a small ArchiMate 4 strategy-domain capability map for retail banking.

## Audience

Beginners, business architects, enterprise architects and transformation sponsors.

## Question answered

Which stable retail banking abilities are in scope before the team discusses process sequence, applications, projects or technology?

Decision or concern: decide capability scope before lower-level modelling begins.

## Required elements

ArchiMate 4 elements:

- Capability: Retail Banking
- Capabilities: Customer Management, Account Management, Payments, Cards, Lending, Customer Support, Financial Crime Management
- Optional Course of Action: Consolidate customer identity
- Optional Outcome: Reduced duplicate customer capture

## Required relationships

Relationship types and directions:

- Composition from Retail Banking capability to each child capability.
- Influence from Consolidate customer identity course of action to Reduced duplicate customer capture outcome, if those optional elements are included.
- Do not use Serving between Financial Crime Management and Customer Management unless a later licensed ArchiMate 4 relationship review confirms that relationship for this example.

## Reusable model concepts

- Customer Management capability must be the same concept reused in FIG-07-02 and FIG-07-06.
- Financial Crime Management capability must align with the Financial Crime Platform application component used in later views, without implying that the capability and application are the same thing.
- Reduced duplicate customer capture outcome must align with FIG-07-05 motivation content.

## Notation and legend

Use ArchiMate 4 strategy-domain notation. Capability boxes may share one colour, and motivation elements, if included, must use a distinct style. The legend must explain capability, course of action, outcome, composition and influence. Colour must not be the only carrier of meaning.

## Main flow or structure

Use a map layout rather than a sequence. Put Retail Banking as the parent capability and arrange child capabilities in readable rows.

## Alternative and exception flows

Not applicable. This is a structural capability view, not a process or exception view.

## Scope

Retail banking capabilities used as a beginner example for ArchiMate strategy modelling.

## Exclusions

No detailed value streams, BPMN process steps, application components, data entities, BIAN Service Domains, technology nodes or project tasks.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]` for ArchiMate 4 strategy-domain concepts and relationships.
- `examples/horizon-bank/README.md` for Horizon Bank business lines and starting problems.

## Accessibility requirements

Use high contrast, readable labels and no colour-only meaning. The figure must remain readable at book-page width and must not rely on small decorative icons.

## Source creation authorisation

The author authorised source creation from the corrected specification on 2026-06-29. The rendered diagram remains in `Review`.

## Review criteria

- Capabilities read as abilities, not activities.
- The map does not imply detailed process sequence.
- Relationship meaning is clear from labels, legend and caption.
- No unverified Serving relationship is shown between capabilities.
- All included element types are valid for ArchiMate 4.
- Terminology matches `GLOSSARY.md` and Chapter 7.
