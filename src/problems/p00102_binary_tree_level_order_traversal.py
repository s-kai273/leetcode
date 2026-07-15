from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append((0, root))
        level_order_list = list()
        cur_level = -1
        while queue:
            level, node = queue.popleft()

            # Update queue with left and right node
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))

            # Update leve_order_dict
            if cur_level != level:
                cur_level += 1
                level_order_list.append(list())
            level_order_list[level].append(node.val)
        return level_order_list
