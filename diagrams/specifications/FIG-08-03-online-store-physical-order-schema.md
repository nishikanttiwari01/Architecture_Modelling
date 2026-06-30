# FIG-08-03 Online Store physical order schema

## Purpose

Show how a physical data model adds implementation choices.

## Audience

Architects, developers, database designers and reviewers.

## Question answered

How might the order part of the logical model be implemented in a relational database while preserving business meaning?

## Notation

PlantUML class-style physical schema view.

## Required elements

- customers table
- orders table
- order_lines table
- products table
- payments table
- shipments table

## Required relationships

- Foreign key from orders to customers
- Foreign key from order_lines to orders
- Foreign key from order_lines to products
- Foreign key from payments to orders
- Foreign key from shipments to orders

## Main flow or structure

Show table names, selected column names, primary keys, foreign keys and a small note about indexes or constraints.

## Alternative and exception flows

No behavioural exception flow is required. Optional payment and shipment rows should remain visible.

## Scope

Simple Online Store relational implementation example for teaching physical modelling.

## Exclusions

No complete production schema, data migration design, security roles, partitioning strategy or vendor-specific syntax.

## Accessibility requirements

Use readable labels and avoid relying on colour. Keep the diagram compact enough for book-page width.

## Source references

- CODD-RELATIONAL-1970
- Simple Online Store example file

## Review criteria

- Physical naming and columns are visibly different from the logical ERD.
- Keys and foreign keys are clear.
- The diagram does not pretend to be a complete production schema.
- It has no clipped text or overlapping labels.
