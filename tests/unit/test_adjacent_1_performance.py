"""Runtime regression checks; elapsed time alone does not prove complexity."""

import unittest
from time import perf_counter

from sanaap_backend_challenge_algorithm.adjacent_1 import find_adjacent_1
from tests.unit.adjacent_1_cases import (
    all_ones_case,
    all_zeros_case,
    alternating_case,
    internal_run_case,
    wraparound_case,
)


class FindAdjacent1PerformanceTests(unittest.TestCase):
    # Allow headroom for slower machines and shared CI runners.
    MAX_DURATION_SECONDS = 5.0

    def assert_large_case(self, make_case):
        text, expected = make_case()
        started = perf_counter()
        actual = find_adjacent_1(text)
        elapsed = perf_counter() - started

        self.assertEqual(actual, expected)
        self.assertLess(
            elapsed,
            self.MAX_DURATION_SECONDS,
            f"{len(text):,} characters took {elapsed:.3f}s "
            f"(limit: {self.MAX_DURATION_SECONDS:.1f}s)",
        )

    def test_one_million_zeros(self):
        self.assert_large_case(all_zeros_case)

    def test_one_million_ones(self):
        self.assert_large_case(all_ones_case)

    def test_one_million_alternating_characters(self):
        self.assert_large_case(alternating_case)

    def test_one_million_characters_with_wraparound_run(self):
        self.assert_large_case(wraparound_case)

    def test_one_million_characters_with_internal_run(self):
        self.assert_large_case(internal_run_case)
