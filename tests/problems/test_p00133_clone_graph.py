import pytest

from collections import deque
from problems.p00133_clone_graph import Node, Solution


@pytest.mark.parametrize(
    "adj_list, expected",
    [
        ([[2], [1, 3], [2]], [[2], [1, 3], [2]]),
        ([[]], [[]]),
        ([], []),
    ],
)
def test_clone_graph(adj_list, expected):
    solution = Solution()
    node_list = [Node(i + 1) for i in range(len(adj_list))]
    for i, adj in enumerate(adj_list):
        node = node_list[i]
        for j in adj:
            node.neighbors.append(node_list[j - 1])
    root_node = node_list[0] if node_list else None
    clone_root = solution.cloneGraph(root_node)

    asserted = [False] * len(adj_list)
    queue = deque()
    if clone_root:
        queue.append(clone_root)

    while queue:
        current = queue.popleft()
        neighbor_vals = [neighbor.val for neighbor in current.neighbors]
        assert sorted(neighbor_vals) == sorted(expected[current.val - 1])
        asserted[current.val - 1] = True
