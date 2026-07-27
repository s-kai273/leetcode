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
            path_sum = root.val
            if left_sum > 0:
                path_sum += left_sum
            if right_sum > 0:
                path_sum += right_sum
            max_sum = max(max_sum, path_sum)

            path_sum = root.val
            if left_sum < 0 and right_sum < 0:
                return path_sum
            path_sum += left_sum if left_sum > right_sum else right_sum
            return path_sum

        dfs(root)
        return max_sum
