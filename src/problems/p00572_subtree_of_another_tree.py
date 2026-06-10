# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def dfs(root_node: TreeNode | None, sub_node: TreeNode | None) -> bool:
            if root_node is None and sub_node is None:
                return True
            if root_node is None or sub_node is None:
                return False
            if root_node.val == sub_node.val:
                return dfs(root_node.left, sub_node.left) and dfs(
                    root_node.right, sub_node.right
                )
            return False

        if root is None or subRoot is None:
            return False
        if root.val == subRoot.val:
            result = dfs(root, subRoot)
            if result:
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
