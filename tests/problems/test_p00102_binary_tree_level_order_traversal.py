import pytest

from collections import deque
from problems.p00102_binary_tree_level_order_traversal import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ],
)
def test_binary_tree_level_order_traversal(root, expected):
    solution = Solution()
    queue = deque()
    root_node = TreeNode(root[0]) if root else None
    queue.append(root_node)
    left_filled = False
    for val in root[1:]:
        current = queue[0]
        if not left_filled:
            current.left = TreeNode(val) if val is not None else None
            if val is not None:
                queue.append(current.left)
            left_filled = True
        else:
            current.right = TreeNode(val) if val is not None else None
            if val is not None:
                queue.append(current.right)
            left_filled = False
            queue.popleft()
    assert solution.levelOrder(root_node) == expected
