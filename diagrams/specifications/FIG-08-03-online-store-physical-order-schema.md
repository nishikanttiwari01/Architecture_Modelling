# FIG-08-03 Online Store relational order implementation model

## Purpose

Show how a logical ERD can be translated into a relational implementation model.

## Audience

Architects, developers, database designers and reviewers.

## Question answered

How might the placed-order part of the logical model be implemented relationally while preserving business meaning?

## Notation

PlantUML class-style relational implementation view.

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

Show table names, selected column names, primary keys, foreign keys and a small note about implementation constraints.

## Alternative and exception flows

No behavioural exception flow is required. Optional payment and shipment rows should remain visible.

## Scope

Placed-order scope for the Simple Online Store. Basket is deliberately excluded because this view begins after an order has been placed.

## Exclusions

No complete production schema, data migration design, security roles, partitioning strategy, storage parameters or PostgreSQL-specific syntax.

## Accessibility requirements

Use readable labels and avoid relying on colour. Keep the diagram compact enough for book-page width.

## Source references

- CODD-RELATIONAL-1970
- Simple Online Store example file

## Review criteria

- Relational table naming and columns are visibly different from the logical ERD.
- Keys and foreign keys are clear.
- The diagram does not pretend to be a complete DBMS-specific physical schema.
- It has no clipped text or overlapping labels.
