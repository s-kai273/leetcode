import pytest

from collections import deque
from problems.p00543_diameter_of_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
    ],
)
def test_diameter_of_binary_tree(root, expected):
    solution = Solution()
    root_node = TreeNode(root[0]) if len(root) > 0 else None
    queue = deque()
    queue.append(root_node)
    for val in root[1:]:
        current = queue[0]
        if current.left is None:
            current.left = TreeNode(val)
            queue.append(current.left)
        else:
            current.right = TreeNode(val)
            queue.append(current.right)
            queue.popleft()
    assert solution.diameterOfBinaryTree(root_node) == expected
