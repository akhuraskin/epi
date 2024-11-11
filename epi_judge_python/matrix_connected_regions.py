from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    N, M = len(image), len(image[0])
    def neighbors(n, m, color: bool):
        yield from ((i, j) for i, j in [(n-1, m), (n+1, m), (n, m-1), (n, m+1)]
                    if 0<=i<N and 0<=j<M and image[i][j] == color)

    src_color = image[x][y]
    q = [(x, y)]
    while q:
        ci, cj = q.pop()
        for ni, nj in neighbors(ci, cj, src_color):
            q.append((ni, nj))
        image[ci][cj] = not src_color


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
