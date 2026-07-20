# Part V Final Source and Copyright Review

- **Review date:** 2026-07-20
- **Scope:** Chapters 31 to 56, with Chapters 30 and 57 reviewed for boundary context
- **Review type:** Final source, attribution and copyright review
- **Reviewer:** Codex

## Verdict

**Pass for source and copyright review, with non-blocking gaps.**

- **Critical source or copyright blocker remains:** No.
- **Important source or copyright blocker remains:** No.

This verdict does not mark any chapter Ready for Author Approval or Approved. It does not replace the technical, beginner, consistency or author reviews required by `WORKFLOW.md`.

## Scope and evidence reviewed

The review covered:

- the repository governance files, source policy, glossary and Part V design and implementation plan dated 2026-07-20;
- Chapters 31 to 56 in `manuscript/part-05-bian-case-study/`;
- Chapters 30 and 57 as the preceding and following chapter boundaries;
- `SOURCE_REGISTER.md` and all source notes used by Chapters 31 to 56;
- `DIAGRAM_REGISTER.md` and the Part V diagram deferrals;
- the distinction between official Banking Industry Architecture Network (BIAN) material and the fictional Horizon Bank author model; and
- possible quotation, copied-table, copied-diagram and other copyright risks.

## Checks performed

| Check | Result | Evidence |
|---|---|---|
| Chapter coverage | Pass | All 26 chapters from 31 to 56 were reviewed. Chapters 30 and 57 were checked for boundary context. |
| Source-key reconciliation | Pass | 38 distinct external-source keys were found in the chapter set. All 38 resolve to entries in `SOURCE_REGISTER.md`; no unregistered key was found. |
| Source-note existence | Pass | Every source-register entry used by the chapters points to an existing note file. |
| Version and date metadata | Pass | Every used source entry has version or current-documentation identification, publication-date information and an access date. |
| Primary URL evidence | Pass | Every used source note contains an official or primary-source URL. |
| Material-claim support | Pass | Material claims about BIAN, banking supervision, customer due diligence, accounting, payments, cards, trade finance, investment services, application programming interfaces, events, security, accessibility, deployment and operational resilience are supported by the cited primary sources or clearly labelled as author design. |
| BIAN fact versus author model | Pass | Chapters consistently distinguish official BIAN concepts and version facts from Horizon Bank mappings, catalogues, identifiers, counts and design recommendations. |
| Regulatory and jurisdiction scope | Pass | Chapters qualify legal, supervisory, scheme, accounting and jurisdiction-specific applicability instead of presenting international guidance as universally binding law. |
| Quotation and reproduction risk | Pass | No block quotation, attributed quotation, verbatim standards passage, copied official table or copied official diagram was found. Short phrases in quotation marks are author examples or labels, not source quotations. |
| Diagram deferral | Pass for this review | `FIG-31-01` to `FIG-36-01` are registered and remain Planned, with source and export pending author approval of their specifications. Chapters 37 to 56 create no diagram source and state the deferral. |
| Internet verification | Not required | No unstable material claim lacked repository evidence. Current claims were already supported by primary-source notes accessed on or before 2026-07-20. |

## Evidence by chapter group

### Chapters 31 to 36

The chapters use official BIAN 14.0 material for the Service Landscape and core concepts, and official sources from the Basel Committee on Banking Supervision (BCBS), the International Financial Reporting Standards Foundation, the World Wide Web Consortium (W3C), the National Institute of Standards and Technology (NIST), The Open Group and OpenTelemetry where relevant.

The chapters explicitly state that Horizon Bank's taxonomy, application estate, information model, critical-operation model, identifiers and counts are fictional author models. They do not equate a BIAN Service Domain with an application, deployable service, database or team. Exact BIAN mappings remain unverified rather than being inferred from similar names.

### Chapters 37 to 40

Customer due diligence, credit-risk and financial-instrument claims are supported by Financial Action Task Force (FATF), BCBS and IFRS sources. Applicability is correctly qualified by legal entity, jurisdiction, contract, facts and reporting framework.

The deposit scenarios are chiefly governed case-study designs. The text explicitly excludes unsupported claims about deposit insurance, disclosure wording, tax treatment, interest conventions and consumer rules.

### Chapters 41 to 44

Payments, correspondent banking and settlement terminology is supported by Committee on Payments and Market Infrastructures sources. Card-security claims use Payment Card Industry Data Security Standard material. Documentary-credit material uses International Chamber of Commerce guidance, and investment-services material uses International Organization of Securities Commissions principles.

