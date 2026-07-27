# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = -1000

        def dfs(root: TreeNode | None) -> int:
            nonlocal max_sum
            if root is None:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            left_max = max(left_sum, 0)
            right_max = max(right_sum, 0)
            max_sum = max(max_sum, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)
        return max_sum
