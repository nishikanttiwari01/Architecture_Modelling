# FIG-13-04: Horizon Bank Platform Evolution Roadmap

## Purpose

Show the intended progression from current point-to-point integration toward platform-mediated APIs and governed events.

## Audience

Transformation leads, enterprise architects, platform teams and sponsors.

## Question answered

How does Horizon Bank move from current payment integration constraints to a more modular target architecture through transition states?

## Notation

Architecture roadmap. A simple timeline or ArchiMate-style implementation and migration view may be used after author approval.

## Required elements

- Current state: retained core and point-to-point integration.
- Near-term transition: Payments Platform uses Enterprise Integration Platform adapters.
- Later transition: Event Platform publishes governed payment-status events.
- Target direction: modular payments, customer and data platforms with governed reuse.
- Dependencies, risks, assumptions, decisions and exit evidence for each state.
- Required details: adapter ownership, service-level monitoring, event schema governance, consumer access control, replay policy, legacy coexistence.

## Required relationships

- States must be ordered from current to target.
- Each transition state must show at least one dependency or risk.
- Target state must not imply all legacy systems vanish immediately.

## Main flow or structure

Use a left-to-right roadmap with four named architecture states: `Current`, `Near-term transition`, `Later transition` and `Target direction`. Put dependencies, risks, assumptions, decisions and exit evidence below the relevant state.

## Alternative and exception flows

None.

## Scope

Chapter 13 introductory roadmap example.

## Exclusions

- Detailed project plan.
- Dates, budgets or delivery team assignments.
- Full BIAN migration roadmap.

## Accessibility requirements

Use labels for state and dependency meaning. Do not use colour alone to show maturity or risk.

## Source references

- `[OPEN-GROUP-ARCHIMATE-4]`
- `examples/horizon-bank/system-landscape.md`

## Review criteria

- Roadmap states are architecture states, not task lists.
- Dependencies, risks, assumptions, decisions and exit evidence are explicit.
- The figure does not promise delivery dates or completion.
