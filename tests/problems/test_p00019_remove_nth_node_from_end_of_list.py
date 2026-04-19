import pytest

from problems.p00019_remove_nth_node_from_end_of_list import ListNode, Solution


@pytest.mark.parametrize(
    "head, n, expected",
    [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), ([1], 1, []), ([1, 2], 1, [1])],
)
def test_remove_nth_node_from_end_of_list(head, n, expected):
    solution = Solution()
    dummy = ListNode(0)
    current = dummy
    for val in head:
        current.next = ListNode(val)
        current = current.next
    node = solution.removeNthFromEnd(dummy.next, n)
    current = node
    for val in expected:
        if current is None:
            raise AssertionError
        assert current.val == val
        current = current.next
