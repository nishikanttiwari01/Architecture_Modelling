# FIG-10-01: Online Store Order Domain Model

## Purpose

Show the main business concepts in the Simple Online Store order domain before database, API or class design.

## Audience

Beginners, analysts, software architects and developers.

## Question answered

Which order-domain concepts matter, and how do they relate at a conceptual level?

## Notation

Conceptual domain model using PlantUML class-style boxes without implementation attributes or methods.

## Required elements

- Customer
- Basket
- Order
- Order Line
- Product
- Payment
- Shipment

## Required relationships

- Customer places Order.
- Customer owns Basket.
- Basket contains Product selections.
- Order contains one or more Order Lines.
- Order Line refers to Product.
- Order has Payment.
- Order may have one or more Shipments.

## Main flow or structure

The diagram should place Customer and Basket on the left, Order in the centre, Product above or near Order Line, and Payment and Shipment on the right to suggest the order lifecycle without turning the diagram into a process flow.

## Alternative and exception flows

Show optional multiple shipments for one order. Do not model returns or refunds in this figure.

## Scope

Conceptual order-domain model for the Simple Online Store example.

## Exclusions

- Database tables, keys and columns.
- API resources and endpoints.
- UML operations or implementation methods.
- Payment-provider internal model.
- Delivery-partner internal model.
- Returns and refund handling.

## Accessibility requirements

Use plain labels, readable font sizes and relationship labels. Do not rely on colour to distinguish relationship meaning.

## Source references

- `[DDD-REFERENCE-2015]`
- `examples/simple-online-store/README.md`

## Review criteria

- The figure reads as a conceptual domain model, not a physical data model.
- All terms match the Simple Online Store example.
- Relationship direction and labels are understandable to a beginner.
- No implementation attributes, table names or transport details appear.
- The model agrees with Chapter 10 prose.
