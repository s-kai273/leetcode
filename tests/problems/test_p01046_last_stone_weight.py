import pytest

from problems.p01046_last_stone_weight import Solution


@pytest.mark.parametrize(
    "stones, expected",
    [
        ([2, 7, 4, 1, 8, 1], 1),
    ],
)
def test_last_stone_weight(stones, expected):
    solution = Solution()
    assert solution.lastStoneWeight(stones) == expected
