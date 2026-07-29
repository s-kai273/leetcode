import pytest

from collections import deque
from problems.p00297_serialize_and_deserialize_binary_tree import Codec, TreeNode


@pytest.mark.parametrize(
    "root, expected",
    [([1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 5]), ([], [])],
)
def test_serialize_and_deserialize_binary_tree(root, expected):
    codec = Codec()
    root_node = TreeNode(root[0]) if root else None
    queue = deque()
    if root_node:
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
    serialized = codec.serialize(root_node)
    deserialized = codec.deserialize(serialized)
    queue = deque()
    queue.append(deserialized)
    for val in expected:
        current = queue.popleft()
        if current:
            assert current.val == val
            queue.append(current.left)
            queue.append(current.right)
        else:
            assert val is None
