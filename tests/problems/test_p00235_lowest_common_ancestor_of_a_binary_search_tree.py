import pytest

from collections import deque
from problems.p00235_lowest_common_ancestor_of_a_binary_search_tree import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    "root, p, q, expected",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ],
)
def test_4sum(root, p, q, expected):
    solution = Solution()
    root_node = TreeNode(root[0])
    p_node = root_node if p == root[0] else None
    q_node = root_node if q == root[0] else None
    expected_node = root_node if expected == root[0] else None
    queue = deque()
    queue.append(root_node)
    left_filled = False
    for val in root[1:]:
        current = queue[0]
        if not left_filled:
            current.left = TreeNode(val)
            queue.append(current.left)
            left_filled = True
            if val == p:
                p_node = current.left
            if val == q:
                q_node = current.left
            if val == expected:
                expected_node = current.left
        else:
            current.right = TreeNode(val)
            queue.append(current.right)
            queue.popleft()
            left_filled = False
            if val == p:
                p_node = current.right
            if val == q:
                q_node = current.right
            if val == expected:
                expected_node = current.right
    assert solution.lowestCommonAncestor(root_node, p_node, q_node) == expected_node
