from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    s0, s1 = [tree], [tree]
    while s0 and s1:
        n0, n1 = s0.pop(), s1.pop()
        if n0 is None and n1 is None:
            continue

        if (n0 is None) != (n1 is None) or n0.data != n1.data:
            return False
        s0 += [n0.left, n0.right]
        s1 += [n1.right, n1.left]
    return s0 == s1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
