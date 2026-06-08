# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        balanced = True

        def dfs(node: TreeNode | None):
            nonlocal balanced
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                balanced = False
            return max(left, right) + 1

        dfs(root)
        return balanced
