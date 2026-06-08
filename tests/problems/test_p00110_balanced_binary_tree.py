import pytest

from collections import deque
from problems.p00110_balanced_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
    ],
)
def test_balanced_binary_tree(root, expected):
    solution = Solution()
    root_node = TreeNode(root[0]) if len(root) > 0 else None
    queue = deque()
    queue.append(root_node)
    left_filled = False
    for val in root[1:]:
        current = queue[0]
        if not left_filled:
            current.left = TreeNode(val) if val else None
            queue.append(current.left)
            left_filled = True
        else:
            current.right = TreeNode(val) if val else None
            queue.append(current.right)
            queue.popleft()
            left_filled = False
    assert solution.isBalanced(root_node) == expected
