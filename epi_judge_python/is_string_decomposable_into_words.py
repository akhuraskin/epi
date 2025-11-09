import functools
from typing import List, Set, Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import functools

def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:

    decomposed_suffix = {}
    def decompose_suffix(i: int):
        if i in decomposed_suffix:
            return decomposed_suffix[i]
        if i == len(domain):
            return []

        # for j in range(i+1, len(domain)+1):
        #     w = domain[i:j]
        #     if w in dictionary:
        #         rest = decompose_suffix(j)
        #         if rest is not None:
        #             decomposed_suffix[i] = [w] + rest
        #             return decomposed_suffix[i]
        # decomposed_suffix[i] = None
        # return None

        for w in dictionary:
            i_next = i + len(w)
            if i_next <= len(domain) and domain[i:i_next] == w:
                rest = decompose_suffix(i_next)
                if rest is not None:
                    decomposed_suffix[i] = [w] + rest
                    return [w]+rest
        decomposed_suffix[i] = None
        return None

    return decompose_suffix(0)


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
