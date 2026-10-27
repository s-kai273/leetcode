import pytest

from problems.p01584_min_cost_to_connect_all_points import Solution


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]], 10),
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
    ],
)
def test_min_cost_to_connect_all_points(points, expected):
    solution = Solution()
    assert solution.minCostConnectPoints(points) == expected
