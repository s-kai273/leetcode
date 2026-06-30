# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Node | None" = None, random: "Node | None" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        dummy = Node(0)
        current_ref = head
        current = dummy
        node_dict = {None: None}
        while current_ref:
            current.next = Node(current_ref.val)
            node_dict[current_ref] = current.next
            current_ref = current_ref.next
            current = current.next
        current_ref = head
        current = dummy
        while current_ref:
            current.next.random = node_dict[current_ref.random]
            current_ref = current_ref.next
            current = current.next
        return dummy.next
