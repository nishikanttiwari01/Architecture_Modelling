# FIG-08-02 Online Store logical ERD

## Purpose

Show how a conceptual model becomes a more precise logical entity relationship diagram.

## Audience

Beginners, analysts, architects and developers.

## Question answered

Which entities, attributes, keys, cardinalities and optional relationships define the order domain before choosing a specific database product?

## Notation

PlantUML class-style ERD with attributes and cardinalities.

## Required elements

- Customer
- Order
- Order Line
- Product
- Payment
- Shipment

## Required relationships

- Customer places zero or more Orders
- Order contains one or more Order Lines
- Order Line refers to one Product
- Order has zero or more Payments
- Order has zero or more Shipments

## Main flow or structure

Show logical attributes and keys with cardinality markers. Keep the model independent from physical database naming and index design.

## Alternative and exception flows

Represent optional Payment and Shipment relationships through cardinality, not process arrows.

## Scope

Simple Online Store order, payment and shipment data at logical level.

## Exclusions

No physical data types, indexes, partitions, API operations or fulfilment process sequence.

## Accessibility requirements

Use readable type size, plain relationship labels and non-colour-dependent cardinality.

## Source references

- CHEN-ER-1976
- CODD-RELATIONAL-1970
- Simple Online Store example file

## Review criteria

- Logical keys and attributes are present.
- Cardinality and optionality are explicit.
- The diagram does not claim to be a physical schema.
- It has no clipped text or overlapping labels.
