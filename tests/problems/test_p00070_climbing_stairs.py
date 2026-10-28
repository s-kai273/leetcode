import pytest

from problems.p00070_climbing_stairs import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 2),
        (3, 3),
    ],
)
def test_climbing_stairs(n, expected):
    solution = Solution()
    assert solution.climbStairs(n) == expected
