import pytest

from problems.p00143_reorder_list import ListNode, Solution


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ],
)
def test_reorder_list(head, expected):
    solution = Solution()
    dummy = ListNode(0)
    current = dummy
    for val in head:
        current.next = ListNode(val)
        current = current.next
    solution.reorderList(dummy.next)
    current = dummy.next
    for val in expected:
        assert current.val == val
        current = current.next
    assert current is None
