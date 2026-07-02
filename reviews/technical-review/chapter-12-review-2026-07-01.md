# Chapter 12 Technical Review, 2026-07-01

## Scope

- Chapter: `manuscript/part-02-modelling-languages/12-security-modelling.md`
- Related specifications: `FIG-12-01`, `FIG-12-02`, `FIG-12-04`, `FIG-12-05`
- Baseline checked: `4d6df859aa5d0da6ce622e895c0208320cc08ff5`
- Actual HEAD before edits: `4d6df859aa5d0da6ce622e895c0208320cc08ff5`
- Status after review: `Revision Required`

## Findings

| ID | Severity | Evidence | Required action | Resolution status |
|---|---|---|---|---|
| CH12-TECH-01 | Major | The draft moved directly from viewpoints into diagrams without first defining assets, objectives, actors, assumptions, dependencies, consequences and evidence. | Add a security-modelling foundation and trace from asset to objective, threat, control, evidence and residual risk. | Resolved in revised chapter. |
| CH12-TECH-02 | Major | The draft used broad trust wording that could imply outside means low trust and inside means high trust. | Define trust boundary by change in trust basis and align wording with NIST zero trust guidance. | Resolved in chapter and `FIG-12-01` spec. |
| CH12-TECH-03 | Major | Authentication flow implied delegated identity without clear separation of credential handling, session handling and later access authorisation. | Revise authentication sequence to show delegated authentication, authentication result validation, session creation and a later protected-action access decision. | Resolved in chapter and `FIG-12-02` spec. |
| CH12-TECH-04 | Major | The payment matrix mixed access authorisation, business approval and payment-provider authorisation language. | Rename the concept to access authorisation, define the three meanings, and change the matrix to `TABLE-12-01`. | Resolved in chapter, glossary, register and decision log. |
| CH12-TECH-05 | Major | Control mapping named controls but did not provide enough traceability to owners, evidence and residual risk. | Add a worked Horizon Bank control map with threat IDs linked to the DFD and attack tree. | Resolved in revised chapter. |
| CH12-TECH-06 | Major | Privacy was treated mainly as classification. | Add privacy modelling guidance for purpose, sharing, access, retention, telemetry and analytics. | Resolved with NIST Privacy Framework source note. |
| CH12-TECH-07 | Major | Attack-tree explanation lacked an explicit source for root, branch and AND/OR semantics. | Add a source note and cite attack-tree semantics. | Resolved with `SCHNEIER-ATTACK-TREES-1999`. |
| CH12-TECH-08 | Major | `FIG-12-05` reused `T12-02` for weak entitlement and tampering, so one ID represented two distinct threat scenarios. | Assign each distinct threat scenario one unique ID and add missing control-map rows for `T12-07` and `T12-08`. | Resolved in manuscript, `FIG-12-04` and `FIG-12-05`. |
| CH12-TECH-09 | Major | `FIG-12-05` included `T12-06`, although payment-status data exposure does not directly release a payment. | Remove non-causal `T12-06` from the attack tree while keeping it in the DFD and control map. | Resolved in manuscript and `FIG-12-05`. |
| CH12-TECH-10 | Major | `FIG-12-05` included `T12-04`, although weak attribution weakens evidence but does not by itself release a payment. | Keep `T12-04` in the DFD and control map, but exclude it from the attack tree. | Resolved in manuscript and `FIG-12-05`. |
| CH12-TECH-11 | Major | The DFD wording implied the Retail Customer supplies trusted identity context. | Change the customer-to-channel flow to session reference and the channel-to-payments flow to validated subject and entitlement context. | Resolved in manuscript and `FIG-12-04`. |

## Technical conclusion

The main technical findings have been applied, but Chapter 12 should remain `Revision Required` until author review confirms the revised prose and the four remaining figure specifications. No diagram source or export was created.

## Diagram-production update, 2026-07-02

The author approved `DEC-020` and the four remaining Chapter 12 figure specifications. PlantUML source, SVG exports and PNG previews were created for `FIG-12-01`, `FIG-12-02`, `FIG-12-04` and `FIG-12-05`.

Technical follow-up checks:

- `FIG-12-01` labels trust-boundary basis, shows the Identity Service as an external supporting security service and keeps support access behind a controlled interface.
- `FIG-12-02` separates credential handling, authentication-result validation, session creation and later access authorisation.
- `FIG-12-04` uses "payment instruction and session reference" from Retail Customer to Horizon Digital Channels, then "payment instruction, validated subject context and entitlement context" from Horizon Digital Channels to Payments Platform.
- `FIG-12-05` excludes non-causal `T12-04` and `T12-06` from the payment-release attack tree while retaining those threats in the DFD and control map.

Chapter 12 can move from `Revision Required` to `Diagramming`. The figures remain `Review`, not `Approved`.

## Final diagram-correction update, 2026-07-02

Applied the final Chapter 12 diagram correction pass from `f1109116fc8ac8adf5e9a7696524ad11d6912d8e`.

- `FIG-12-01` no longer treats the incoming public request as authenticated. The edge receives a public request and sends a filtered and routed request to the application runtime.
- `FIG-12-01` keeps authentication-result validation, session validation, input validation, authorisation and business-rule enforcement inside the application runtime.
- `FIG-12-04` now uses Digital Channel Access Context with the approved bank-controlled boundary basis.
- `FIG-12-04` now shows repair work item and permitted payment context presented through an authorised operations interface, and screening case plus permitted customer context presented to the Compliance Officer.
- `FIG-12-04` now completes the `T12-06` exposure path from Event Platform to Approved Event Consumer.
- `FIG-12-05` now represents `T12-08` as a structural AND branch with two visible child conditions.

Final author and page-layout approval remain pending.
