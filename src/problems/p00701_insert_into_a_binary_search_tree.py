# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)

        def recursive(root: TreeNode, val):
            if root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    recursive(root.right, val)
                return
            else:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    recursive(root.left, val)
                return

        recursive(root, val)
        return root
