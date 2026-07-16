import pytest

from collections import deque
from problems.p00199_binary_tree_right_side_view import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
        ([1, None, 3], [1, 3]),
        ([], []),
    ],
)
def test_binary_tree_right_side_view(root, expected):
    solution = Solution()
    root_node = TreeNode(root[0]) if root else None
    queue = deque()
    queue.append(root_node)
    filled_left = False
    for val in root[1:]:
        current = queue[0]
        if not filled_left:
            if val:
                current.left = TreeNode(val)
                queue.append(current.left)
            filled_left = True
        else:
            if val:
                current.right = TreeNode(val)
                queue.append(current.right)
            queue.popleft()
            filled_left = False
    assert solution.rightSideView(root_node) == expected
