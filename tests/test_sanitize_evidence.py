from scripts.sanitize_evidence import sanitize_text


def test_redacts_common_sensitive_values():
    source = (
        "Authorization: Bearer demo-token\n"
        "email=researcher@example.test\n"
        "source=192.0.2.10\n"
        "api_key=sample-secret\n"
    )
    result = sanitize_text(source)

    assert "demo-token" not in result
    assert "researcher@example.test" not in result
    assert "192.0.2.10" not in result
    assert "sample-secret" not in result
    assert result.count("[REDACTED") >= 4


def test_redacts_private_key_block():
    source = "-----BEGIN PRIVATE KEY-----\nEXAMPLE\n-----END PRIVATE KEY-----\n"
    result = sanitize_text(source)

    assert "EXAMPLE" not in result
    assert result.strip() == "[REDACTED PRIVATE KEY]"


def test_preserves_non_sensitive_text():
    source = "Finding: authorization checks rejected an unauthorized request.\n"
    assert sanitize_text(source) == source
