---
title: "Security Modelling"
chapter: 12
part: "part-02-modelling-languages"
status: "Diagramming"
author: "Nishikant Tiwari"
last_updated: "2026-07-01"
---

# 12. Security Modelling

## Chapter purpose

Teach practical modelling of trust boundaries, identity, authorisation, threats, controls and security flows without turning every architecture diagram into a security diagram.

## Reader outcomes

By the end of this chapter, the reader should be able to:

- Explain security viewpoints, trust boundaries, authentication, authorisation, threat modelling, STRIDE, attack trees, threat-model Data Flow Diagrams (DFDs), control mapping and data classification in plain language.
- Identify the architecture question answered by each security model.
- Distinguish authentication from authorisation, threats from controls, and control intent from implementation evidence.
- Review simple security models for missing assets, unclear trust assumptions, weak access decisions, hidden data movement and vague mitigations.
- Apply security modelling to both the Simple Online Store and Horizon Bank examples.

## Prerequisites and dependencies

- Chapter 3: How to Read Architecture Diagrams
- Chapter 4: Unified Modeling Language (UML)
- Chapter 6: Business Process Model and Notation (BPMN)
- Chapter 8: Data Modelling
- Chapter 11: Infrastructure and Deployment Modelling

## Required models and artefacts

- FIG-12-01: Online Store Trust Boundary View, specification created, source deferred pending author approval.
- FIG-12-02: Online Store Customer Authentication Sequence, specification created, source deferred pending author approval.
- FIG-12-03: Horizon Bank Payment Authorisation Matrix, specification created, source deferred pending author approval.
- FIG-12-04: Horizon Bank Payment Threat-Model DFD, specification created, source deferred pending author approval.
- FIG-12-05: Horizon Bank Payment Attack Tree, specification created, source deferred pending author approval.

## Worked examples

- Simple Online Store customer login and checkout.
- Horizon Bank outgoing retail payment authorisation.
- Horizon Bank payment threat review and control mapping.

## Source requirements

- `[NIST-CSF-2.0]` supports the connection between security modelling and broader cybersecurity risk management.
- `[NIST-SP-800-207]` supports trust, identity and explicit access-decision guidance drawn from zero trust architecture.
- `[NIST-SP-800-53R5]` supports security and privacy control mapping as control-catalogue context, not as a universal mandatory baseline.
- `[OWASP-THREAT-MODELLING-2026]` supports the threat-modelling workflow and the use of DFDs with trust boundaries.
- `[OWASP-ASVS-5.0.0]` supports application security verification framing for identity, authentication, access control and data protection.
- `[OWASP-AUTH-CHEATSHEETS-2026]` supports the distinction between authentication and authorisation and practical access-control review concerns.
- `[MICROSOFT-STRIDE-2026]` supports the six STRIDE threat categories.

## Planned chapter structure

This draft follows the approved Chapter 5 teaching pattern: explain the security modelling question, introduce focused viewpoints, demonstrate simple and banking examples, compare nearby approaches, list common mistakes, and end with a practical exercise and review checklist.

## Why security needs its own models

Security modelling answers: **what must be protected, who or what is trusted, what can go wrong, and what controls reduce the risk?**

Many architecture diagrams include a lock icon, a firewall symbol or the word "secure". That is not enough. A security model must make assumptions reviewable. It should show assets, identities, trust boundaries, data movement, access decisions, threats, controls and evidence at a level the intended audience can inspect.

A general deployment diagram may show where the Online Store API runs. A security model asks a different question: where does untrusted customer traffic enter, where does payment data cross a boundary, which identity is authenticated, which action is authorised, and which controls protect the flow? Chapter 11 showed runtime placement and infrastructure. This chapter adds the security questions that sit across those views.

Security modelling should also separate fact, interpretation and recommendation. A fact might be that a customer submits credentials to the Online Store. An interpretation might be that the customer device is outside the organisation's trust boundary. A recommendation might be that privileged administration must use a stronger authentication path than ordinary customer browsing. Keeping those separate helps beginners avoid treating a diagram as proof that the design is secure.

