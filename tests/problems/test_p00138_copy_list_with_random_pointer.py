import pytest

from problems.p00138_copy_list_with_random_pointer import Node, Solution


@pytest.mark.parametrize(
    "head, expected",
    [
        (
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        ),
        ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
        ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),
    ],
)
def test_copy_list_with_random_pointer(head, expected):
    solution = Solution()
    dummy = Node(0)
    current = dummy
    node_list = list()
    for val, _ in head:
        current.next = Node(val)
        current = current.next
        node_list.append(current)
    current = dummy
    for _, random in head:
        current.next.random = node_list[random] if random is not None else None
        current = current.next
    result = solution.copyRandomList(dummy.next)
    current = result
    for val, random in expected:
        assert current.val == val
        if random is None:
            assert current.random is None
        else:
            assert current.random.val == node_list[random].val
        current = current.next
    assert current is None
