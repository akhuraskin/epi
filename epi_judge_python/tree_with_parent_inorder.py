from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

def down_left(n: BinaryTreeNode) -> BinaryTreeNode:
    while n.left is not None:
        n = n.left
    return n

def successor(n: BinaryTreeNode) -> BinaryTreeNode:
    if n.right:
        return down_left(n.right)
    else:
        parent = n.parent
        while parent and parent.right == n:
            n, parent = parent, parent.parent
        return parent


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    res = []
    n = down_left(tree)
    if n is not None:
        res.append(n.data)
        while n:= successor(n):
            res.append(n.data)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
