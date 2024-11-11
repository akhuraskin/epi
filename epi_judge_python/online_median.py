import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    res = []
    max_heap, min_heap = [], []
    for v in sequence:
        heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -v))
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(max_heap) > len(min_heap):
            res.append(-max_heap[0])
        elif len(max_heap) == len(min_heap):
            res.append((-max_heap[0] + min_heap[0]) / 2)
        else:
            res.append(min_heap[0])

    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
