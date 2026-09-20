# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return None

        node_dict = dict()

        def dfs(base_node: Node):
            if base_node.val in node_dict:
                return
            copy_node = Node(base_node.val)
            node_dict[base_node.val] = copy_node
            for neighbor in base_node.neighbors:
                dfs(neighbor)
                copy_neighbor = node_dict[neighbor.val]
                copy_node.neighbors.append(copy_neighbor)

        dfs(node)
        return node_dict[1]
