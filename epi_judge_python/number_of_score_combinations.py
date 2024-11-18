from typing import List, Dict

from test_framework import generic_test


def f(n: int, individual_play_scores: List[int], cache: Dict[int, int]) -> int:
    key = (n, tuple(individual_play_scores))
    if key in cache:
        return cache[key]
    elif n < 0:
        return 0
    elif n == 0:
        return 1

    f_ = 0
    for i in range(len(individual_play_scores)):
        f_ += f(n-individual_play_scores[i], individual_play_scores[i:], cache)
    cache[key] = f_
    return f_



def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    cache = {0: 1}
    return f(final_score, individual_play_scores, cache)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
