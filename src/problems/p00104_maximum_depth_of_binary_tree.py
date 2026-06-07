from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append((root, 1))
        last_depth = 0
        while queue:
            current, depth = queue.popleft()
            if current and current.left:
                queue.append((current.left, depth + 1))
            if current and current.right:
                queue.append((current.right, depth + 1))
            last_depth = depth
        return last_depth
