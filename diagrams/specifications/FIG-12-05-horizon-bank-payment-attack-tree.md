# FIG-12-05: Horizon Bank Payment Attack Tree

## Purpose

Show alternative and combined paths by which an attacker could cause an unauthorised or prohibited outgoing retail payment to be released.

## Audience

Security teams, architects, risk reviewers, developers and operations teams.

## Question answered

What paths could lead to the harmful goal of unauthorised or prohibited payment release?

## Notation

Attack tree. PlantUML mind map or tree layout is the intended source approach after author approval.

## Required elements

- Root goal: cause an unauthorised or prohibited outgoing payment to be released.
- Branch T12-01: use stolen or replayed customer session to create payment.
- Branch T12-02: abuse weak entitlement check to create payment from the wrong account.
- Branch T12-02: tamper with amount or beneficiary between channel and platform.
- Branch T12-03: use stolen service credential to submit posting request.
- Branch T12-04: exploit operations repair path and weak separation-of-duties rule.
- Branch T12-05: misuse privileged financial-crime release function.
- Branch T12-06: expose sensitive status event data for later misuse.
- Mitigation prompts shown as notes or linked annotations, not as ordinary attack branches.

## Required relationships

- Branches are alternative paths to the root goal unless explicitly marked as combined steps.
- Where a path requires two conditions together, label the relationship as AND.
- Where paths are alternatives, label the relationship as OR.
- Each main branch connects to a threat ID used in the manuscript control map and `FIG-12-04`.
- Each mitigation prompt connects to architecture or control review, such as stronger authentication, ownership check, message integrity, service identity control, maker-checker rule, privileged-access review, event data minimisation or audit alerting.

## Main flow or structure

Place the harmful goal at the root. Show attack paths as branches. Keep branch text concrete and reviewable without adding exploit instructions.

## Alternative and exception flows

Do not add low-level exploit steps, vulnerability scoring, probability values or cost values. The tree is a teaching view for architectural threat paths.

## Scope

Horizon Bank outgoing retail payment attack-path teaching example.

## Exclusions

- Detailed exploit instructions.
- Real-world bank-specific attack intelligence.
- Vulnerability scoring.
- Quantitative attack probability or cost analysis.
- Complete control catalogue.

## Accessibility requirements

Use text labels for AND and OR semantics. Do not encode branch status only by colour.

## Source references

- `[OWASP-THREAT-MODELLING-2026]`
- `[MICROSOFT-STRIDE-2026]`
- `[NIST-CSF-2.0]`
- `[SCHNEIER-ATTACK-TREES-1999]`

## Review criteria

- The root harmful goal is concrete.
- Branches are specific enough to review.
- AND and OR semantics are visible in text.
- Mitigation prompts are not confused with attack branches.
- The diagram does not provide exploit instructions.
- Threat IDs connect to the manuscript control map and `FIG-12-04`.
