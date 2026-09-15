# Evidence Handling Standard

## Purpose

Security evidence should prove a finding while exposing as little sensitive information as possible. This standard covers collection, storage, sanitization, review, and public release for this repository.

## Evidence Classes

### Private raw evidence

Raw captures belong in approved private storage, not this repository. Examples include original HTTP traffic, full logs, packet captures, program messages, and screenshots from live systems.

### Working evidence

Working evidence contains only the fields needed for analysis. Keep it outside the public repository until sanitization and review are complete.

### Publication evidence

Publication evidence contains sanitized material approved for portfolio use. It uses neutral placeholders and removes target-specific details.

## Collection Rules

Collect the minimum evidence needed to support the security claim.

Prefer:

- controlled test accounts
- synthetic records
- narrow request and response excerpts
- timestamps needed for correlation
- status codes and relevant security fields
- short observations tied to a test objective

Avoid collecting unrelated records, bulk data, or information from real users.

## Sensitive Data Checklist

Treat the following as private unless a clear publication rule states otherwise:

- organization and program names linked to non-public findings
- live domains, hosts, internal names, and target-specific paths
- report and ticket identifiers
- usernames, email addresses, phone numbers, and customer records
- session cookies, bearer tokens, CSRF tokens, API keys, and passwords
- private keys, signing material, and recovery codes
- private disclosure messages
- internal infrastructure details unrelated to the finding
- file metadata that identifies a target or person

## Sanitization Rules

Use stable placeholders so a reviewer still understands relationships between objects.

Example mapping:

| Original type | Publication placeholder |
| --- | --- |
| First test account | `USER_A` |
| Second test account | `USER_B` |
| First test object | `RESOURCE_1` |
| Host | `example.invalid` |
| Secret value | `[REDACTED_SECRET]` |
| Session value | `[REDACTED_SESSION]` |

Do not use a shortened real secret as a placeholder. Remove the entire value.

## HTTP Evidence

For a sanitized request or response:

1. Replace the host with `example.invalid`.
2. Replace real object identifiers with stable synthetic values.
3. Remove cookies and authorization values.
4. Remove anti-CSRF values if they identify a session.
5. Remove unrelated headers.
6. Remove personal and customer data from bodies.
7. Keep only fields needed to explain the control failure.
8. Review the final excerpt as if it were public.

## Screenshot Handling

Use screenshots only when they improve technical understanding. Do not fabricate them.

Before adding a screenshot:

1. crop unrelated application areas
2. redact organization and program names
3. redact live domains and identifiers
4. redact authentication values and secrets
5. redact personal data
6. check browser tabs, bookmarks, terminal prompts, and window titles
7. check image metadata before publication
8. use a descriptive file name without target information

Store approved portfolio screenshots under `screenshots/`.

## Storage Rules

The repository `.gitignore` blocks common raw evidence formats and local secret files. Treat ignore rules as a backup control, not as permission to place sensitive material in the repository directory.

Keep raw evidence in storage approved for the research program. Follow its retention and deletion rules.

## Review Before Commit

Run this review before each evidence commit:

- Does the file identify a real target?
- Does it contain a live endpoint?
- Does it contain a report ID?
- Does it contain a credential, token, key, or session value?
- Does it contain personal or customer data?
- Does it quote private program communication?
- Does it include more data than the security claim needs?
- Does the file name or metadata expose private information?

If any answer is yes, do not commit the file until the issue is removed.

## Evidence Integrity

Do not change the technical meaning of evidence during sanitization. Preserve relationships between actors, objects, requests, and results with stable placeholders.

Keep a private mapping only when the authorized research process requires one. Never commit the mapping to this repository.

## Deletion and Retention

Follow the applicable program rules for retention. Delete local raw copies when they are no longer required and when policy permits deletion.

Public portfolio material should contain only the sanitized educational record.