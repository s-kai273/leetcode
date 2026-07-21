import pytest

from collections import deque
from problems.p00230_kth_smallest_element_in_a_bst import Solution, TreeNode


@pytest.mark.parametrize(
    "root, k, expected",
    [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ],
)
def test_kth_smallest_element_in_a_bst(root, k, expected):
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
            queue.popleft()
            filled_left = False
    assert solution.kthSmallest(root_node, k) == expected
