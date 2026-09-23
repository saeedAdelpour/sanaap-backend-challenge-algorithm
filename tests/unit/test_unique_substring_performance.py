"""Runtime regression checks; elapsed time alone does not prove complexity."""

import unittest
from time import perf_counter

from sanaap_backend_challenge_algorithm.unique_substring import find_substring
from tests.unit.unique_substring_cases import (
    distinct_characters_case,
    repeated_alphabet_case,
    repeated_character_case,
)


class FindSubstringPerformanceTests(unittest.TestCase):
    # Allow headroom for slower machines and shared CI runners.
    MAX_DURATION_SECONDS = 5.0

    def assert_large_case(self, make_case):
        text, expected = make_case()
        # Exclude input generation and correctness assertions from the timing.
        started = perf_counter()
        actual = find_substring(text)
        elapsed = perf_counter() - started

        self.assertEqual(actual, expected)
        self.assertLess(
            elapsed,
            self.MAX_DURATION_SECONDS,
            f"{len(text):,} characters took {elapsed:.3f}s "
            f"(limit: {self.MAX_DURATION_SECONDS:.1f}s)",
        )

    def test_one_million_repeated_characters(self):
        self.assert_large_case(repeated_character_case)

    def test_one_hundred_thousand_distinct_characters(self):
        self.assert_large_case(distinct_characters_case)

    def test_one_million_characters_with_large_unique_windows(self):
        self.assert_large_case(repeated_alphabet_case)
