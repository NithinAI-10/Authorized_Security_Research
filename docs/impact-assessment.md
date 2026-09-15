# Impact Assessment

## Purpose

This framework links a technical finding to demonstrated security impact. It separates observed facts from assumptions and gives reviewers a consistent basis for severity discussions.

## Start With the Security Boundary

Identify the control the test crossed or weakened.

Common boundaries include:

- one user accessing another user's object
- a low privilege role reaching an administrative function
- an untrusted origin receiving protected browser data
- a secret exposed outside its intended trust boundary
- an authentication flow revealing account state

State the boundary before assigning severity.

## Record Preconditions

List the access needed before the issue occurs.

Examples:

- no account
- normal user account
- privileged account
- possession of a valid session
- knowledge of an object identifier
- user interaction
- network position

Do not omit preconditions. They affect practical risk.

## Separate Observed and Potential Impact

### Observed impact

Record only what the controlled test demonstrated.

Example:

> USER_B received RESOURCE_1 after authentication even though RESOURCE_1 belonged to USER_A.

### Potential impact

Describe a broader outcome only when the application design and evidence support it. Label it as potential impact.

Do not increase data access, modify real records, or test destructive actions to strengthen a severity claim.

## Evaluate Security Properties

### Confidentiality

Ask whether an unauthorized party received protected information.

Record:

- type of data demonstrated
- amount of controlled data exposed
- required role
- whether access crosses users or tenants

### Integrity

Ask whether an unauthorized party changed protected state.

Record the exact controlled change and the authorization boundary crossed.

### Availability

Ask whether the finding affected service access or resource availability. Do not run load or destructive tests unless the scope explicitly permits them.

### Authentication and authorization

Record whether the issue bypassed identity verification, role checks, object ownership, tenant separation, or another access rule.

## Evaluate Reach

Describe how broadly the demonstrated condition applies without probing beyond authorization.

Use evidence such as:

- one tested object type
- one tested role pair
- one tested endpoint pattern
- one controlled workflow

Do not state that all users or all records are affected unless evidence supports that scope.

## Evaluate Exploit Requirements

Document practical requirements:

- authentication level
- user interaction
- identifier knowledge
- timing requirements
- browser security conditions
- special configuration
- repeated requests

A reviewer should understand what must be true before the security effect occurs.

## Confidence Level

Use one of these labels:

### Confirmed

Repeatable controlled evidence demonstrates the security boundary failure.

### Supported

Evidence supports the finding, but one part of scope or impact remains untested because of safety or authorization limits.

### Unconfirmed

Evidence is insufficient for a security claim.

Do not present an unconfirmed result as a vulnerability.

## Severity Discussion

If a program defines a rating system, follow that system in the private report. For this public portfolio, explain the risk factors instead of assigning an unsupported score.

A useful assessment states:

1. the failed security control
2. the access required
3. the demonstrated result
4. the affected security property
5. the tested reach
6. limiting conditions
7. remediation priority

## Example Assessment

Finding type: object authorization failure

Precondition: authenticated normal user

Observed result: USER_B reads a synthetic object owned by USER_A

Security property: confidentiality

Tested reach: one object type with controlled records

User interaction: none after USER_B authenticates

Confidence: confirmed

Defensive priority: enforce object-level authorization on the server before returning protected data

This example does not claim access to real customer data or broader application coverage.

## Retest Criteria

Define success before remediation testing.

For the example above, successful remediation requires the server to reject USER_B's request for RESOURCE_1 unless an explicit policy grants USER_B access. Test both allowed and denied cases with controlled accounts.

## Publication Check

Before publishing an impact statement, confirm:

- each factual claim has supporting sanitized evidence
- potential outcomes are labeled as potential
- no claim depends on unperformed destructive testing
- no target identity or private program detail appears
- the assessment states relevant preconditions and limits
- remediation addresses the failed control