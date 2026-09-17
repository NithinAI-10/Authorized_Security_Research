# Sanitized Case Studies

This directory contains defensive case studies based on patterns observed during authorized security research.

Each case study removes target identities, report identifiers, live endpoints, credentials, secrets, private communications, personal data, and sensitive proof of concept details. The goal is to show research reasoning, impact analysis, and remediation without exposing a production target.

## Case Study Format

Each study records:

1. the security boundary under review
2. the safe validation approach
3. the observed security behavior
4. the impact supported by evidence
5. the remediation approach
6. the checks used for retesting
7. the lessons that transfer to defensive engineering

## Cases

| Case | Topic | Primary Security Area |
| --- | --- | --- |
| [Case 01](case-01-access-control.md) | Access control weakness | Authorization |
| [Case 02](case-02-cors-misconfiguration.md) | CORS misconfiguration | Browser and API security |

Additional sanitized cases will be added as the project progresses.

## Publication Rules

Do not add raw request captures, production URLs, organization names, report IDs, account identifiers, tokens, keys, customer records, or disclosure messages to this directory.

Use placeholders such as `example.invalid`, `USER_A`, `USER_B`, and `RESOURCE_1`. Record only the evidence needed to explain the defensive lesson.
