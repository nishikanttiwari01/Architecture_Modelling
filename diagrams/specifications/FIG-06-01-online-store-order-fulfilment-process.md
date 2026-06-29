# FIG-06-01: Online Store Order Fulfilment BPMN Process

## Purpose

Show a small BPMN process diagram for the main Simple Online Store order fulfilment flow.

## Audience

Beginners, business analysts, process owners and architects.

## Question answered

What are the main fulfilment steps inside the Online Store after an order is placed?

## Abstraction level

Business process overview. It shows process behaviour and responsibility, not system architecture or warehouse implementation.

## Notation

BPMN process diagram.

## Required elements

- Pool: Online Store
- Lanes: Customer Service, Fulfilment
- Start event: Order placed
- Tasks: Receive order, Check stock, Pick items, Pack parcel, Dispatch parcel, Notify customer, Cancel order
- Exclusive gateway: Stock available?
- End events: Order dispatched, Customer notified of cancellation

## Required relationships

- Order placed starts Receive order.
- Receive order leads to Check stock.
- Check stock leads to Stock available?
- `[in stock]` leads to Pick items, Pack parcel, Dispatch parcel and Order dispatched.
- `[out of stock]` leads to Cancel order, Notify customer and Customer notified of cancellation.

## Main flow or structure

Place the Online Store pool horizontally with two lanes. Show the normal fulfilment path in the Fulfilment lane and cancellation communication in the Customer Service lane.

## Alternative and exception flows

Show only the out-of-stock alternative. Do not model payment failure, delivery exception, return handling or customer cancellation.

## Scope

Order fulfilment after order placement and before external delivery-provider processing.

## Exclusions

No payment authorisation, inventory-system internals, delivery-provider process, database tables, API calls or deployment detail.

## Accessibility requirements

Use high contrast, readable text and labelled gateway conditions. The diagram must fit at book-page width.

## Source references

- `[OMG-BPMN]` for BPMN process notation.
- `examples/simple-online-store/README.md` for stable actors, systems and process names.

## Review criteria

- Sequence flows stay inside the Online Store pool.
- Lanes clarify responsibility without adding unnecessary roles.
- Gateway conditions are readable.
- The figure does not imply a complete warehouse-management process.