The text does not claim membership of a payment scheme, market infrastructure, correspondent network or securities venue. Legal duties, settlement finality and product suitability are left dependent on the applicable arrangement and jurisdiction.

### Chapters 45 to 48

Liquidity, interest-rate risk, accounting, tax, risk data, governance, accessibility, digital identity, cybersecurity and operational-resilience claims are supported by official BCBS, IFRS, Institute of Internal Auditors, W3C and NIST material. The author model remains separate from regulatory scope and accounting policy.

The BIAN release evidence is used cautiously. The February 2026 Service Landscape 14.0 baseline and the 13 March 2026 release announcement are distinguishable records, not contradictory dates. Neither record is treated as proof of a detailed Horizon Bank mapping.

### Chapters 49 to 52

BIAN mapping guidance, OpenAPI Specification 3.2, CloudEvents 1.0.2, AsyncAPI 3.1.0, Kubernetes, NIST zero-trust guidance, OpenTelemetry and BCBS operational-resilience material are traced to official sources. The chapters clearly separate logical responsibilities, application boundaries, software services, deployment units and teams.

Candidate mappings `HB-BIAN-01` to `HB-BIAN-04` remain explicitly unverified. The text does not promote confidence to verification or present a reference contract as a production endpoint.

### Chapters 53 to 56

Operational-risk, corporate-governance, operational-resilience and risk-data claims are supported by BCBS sources. The transition method, governance workflow, measures, review gates and quick-reference guidance are clearly presented as author recommendations for Horizon Bank.

## Issues resolved or adequately controlled

| Issue | Resolution |
|---|---|
| BIAN version currency | Service Landscape 14.0 is the stated baseline. Older exact names are not carried forward without re-verification. |
| BIAN release-date ambiguity | The February 2026 landscape publication and 13 March 2026 announcement are recorded separately and used for different claims. |
| False BIAN precision | Exact Service Domain, operation and relationship mappings remain pending. Only four candidate Horizon Bank mapping records are named, and all are labelled unverified. |
| BIAN-to-implementation equivalence | The chapters repeatedly reject one-to-one equivalence between a Service Domain and an application, microservice, database, deployment or team. |
| Regulatory overreach | International principles and frameworks are qualified for jurisdiction, entity, contract and supervisory applicability. |
| Copyright exposure | Source content is paraphrased, and no official diagram, table or extended passage is reproduced. |
| Diagram governance | Source creation remains deferred until the author approves the relevant specifications. No unapproved diagram source was introduced. |

## Remaining non-blocking gaps

1. **Exact BIAN mapping evidence remains incomplete.** The mapping register now contains controlled `Confidence` and `Verification Status` fields, with the four candidates recorded as `Pending` and `Unverified`. Exact BIAN 14.0 objects, detailed evidence and resolved confidence remain pending. The chapters disclose this gap, so it is not a source blocker for the present draft. Those items remain required before any exact mapping is claimed.

2. **Chapter 38 has intentionally light external sourcing.** Its deposit lifecycle, interest and fee treatment is framed as a Horizon Bank teaching model, with jurisdiction, product-contract, disclosure, tax and deposit-insurance matters excluded. If later revisions add normative product or regulatory claims, dedicated primary sources will be required.

3. **Chapter 42 mentions strong customer authentication, 3-D Secure, token controls, personal identification number controls, rewards and billing as areas needing further detail.** The chapter does not make an unsupported compliance claim, but any expanded treatment should add current scheme, regulatory or standards sources appropriate to the stated jurisdiction and card arrangement.

4. **Diagram production remains deferred.** `FIG-31-01` to `FIG-36-01` still require author approval of their specifications before source creation and export. Chapters 37 to 56 have no new registered chapter-specific figure in this pass. This is a workflow dependency, not a source or copyright defect.

5. **Current-documentation sources need a publication-stage currency check.** Sources such as BIAN release material, NIST web documentation, Kubernetes documentation, OpenTelemetry documentation and industry standards should be rechecked immediately before publication if the publication date is materially later than this review.

## Severity summary

| Severity | Count | Disposition |
|---|---:|---|
| Critical | 0 | No blocker remains. |
| Important | 0 | No blocker remains. |
| Non-blocking gap | 5 | Disclosed above; none invalidates a current material claim or creates a present copyright breach. |

## Final decision

No Critical or Important source or copyright blocker remains in Chapters 31 to 56 as reviewed on 2026-07-20. The source set is traceable, primary-source-led and appropriately qualified. BIAN facts are kept separate from the Horizon Bank author model, and the text avoids unverified exact mappings and copyrighted reproduction.

No source note, source-register entry, decision record, chapter status or diagram status was changed by this review.
