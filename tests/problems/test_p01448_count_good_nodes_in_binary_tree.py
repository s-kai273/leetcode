import pytest

from collections import deque
from problems.p01448_count_good_nodes_in_binary_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 1, 4, 3, None, 1, 5], 4),
        ([3, 3, None, 4, 2], 3),
        ([1], 1),
    ],
)
def test_count_good_nodes_in_binary_tree(root, expected):
    solution = Solution()
    root_node = TreeNode(root[0])
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
    assert solution.goodNodes(root_node) == expected
