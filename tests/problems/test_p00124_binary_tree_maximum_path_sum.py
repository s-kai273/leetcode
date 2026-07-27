import pytest

from collections import deque

from problems.p00124_binary_tree_maximum_path_sum import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
    ],
)
def test_binary_tree_maximum_path_sum(root, expected):
    solution = Solution()
    root_node = TreeNode(root[0]) if root else None
    queue = deque()
    queue.append(root_node)
    filled_left = False
    for val in root[1:]:
        current = queue[0]
        if not filled_left:
            if val is not None:
                current.left = TreeNode(val)
                queue.append(current.left)
            filled_left = True
        else:
            if val is not None:
                current.right = TreeNode(val)
                queue.append(current.right)
            filled_left = False
            queue.popleft()
    assert solution.maxPathSum(root_node) == expected