## Security viewpoints

A security viewpoint defines how a security concern will be represented and reviewed. It answers: **which security question are we trying to answer for which audience?**

Different stakeholders need different security views. A developer may need to know which API action requires which role. A platform engineer may need to understand trust boundaries and network zones. A security reviewer may need to see threats, mitigations and remaining risk. A data protection reviewer may need to know where personal or financial data is stored, transformed and retained.

| Viewpoint | Main question | Useful audience | Typical artefact |
|---|---|---|---|
| Trust boundary view | Where does the basis of trust change? | Architects, security reviewers, platform teams | Boundary diagram |
| Authentication flow | How is identity established? | Developers, identity teams, testers | Sequence diagram |
| Authorisation model | Who or what may perform which action? | Product owners, developers, auditors | Matrix or policy view |
| Threat model | What can go wrong and where? | Security reviewers, architects, delivery teams | DFD, STRIDE table or risk list |
| Attack tree | How could an attacker reach a harmful goal? | Security teams, architects, risk reviewers | Tree of attack paths |
| Control map | Which controls reduce which risks? | Security, risk, audit and delivery teams | Control mapping table |
| Data classification view | Which data needs stronger handling? | Data, security, privacy and architecture teams | Classification matrix or data-flow annotation |

The important habit is to choose the question before choosing the notation. A trust boundary diagram is not a complete threat model. An authorisation matrix is not an authentication flow. An attack tree is not a control catalogue. Each model earns its place by making one review question easier to answer.

## Trust-boundary diagrams

A trust-boundary diagram answers: **where does a request, user, device, system or data item cross from one trust context into another?**

A **trust boundary** is a boundary across which the level or basis of trust changes. The boundary may be organisational, technical, operational or data-related. For example, the customer's browser is outside the Online Store's control. The edge gateway is inside a managed platform boundary. The payment provider is a separate organisation. A staff administration console may be more trusted than a public customer channel, but it still needs explicit controls.

NIST zero trust guidance is useful here because it warns against assuming trust merely because something sits inside a network location [NIST-SP-800-207]. For modelling, the practical lesson is simple: do not let a diagram imply that "inside the network" means "trusted for every action".

For the Simple Online Store, a first trust-boundary view should show:

- Customer device and internet as untrusted or external.
- Online Store edge as the controlled public entry point.
- Application runtime as the place where requests are validated and business actions begin.
- Order and payment data store as a more restricted data area.
- Payment Provider System and Delivery Partner System as external systems with separate trust assumptions.
- Operations access as a separate path, not the same path as customer traffic.

The diagram should label important crossings. Customer login crosses from external customer device to the store edge. Checkout crosses from application runtime to payment provider. Operations access crosses from staff tooling into the production environment. The point is not to show every firewall rule. The point is to reveal where trust changes and where controls should be discussed.

## Authentication flows

An authentication flow answers: **how does the system establish the identity of a user, system or device?**

**Authentication** is about proving or establishing identity. **Authorisation** is about deciding what that identity is allowed to do. Beginners often merge these ideas into one phrase such as "login security". That hides important design questions. A customer may be authenticated but not authorised to view another customer's order. A service may authenticate successfully but still lack permission to post a payment.

An authentication flow is often shown as a sequence diagram because order matters. The diagram can show the customer, browser or mobile app, Online Store, identity service and session or token handling. It can also show error paths such as failed login, step-up authentication or account lockout, but it should not become a full implementation trace unless that is the purpose.

OWASP authentication guidance supports reviewing authentication design as a specific concern, while OWASP authorisation guidance treats access decisions as a separate concern [OWASP-AUTH-CHEATSHEETS-2026]. For Chapter 12, the modelling recommendation is to keep these flows separate until there is a reason to combine them.

A simple Online Store login sequence might show:

1. Customer submits credentials or a federated identity request.
2. Online Store sends the authentication request to an identity service.
3. Identity service validates the request and returns an authentication result.
4. Online Store creates a session or receives a token.
5. Customer requests an account or order action using that session or token.

