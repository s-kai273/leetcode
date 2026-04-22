import pytest

from problems.p00023_merge_k_sorted_lists import ListNode, Solution


@pytest.mark.parametrize(
    "lists, expected",
    [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]), ([], []), ([[]], [])],
)
def test_merge_k_sorted_lists(lists, expected):
    solution = Solution()
    nodes = []
    for arr in lists:
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        nodes.append(dummy.next)

    result = solution.mergeKLists(nodes)
    for val in expected:
        if result is None:
            raise AssertionError
        assert result.val == val
        result = result.next
    assert result is None
