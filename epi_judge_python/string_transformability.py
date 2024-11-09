import collections
import string
from collections import defaultdict
from typing import Set

from test_framework import generic_test


# def adjacent(w1, w2):
#     assert len(w1) == len(w2)
#     return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1
#
#
# def transform_string(D: Set[str], s: str, t: str) -> int:
#     adjacency_list = ((w1, w2) for w1 in D for w2 in D if w1 != w2 and adjacent(w1, w2))
#
#     adj = defaultdict(set)
#     for w1, w2 in adjacency_list:
#         adj[w1].add(w2)
#
#     processed = set()
#     q = collections.deque([(s, 0)])
#     while q:
#         w, l = q.popleft()
#         processed.add(w)
#         if w == t:
#             return l
#         for n in adj[w]:
#             if n not in processed:
#                 q.append((n, l+1))
#     return -1

def transform_string(D: Set[str], s: str, t: str) -> int:
    q = collections.deque([(s, 0)])
    while q:
        w, l = q.popleft()

        if w == t:
            return l

        for c in string.ascii_lowercase:
            for i in range(len(w)):
                if (n:=w[:i] + c + w[i + 1:]) in D:
                    D.remove(n)
                    q.append((n, l+1))
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