The sequence should label where sensitive information is sent and where it should not be stored. It should also avoid promising security properties that the diagram does not prove. A sequence diagram can show that a token is issued. It does not prove that the token is well protected, expires correctly or cannot be stolen.

## Authorisation models

An authorisation model answers: **which subject may perform which action on which resource under which conditions?**

An authorisation matrix is a practical beginner artefact. It can list roles or subjects down one side and actions across the top. The cells record whether access is allowed, denied or conditional. In more advanced designs, the model may use attributes, policies, relationship-based access or central policy decision and enforcement points. The beginner principle stays the same: make the access decision visible.

For Horizon Bank payment authorisation, the matrix should distinguish customers, operations analysts, compliance officers and service identities. It should also distinguish actions such as create payment instruction, approve high-value payment, repair rejected payment, override screening result, post to core deposit system and view audit history.

| Subject | Example allowed action | Example condition | Review concern |
|---|---|---|---|
| Retail Customer | Create own payment instruction | Own account and valid entitlement | Cannot create payments from another customer's account |
| Operations Analyst | Repair operational exception | Assigned queue and maker-checker rules | Cannot approve own repair when separation is required |
| Compliance Officer | Review screening alert | Case assignment and policy authority | Cannot alter unrelated customer data without reason |
| Payments Platform service identity | Submit posting request | Approved payment and valid service credential | Cannot bypass business authorisation |
| Core Deposit System service identity | Return posting result | Trusted integration path | Cannot initiate customer payment by itself |

NIST SP 800-207 is again useful because it highlights explicit access decisions, policy decision points and policy enforcement points [NIST-SP-800-207]. In a model, a **policy decision point** decides whether access should be allowed. A **policy enforcement point** applies that decision at the system boundary or service boundary. The same component may perform both in a simple system, but the model should not hide where the decision is made.

## Threat modelling

Threat modelling answers: **what could go wrong, where could it happen, and what will we do about it?**

A **threat** is a potential cause of harm. A **vulnerability** is a weakness that could be exploited. A **control** is a safeguard that reduces likelihood, impact or exposure. A **threat model** is the structured record that connects the system, assets, threats, mitigations and open questions.

OWASP describes threat modelling as a structured activity for understanding a system, identifying threats and deciding mitigations [OWASP-THREAT-MODELLING-2026]. In this book, the modelling emphasis is on reviewability. A useful threat model should make it possible to ask:

- What asset or process is being protected?
- Which boundary or flow is exposed?
- Which threat category applies?
- Which control reduces the risk?
- Who owns the control?
- What remains unresolved?

Threat modelling is not the same as penetration testing. Penetration testing tries to find exploitable weaknesses in a running or testable system. Threat modelling can begin earlier, when the architecture is still being designed. It is also not the same as a list of security tools. A tool may implement a control, but the model should explain the risk and the reason for the control.

## STRIDE

STRIDE answers: **which common threat categories should we check against each element or data flow?**

STRIDE is a mnemonic for six threat categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service and Elevation of Privilege [MICROSOFT-STRIDE-2026].

| STRIDE category | Plain question | Payment example |
|---|---|---|
| Spoofing | Could someone pretend to be another user, service or system? | A fake service calls the Payments Platform as if it were Horizon Digital Channels. |
| Tampering | Could data or messages be changed without detection? | A payment amount is changed between channel submission and payment orchestration. |
| Repudiation | Could someone deny performing an action? | A staff user disputes approving a manual repair. |
| Information Disclosure | Could sensitive data be exposed? | Payment details appear in broad operational logs. |
| Denial of Service | Could service be made unavailable or degraded? | Payment submission is flooded so legitimate customers cannot submit payments. |
| Elevation of Privilege | Could someone gain permissions they should not have? | An operations user gains compliance override capability. |

