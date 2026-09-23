import unittest

from sanaap_backend_challenge_algorithm.unique_substring import find_substring
from tests.unit.unique_substring_cases import CORRECTNESS_CASES


class FindSubstringTests(unittest.TestCase):
    def test_longest_unique_substring(self):
        for text, expected_substring, expected_len in CORRECTNESS_CASES:
            with self.subTest(text=text):
                self.assertEqual(
                    find_substring(text), (expected_substring, expected_len)
                )
