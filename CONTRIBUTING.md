# Contributing

This repository accepts work focused on authorized, defensive security research and portfolio-safe documentation.

## Before You Contribute

Read `SECURITY.md` and the evidence handling guidance in `docs/evidence-handling.md`. Do not submit material collected outside explicit authorization.

## Content Rules

Do not include:

- company or program names tied to private findings
- bug bounty report identifiers
- live endpoints or target-specific reproduction details
- credentials, tokens, cookies, private keys, or other secrets
- customer or personal data
- private program communications
- raw evidence from a live target

Use neutral labels and synthetic examples when an example helps explain the security concept.

## Development Checks

Install the test dependency and run the local checks before submitting changes:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/validate_markdown.py .
```

The Markdown validator checks a limited set of patterns. Manual review is still required.

## Case Study Review

A case study should identify the security boundary, describe the authorized test method, separate observed behavior from potential impact, propose remediation, and define a retest. Remove details that identify or expose a live target.

## Commit Scope

Keep each commit focused on one meaningful change. Use a short professional message that describes the change. Do not create empty or cosmetic commits to increase commit count.

## Screenshot Review

Follow `screenshots/README.md` before adding images. Commit only the approved sanitized image. Do not store the raw image in the repository.
