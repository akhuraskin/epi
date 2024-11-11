import heapq
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    res = []
    h = []
    for v in sequence:
        if len(h) < k:
            heapq.heappush(h, v)
        else:
            res.append(heapq.heappushpop(h, v))
    while h:
        res.append(heapq.heappop(h))
    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
