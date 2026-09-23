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
    length = max(map(len, seen.values()))
    return length, length >= expect_to_found
