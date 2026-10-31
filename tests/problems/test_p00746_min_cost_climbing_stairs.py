import pytest

from problems.p00746_min_cost_climbing_stairs import Solution


@pytest.mark.parametrize(
    "cost, expected",
    [
        ([1, 2, 3], 2),
        ([1, 2, 1, 2, 1, 1, 1], 4),
    ],
)
def test_min_cost_climbing_stairs(cost, expected):
    solution = Solution()
    assert solution.minCostClimbingStairs(cost) == expected
