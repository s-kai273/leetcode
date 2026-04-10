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
        answer_list = []
        node1 = l1
        node2 = l2
        is_carry_over = False
        while True:
            if node1 is None and node2 is None:
                break
            val1 = node1.val if node1 is not None else 0
            val2 = node2.val if node2 is not None else 0
            val = val1 + val2
            if is_carry_over:
                val += 1
            answer_list.append(val % 10)
            is_carry_over = val // 10 > 0
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        if is_carry_over:
            answer_list.append(1)
        return create_node(answer_list)


def create_node(lnode: list[int]):
    next_node = ListNode(val=lnode[len(lnode) - 1], next=None)
    for i in range(len(lnode) - 2, -1, -1):
        next_node = ListNode(val=lnode[i], next=next_node)
    return next_node
