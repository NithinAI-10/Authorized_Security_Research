# Case 03: Sensitive Key Exposure

## Summary

This case study examines a sensitive cryptographic key exposed through application-accessible content during authorized research. All target details, identifiers, paths, values, and original evidence are omitted.

The research question was simple: does material delivered to an untrusted client contain a key that should remain private?

## Security Boundary

Private cryptographic material belongs on a trusted system with strict access controls. Client-side code, public files, application responses, logs, and downloadable assets do not provide a safe storage boundary for a private key.

## Safe Validation

The review used the minimum evidence needed to classify the exposed material.

1. Confirm the tested asset was in authorized scope.
2. Identify the material type without copying its value into public notes.
3. Confirm an untrusted client received or accessed the material.
4. Check whether the key role required confidentiality.
5. Stop after confirming the exposure. Do not use the key to access another system, impersonate a user, or decrypt unrelated data.

This public case study does not include the key, a fingerprint, a live path, target metadata, or a request and response pair.

## Observed Impact

The observed condition was disclosure of cryptographic material across a trust boundary. The evidence supported an exposure finding. It did not, by itself, prove downstream account access, data decryption, signing abuse, or compromise of another service.

Potential impact depends on the key purpose, trust relationships, permissions, deployment state, and whether the exposed value remains active. Those factors require separate evidence.

## Remediation

- Remove private key material from client-accessible content and source artifacts.
- Revoke or rotate the exposed key according to its role.
- Store replacement secrets in an approved secret-management system.
- Limit secret access to the service identities that need it.
- Review build output, logs, backups, and deployment artifacts for copies.
- Add secret scanning to local development and CI checks.
- Record rotation and retest results without placing secret values in tickets or source control.

## Retest

A successful retest should show the sensitive material is absent from untrusted content, the old key is no longer trusted where rotation applies, and the replacement secret is stored behind the intended access boundary.

## Defensive Lesson

Treat private cryptographic material as a secret for its full lifecycle. Prevention requires secure storage, narrow access, safe build processes, scanning, rotation procedures, and verification after remediation.
