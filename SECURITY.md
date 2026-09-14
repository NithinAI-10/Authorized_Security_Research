# Security Policy

## Repository Intent

This repository documents defensive practices for authorized security research. The material focuses on research methods, evidence handling, impact analysis, remediation, and safe reporting.

## Authorization Requirement

Test systems, applications, accounts, or environments only with explicit permission. Follow applicable bug bounty rules, coordinated disclosure policies, contracts, laws, and platform terms.

This repository does not grant permission to test any third party system.

## Sensitive Information Policy

Do not commit or publish:

- Company or program names linked to nonpublic findings.
- Bug bounty report identifiers.
- Live endpoints, internal hostnames, or target specific request paths.
- Credentials, session tokens, API keys, private keys, or secrets.
- Customer, employee, or other personal data.
- Private program communications or disclosure correspondence.
- Raw evidence that identifies a vulnerable production target.
- Proof of concept details that increase exploitation risk without a defensive need.

Use neutral placeholders such as `example.invalid`, `[REDACTED]`, `USER_A`, and `RESOURCE_1` in public examples.

## Evidence Handling

Before adding material to this repository:

1. Confirm publication permission.
2. Retain only the evidence required for the educational point.
3. Remove target identifying and user identifying data.
4. Remove secrets and authentication artifacts.
5. Review screenshots and metadata for accidental disclosure.
6. Describe impact and remediation without exposing reusable attack material against a live system.

Phase 2 adds the detailed evidence handling standard in `docs/evidence-handling.md`.

## Reporting a Repository Security Issue

Do not place exploit details or sensitive data in a public issue. Contact the repository owner through an appropriate private channel listed on the associated GitHub profile.

Provide only the information required to reproduce and remediate the repository issue safely.

## Defensive Use

Examples and case studies use sanitized, generalized data. Use the material to improve access control, validation, monitoring, secure configuration, incident response, and remediation. Do not use it to target systems without authorization.
