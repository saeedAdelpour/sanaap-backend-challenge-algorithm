"""Correctness cases and deterministic large-input generators."""

CORRECTNESS_CASES = (
    ('abbac', 'bac', 3),
    ('', '', 0),
    ('a', 'a', 1),
    ('aaaa', 'a', 1),
    ('abcd', 'abcd', 4),
    ('abba', 'ab', 2),
    ('ABCABCFKAB', 'ABCFK', 5),
    ('abcabcbb', 'abc', 3),
    ('pwwkew', 'wke', 3),
    ('dvdf', 'vdf', 3),
    ('a🙂a界', '🙂a界', 3),
    ('a b a', 'a b', 3),
)


def repeated_character_case():
    return 'a' * 1_000_000, ('a', 1)


def distinct_characters_case():
    # Start beyond the surrogate range to generate valid Unicode characters.
    text = ''.join(chr(0x10000 + index) for index in range(100_000))
    return text, (text, len(text))


def repeated_alphabet_case():
    alphabet, _ = distinct_characters_case()
    return alphabet * 10, (alphabet, len(alphabet))
