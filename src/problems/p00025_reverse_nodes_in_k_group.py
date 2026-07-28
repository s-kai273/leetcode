from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, reverse_list: list[ListNode]):
        top = reverse_list[-1].next
        for i in range(1, len(reverse_list)):
            target = reverse_list[i]
            target.next = top
            top = target
        reverse_list[0].next = top

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        reverse_list = list()
        while current:
            reverse_list.append(current)
            current = current.next
            if len(reverse_list) == k + 1:
                self.reverseList(reverse_list)
                reverse_list = [reverse_list[1]]
        return dummy.next
