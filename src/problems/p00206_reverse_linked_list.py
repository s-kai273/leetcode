# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        current = head.next
        next = head
        head.next = None
        while current is not None:
            tmp = current.next
            current.next = next
            next = current
            current = tmp
        return next
