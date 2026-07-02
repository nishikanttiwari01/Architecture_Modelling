# Chapter 13 Consistency Review, 2026-07-02

Reviewed baseline: `21c66d430c42eb1c1a404fcbcf2d1e827d59c455`

Focused correction baseline: `4e5b90d7fbf355ae9ade5772fbc40e9218c3513b`

| ID | Severity | Affected file/section | Evidence | Required action | Resolution status |
|---|---|---|---|---|---|
| CH13-CON-01 | High | `STATUS.md` and chapter frontmatter | Chapter 13 was in `Diagramming` while review findings still required changes. | Move Chapter 13 to `Revision Required`. | Resolved in `STATUS.md`, `RESUME.md` and chapter frontmatter. |
| CH13-CON-02 | Medium | `DIAGRAM_REGISTER.md`, `FIG-13-01` specification and manuscript | Figure title was less precise than the requested traceability-view title. | Rename consistently to `Online Store SysML-style Requirement Traceability View`. | Resolved in register, manuscript and specification. |
| CH13-CON-03 | Medium | `examples/horizon-bank/system-landscape.md` and `FIG-13-03` | Lifecycle values were not controlled. | Define lifecycle markers and require them in the figure specification. | Resolved in example file and specification. |
| CH13-CON-04 | Medium | `SOURCE_REGISTER.md` and research notes | Business capability and value-stream source support relied too heavily on adjacent ArchiMate framing. | Add official Open Group public guide source note and register entry. | Resolved in source note and register. |
| CH13-CON-05 | Low | `GLOSSARY.md` | Verification case and verification evidence were used but not separately defined. | Add glossary terms. | Resolved in glossary. |
| CH13-CON-06 | High | Manuscript and `FIG-13-01` specification | SysML verification relationship semantics were inconsistent with requirement verification. | Align manuscript and specification so Requirement to Verification case uses `verified by`. | Resolved in manuscript and specification. |
| CH13-CON-07 | Medium | `FIG-13-05` source references | Heat-map specification still referenced `examples/horizon-bank/README.md` for controlled capability names. | Replace the generic README reference with the heat-map convention source, Open Group business architecture source and capability catalogue. | Resolved in `FIG-13-05` specification. |
| CH13-CON-08 | Medium | Manuscript and `FIG-13-06` specification | Wardley component name varied between event distribution and payment-status event distribution. | Use `Payment-status event distribution` consistently and define positions for all components. | Resolved in manuscript and specification. |

Open consistency issue: `FIG-13-01` through `FIG-13-06` remain at `Planned` until author-approved specifications allow diagram source creation.
