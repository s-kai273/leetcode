import heapq
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node is None:
                continue
            heapq.heappush(heap, (node.val, i))
        while heap:
            val, i = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            node = lists[i]
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i))
                lists[i] = node.next
        return dummy.next
