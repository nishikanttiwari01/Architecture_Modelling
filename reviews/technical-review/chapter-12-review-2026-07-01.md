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

## Technical conclusion

The main technical findings have been applied, but Chapter 12 should remain `Revision Required` until author review confirms the revised prose and the four remaining figure specifications. No diagram source or export was created.
