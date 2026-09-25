"""Correctness cases and deterministic large-input generators."""

CORRECTNESS_CASES = (
    ("1010111", (4, True)),
    ("1110", (3, False)),
    ("0010111", (3, False)),
    # Preserve the current doubled-string behavior for inputs containing only 1s.
    ("1111", (8, True)),
    ("0111110", (5, True)),
    ("01101110", (3, False)),
    ("0000", (0, False)),
    ("", (0, False)),
    ("0", (0, False)),
    ("1", (2, False)),
    ("11", (4, True)),
    ("0101010", (1, False)),
    ("11000111", (5, True)),
    ("011110", (4, True)),
)


def all_zeros_case():
    return "0" * 1_000_000, (0, False)


def all_ones_case():
    return "1" * 1_000_000, (2_000_000, True)


def alternating_case():
    return "10" * 500_000, (1, False)


def wraparound_case():
    return "1" * 300_000 + "0" * 300_000 + "1" * 400_000, (700_000, True)


def internal_run_case():
    return "0" * 100_000 + "1" * 800_000 + "0" * 100_000, (800_000, True)
