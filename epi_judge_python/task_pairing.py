import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    task_durations = sorted(task_durations)
    m = len(task_durations) // 2
    tasks1, tasks2 = task_durations[:m], task_durations[m:][::-1]

    return [PairedTasks(t1, t2) for t1, t2 in zip(tasks1, tasks2)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
