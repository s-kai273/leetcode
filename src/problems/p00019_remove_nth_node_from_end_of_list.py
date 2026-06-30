from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        current = head
        while current:
            len_list += 1
            current = current.next
        i_target = len_list - n
        dummy = ListNode(0, head)
        current = dummy
        for i in range(len_list):
            if i == i_target:
                current.next = current.next.next if current.next else None
                break
            current = current.next
        return dummy.next
