from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getVals(self, lists: list[Optional[ListNode]]):
        vals = []
        for node in lists:
            current = node
            while current is not None:
                vals.append(current.val)
                current = current.next
        return vals

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        vals = self.getVals(lists)
        vals.sort()
        for val in vals:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