STRIDE is useful because it gives beginners a repeatable lens. It is not a complete security architecture by itself. If the diagram does not show assets, boundaries and flows, STRIDE has nothing concrete to inspect. If the model lists threats without mitigations or owners, it is still incomplete.

## Attack trees

An attack tree answers: **what alternative paths could lead to one harmful goal?**

The root of an attack tree is the attacker's goal, such as "submit an unauthorised payment" or "access another customer's statement". Branches show ways the goal could be reached. Some branches are alternatives, while others require several steps together. The model helps reviewers see that a harmful outcome may have more than one path.

For Horizon Bank, an attack tree for unauthorised payment submission might include:

- Compromise customer authentication.
- Abuse a weak payment entitlement.
- Tamper with a payment request between channel and platform.
- Use a stolen service credential.
- Exploit an operations repair path.
- Bypass screening or approval through a privileged function.

Attack trees are most useful when the team can compare paths and decide where controls matter most. They are less useful when every branch is vague, such as "hack the bank". A good branch names a concrete path that can be reviewed against architecture and operations.

## Threat-model Data Flow Diagrams

A threat-model DFD answers: **how does data move through the system, and where do trust boundaries and threats appear?**

A DFD for threat modelling is different from a detailed business process. It usually shows external entities, processes, data stores, data flows and trust boundaries. OWASP guidance supports DFDs as a practical way to understand the system during threat modelling [OWASP-THREAT-MODELLING-2026]. Chapter 8 introduced data movement for architecture. Here, the same idea is used to expose security concerns.

For Horizon Bank payment submission, a threat-model DFD might show:

- Retail Customer as an external entity.
- Horizon Digital Channels as a process that captures the payment instruction.
- Payments Platform as the orchestration process.
- Financial Crime Platform as a screening process.
- Core Deposit System as the posting system.
- Event Platform as the event distribution path.
- Payment record store and audit log as data stores.
- Trust boundaries around customer access, bank digital platform, retained core system and external or shared platforms.

The flows should be labelled with the data that moves, not only with verbs. "Payment instruction", "screening request", "screening result", "posting request", "posting result", "payment status event" and "audit event" are reviewable labels. A vague arrow labelled "secure API" does not tell a reviewer what is at risk.

## Security control mapping

Security control mapping answers: **which control reduces which risk, where is it implemented, and what evidence will show that it works?**

NIST Cybersecurity Framework 2.0 provides high-level cybersecurity risk-management framing [NIST-CSF-2.0]. NIST SP 800-53 Revision 5 provides a broad catalogue of security and privacy controls [NIST-SP-800-53R5]. This chapter does not treat either source as a universal mandatory baseline for every reader. Instead, it uses them to teach traceability between architecture concerns, control intent and review evidence.

A practical control mapping should record:

- The threat or risk being addressed.
- The control intent.
- The place in the architecture where the control applies.
- The owner responsible for implementing or operating it.
- The evidence used for review.
- Any residual risk or open question.

For example, the threat "stolen service credential submits posting request" might map to service identity, short-lived credentials, mutual authentication, policy enforcement at the Payments Platform boundary, audit logging and alerting on unusual service calls. The implementation evidence might include identity-provider configuration, integration test evidence, audit log samples and operational alert rules.

Avoid mapping controls only by name. A table that says "access control exists" does not explain who makes the decision, where it is enforced or how a reviewer can verify it.

## Privacy and data classification

Privacy and data classification answer: **which data requires stronger handling, and where does it move or persist?**

Architecture models often show systems before they show the sensitivity of the data those systems handle. That can hide important risk. A payment flow may include customer identity, account number, payment amount, beneficiary information, screening result, audit data and operational telemetry. These data items do not all need the same treatment, but the model must make their handling visible enough to review.

A simple classification model can label data as public, internal, confidential or restricted. The exact categories differ by organisation. The book should not invent legal obligations for every jurisdiction. For architecture modelling, the point is to ask whether sensitive data crosses boundaries, appears in logs, reaches analytics stores, is retained longer than needed or is visible to staff roles without a clear purpose.

