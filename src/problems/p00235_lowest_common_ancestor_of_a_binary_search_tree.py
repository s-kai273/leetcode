# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_target_path(self, root: TreeNode, target: int, path: list[int]) -> bool:
        """
        return reverse path from target to root
        """
        if root.val == target:
            return True
        if root.left is not None and self.find_target_path(root.left, target, path):
            path.append(True)
            return True
        if root.right is not None and self.find_target_path(root.right, target, path):
            path.append(False)
            return True
        return False

    def find_common_node(
        self, root: TreeNode, path1: list[int], path2: list[int]
    ) -> TreeNode:
        """
        return last common value from both of path
        """
        i = 0
        common_node = root
        while True:
            if i == len(path1) or i == len(path2):
                break
            if path1[-1 - i] == path2[-1 - i]:
                common_node = common_node.left if path1[-1 - i] else common_node.right
                i += 1
            else:
                break
        return common_node

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        p_path = list()
        q_path = list()
        self.find_target_path(root, p.val, p_path)
        self.find_target_path(root, q.val, q_path)
        return self.find_common_node(root, p_path, q_path)
