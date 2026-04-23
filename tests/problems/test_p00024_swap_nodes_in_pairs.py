import pytest

from problems.p00024_swap_nodes_in_pairs import ListNode, Solution


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
    ],
)
def test_swap_nodes_in_pairs(head, expected):
    solution = Solution()
    dummy = ListNode(0)
    current = dummy
    for val in head:
        current.next = ListNode(val)
        current = current.next
    node = solution.swapPairs(dummy.next)
    for val in expected:
        if node is None:
            raise AssertionError
        assert node.val == val
        node = node.next
    assert node is None
