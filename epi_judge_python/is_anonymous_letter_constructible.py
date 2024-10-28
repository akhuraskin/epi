import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    counts_m = collections.Counter(magazine_text)
    counts_l = collections.Counter(letter_text)
    return not(counts_l - counts_m)
    # for c, v in counts_l.items():
    #     if counts_m[c] < v:
    #         return False
    # return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
