from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        queue = deque()
        if root is None:
            return []
        queue.append(root)
        right_side_list = list()
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                # get elements of ith level
                # - Determine right side of each level
                # - Update queue to add next level elements
                cur = queue.popleft()
                if i == q_len - 1:
                    right_side_list.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
        return right_side_list
