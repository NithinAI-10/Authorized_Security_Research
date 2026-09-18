# Case 04: OTP Enumeration and Resend Controls

## Summary

This case study examines an account verification flow where response behavior or resend controls exposed information about account state during authorized research. Target identity, report identifiers, endpoints, account data, exact response values, and operational proof are omitted.

The research question was: does the verification flow reveal whether an account or identifier exists, or permit resend behavior that weakens abuse controls?

## Security Boundary

Authentication and recovery flows process sensitive account-state information. Responses should avoid giving an unauthenticated requester a reliable account-existence signal. OTP delivery controls should also limit repeated requests and protect users from message flooding and automated abuse.

## Safe Validation

Testing used researcher-controlled accounts and the minimum number of requests needed to compare behavior.

1. Confirm the verification flow was in authorized scope.
2. Use controlled test identifiers only.
3. Compare success, error, status, timing, and workflow behavior at a low request volume.
4. Check resend limits without generating sustained traffic or affecting another person's contact channel.
5. Stop after establishing a reproducible difference or control weakness.

This public case study omits exact endpoints, response bodies, thresholds, timing measurements, and automation details that would make testing a live service easier.

## Observed Impact

A reliable difference between known and unknown identifiers can expose account existence. Weak resend controls can increase unwanted OTP delivery and automation risk.

The observed evidence should remain separate from broader claims. Account takeover, large-scale enumeration, service disruption, or financial impact require their own proof and should not be inferred from a response difference alone.

## Remediation

- Return consistent public responses for account-existence checks where the workflow permits it.
- Keep status codes, response structure, and user-facing messages consistent across equivalent states.
- Apply server-side rate limits to OTP requests and resend actions.
- Add cooldowns, bounded retry rules, and abuse detection based on risk.
- Protect both account identifiers and delivery destinations from repeated requests.
- Log suspicious verification activity without storing OTP values in logs.
- Test recovery and verification changes for account enumeration regressions.

## Retest

A successful retest should show equivalent public behavior for controlled existing and non-existing identifiers where appropriate. Resend requests should follow documented limits, and repeated attempts should trigger the intended defensive controls without exposing OTP values.

## Defensive Lesson

Authentication flows need both privacy controls and abuse controls. Uniform responses reduce account-state disclosure. Server-side resend limits reduce message flooding and automated verification abuse.
