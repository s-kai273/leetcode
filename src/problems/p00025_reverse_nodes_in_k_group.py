from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        node_list = []

        def swap_nodes(nl: list[ListNode], si: int, ei: int):
            ps_node = nl[si - 1]
            s_node = nl[si]
            pe_node = nl[ei - 1]
            e_node = nl[ei]

            if ei - si == 1:
                tmp = e_node.next
                ps_node.next = e_node
                e_node.next = s_node
                s_node.next = tmp
            else:
                s_tmp = s_node.next
                e_tmp = e_node.next
                ps_node.next = e_node
                e_node.next = s_tmp
                pe_node.next = s_node
                s_node.next = e_tmp
            nl[si], nl[ei] = nl[ei], nl[si]
            if ei - si > 2:
                swap_nodes(nl, si + 1, ei - 1)

        while current is not None:
            node_list.append(current)
            current = current.next
            if len(node_list) == k + 1:
                current = node_list[1]
                swap_nodes(node_list, 1, k)
                node_list = []
        return dummy.next
