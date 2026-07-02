# FIG-13-06: Horizon Bank Payment Modernisation Wardley Map

## Purpose

Show a simplified Wardley map for Horizon Bank payment modernisation, anchored in user need and component evolution.

## Audience

Strategy, product, enterprise architecture and platform leaders.

## Question answered

Which payment-modernisation components support the user need, how do they depend on each other, and where might evolution affect strategy?

## Notation

Wardley map teaching view.

## Required elements

- User: Retail Customer.
- User need: make a reliable outgoing payment.
- Components: Digital payment experience, Payment orchestration, Financial crime screening service, Fraud decisioning service, Event distribution, Customer and account data access, Compute service, Storage service, Network service.
- Evolution axis labels: Genesis, Custom-built, Product or rental, Commodity or utility.
- Dependency links from user need down through visible and supporting components.
- Note that positions are assumptions for discussion.
- Component assumptions table matching the manuscript.

## Required relationships

- User need must anchor the top of the map.
- Components must connect through value-chain dependency lines, not data-flow or integration arrows.
- Components must be positioned on the evolution axis.

## Main flow or structure

Use a conventional Wardley-map layout: visibility or value chain vertically, evolution horizontally.

## Alternative and exception flows

None.

## Scope

Strategic discussion map for Chapter 13. It is not an implementation design.

## Exclusions

- Exact vendor selection.
- Full competitive analysis.
- Full BIAN mapping.
- Detailed application integration.

## Accessibility requirements

Every component must have a text label. The axes must be labelled. The note must say that positions are assumptions.

## Source references

- `[WARDLEY-MAPS-OFFICIAL-2026]`
- `examples/horizon-bank/system-landscape.md`

## Review criteria

- The map is anchored in user need.
- Component positions are not presented as facts.
- Dependencies are readable.
- The figure is not confused with an application landscape or roadmap.
