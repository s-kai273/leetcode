import pytest

from collections import deque
from problems.p02641_cousins_in_binary_tree2 import Solution, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [
        ([8, 2, 6, 3, 5, 7, 1], [0, 0, 0, 8, 8, 8, 8]),
        ([4, 2, 9, None, 6, 3], [0, 0, 0, None, 3, 6]),
        ([10], [0]),
    ],
)
def test_cousins_in_binary_tree2(root, expected):
    solution = Solution()
    root_node = TreeNode(root[0])

    queue = deque([root_node])
    is_left_filled = False
    for i in range(1, len(root)):
        current = queue[0]
        node = TreeNode(root[i]) if root[i] is not None else None
        if not is_left_filled:
            if node is not None:
                current.left = node
                queue.append(node)
            is_left_filled = True
        else:
            if node is not None:
                current.right = node
                queue.append(node)
            queue.popleft()
            is_left_filled = False

    result = solution.replaceValueInTree(root_node)

    queue = deque([result])
    for val in expected:
        current = queue.popleft()
        if current is not None:
            assert val == current.val
            queue.append(current.left)
            queue.append(current.right)
        else:
            assert val == current
