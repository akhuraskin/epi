from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    result = []

    def unique(arr):
        prev = None
        for v in arr:
            if prev is None or prev != v:
                prev = v
                yield v

    arr_a = unique(A)
    arr_b = unique(B)

    a = next(arr_a, None)
    b = next(arr_b, None)
    while a is not None and b is not None:
        if a == b:
            result.append(a)
            a = next(arr_a, None)
            b = next(arr_b, None)
        elif a < b:
            a = next(arr_a, None)
        elif b < a:
            b = next(arr_b, None)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
