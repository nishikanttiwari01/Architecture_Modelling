# Chapter 16 Technical Review

## Review metadata

- Chapter: 16, Modelling Software Structure
- Review date: 2026-07-07
- Reviewer: Codex
- Scope: Technical accuracy of software-structure view selection, source usage, logical versus physical structure and diagram integration.
- Result: Pass for author review.

## Pass 1: Technical accuracy

- Result: Pass.
- Findings: The chapter distinguishes system landscape, system context, container, component, package, class, dependency and deployment views.
- Findings: C4 concepts are limited to landscape, context, container, component, code and deployment framing already introduced in Chapter 5.
- Findings: UML concepts are limited to package, class, component, dependency and deployment terminology already introduced in Chapter 4.
- Findings: The chapter does not present C4 as mandatory and does not present UML as obsolete.
- Fixes made: Replaced the scaffold with a complete selection chapter that states the question each view answers.
- Fixes made: Added explicit cautions that a C4 container is not automatically Docker and a component is not automatically a microservice.
- Remaining risks: Final author review may prefer a different balance between C4 and UML examples.

## Pass 2: Boundary and abstraction review

- Result: Pass.
- Findings: Business capability, business process and software structure are kept distinct in the opening sections.
- Findings: The manuscript separates landscape, context, container, component, package, class, dependency and deployment boundaries.
- Findings: Logical software responsibility is separated from runtime placement.
- Fixes made: Added a deployment-boundary section that explains why deployment is related to structure but not the same as logical design.
- Fixes made: Added review checklist items for boundary, audience and abstraction consistency.
- Remaining risks: None major.

## Pass 3: Example technical review

- Result: Pass.
- Findings: Simple Online Store examples use Customer, Customer Support Agent, Payment Provider System, Delivery Partner System and Inventory System consistently.
- Findings: Horizon Bank examples use Horizon Digital Channels, Customer Onboarding Platform, Party and Customer Platform, Payments Platform, Core Deposit System, Financial Crime Platform, Enterprise Integration Platform, Event Platform and Enterprise Data Platform consistently.
- Findings: The Horizon Bank example avoids deep BIAN treatment and avoids mapping one domain automatically to one microservice.
- Fixes made: Added concrete Online Store and Horizon Bank selection paths across all required views.
- Remaining risks: The examples are intentionally compact; implementation detail belongs in later chapters.

## Pass 4: Source verification

- Result: Pass.
- Findings: `[C4-OFFICIAL]` is used for the C4 structure hierarchy and view framing.
- Findings: `[OMG-UML]` is used for UML package, class, component, dependency and deployment terminology.
- Findings: No unstable current claim or new normative source requirement was introduced.
- Fixes made: Kept source requirements to existing registered source notes.
- Remaining risks: None.

## Overall technical conclusion

- No unresolved Critical issue.
- No unresolved Major issue.
- Minor author preference remains possible around example emphasis.
- Recommendation: Chapter 16 may move to `Ready for Author Approval`.
