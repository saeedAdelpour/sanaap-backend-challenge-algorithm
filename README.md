# Sanaap Backend Challenge — Algorithms

Python solutions for two algorithm challenges. Requires Python 3.11+ and uv.

- [Unique substring](src/sanaap_backend_challenge_algorithm/unique_substring.py): Finds the longest substring without repeated characters and returns the substring and its length.
- [Adjacent ones](src/sanaap_backend_challenge_algorithm/adjacent_1.py): Finds the longest run of adjacent `1` characters, including runs across the end and start of the input. Returns the run length and whether it reaches a configurable threshold (default: 4). The implementation scans the doubled input, so an all-ones input returns twice its original length.

Run all tests from the project root:

```sh
uv run python -m unittest discover -s tests -t . -v
```

Tests use Python's `unittest` and cover correctness and large inputs, including million-character cases with a five-second runtime limit per case.
