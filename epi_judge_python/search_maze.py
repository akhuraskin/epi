import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def neighbors(maze, c: Coordinate):
    N = len(maze)
    M = len(maze[0])
    i, j = c
    for (di, dj) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if 0 <= i + di < N and 0 <= j + dj < M and maze[i+di][j+dj] != BLACK:
            yield Coordinate(i + di, j + dj)

def dfs(maze, path: List[Coordinate], e: Coordinate):
    if path[-1] == e:
        return path
    i, j = path[-1]
    maze[i][j] = BLACK

    for n in neighbors(maze, path[-1]):
        p = dfs(maze, path+[n], e)
        if p:
            return p
    return []


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    return dfs(maze, [s], e)


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
