from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        first_val = None
        while head is not None:
            if first_val is None:
                first_val = head.val
            else:
                current.next = ListNode(head.val, ListNode(first_val))
                current = current.next.next
                first_val = None
            head = head.next
        if first_val is not None:
            current.next = ListNode(first_val)
        return dummy.next
