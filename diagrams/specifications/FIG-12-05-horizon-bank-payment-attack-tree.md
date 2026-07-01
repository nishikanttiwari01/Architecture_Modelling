# FIG-12-05: Horizon Bank Payment Attack Tree

## Purpose

Show alternative paths by which an attacker could submit or cause an unauthorised outgoing retail payment.

## Audience

Security teams, architects, risk reviewers, developers and operations teams.

## Question answered

What paths could lead to the harmful goal of unauthorised payment submission?

## Notation

Attack tree. PlantUML mind map or tree layout is the intended source approach after author approval.

## Required elements

- Root goal: submit unauthorised payment.
- Branch: compromise customer authentication.
- Branch: abuse weak payment entitlement.
- Branch: tamper with payment request between channel and platform.
- Branch: use stolen service credential.
- Branch: exploit operations repair path.
- Branch: bypass screening or approval through privileged function.
- Mitigation prompts beside or beneath each main branch.

## Required relationships

- Branches are alternative paths to the root goal unless explicitly marked as combined steps.
- Each branch has at least one concrete mitigation prompt, such as stronger authentication, entitlement check, message integrity, service identity control, maker-checker rule, privileged-access review or audit alert.

## Main flow or structure

Place the harmful goal at the root. Show attack paths as branches. Keep branch text concrete and reviewable.

## Alternative and exception flows

Where a path requires two conditions together, mark the relationship as AND. Where paths are alternatives, mark as OR or use visual grouping with textual explanation.

## Scope

Horizon Bank outgoing retail payment attack-path teaching example.

## Exclusions

- Detailed exploit instructions.
- Real-world bank-specific attack intelligence.
- Vulnerability scoring.
- Complete control catalogue.

## Accessibility requirements

Use text labels for AND and OR semantics. Do not encode branch status only by colour.

## Source references

- `[OWASP-THREAT-MODELLING-2026]`
- `[MICROSOFT-STRIDE-2026]`
- `[NIST-CSF-2.0]`

## Review criteria

- The root harmful goal is concrete.
- Branches are specific enough to review.
- The diagram does not provide exploit instructions.
- Mitigation prompts connect to architecture or control review.
