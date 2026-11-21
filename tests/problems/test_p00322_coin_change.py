import pytest

from problems.p00322_coin_change import Solution


@pytest.mark.parametrize(
    "coins, amount, expected",
    [([1, 5, 10], 12, 3), ([2], 3, -1), ([1], 0, 0)],
)
def test_coin_change(coins, amount, expected):
    solution = Solution()
    assert solution.coinChange(coins, amount) == expected