Chapter 11 introduced observability and sensitive-data redaction. Chapter 12 extends that idea: security models should show where sensitive data is protected, masked, tokenised, encrypted, retained, deleted or access-controlled. Do not rely on colour alone for classification. Use labels and textual explanation so the model remains accessible and reviewable.

## Security modelling versus nearby approaches

Security models often overlap with other architecture models, but they should not replace them.

| Approach | Main concern | Security relationship |
|---|---|---|
| Deployment view | Where software runs | Provides runtime context for boundaries and controls |
| Network topology | Zones and traffic paths | Helps locate trust boundaries and exposed paths |
| BPMN process model | Business process sequence | Helps find human approvals, exceptions and segregation of duties |
| Data model or lineage view | Data meaning and movement | Helps identify sensitive data and retention concerns |
| Threat-model DFD | Data movement for threat review | Adds trust boundaries, threats and mitigations |
| Control map | Traceability from risk to control and evidence | Helps review whether the design addresses known risks |

The same system may need several views. Horizon Bank payment authorisation needs a process view for business approval flow, a deployment view for runtime placement, a DFD for data movement, an authorisation matrix for access decisions and a control map for review evidence. Combining all of that into one picture would be hard to read.

## Common mistakes

The first mistake is treating a security icon as a security model. A lock symbol does not explain identity, data sensitivity, trust boundaries, threats or controls.

The second mistake is confusing authentication with authorisation. Login proves or establishes identity; it does not automatically grant every action.

The third mistake is assuming that an internal network is trusted for every purpose. Modern security models should make trust assumptions explicit.

The fourth mistake is drawing a threat model without assets. If the model does not say what is being protected, threat discussion becomes abstract.

The fifth mistake is labelling an arrow "secure" without saying what protects it or what data moves across it.

The sixth mistake is listing STRIDE categories without linking them to elements, flows, mitigations and owners.

The seventh mistake is using a control catalogue as a diagram. Controls need context, ownership and evidence.

The eighth mistake is hiding operational and support paths. Administration, repair, override and monitoring paths often carry high security risk.

The ninth mistake is using colour as the only indicator of data classification or trust level.

The tenth mistake is trying to show every security concern on one diagram. Use several focused views instead.

## Chapter cheat sheet

| Topic | Question answered | Useful for | Watch out for |
|---|---|---|---|
| Security viewpoint | Which security concern are we modelling? | Choosing the right artefact | Starting with notation before purpose |
| Trust boundary | Where does trust change? | Boundary and control review | Assuming internal means trusted |
| Authentication flow | How is identity established? | Login and service identity review | Mixing it with every access rule |
| Authorisation model | Who may do what, when? | Access-control review | Omitting conditions and enforcement points |
| Threat model | What can go wrong and what will we do? | Early security design review | Treating it as penetration testing |
| STRIDE | Which threat categories should we check? | Repeatable threat prompts | Listing categories without mitigations |
| Attack tree | How could one harmful goal be reached? | Comparing attack paths | Vague branches such as "hack system" |
| Threat-model DFD | How does data move across boundaries? | Security review of flows | Turning it into a business process diagram |
| Control map | Which control addresses which risk? | Audit and risk traceability | Naming controls without evidence |
| Data classification | Which data needs stronger handling? | Privacy and data protection review | Colour-only classification |

## Key takeaways

- Security models make assumptions visible so they can be reviewed.
- A trust boundary marks a change in the basis or level of trust, not merely a box boundary.
- Authentication and authorisation should be modelled separately before they are combined.
- Threat modelling can start before the system is built because it reviews design assumptions.
- STRIDE is a useful threat-category prompt, but it needs assets, flows, boundaries, controls and owners.
- Threat-model DFDs are useful when data movement and trust boundaries matter.
- Control mapping should connect risk, control intent, architecture location, owner and evidence.
- Data classification should be shown with labels and explanation, not colour alone.

## Practical exercise

