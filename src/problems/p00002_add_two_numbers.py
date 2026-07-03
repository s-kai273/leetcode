# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        cur_l1 = l1
        cur_l2 = l2
        carry = 0
        if not cur_l1:
            return cur_l2
        prev_l = None
        while cur_l1 and cur_l2:
            cur_l1.val += cur_l2.val + carry
            carry = cur_l1.val // 10
            cur_l1.val %= 10
            prev_l = cur_l1
            if cur_l1.next:
                cur_l1 = cur_l1.next
                cur_l2 = cur_l2.next
            else:
                cur_l1.next = cur_l2.next
                cur_l1 = cur_l1.next
                break
        while carry > 0:
            if cur_l1:
                cur_l1.val += carry
                carry = cur_l1.val // 10
                cur_l1.val %= 10
                prev_l = cur_l1
                cur_l1 = cur_l1.next
            else:
                prev_l.next = ListNode(carry)
                break
        return l1
