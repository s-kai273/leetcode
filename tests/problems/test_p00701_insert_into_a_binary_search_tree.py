import pytest

from collections import deque
from problems.p00701_insert_into_a_binary_search_tree import Solution, TreeNode


@pytest.mark.parametrize(
    "root, val, expected",
    [
        ([4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5]),
        (
            [40, 20, 60, 10, 30, 50, 70],
            25,
            [40, 20, 60, 10, 30, 50, 70, None, None, 25],
        ),
        ([4, 2, 7, 1, 3, None, None, None, None, None, None], 5, [4, 2, 7, 1, 3, 5]),
    ],
)
def test_insert_a_binary_search_tree(root, val, expected):
    solution = Solution()
    root_node = TreeNode(root[0]) if root else None
    queue = deque()
    queue.append(root_node)
    left_filled = False
    for current_val in root[1:]:
        current = queue[0]
        if not left_filled:
            if current_val is not None:
                current.left = TreeNode(current_val)
                queue.append(current.left)
            left_filled = True
        else:
            if current_val is not None:
                current.right = TreeNode(current_val)
                queue.append(current.right)
            left_filled = False
            queue.popleft()
    result = solution.insertIntoBST(root_node, val)
    queue = deque()
    queue.append(result)
    for current_val in expected:
        current = queue[0]
        if current:
            assert current.val == current_val
            queue.append(current.left)
            queue.append(current.right)
        else:
            assert current == current_val
        queue.popleft()
