# FIG-09-01: Online Store Delivery Decision Table

## Purpose

Show a beginner-readable DMN-style decision table for selecting an Online Store delivery decision.

## Audience

Beginners, business analysts, architects and testers.

## Question answered

Which delivery decision applies for a combination of order value, stock availability and destination?

## Notation

DMN-style decision table rendered as a PlantUML teaching figure. It is not semantic `.dmn` XML.

## Required elements

- Figure title.
- Unique hit-policy indicator `U`.
- Input clauses: Order value, All items in stock, Destination.
- Output clause: Delivery decision.
- Four non-overlapping rules.
- Note explaining that `-` means any value.

## Required relationships

The table must show rule rows rather than arrows.

## Main flow or structure

Rules:

1. `>= 50`, Yes, Domestic, Free standard delivery.
2. `< 50`, Yes, Domestic, Paid standard delivery.
3. `-`, No, `-`, Stock exception review.
4. `-`, Yes, International, Obtain international delivery quote.

## Alternative and exception flows

Stock unavailable maps to Stock exception review regardless of order value or destination.

## Scope

Simple Online Store teaching example for delivery decision logic.

## Exclusions

Tax, carrier selection, international customs, delivery time calculation, warehouse allocation and implementation binding.

## Accessibility requirements

Use readable table text, high contrast, and surrounding prose explaining the hit policy and dash notation.

## Source references

- `[OMG-DMN-1.5]`

## Review criteria

- Unique hit policy is visible.
- Rules are non-overlapping in the simplified domain.
- The dash notation is explained.
- The figure remains readable at book-page width.
- The diagram status remains `Review`.

## Authorisation

The author authorised source creation through the Chapter 9 completion request on 2026-06-30.
