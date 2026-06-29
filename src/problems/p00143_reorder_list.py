from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        current = head
        while current:
            queue.append(current)
            current = current.next
        current = queue.popleft()
        while True:
            if not queue:
                current.next = None
                break
            current.next = queue.pop()
            if not queue:
                current.next.next = None
                break
            current.next.next = queue.popleft()
            current = current.next.next
