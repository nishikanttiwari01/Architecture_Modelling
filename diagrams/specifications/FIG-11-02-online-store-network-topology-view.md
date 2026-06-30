# FIG-11-02: Online Store Network Topology View

## Purpose

Show how a network topology view differs from a deployment view by focusing on zones, connectivity and traffic paths.

## Audience

Beginners, platform architects, network teams and security reviewers.

## Question answered

Which network zones does Online Store traffic cross, and what are the allowed traffic paths?

## Notation

Network topology teaching view, rendered with PlantUML after author acceptance of this specification.

## Required elements

- Internet.
- Edge zone.
- Application zone.
- Data zone.
- Operations access path.
- Payment Provider System.
- Delivery Partner System.

## Required relationships

- Customer traffic enters through the edge zone.
- Edge zone routes HTTPS traffic to the application zone.
- Application zone connects to the data zone through a controlled database path.
- Application zone calls external provider systems through controlled outbound paths.
- Operations access is separate from customer traffic.

## Main flow or structure

Use layered network zones or grouped boundaries. Show allowed direction and protocol at a high level without listing firewall rules line by line.

## Alternative and exception flows

None. The diagram should stay focused on topology rather than failure handling.

## Scope

Simple Online Store network zones and traffic direction for a conceptual production environment.

## Exclusions

- No vendor-specific subnet names unless a later source diagram needs them.
- No complete firewall rule table.
- No identity and access-management detail.
- No detailed application component structure.

## Accessibility requirements

Use zone labels and line labels rather than relying on colour. Ensure direction arrows are large enough to read in monochrome.

## Source references

- [NIST-SP-800-145]
- [AWS-WA-RELIABILITY-2026]

## Review criteria

- Network zones are named clearly.
- Application responsibility is not mixed with detailed process steps.
- Traffic direction and boundary crossing are visible.
- Specification must be accepted by the author before creating the PlantUML source.
