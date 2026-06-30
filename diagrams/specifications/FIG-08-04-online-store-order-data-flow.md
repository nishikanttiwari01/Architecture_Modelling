# FIG-08-04 Online Store order data flow

## Purpose

Show a data flow diagram for order placement.

## Audience

Beginners, analysts, integration architects and reviewers.

## Question answered

Where does order data move, which processes transform it, and which data stores or external systems are involved?

## Notation

Informal data flow diagram in PlantUML.

## Required elements

- Customer external entity
- Capture order process
- Authorise payment process
- Create shipment request process
- Order data store
- Payment Provider System
- Delivery Partner System

## Required relationships

- Customer sends basket and delivery details to Capture order
- Capture order writes order data
- Authorise payment exchanges payment request and response with Payment Provider System
- Create shipment request sends shipment request to Delivery Partner System

## Main flow or structure

Show movement and transformation of data. Distinguish processes, external entities and data stores through labels and stereotypes.

## Alternative and exception flows

Show payment declined as a labelled data response, but do not model the full exception process.

## Scope

Order placement data movement for Simple Online Store.

## Exclusions

No database schema, BPMN task sequence, C4 container structure or deployment detail.

## Accessibility requirements

Use readable arrows, labelled flows and sufficient contrast. Meaning must not depend on colour alone.

## Source references

- DEMARCO-STRUCTURED-ANALYSIS-1979
- Simple Online Store example file

## Review criteria

- Data flows are labelled with information names.
- Processes are verbs, data stores are nouns and external entities are clear.
- The diagram is not confused with an ERD or BPMN process.
- It has no clipped text or overlapping labels.
