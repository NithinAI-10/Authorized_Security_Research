# Reporting Workflow

This workflow turns validated research into a clear security report. Use it only for authorized testing.

## 1. Confirm the finding

Reproduce the behavior with the smallest safe test.

Record:

- expected behavior
- observed behavior
- affected security boundary
- required account or privilege level
- minimum evidence needed to support the result

Stop if the result depends on uncertain assumptions. Record the uncertainty instead of presenting it as fact.

## 2. Separate observation from impact

Describe what the test proved before discussing possible outcomes.

Use this structure:

- Observed: what happened during the authorized test
- Impact: what the observed behavior changes for confidentiality, integrity, availability, or authorization
- Preconditions: what an actor needs before reaching the behavior
- Limits: what the test did not prove

Use `docs/impact-assessment.md` for the full assessment process.

## 3. Prepare evidence

Follow `docs/evidence-handling.md` before moving evidence into a report.

Remove:

- organization and program names
- report identifiers
- live hosts and target paths
- credentials, tokens, cookies, and keys
- personal or customer data
- private disclosure messages
- unrelated response data

Use placeholders such as `example.invalid`, `USER_A`, `RESOURCE_1`, and `[REDACTED]`.

## 4. Write reproduction steps

Write the minimum steps needed for an authorized reviewer to verify the issue.

Each step should state one action and its expected result. Avoid destructive actions, broad scanning instructions, persistence steps, or target specific exploit material.

A useful sequence is:

1. establish the required test state
2. perform the controlled request or action
3. record the security relevant response
4. compare the response with the expected access or validation rule

## 5. Assign severity with evidence

Base severity on demonstrated impact, required access, affected data or action, reach, and repeatability.

Do not increase severity based on an untested attack chain. Mark uncertain impact as unverified.

## 6. Recommend remediation

Tie each recommendation to the failed security control.

Prefer fixes at the enforcement point. Examples include server side authorization, strict origin validation, secret rotation, uniform authentication responses, rate controls, and monitoring.

Include a verification condition for each primary fix.

## 7. Review the report

Before submission, check:

- authorization remained valid during testing
- title states the security problem
- summary describes the failed control
- evidence supports each factual claim
- reproduction steps use the minimum safe actions
- impact distinguishes observed and potential outcomes
- remediation addresses the root control failure
- secrets and identifying data are absent

## 8. Submit through the approved channel

Follow the program or system owner's reporting process. Keep private material in the approved private channel.

Do not place private report content in this public repository.

## 9. Retest a fix

When authorized, repeat the minimum validation after remediation.

Record:

- original security condition
- expected fixed behavior
- observed fixed behavior
- regression checks relevant to the control

A successful retest should show the unauthorized or unsafe behavior no longer succeeds while expected use still works.

## 10. Prepare a portfolio case study

Create a public case study only after checking publication rules.

Remove target identity, private communications, live endpoints, report IDs, secrets, user data, and reusable target specific exploit details.

Focus the public version on the security class, reasoning process, evidence discipline, impact assessment, remediation, and lessons learned.