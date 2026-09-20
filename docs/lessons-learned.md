# Lessons Learned

## Authorization Defines the Work

Start with scope. Record what testing the program permits, which assets are in scope, and which actions are prohibited. Stop when a test would cross those limits.

## Separate Observation From Impact

Record what you observed before describing risk. A response difference, exposed value, or missing control does not prove every possible consequence. Label assumptions and keep impact claims tied to evidence.

## Collect the Minimum Evidence

Keep the smallest evidence set needed to support a finding. Redact identifiers, secrets, personal data, and target details before material enters a public repository.

## Test One Question at a Time

Use controlled changes. Change one input or condition, compare the result with a baseline, and record the difference. This makes findings easier to review and reduces unnecessary traffic.

## Remediation Needs Verification

A proposed fix is incomplete without a retest plan. Define the expected secure result, a positive test for intended behavior, a negative test for blocked behavior, and a regression check for related paths.

## Automation Supports Review

Small tools reduce repeat work. This repository uses scripts to sanitize common evidence patterns, generate a case index, and validate public Markdown. Human review remains required before publication because pattern matching does not identify every sensitive value.

## Sanitized Work Still Needs Technical Value

Remove target identity and sensitive reproduction details while preserving the security boundary, test method, observed behavior, impact reasoning, remediation, and retest logic. A portfolio case study should explain the reasoning without creating risk for the affected system.
