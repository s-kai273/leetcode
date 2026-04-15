# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        current = dummy
        node1 = l1
        node2 = l2
        carry = 0
        while node1 is not None or node2 is not None:
            val1 = node1.val if node1 is not None else 0
            val2 = node2.val if node2 is not None else 0
            val = val1 + val2 + carry
            current.next = ListNode(val % 10)
            current = current.next
            carry = val // 10
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next
