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

        kth_smallest = None
        count = 0

        def dfs(root: TreeNode | None) -> None:
            nonlocal kth_smallest, count
            if not root:
                return

            dfs(root.left)
            if kth_smallest is not None:
                return
            count += 1
            if count == k:
                kth_smallest = root.val
                return
            dfs(root.right)

        dfs(root)
        return kth_smallest
