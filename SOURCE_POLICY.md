# Source and Citation Policy

## Purpose

Ensure that definitions, standards, current framework details and banking claims are accurate, traceable and legally reusable.

## Source priority

1. Official specification or standards body
2. Official framework or industry organisation documentation
3. Peer-reviewed or recognised academic source
4. Official vendor-neutral guidance
5. Reputable specialist secondary source
6. Blog or community source only for non-normative practical experience

## Preferred authorities

- **UML, BPMN and DMN:** Object Management Group
- **ArchiMate:** The Open Group
- **C4:** Official C4 model documentation and Structurizr documentation where relevant
- **BIAN:** Banking Industry Architecture Network official deliverables
- **Security:** NIST, OWASP, ISO publications where legally accessible, and recognised cloud-provider documentation for implementation details
- **Cloud and Kubernetes:** Official platform documentation

## Research procedure

For every material source:

1. Create a note using `templates/source-note-template.md`.
2. Save it under the relevant `research/<topic>/` directory.
3. Record the framework or standard version.
4. Record publication and access dates.
5. Identify exactly which claims it supports.
6. Distinguish normative statements from interpretation.
7. Add the source to `SOURCE_REGISTER.md` when it supports more than one chapter or major claim.

## Citation approach

During drafting, use a stable source key such as:

```text
[OMG-UML-2.5.1]
[OPEN-GROUP-ARCHIMATE-3.2]
[BIAN-SERVICE-LANDSCAPE-<VERSION>]
```

The final publication citation format will be selected before copy-editing. Do not remove source keys during drafting.

## Currency and versioning

- Verify current versions before making claims about what a framework contains.
- Record version-specific differences when they matter to a reader.
- Do not silently combine terminology from different versions.
- Recheck external links and current specifications during final review.

## Copyright

- Paraphrase definitions unless a brief quotation is necessary.
- Keep quotations short and attributed.
- Create original diagrams based on understanding, not traced copies.
- Do not reproduce standards tables, metamodels or proprietary diagrams without explicit permission.
- Record image or figure licences when external material is permitted.

## Banking claims

- Distinguish BIAN reference concepts from Horizon Bank design choices.
- Distinguish common banking practice from legal or regulatory requirements.
- For regulatory statements, identify jurisdiction and effective date.
- Avoid presenting the fictional case study as advice to a real bank.

## Quality test

A source is not adequate merely because it agrees with the draft. It must be authoritative enough for the claim, current enough for the context and represented accurately.

Last updated: 2026-06-28
