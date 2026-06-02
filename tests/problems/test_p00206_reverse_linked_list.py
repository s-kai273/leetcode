import pytest

from problems.p00206_reverse_linked_list import ListNode, Solution


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_reverse_nodes_in_k_group(head, expected):
    solution = Solution()
    dummy = ListNode(0)
    current = dummy
    for val in head:
        current.next = ListNode(val)
        current = current.next
    node = solution.reverseList(dummy.next)
    for val in expected:
        if node is None:
            raise AssertionError
        print(f"{node.val}, {val}")
        assert node.val == val
        node = node.next
    assert node is None
