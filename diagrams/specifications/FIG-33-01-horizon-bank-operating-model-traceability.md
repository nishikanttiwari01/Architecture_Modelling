# FIG-33-01: Horizon Bank operating-model traceability view

- **Status:** Review
- **Specification checkpoint:** Author-approved chapter programme and figure production checkpoint, 2026-07-11
- **Production history:** An uncommitted draft source and export were generated before
  this specification checkpoint was committed. They must be treated as previews only.
  Source and exports will be regenerated from the committed specification before the
  figure can move to `Review`.
- **Purpose:** Show one selected, qualified traceability thread through Horizon Bank's operating-model set.
- **Audience:** Beginner architects, business architects, bank transformation stakeholders and reviewers.
- **Question:** How do unlike operating-model elements connect without being treated as equivalent?
- **Scope:** Retail customer onboarding excerpt only. This is not a universal or complete bank diagram.
- **Notation:** Original layered explanatory view using labelled arrows, not formal BIAN notation.
- **Format:** Page-readable portrait or compact landscape, SVG primary and PNG preview.
- **Accessibility:** Light backgrounds, dark text, redundant layer labels and relationship labels; colour is not the only carrier of meaning.

## Required content

Show these selected elements in a left-to-right or top-to-bottom thread:

1. Customer outcome: `Usable banking relationship`.
2. Value stage: `Identity and eligibility confirmed`.
3. Capabilities: `Customer Onboarding` plus contributing `Identity Verification` and `Financial Crime Screening`.
4. Process: `Establish customer and account`.
5. Reference responsibility: `Candidate BIAN Service Domain responsibilities`, explicitly labelled `BIAN 14.0 logical reference`.
6. Roles: `Process owner`, `Operations` and `Control owner`.
7. Information: `Party`, `Identity Evidence`, `Screening Result` and `Account`.
8. Applications: `Customer Onboarding Platform`, `Party and Customer Platform`, `Financial Crime Platform` and `Core Deposit System`.
9. Technology: `Runtime, integration and operational views`.
10. Controls and measures: identity and screening evidence; completion time, straight-through processing and control failures.

Label relationships with qualified verbs such as `is enabled by`, `is exercised by`, `is informed by`, `is supported in part by`, `uses`, `runs on`, `is constrained by` and `is measured by`. Include a note that mappings can be partial and many-to-many. Do not name unverified Service Domains.

## Exclusions

- No claim that the view is the full bank.
- No one-to-one mapping between Service Domain and capability, process, organisation, application or microservice.
- No detailed BPMN sequence, application interface design or physical infrastructure.
- No copied BIAN diagram or copyrighted standards artwork.

## Acceptance checks

- SVG and PNG exist and render without errors.
- Text is readable at intended book-page width.
- No clipped text, overlaps or excessive crossings.
- Arrow direction and relationship labels agree with the chapter.
- Controlled Horizon Bank names are used.
- Status remains `Review`, never `Approved`.