Horizon Bank is designing outgoing retail payment submission. A Retail Customer uses Horizon Digital Channels to create a payment instruction. The Payments Platform validates and orchestrates the payment. The Financial Crime Platform screens the payment. The Core Deposit System posts accepted payments. The Event Platform publishes payment status events. Operations Analysts can repair exceptions, and Compliance Officers can review screening alerts.

Choose the right model for each question:

1. Which model should show that the customer device, bank digital channel, payment platform, retained core system and event platform sit in different trust contexts?
2. Which model should show how a customer identity is established before payment submission?
3. Which model should show whether an Operations Analyst may repair a payment but not approve their own repair?
4. Which model should show payment instruction, screening request, posting request and audit event flows across boundaries?
5. Which model should explore alternative ways an attacker might submit an unauthorised payment?
6. Which model should connect spoofing or tampering threats to controls, owners and evidence?
7. Which model should highlight customer, account and payment data that must not appear in broad operational logs?

Suggested answer:

- Use a trust-boundary view for different trust contexts.
- Use an authentication sequence for identity establishment.
- Use an authorisation matrix or policy view for allowed actions and separation rules.
- Use a threat-model DFD for data movement across trust boundaries.
- Use an attack tree for alternative attack paths to one harmful goal.
- Use a STRIDE-supported threat model plus a control map for threat, mitigation, owner and evidence traceability.
- Use data classification labels on flows, stores and telemetry paths for sensitive data handling.

## Review checklist

- [ ] The question answered by each security model is explicit.
- [ ] The audience and abstraction level are clear.
- [ ] Formal terms are introduced after a plain-language explanation.
- [ ] Authentication and authorisation are separated.
- [ ] Trust boundaries show a change in trust assumption, not decorative grouping.
- [ ] Threats are linked to assets, flows, boundaries, controls and owners.
- [ ] STRIDE categories are used consistently and not treated as a complete architecture by themselves.
- [ ] Threat-model DFDs show external entities, processes, data stores, data flows and trust boundaries.
- [ ] Authorisation models show subjects, actions, resources, conditions and enforcement points where relevant.
- [ ] Control mapping distinguishes control intent, implementation location, owner and evidence.
- [ ] Sensitive data and classification are explained with text, not colour alone.
- [ ] The simple and banking examples are consistent with repository example files.
- [ ] Comparisons do not imply that one notation is universally superior.
- [ ] Common mistakes are concrete and actionable.
- [ ] Required sources and diagram specifications are registered.
- [ ] Diagram source and exports are deferred until author approval of specifications.
- [ ] Terminology, link and word-count checks pass.

## Drafting notes

- Target length: 2,000 to 4,000 words unless the chapter scope justifies more. Current draft is slightly above target because it includes the full first-pass teaching sequence.
- Diagram source and exports for `FIG-12-01` through `FIG-12-05` must not be created until the author approves the specifications.
- During revision, check whether the author wants Chapter 12 to remain a broad security-modelling overview or to defer deeper privacy and control-mapping detail to Chapters 21 and 48.

## References and further reading

Chapter source notes are maintained in the repository under `research/security/` and registered in `SOURCE_REGISTER.md`. Appendix H, [Glossary and Source Notes](../appendices/appendix-h-glossary-sources.md), is the intended publication location for the final source-key index once the appendix is completed.

- `[NIST-CSF-2.0]`: National Institute of Standards and Technology, Cybersecurity Framework 2.0.
- `[NIST-SP-800-207]`: National Institute of Standards and Technology, Zero Trust Architecture.
- `[NIST-SP-800-53R5]`: National Institute of Standards and Technology, Security and Privacy Controls for Information Systems and Organizations, Revision 5.
- `[OWASP-THREAT-MODELLING-2026]`: OWASP threat-modelling cheat sheet.
- `[OWASP-ASVS-5.0.0]`: OWASP Application Security Verification Standard 5.0.0.
- `[OWASP-AUTH-CHEATSHEETS-2026]`: OWASP authentication and authorisation cheat sheets.
- `[MICROSOFT-STRIDE-2026]`: Microsoft STRIDE threat-category documentation.
