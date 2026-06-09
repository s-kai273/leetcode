from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue = deque()
        queue.append((p, q))
        while queue:
            p, q = queue.popleft()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        return True
