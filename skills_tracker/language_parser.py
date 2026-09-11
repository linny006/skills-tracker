"""Utilities for normalizing GitHub repository language metadata."""

from __future__ import annotations

import math
from collections.abc import Mapping


def normalize_languages(raw_dict: Mapping[str, int | float] | None) -> dict[str, float]:
    """Convert GitHub language byte counts into fractions that sum to one.

    Languages with a zero byte count are omitted. Missing data, invalid values,
    and mappings whose total byte count is zero raise ValueError because no
    meaningful percentage breakdown can be calculated.
    """
    if not raw_dict:
        raise ValueError("language data must not be empty")

    counts: dict[str, float] = {}
    for language, value in raw_dict.items():
        if not isinstance(language, str) or not language.strip():
            raise ValueError("language names must be non-empty strings")
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"language count for {language!r} must be a number")
        if not math.isfinite(value) or value < 0:
            raise ValueError(f"language count for {language!r} must be finite and non-negative")
        if value > 0:
            counts[language] = float(value)

    total = sum(counts.values())
    if total == 0:
        raise ValueError("language data must contain a positive byte count")

    return {language: count / total for language, count in counts.items()}
