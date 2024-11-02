from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def conflicts(row: int, col: int):
        return any(abs(c-col) in (0, abs(row-r)) for r, c in enumerate(col_placement[:row]))

    def solve_n_queens(row: int):
        if row == n:
            result.append(col_placement[:])
        else:
            for col in range(n):
                if not conflicts(row, col):
                    col_placement[row] = col
                    solve_n_queens(row + 1)


    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
