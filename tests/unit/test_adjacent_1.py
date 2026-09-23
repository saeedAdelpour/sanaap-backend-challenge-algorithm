import unittest

from sanaap_backend_challenge_algorithm.adjacent_1 import find_adjacent_1
from tests.unit.adjacent_1_cases import CORRECTNESS_CASES


class FindAdjacent1Tests(unittest.TestCase):
    def test_longest_adjacent_ones(self):
        for text, expected in CORRECTNESS_CASES:
            with self.subTest(text=text):
                self.assertEqual(find_adjacent_1(text), expected)

    def test_custom_threshold(self):
        for threshold, expected_found in ((1, True), (4, True), (5, False)):
            with self.subTest(threshold=threshold):
                self.assertEqual(
                    find_adjacent_1("1010111", expect_to_found=threshold),
                    (4, expected_found),
                )

    def test_no_ones_with_positive_threshold(self):
        for text in ("", "0000"):
            with self.subTest(text=text):
                self.assertEqual(find_adjacent_1(text, expect_to_found=1), (0, False))
