import pytest

from problems.p00141_linked_list_cycle import ListNode, Solution


@pytest.mark.parametrize(
    "head, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
    ],
)
def test_linked_list_cycle(head, pos, expected):
    solution = Solution()
    node_list = list()
    dummy = ListNode(0)
    current = dummy
    for val in head:
        current.next = ListNode(val)
        current = current.next
        node_list.append(current)
    if pos != -1:
        current.next = node_list[pos]
    assert solution.hasCycle(dummy.next) == expected
