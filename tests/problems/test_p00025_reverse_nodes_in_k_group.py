import pytest

from problems.p00025_reverse_nodes_in_k_group import ListNode, Solution


@pytest.mark.parametrize(
    "head, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
    ],
)
def test_reverse_nodes_in_k_group(head, k, expected):
    solution = Solution()
    dummy = ListNode(0)
    current = dummy
    for val in head:
        current.next = ListNode(val)
        current = current.next
    node = solution.reverseKGroup(dummy.next, k)
    for val in expected:
        if node is None:
            raise AssertionError
        print(f"{node.val}, {val}")
        assert node.val == val
        node = node.next
    assert node is None
