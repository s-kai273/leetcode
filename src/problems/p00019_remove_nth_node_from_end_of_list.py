from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_val_list = []
        current = head
        while current is not None:
            head_val_list.append(current.val)
            current = current.next
        head_len = len(head_val_list)
        ti = head_len - n
        dummy = ListNode(0)
        current = dummy
        for i in range(head_len):
            if i == ti:
                continue
            current.next = ListNode(head_val_list[i])
            current = current.next
        return dummy.next
