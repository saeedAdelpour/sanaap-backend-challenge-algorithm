from collections import Counter


def find_substring(text):
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

if __name__ == '__main__':
    test_cases = (
        ('abbac', 'bac', 3),
        ('', '', 0),
        ('a', 'a', 1),
        ('aaaa', 'a', 1),
        ('abcd', 'abcd', 4),
        ('abba', 'ab', 2),
        ('ABCABCFKAB', 'ABCFK', 5),
    )
    for text, expected_substring, expected_len in test_cases:
        substring, _len = find_substring(text)
        assert substring == expected_substring
        assert _len == expected_len


    print('ok')
