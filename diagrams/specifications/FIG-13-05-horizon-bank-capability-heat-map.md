# FIG-13-05: Horizon Bank Capability Heat Map

## Purpose

Show how a heat map can overlay attention ratings on stable Horizon Bank capabilities.

## Audience

Business architects, portfolio teams, risk reviewers and sponsors.

## Question answered

Which capabilities need the most attention, and what scoring basis is being used?

## Notation

Capability heat map.

## Required elements

- Capabilities: Digital Servicing, Customer Onboarding, Party Management, Product Management, Payment Initiation, Payment Screening, Account Servicing, Fraud Management, Data Governance, Event Governance.
- Rating legend: `H`, `M`, `L`.
- Separate dimensions: Current pain, Strategic importance, Delivery risk.
- Scoring criteria note for each dimension.
- Date, owner and version note.
- Explicit note that the scores are illustrative.

## Required relationships

- Capabilities should be grouped into coherent areas.
- Each capability must carry a text rating or marker for each dimension, not only a colour.

## Main flow or structure

Use a grid or grouped capability map. Apply heat indicators with text labels for each dimension.

## Alternative and exception flows

None.

## Scope

Teaching view for interpreting heat maps. It is not a real bank assessment.

## Exclusions

- Financial scoring model.
- Detailed investment portfolio.
- Regulatory risk assessment.

## Accessibility requirements

Text labels must state rating values. Colour must not be the only meaning carrier.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]`
- `[AUTHOR-HEAT-MAP-CONVENTIONS-2026]`
- `[OPEN-GROUP-BIZARCH-GUIDES-2022]`
- `examples/horizon-bank/capabilities.md`

## Review criteria

- The scoring basis, date, owner and version are visible.
- The heat map does not imply false precision or collapse dimensions into one composite score.
- Capability names are stable and not process tasks.
