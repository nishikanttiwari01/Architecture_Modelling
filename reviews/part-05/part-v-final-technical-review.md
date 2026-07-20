# Part V Final Technical Review

**Review date:** 2026-07-20  
**Review scope:** Chapters 31 to 56, with Chapter 30 and Chapter 57 checked only as boundaries  
**Reviewer:** Codex technical review  
**Verdict:** **Pass. No Critical or Important technical blockers remain.**

## Scope and review basis

This review assessed the completed Part V manuscript against the repository's approved book plan, workflow, style and source policies, terminology decisions, Part V completion design and implementation plan. It also checked the manuscript against the governed Horizon Bank catalogues, research notes, source metadata and diagram register.

The technical review concentrated on:

- internal identifiers and exact governed names;
- interface direction and responsibility boundaries;
- consistency among applications, interfaces, data, technology, controls, business domains and scenarios;
- BIAN mapping discipline, including the distinction between semantic reference and implementation design;
- evidential qualification of regulatory, operational and framework claims;
- explicit treatment of known gaps rather than invented detail;
- diagram governance; and
- repository validation gates.

All chapters from 31 to 56 were read in full. Chapter 30 and Chapter 57 were read to check the transitions into and out of Part V. Relevant Horizon Bank catalogues, the coverage matrix and summary, the BIAN mapping register, source notes and the `FIG-31-01` to `FIG-36-01` diagram records and specifications were also reviewed.

## Technical checks and evidence

| Check | Evidence | Result |
|---|---|---|
| Governed ID references | The Part V manuscript contains 749 unique `HB-*` references. Each resolved to the governed catalogues, including coverage records `HB-COV-002` and `HB-COV-010`. | Pass |
| Exact governed names | A fresh catalogue-to-manuscript comparison found zero heuristic exact-name mismatches after the Chapter 50 correction. | Pass |
| Explicit interface arrows | Every explicit code-form `HB-APP --HB-INT--> HB-APP` statement was compared with the interface catalogue. Zero direction mismatches remained. | Pass |
| Interface type totals | The catalogue contains 106 interfaces: 37 API, 7 Batch, 10 Command, 19 Event, 4 File, 20 Message and 9 Workflow. These totals agree with Chapter 34. | Pass |
| Catalogue totals | Verified totals include 90 applications, 17 external-network records, 95 business-domain records, 20 data domains, 25 systems of record, 30 technology/resilience classifications, 20 critical operations, 20 scenarios, 38 reconciliation records and 30 accounting events. Relevant chapter statements agree. | Pass |
| Scenario coverage | All `HB-SCN-01` to `HB-SCN-20` records appear in the coverage matrix. The matrix contains 26 rows, including three enabling rows whose scenario is explicitly `Pending`; Chapter 55 describes this distinction accurately. | Pass |
| BIAN non-equivalence | The chapters consistently treat BIAN as a semantic reference. They do not equate a BIAN Service Domain with one microservice, application, team or database. Many-to-many mappings and implementation judgement are stated explicitly. | Pass |
| BIAN evidence state | `HB-BIAN-01` to `HB-BIAN-04` now contain controlled `Confidence` and `Verification Status` fields. Their values are deliberately `Pending` and `Unverified`, and the manuscript does not present exact BIAN 14.0 objects as verified. | Pass |
| Source qualification | Unstable, jurisdiction-dependent and framework-specific claims are qualified and traceable to repository research notes or registered sources. Quantitative recovery, capacity and availability targets are not fabricated. | Pass |
| Diagram governance | `FIG-31-01` to `FIG-36-01` are registered and have specifications, but remain planned pending author approval. No source was created prematurely. Later chapters explicitly defer figures where none are required in this pass. | Pass |
| Boundary continuity | Chapter 31 follows the modelling method established before Part V, and Chapter 56 provides an integrated close before the transition to Chapter 57. | Pass within reviewed scope |

## Issues resolved during review

### Important: BIAN mapping governance fields were incomplete

The original BIAN mapping register did not contain the controlled `Confidence` and `Verification Status` columns required by the Part V design and described by Chapters 49 and 54. This weakened the separation between a plausible candidate mapping and a verified mapping.

