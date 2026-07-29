from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode | None) -> str:
        val_list = list()
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            current = queue.popleft()
            # Create proper val_list by appending values
            if current is not None:
                val_list.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                val_list.append("N")
        return ",".join(val_list)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode | None:
        si, ei = 0, 0
        val_list = list()
        while ei < len(data):
            # Parse and update current node
            while ei < len(data) and data[ei] != ",":
                ei += 1
            val = None if data[si:ei] == "N" else int(data[si:ei])
            val_list.append(val)
            si = ei = ei + 1

        if len(val_list) == 0:
            return None
        if val_list[0] is None:
            return None
        root = TreeNode(val_list[0])
        queue = deque()
        queue.append(root)
        filled_left = False
        for val in val_list[1:]:
            # Update tree
            current = queue[0]
            if not filled_left:
                if val is not None:
                    current.left = TreeNode(val)
                    queue.append(current.left)
                filled_left = True
            else:
                if val is not None:
                    current.right = TreeNode(val)
                    queue.append(current.right)
                filled_left = False
                queue.popleft()
        return root
