# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        current = root
        while True:
            # if p and q are categorized to same side, break
            if p.val == current.val or q.val == current.val:
                break
            p_side = p.val < current.val
            q_side = q.val < current.val
            if p_side != q_side:
                break
            current = current.left if p_side else current.right
            if current is None:
                raise RuntimeError
        return current
