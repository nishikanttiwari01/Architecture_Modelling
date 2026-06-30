# FIG-09-02: Online Store Product Eligibility Decision Tree

## Purpose

Show a general decision tree for Online Store product eligibility and distinguish it from a formal DMN DRD.

## Audience

Beginners, analysts and architects.

## Question answered

Which path through basic product and destination questions leads to an eligibility outcome?

## Notation

General decision tree rendered with PlantUML activity notation. It is not a formal DMN DRD element.

## Required elements

- Figure title.
- Restricted product question.
- Destination allowed question.
- Stock available question.
- Outcomes: Eligible, Eligible with restricted delivery, Not eligible.
- Note stating that a decision tree is a general technique, not a formal DMN DRD element.

## Required relationships

Branches must show clear yes/no direction and outcomes.

## Main flow or structure

Start by checking whether the product is restricted. If it is restricted, check destination allowance first, then stock availability. If it is not restricted, check stock availability directly. End in one of three product eligibility outcomes.

## Alternative and exception flows

Out-of-stock or disallowed destination paths end in Not eligible. A restricted product is eligible with restricted delivery only when the destination is allowed and the product is in stock.

## Scope

Simple Online Store teaching example.

## Exclusions

Pricing, delivery cost, returns policy, fraud screening, customer entitlements and implementation logic.

## Accessibility requirements

Use explicit branch labels, readable text and surrounding prose that explains the limitation.

## Source references

- `[OMG-DMN-1.5]`, for contrast with formal DMN DRDs.

## Review criteria

- The figure is not described as a formal DMN DRD.
- Stock availability is checked for both restricted and unrestricted products.
- Branch labels are readable.
- Outcomes are visually distinct.
- The diagram status remains `Review`.

## Authorisation

The author authorised source creation through the Chapter 9 completion request on 2026-06-30.
