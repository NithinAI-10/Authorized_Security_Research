# Authorized Security Research

A portfolio project for authorized vulnerability research, defensive analysis, evidence handling, remediation, and security automation.

The repository shows how I move from a scoped research question to a documented security finding while protecting target information. Public material uses sanitized examples and removes sensitive details.

## What This Project Demonstrates

- authorization and scope review before testing
- controlled validation with clear baselines
- evidence collection and publication sanitization
- observed versus potential impact analysis
- remediation and retest planning
- defensive Python automation
- unit testing and continuous integration
- responsible public documentation

## Research Workflow

1. Confirm authorization and scope.
2. Define the security question and expected secure behavior.
3. Record a baseline.
4. Change one relevant condition and compare the result.
5. Collect the minimum evidence needed for review.
6. Separate observed behavior from potential impact.
7. Propose remediation and a retest plan.
8. Sanitize all material before public use.

See `docs/methodology.md`, `docs/evidence-handling.md`, `docs/impact-assessment.md`, and `docs/reporting-workflow.md` for the full process.

## Sanitized Case Studies

The `case-studies/` directory contains four defensive studies:

- Access control: server-side authorization and object access boundaries.
- CORS configuration: origin trust, credential handling, and browser access policy.
- Sensitive key exposure: secret boundaries, rotation, storage, and validation.
- OTP enumeration: response consistency, resend controls, rate limits, and abuse detection.

Each study removes target identity, live endpoints, private communications, customer data, secrets, and sensitive proof of concept details.

## Defensive Automation

`scripts/sanitize_evidence.py` redacts common sensitive patterns from text before review.

`scripts/generate_case_index.py` builds a deterministic index from sanitized case-study files.

`scripts/validate_markdown.py` checks public Markdown for basic structure and selected sensitive-data patterns.

These tools support review. They do not replace manual inspection before publication.

## Tests and CI

The test suite covers evidence sanitization and deterministic case index generation. GitHub Actions runs the unit tests and Markdown validation on repository changes.

Run the checks locally:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/validate_markdown.py .
```

## Repository Structure

```text
.github/workflows/   Continuous integration
docs/                Research and reporting methodology
templates/           Reusable reporting templates
case-studies/        Sanitized defensive case studies
scripts/             Defensive research automation
tests/               Unit tests
screenshots/         Guidance and future sanitized visual evidence
```

## Safety Boundary

This repository does not publish company names tied to private findings, bug bounty report IDs, live targets, credentials, tokens, private keys, customer information, private program communications, or sensitive proof of concept details.

Research belongs here only when the underlying work was authorized. Public examples stay focused on security reasoning, defensive lessons, remediation, and verification.

## Project Documentation

- `SECURITY.md` defines authorization and disclosure rules.
- `CONTRIBUTING.md` defines safe contribution checks.
- `docs/lessons-learned.md` records practical research lessons.
- `screenshots/README.md` defines the screenshot publication gate.
- `ROADMAP.md` tracks useful future work.
- `CHANGELOG.md` records project milestones.

## Status

Phases 1 through 7 are complete. Screenshot evidence remains pending until safe source images are available and pass the publication review process.
