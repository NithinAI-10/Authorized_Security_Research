# Screenshot Guidance

Screenshot work is pending. No screenshot in this repository should be fabricated or reconstructed as if it were original evidence.

## Publication Gate

Before adding an image, confirm all of these points:

- The image comes from authorized work or from this repository's own tooling.
- The image adds technical value beyond the written case study.
- Organization names, report IDs, live hosts, account identifiers, personal data, tokens, cookies, credentials, keys, and private communications are absent or fully redacted.
- Browser tabs, bookmarks, window titles, terminal prompts, file paths, timestamps, and metadata do not expose sensitive context.
- The remaining content does not provide sensitive proof of concept details for a live system.
- A second manual review confirms the redaction before commit.

## Useful Screenshots

The following images would improve portfolio review after safe source material exists:

1. `sanitized-request-response.png`: a sanitized HTTP request and response. Show the relevant headers or fields and the observed security behavior. Redact the host, path identifiers, cookies, tokens, account data, and unique target details.
2. `sanitized-api-flow.png`: a sanitized API flow or diagram. Show trust boundaries and request sequence. Replace target names and live endpoints with neutral labels.
3. `ci-success.png`: the GitHub Actions result for this repository. Show the workflow name, successful test and validation steps, and commit context. Review the page for account or notification details before capture.
4. `research-workflow.png`: a diagram of authorization, baseline testing, controlled validation, impact review, remediation, retest, and publication review. Use generic labels only.
5. `report-template-preview.png`: a preview of the repository's sanitized report template. Use placeholder data only.

## Storage

Store approved images in this `screenshots/` directory. Use descriptive lowercase file names with hyphens. Do not commit raw versions beside redacted copies.
