from scripts.generate_case_index import build_index


def test_builds_sorted_index_from_case_titles(tmp_path):
    (tmp_path / "case-02-second.md").write_text("# Second Case\n", encoding="utf-8")
    (tmp_path / "case-01-first.md").write_text("# First Case\n", encoding="utf-8")

    result = build_index(tmp_path)

    assert "[First Case](case-01-first.md)" in result
    assert "[Second Case](case-02-second.md)" in result
    assert result.index("First Case") < result.index("Second Case")


def test_uses_safe_filename_fallback_when_heading_is_missing(tmp_path):
    (tmp_path / "case-03-safe-example.md").write_text("Sanitized notes.\n", encoding="utf-8")

    result = build_index(tmp_path)

    assert "[Case 03 Safe Example](case-03-safe-example.md)" in result
