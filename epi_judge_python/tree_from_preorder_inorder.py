from typing import List, Dict

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def process(preorder: List[int],inorder: List[int], idx: Dict[int, int]) -> BinaryTreeNode:
    assert len(preorder) == len(inorder)
    if len(preorder) == 1:
        return BinaryTreeNode(data=preorder[0])
    if not (preorder and inorder):
        return BinaryTreeNode()
    root = preorder[0]
    root_idx = inorder.index(root)
    return BinaryTreeNode(
        data=root,
        left=process(
            preorder=preorder[1:root_idx+1],
            inorder=inorder[:root_idx],
            idx=idx
        ),
        right=process(
            preorder=preorder[root_idx+1:],
            inorder=inorder[root_idx+1:],
            idx=idx
        )
    )

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    idx = {x: i for i, x in enumerate(inorder)}
    return process(preorder, inorder, idx)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
