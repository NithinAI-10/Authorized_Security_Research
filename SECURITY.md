# Security Policy

## Repository Intent

This repository documents defensive practices for **authorized security research**. Its contents are intended to demonstrate professional research methodology, responsible evidence handling, impact analysis, remediation thinking, and safe reporting practices.

## Authorization Requirement

Only test systems, applications, accounts, or environments when you have explicit permission to do so. Applicable bug-bounty rules, coordinated disclosure policies, contracts, laws, and platform terms must always be respected.

Nothing in this repository should be interpreted as permission to test a third-party system.

## Sensitive Information Policy

Do not commit or publish:

- company or program names tied to non-public findings;
- bug-bounty report identifiers;
- live endpoints, internal hostnames, or target-specific request paths;
- credentials, session tokens, API keys, private keys, or secrets;
- customer, employee, or other personal data;
- private program communications or disclosure correspondence;
- raw evidence that could identify a vulnerable production target;
- proof-of-concept details that unnecessarily increase exploitation risk.

Use neutral placeholders such as `example.invalid`, `[REDACTED]`, `USER_A`, and `RESOURCE_1` when illustrating a workflow.

## Evidence Handling

Before material is added to this repository:

1. confirm that publication is permitted;
2. retain only the minimum evidence needed for the educational point;
3. remove target-identifying and user-identifying data;
4. remove secrets and authentication artifacts;
5. review screenshots and metadata for accidental disclosure;
6. describe impact and remediation without exposing reusable attack material against a live system.

A dedicated evidence-handling standard will be maintained in `docs/evidence-handling.md` during the methodology phase.

## Reporting a Security Issue in This Repository

If you discover a security problem in code or automation contained in this repository, avoid placing exploit details or sensitive data in a public issue. Contact the repository owner through an appropriate private channel available on the associated GitHub profile.

Include only the information needed to reproduce and remediate the repository-level issue safely.

## Defensive Use

Examples and future case studies are intentionally sanitized and generalized. They should be used to improve access control, validation, monitoring, secure configuration, incident response, and remediation practices—not to target systems without authorization.
