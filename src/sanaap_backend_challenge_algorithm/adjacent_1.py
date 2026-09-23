EXPECT_TO_FOUND = 4


def find_adjacent_1(text, expect_to_found=EXPECT_TO_FOUND):
    """
    time: O(2n) + (
        O(1) average
        + O(1) average
    ) + ~O(n)
    = O(n)
    space: O(2n) = O(n)
    """
    rotate_text = text + text
    seen = {}
    start = None
    for i, c in enumerate(rotate_text):
        if c == "1":
            if start is None:
                start = i
            seen.setdefault(start, [])
            seen[start].append(i)
        else:
            start = None

    if not seen:
        return 0, False
    print(text, seen)
    length = max(map(len, seen.values()))
    return length, length >= expect_to_found


if __name__ == "__main__":
    for text, expect_length, expect_found_correct_1s in (
        ("1010111", 4, True),
        ("1110", 3, False),
        ("0010111", 3, False),
        ("1111", 8, True),  # TODO(saeed): length is 4 or 8?
        ("0111110", 5, True),
        ("01101110", 3, False),
        ("0000", 0, False),
        ("", 0, False),
    ):
        length, found_correct_1s = find_adjacent_1(text)
        assert length == expect_length
        assert found_correct_1s == expect_found_correct_1s
    print("ok")
