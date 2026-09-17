# Case 01: Authorization Design Review

## Scope

This case documents a sanitized authorization design pattern for defensive review. It contains no target identity or private evidence.

## Security Goal

A protected service should verify the authenticated identity and its permission for each protected resource.

## Review Model

Use synthetic identities and synthetic resources in a controlled environment. Define the expected ownership and role rules before testing. Compare observed access decisions with those rules.

## Risk Pattern

An application that confirms identity without enforcing the resource permission policy has an authorization design weakness. Report impact only at the level supported by controlled evidence.

## Defensive Fix

Enforce permission checks on the server for every protected operation. Base decisions on trusted identity and authorization data. Use deny by default behavior when the required permission is absent.

Keep policy checks consistent across related operations.

## Verification

Confirm that each synthetic identity receives only the access defined by the policy. Confirm that denial responses contain no protected content. Confirm that related protected operations use the same authorization rules. Review server logs for useful authorization decision records.

## Lesson

Authentication establishes identity. Authorization applies permission rules. Protected services need both controls.

## Publication Safety

This document contains no organization name, production address, report identifier, real account identifier, customer record, credential, secret, private communication, or raw traffic capture.
