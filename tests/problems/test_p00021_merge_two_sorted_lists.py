import pytest

from problems.p00021_merge_two_sorted_lists import ListNode, Solution


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_merge_two_sorted_lists(list1, list2, expected):
    solution = Solution()

    dummy1 = ListNode(0)
    current = dummy1
    for val in list1:
        current.next = ListNode(val)
        current = current.next

    dummy2 = ListNode(0)
    current = dummy2
    for val in list2:
        current.next = ListNode(val)
        current = current.next

    dummy3 = solution.mergeTwoLists(dummy1.next, dummy2.next)
    current = dummy3
    for val in expected:
        if current is None:
            raise AssertionError
        assert current.val == val
        current = current.next
    assert current is None
