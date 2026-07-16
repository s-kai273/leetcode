# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode, max_val: int, min_val: int) -> bool:
            if node.val >= max_val or node.val <= min_val:
                return False
            l_bst = dfs(node.left, node.val, min_val) if node.left else True
            r_bst = dfs(node.right, max_val, node.val) if node.right else True
            return l_bst and r_bst

        if not root:
            raise ValueError
        l_bst = dfs(root.left, root.val, -(2**35)) if root.left else True
        r_bst = dfs(root.right, 2**35, root.val) if root.right else True
        return l_bst and r_bst
