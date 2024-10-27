from typing import List

from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    merged = []
    minheap = []
    iterators = list(map(iter, sorted_arrays))
    for i, it in enumerate(iterators):
        e = next(it, None)
        if e is not None:
            heapq.heappush(minheap, (e, i))

    while minheap:
        min_elem, i = heapq.heappop(minheap)
        merged.append(min_elem)
        next_elem = next(iterators[i], None)
        if next_elem is not None:
            heapq.heappush(minheap, (next_elem, i))
    return merged


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
