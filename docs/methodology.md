# Research Methodology

## Purpose

This process defines a repeatable method for authorized security research. It keeps testing inside scope, limits data collection, records evidence, and links each finding to a defensive fix.

## 1. Confirm Authorization

Before testing, record the approved scope and rules in private working notes.

Check:

- approved assets and account types
- allowed test methods
- prohibited actions
- rate limits and traffic rules
- data access restrictions
- disclosure requirements
- testing dates, if the program sets them

Stop if scope is unclear. Resolve the scope before sending test traffic.

## 2. Define the Security Question

Write one testable question before collecting evidence.

Example:

> Does the application enforce object ownership when one test account requests a resource created by another test account?

A narrow question reduces unnecessary requests and keeps evidence focused.

## 3. Establish a Baseline

Record expected behavior with an authorized test account. Use controlled test data rather than real user data.

For an access control review, a baseline might record:

1. USER_A creates RESOURCE_1.
2. USER_A reads RESOURCE_1.
3. USER_B requests RESOURCE_1.
4. The application should reject USER_B unless policy grants access.

Do not publish live hosts, real identifiers, session values, or private program details.

## 4. Test One Variable at a Time

Change one relevant input per test. Record the expected result and observed result.

Useful fields include:

- test objective
- preconditions
- changed input
- expected behavior
- observed behavior
- timestamp
- evidence reference

This structure makes retesting easier and reduces unsupported conclusions.

## 5. Validate the Finding

Repeat the minimum safe test needed to rule out a transient result or test error. Do not increase impact to prove severity.

Ask:

- Is the result repeatable?
- Does it depend on a specific role or state?
- Does the result cross a security boundary?
- Does a normal product feature explain the behavior?
- Is the collected evidence sufficient for review?

If evidence does not support a claim, record the result as unconfirmed.

## 6. Assess Impact

Separate observed impact from possible impact. Base the primary assessment on behavior demonstrated with controlled data.

Consider:

- confidentiality
- integrity
- availability
- authorization boundary
- affected user role
- required attacker access
- interaction required from another user
- scope of exposed or changed data

Use `docs/impact-assessment.md` for the full process.

## 7. Sanitize Evidence

Create a publication copy separate from raw research material. Replace identifying values with stable placeholders such as `USER_A`, `RESOURCE_1`, and `example.invalid`.

Remove:

- organization names
- report identifiers
- live hosts and paths
- credentials and authentication artifacts
- secrets and keys
- personal data
- private communications
- unrelated response data

Follow `docs/evidence-handling.md` before committing evidence or a case study.

## 8. Write Remediation Guidance

Tie each recommendation to the failed control. Prefer fixes at the enforcement point instead of client-side checks.

For an object authorization issue, guidance might require the server to verify the authenticated subject has permission for the requested object on every protected operation.

Include a retest condition so reviewers know what successful remediation looks like.

## 9. Report Through the Approved Channel

Submit findings through the program or system owner's approved reporting process. Keep private report material outside this public repository.

A report should state:

- affected security control
- safe reproduction steps
- observed result
- expected result
- demonstrated impact
- remediation guidance
- sanitized evidence references

## 10. Retest and Close

When authorized, repeat the original minimum test after remediation. Record whether the expected control now holds.

Do not expand scope during retesting without new authorization.

## Publication Gate

Before publishing any repository material, confirm all of these conditions:

- the content is permitted for public release
- target identity is removed
- user identity is removed
- secrets and authentication data are removed
- evidence uses controlled or synthetic data
- reproduction details do not expose a live target
- impact claims match observed evidence
- remediation guidance is present

If any condition fails, keep the material private.