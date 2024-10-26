from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def height(n: BinaryTreeNode) -> int:
    if not n:
        return 0
    else:
        hl = height(n.left)
        hr = height(n.right)
        if abs(hr-hl) > 1:
            raise Exception
        return max(hl, hr) + 1

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    try:
        height(tree)
    except Exception:
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
