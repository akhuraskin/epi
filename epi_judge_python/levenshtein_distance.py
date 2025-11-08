from test_framework import generic_test
import functools

def levenshtein_distance(A: str, B: str) -> int:
    @functools.cache
    def f(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if A[i-1] == B[j-1]:
            return f(i-1, j-1)
        return 1+min(
            f(i-1, j-1),
            f(i-1, j),
            f(i, j-1)
        )

    return f(len(A), len(B))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
