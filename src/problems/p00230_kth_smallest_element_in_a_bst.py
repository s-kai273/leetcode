# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if not root:
            raise ValueError

        kth_smallest = 10**4

        def dfs(root: TreeNode | None, k: int) -> int:
            """
            Return value: node number
            """
            nonlocal kth_smallest
            if not root:
                return 0

            left_count = dfs(root.left, k)
            if left_count == -1:
                return -1
            if left_count + 1 == k:
                kth_smallest = root.val
                return -1

            right_count = dfs(root.right, k - (left_count + 1))
            if right_count == -1:
                return -1
            return left_count + right_count + 1

        dfs(root, k)
        return kth_smallest
