from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        sum_level = 0
        sum_dict = dict()
        cur_node_count = 1

        queue = deque([(root, None)])

        while queue:
            child, parent = queue.popleft()
            child.val = sum_level - sum_dict[parent] if parent else 0
            if child.left:
                queue.append((child.left, child))
            if child.right:
                queue.append((child.right, child))

            cur_node_count -= 1
            if cur_node_count == 0:
                cur_node_count = len(queue)
                sum_level = 0
                sum_dict = dict()
                for i in range(cur_node_count):
                    child, parent = queue[i]
                    sum_level += child.val
                    sum_dict[parent] = sum_dict.get(parent, 0) + child.val
        return root
