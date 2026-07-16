import pytest

from collections import deque
from problems.p00098_validate_binary_search_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
    ],
)
def test_validate_binary_search_tree(root, expected):
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
    assert solution.isValidBST(root_node) == expected
