import pytest

from problems.p00226_invert_binary_tree import Solution, TreeNode
from collections import deque


@pytest.mark.parametrize(
    "root, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ],
)
def test_invert_binary_tree(root, expected):
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
    result = solution.invertTree(root_node)
    queue.clear()
    if result:
        queue.append(result)
    for val in expected:
        node = queue.popleft()
        assert node.val == val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    assert len(queue) == 0
