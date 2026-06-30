# FIG-08-01 Online Store conceptual data model

## Purpose

Introduce a conceptual data model using the Simple Online Store example.

## Audience

Beginners, analysts and architects.

## Question answered

Which important business information concepts exist, and how do they relate before database design starts?

## Notation

Informal conceptual entity relationship view in PlantUML.

## Required elements

- Customer
- Basket
- Product
- Order
- Payment
- Shipment

## Required relationships

- Customer owns Basket
- Customer places Order
- Basket contains Product
- Order contains Product
- Order is paid by Payment
- Order is delivered by Shipment

## Main flow or structure

Show a small business-level model with concepts and plain relationship labels. Avoid physical attributes and implementation keys.

## Alternative and exception flows

No exception flow is required. The diagram should state that returns and support cases are outside the view.

## Scope

Simple Online Store order and fulfilment information at conceptual level.

## Exclusions

No database tables, columns, indexes, API payloads, event schemas or warehouse details.

## Accessibility requirements

Use readable labels, sufficient contrast and relationship text that does not depend on colour.

## Source references

- CHEN-ER-1976
- Simple Online Store example file

## Review criteria

- The diagram is clearly conceptual, not physical.
- Relationship labels are readable.
- It uses only stable Simple Online Store terms.
- It has no clipped text or overlapping labels.
