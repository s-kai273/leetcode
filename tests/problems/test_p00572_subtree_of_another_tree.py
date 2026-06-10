import pytest

from collections import deque
from problems.p00572_subtree_of_another_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, subRoot, expected",
    [
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ],
)
def test_subtree_of_another_tree(root, subRoot, expected):
    solution = Solution()
    root_node = TreeNode(root[0]) if len(root) > 0 else None
    queue = deque()
    queue.append(root_node)
    is_left_filled = False
    for val in root[1:]:
        current = queue[0]
        if not is_left_filled:
            current.left = TreeNode(val)
            queue.append(current.left)
            is_left_filled = True
        else:
            current.right = TreeNode(val)
            queue.append(current.right)
            queue.popleft()
            is_left_filled = False

    sub_node = TreeNode(subRoot[0]) if len(subRoot) > 0 else None
    queue.clear()
    queue.append(sub_node)
    is_left_filled = False
    for val in subRoot[1:]:
        current = queue[0]
        if not is_left_filled:
            current.left = TreeNode(val)
            queue.append(current.left)
            is_left_filled = True
        else:
            current.right = TreeNode(val)
            queue.append(current.right)
            queue.popleft()
            is_left_filled = False
    assert solution.isSubtree(root_node, sub_node) == expected
