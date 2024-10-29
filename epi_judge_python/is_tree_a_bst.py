from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst_(r: BinaryTreeNode, low=float('-inf'), high=float('inf')) -> None:
    if not r:
        return
    if low <= r.data <= high:
        is_binary_tree_bst_(r.left, low=low, high=r.data)
        is_binary_tree_bst_(r.right, low=r.data, high=high)
    else:
        raise ValueError(f"Failed at {r.data}")

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    try:
        is_binary_tree_bst_(tree)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
