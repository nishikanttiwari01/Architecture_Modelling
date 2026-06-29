# FIG-04-02: Online Store order concept class diagram

## Purpose

Show a small UML class diagram at analysis level for online store order concepts.

## Audience

Beginners, analysts and developers.

## Question answered

What important order-domain concepts exist, and how are they related?

## Notation

UML class diagram.

## Required elements

- Customer
- Basket
- Product
- Order
- Order Line
- Payment
- Shipment

## Required relationships

- Customer places Order
- Customer owns Basket
- Basket contains Product references or basket items
- Order contains Order Line
- Order Line refers to Product
- Order has Payment
- Order has Shipment

## Main flow or structure

Use a compact conceptual class diagram. Include multiplicities only where they aid beginner understanding, such as one Order containing one or more Order Lines.

## Alternative and exception flows

Not applicable. This is a structural diagram, not a flow diagram.

## Scope

Conceptual order-domain structure for the Simple Online Store.

## Exclusions

No private attributes, methods, persistence annotations, table names or implementation classes.

## Accessibility requirements

Keep class boxes simple and readable. Avoid dense compartments.

## Source references

- `[OMG-UML]` for UML class diagram notation.
- `examples/simple-online-store/README.md` for stable information concepts.

## Review criteria

- Diagram is clearly analysis-level, not physical database design.
- Multiplicities are readable and not excessive.
- Concepts match the repository example.
