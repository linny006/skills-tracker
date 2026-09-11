import pytest

from skills_tracker.language_parser import normalize_languages


def test_normalizes_byte_counts_to_fractions():
    assert normalize_languages({"Python": 65, "JavaScript": 35}) == {
        "Python": 0.65,
        "JavaScript": 0.35,
    }


@pytest.mark.parametrize("raw", [None, {}])
def test_rejects_missing_or_empty_input(raw):
    with pytest.raises(ValueError, match="must not be empty"):
        normalize_languages(raw)


def test_omits_zero_byte_languages():
    assert normalize_languages({"Python": 10, "JavaScript": 0}) == {"Python": 1.0}


@pytest.mark.parametrize("value", [None, -1, float("inf"), True])
def test_rejects_invalid_language_counts(value):
    with pytest.raises(ValueError, match="language count"):
        normalize_languages({"Python": value})


def test_rejects_all_zero_counts():
    with pytest.raises(ValueError, match="positive byte count"):
        normalize_languages({"Python": 0, "JavaScript": 0})


def test_output_sums_to_one_for_uneven_counts():
    result = normalize_languages({"Python": 12_345, "JavaScript": 6_789})

    assert sum(result.values()) == pytest.approx(1.0)
    assert result["Python"] == pytest.approx(12_345 / 19_134)
