from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        current1 = list1
        current2 = list2
        while current1 is not None or current2 is not None:
            if current1 is None:
                current.next = ListNode(current2.val)
                current2 = current2.next
            elif current2 is None:
                current.next = ListNode(current1.val)
                current1 = current1.next
            else:
                if current1.val < current2.val:
                    current.next = ListNode(current1.val)
                    current1 = current1.next
                else:
                    current.next = ListNode(current2.val)
                    current2 = current2.next
            current = current.next
        return dummy.next
