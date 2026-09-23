from collections import Counter


def find_substring_naive(text):
    """
    find best substring that has no duplicate char

    time: O(n^2)
    space: O(n^2)
    """
    out = []
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            t = text[i:j]
            has_dup = any(x > 1 for x in Counter(t).values())
            if has_dup:
                break
            out.append(t)
    if not out:
        return '', 0
    best = max(out, key=lambda x: len(x))
    return best, len(best)


def find_substring(text):
    """
    time: O(n)
    space: O(k), for k distinct characters.
    """
    last_seen = {}
    start = 0
    best_start = 0
    best_length = 0

    for end, char in enumerate(text):
        start = max(start, last_seen.get(char, -1) + 1)
        last_seen[char] = end
        length = end - start + 1
        if length > best_length:
            best_start = start
            best_length = length

    return text[best_start:best_start + best_length], best_length