The register now contains both fields for every candidate. `HB-BIAN-01` to `HB-BIAN-04` correctly remain `Pending` and `Unverified`. The Horizon Bank validator now requires the columns and controlled values, and the unit suite contains regression coverage. The Chapter 49 wording was synchronised with the repaired schema and current candidate state.

**Resolution:** Verified. The validator passes and all 17 validator unit tests pass.

### Important: Chapter 50 reversed a payment interface boundary

Chapter 50 originally described `HB-INT-036` in the wrong direction, from payment orchestration towards routing. The governed interface instead carries the accepted payment command from `HB-APP-033 Payment Initiation Service` to `HB-APP-034 Payment Orchestration`. Routing begins with `HB-INT-037 Payment Clearing Instruction`, from `HB-APP-034` to `HB-APP-035 Payment Routing and Clearing`.

The prose now uses the correct direction and exact catalogue names. A fresh explicit-arrow audit and exact-name comparison found no remaining mismatch.

**Resolution:** Verified.

### Routine: Chapter 49 became stale after the register repair

Two Chapter 49 statements still said that the mapping register needed confidence and verification fields after those fields had been added. They now state that the fields exist, while the four candidate values remain `Pending` and `Unverified` until exact BIAN 14.0 objects, evidence and review decisions are supplied.

**Resolution:** Verified.

## Severity summary

| Severity | Found | Resolved | Open | Assessment |
|---|---:|---:|---:|---|
| Critical | 0 | 0 | 0 | No issue threatens technical validity or safe publication review. |
| Important | 2 | 2 | 0 | BIAN evidence-state governance and the Chapter 50 interface direction were corrected and revalidated. |
| Routine | 1 | 1 | 0 | Post-repair Chapter 49 wording was brought back into line with the register. |
| Observation | 3 | 0 | 3 | These are deliberate, visible evidence or approval gaps and are not blockers. |

## Remaining non-blocking gaps

The following gaps are explicit and technically honest. None requires a manuscript correction before Part V proceeds to the next editorial gate:

1. **Exact BIAN 14.0 mappings remain unverified.** The four records are candidate author models, not claimed standard mappings. Exact objects, evidence links, confidence decisions and formal verification remain future specialist work.
2. **Institution-specific operating values remain pending.** Quantitative recovery time objectives, recovery point objectives, service-level objectives, impact tolerances, volumes and capacity limits require authorised Horizon Bank evidence. The chapters use method and placeholders rather than invented numbers.
3. **Diagram production remains author-gated.** The six planned Part V figures must not proceed to source or export until their specifications receive author approval. Their absence is correctly represented in the diagram register and manuscript.

Other jurisdictional memberships, product variants and physical deployment choices are also identified as author-model gaps where relevant. They are not silently assumed.

## Validation evidence

The following checks were run against the reviewed repository state:

| Command | Result |
|---|---|
| `python -m compileall -q scripts` | Pass |
| `python -m unittest scripts.test_validate_horizon_bank` | Pass, 17 tests |
| `python scripts/validate_horizon_bank.py` | Pass |
| `python scripts/check-structure.py` | Pass; 63 chapters and the plan, status, contents and titles agree |
| `python scripts/check-links.py` | Pass |
| `python scripts/check-terminology.py` | Pass |
| `python scripts/validate-diagrams.py` | Pass |
| `python scripts/check-diagram-register.py` | Pass; 72 diagram entries |
| `python scripts/word-count.py` | Pass |
| `git diff --check` | Pass; no whitespace errors |

## Final verdict

Part V is technically coherent at the level claimed by the manuscript. Its identifiers, names, interface directions, catalogue totals, scenario coverage and responsibility boundaries agree with the governed Horizon Bank model. Its BIAN treatment is appropriately cautious and does not turn a semantic framework into an unsupported one-to-one implementation prescription. Known evidence gaps are visible and controlled.

**Final technical verdict: Pass. No Critical or Important blockers remain for Chapters 31 to 56.**
