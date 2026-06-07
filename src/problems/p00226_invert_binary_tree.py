from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            current = queue.popleft()
            tmp = current.left
            current.left = current.right
            current.right = tmp
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root
