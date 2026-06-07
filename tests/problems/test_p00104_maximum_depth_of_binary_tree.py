import pytest
from collections import deque
from problems.p00104_maximum_depth_of_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ],
)
def test_maximum_depth_of_binary_tree(root, expected):
    solution = Solution()
    queue = deque()
    root_node = TreeNode(root[0]) if len(root) > 0 else None
    if root_node:
        queue.append(root_node)
    for val in root[1:]:
        node = queue[0]
        if node.left is None:
            node.left = TreeNode(val)
            queue.append(node.left)
        else:
            node.right = TreeNode(val)
            queue.append(node.right)
            queue.popleft()
    assert solution.maxDepth(root_node) == expected
