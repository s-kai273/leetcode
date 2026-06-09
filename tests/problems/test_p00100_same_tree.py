import pytest

from collections import deque
from problems.p00100_same_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "p, q, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_search_a_2d_matrix(p, q, expected):
    solution = Solution()
    p_node = TreeNode(p[0]) if len(p) > 0 else None
    q_node = TreeNode(q[0]) if len(q) > 0 else None

    queue = deque()
    queue.append(p_node)
    is_left_filled = False
    for val in p[1:]:
        current = queue[0]
        if not is_left_filled:
            current.left = TreeNode(val) if val else None
            queue.append(current.left)
            is_left_filled = True
        else:
            current.right = TreeNode(val) if val else None
            queue.append(current.right)
            is_left_filled = False

    queue.clear()
    queue.append(q_node)
    is_left_filled = False
    for val in q[1:]:
        current = queue[0]
        if not is_left_filled:
            current.left = TreeNode(val) if val else None
            queue.append(current.left)
            is_left_filled = True
        else:
            current.right = TreeNode(val) if val else None
            queue.append(current.right)
            is_left_filled = False
    assert solution.isSameTree(p_node, q_node) == expected
