import pytest

from collections import deque
from problems.p00105_construct_binary_tree_from_preorder_and_inorder_traversal import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    "preorder, inorder, expected",
    [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ],
)
def test_product_of_array_except_self(preorder, inorder, expected):
    solution = Solution()
    node = solution.buildTree(preorder, inorder)
    queue = deque()
    queue.append(node)
    for val in expected:
        current = queue.popleft()
        if current:
            assert current.val == val
            queue.append(current.left)
            queue.append(current.right)
        else:
            assert current == val
    for val in queue:
        assert val is None
