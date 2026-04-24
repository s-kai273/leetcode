from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        odd_node = None
        while head is not None:
            if odd_node is None:
                odd_node = head
            else:
                tmp_node = head.next
                head.next = odd_node
                odd_node.next = tmp_node
                print(
                    f"## tmp_node: {tmp_node.val}, head: {head.val}, odd_node: {odd_node.val}"
                )
                if first is None:
                    first = head
                head = odd_node
                odd_node = None
            print(f"## head.val: {head.val}")
            head = head.next
        return first
