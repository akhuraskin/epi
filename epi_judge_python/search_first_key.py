from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    l, r = 0, len(A)    # k is within [l, r)
    while l < r:
        m = l + (r-l) // 2
        if A[m] >= k:
            r = m
        else:
            l = m+1
    if 0 <= l < len(A) and A[l] == k:
        return l
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
