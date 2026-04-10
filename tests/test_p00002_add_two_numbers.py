import pytest

from p00002_add_two_numbers import Solution, create_node


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_add_two_numbers(l1, l2, expected):
    s = Solution()
    node1 = create_node(l1)
    node2 = create_node(l2)
    expected_node = create_node(expected)
    answer_node = s.addTwoNumbers(node1, node2)
    while True:
        if answer_node is None and expected_node is None:
            break
        if answer_node is None or expected_node is None:
            raise AssertionError(
                f"Created node is not equal to the expected one\nanswer_node: {answer_node}, expected_node: {expected_node}"
            )
        assert answer_node.val == expected_node.val
        answer_node = answer_node.next
        expected_node = expected_node.next
