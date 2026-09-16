# Remediation Template

## Finding Reference

Security class: [General vulnerability class]

Affected control: [Authorization, origin policy, secret management, authentication, input validation, other]

## Root Cause

[Describe why the security control failed. Focus on the enforcement point.]

## Primary Remediation

[Describe the required control change.]

Owner: [Application, API, identity, platform, infrastructure, other]

Priority: [Low, Medium, High, Urgent]

## Implementation Requirements

- [Required security rule]
- [Required server side or system side enforcement]
- [Failure behavior]
- [Logging or monitoring requirement]

## Supporting Controls

[Add controls that reduce risk or improve detection. Do not replace the primary fix with monitoring alone.]

Examples:

- structured audit logging for denied actions
- rate controls for abuse prone authentication flows
- secret scanning and rotation procedures
- strict allowlists for trusted origins
- automated authorization regression tests

## Verification Plan

### Negative test

Action: [Repeat the prior unauthorized or unsafe condition.]

Expected result: [The system rejects or safely handles the action.]

### Positive test

Action: [Perform the expected authorized workflow.]

Expected result: [Normal authorized use succeeds.]

### Regression test

Action: [Test a nearby security rule affected by the change.]

Expected result: [The related control still works as designed.]

## Evidence Required for Closure

- [Sanitized response or test result showing the unsafe path fails]
- [Result showing expected use still works]
- [Relevant log or automated test result when available]

## Residual Risk

[State any remaining risk after the fix. If evidence does not support a conclusion, write "I don’t know" and identify what needs verification.]

## Closure Criteria

Close the finding when the primary control is enforced, the negative test fails safely, expected use still works, and relevant regression checks pass.