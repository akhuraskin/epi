from test_framework import generic_test


def square_root(k: int) -> int:
    l, r = 0, k

    while l <= r:
        m = l + (r-l) // 2
        sq = m*m
        if sq < k:
            l = m+1
        elif sq == k:
            return m
        else:   # sq > k
            r = m - 1
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
