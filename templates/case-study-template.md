# Case Study Template

## Security Class

[Example: access control, cross origin policy, secret exposure, authentication workflow]

## Context

[Describe the type of application or workflow without naming the organization, program, product, live host, or report.]

Authorization: [State that testing occurred in an authorized setting.]

## Research Question

[State the security question tested.]

Example: Does the server enforce resource ownership when a signed in user requests an object by identifier?

## Expected Control

[Describe the security rule expected from the system.]

## Test Method

1. [Create or identify the minimum authorized test state.]
2. [Perform the controlled comparison.]
3. [Record only the evidence needed to answer the research question.]
4. [Stop once the result is established.]

## Finding

[Describe the observed behavior without target specific exploit details.]

## Evidence Summary

[Explain what evidence supported the finding. Use sanitized placeholders only.]

Example placeholders:

- `USER_A`
- `USER_B`
- `RESOURCE_1`
- `example.invalid`
- `[REDACTED]`

## Impact Assessment

Observed impact: [State what the test demonstrated.]

Potential impact: [State only supported extensions and mark unverified paths.]

Security boundary: [State the boundary involved.]

Confidence: [High, Medium, Low, with reason]

## Root Control Failure

[Describe the missing, weak, or misplaced security control.]

## Remediation

[Describe the primary server side or system level fix.]

Verification condition: [State the result expected after the fix.]

## Defensive Lessons

- [Lesson about design or enforcement]
- [Lesson about evidence handling]
- [Lesson about impact analysis or retesting]

## Publication Safety Check

Confirm this case study contains no company names, report IDs, live endpoints, credentials, tokens, private keys, customer data, private program communications, or sensitive target specific proof of concept details.

Screenshot status: [Pending, not needed, or sanitized user supplied evidence available]

Never invent screenshot evidence.