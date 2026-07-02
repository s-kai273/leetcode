# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy_sum = ListNode(0)
        cur_l1 = l1
        cur_l2 = l2
        cur_sum = dummy_sum
        carry = 0
        while cur_l1 and cur_l2:
            cur_sum.next = ListNode((cur_l1.val + cur_l2.val + carry) % 10)
            carry = (cur_l1.val + cur_l2.val + carry) // 10
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            cur_sum = cur_sum.next
        rest_l = cur_l1 if not cur_l2 else cur_l2
        while carry > 0:
            l_val = rest_l.val if rest_l else 0
            cur_sum.next = ListNode((l_val + carry) % 10)
            carry = (l_val + carry) // 10
            if rest_l:
                rest_l = rest_l.next
            cur_sum = cur_sum.next
        cur_sum.next = rest_l
        return dummy_sum.next
