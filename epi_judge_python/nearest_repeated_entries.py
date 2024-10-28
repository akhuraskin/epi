from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    last_pos = {}
    min_distance = len(paragraph) + 1
    for i, w in enumerate(paragraph):
        if w in last_pos:
            min_distance = min(min_distance, i-last_pos[w])
        last_pos[w] = i
    return min_distance if min_distance <= len(paragraph) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
