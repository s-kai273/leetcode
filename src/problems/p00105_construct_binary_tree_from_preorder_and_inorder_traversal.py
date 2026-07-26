# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        indices = dict()
        for i, val in enumerate(inorder):
            indices[val] = i

        pre_idx = 0

        def rec(left: int, right: int):
            nonlocal pre_idx
            if left >= right:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(root_val)
            node.left = rec(left, indices[node.val])
            node.right = rec(indices[node.val] + 1, right)
            return node

        return rec(0, len(inorder))
