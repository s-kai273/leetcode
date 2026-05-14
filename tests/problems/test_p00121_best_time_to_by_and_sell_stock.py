import pytest

from problems.p00121_best_time_to_by_and_sell_stock import Solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_best_time_to_buy_and_sell_stock(prices, expected):
    solution = Solution()
    assert solution.maxProfit(prices) == expected
