import pytest

from problems.p00198_house_robber import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 3, 3], 4),
        ([2, 9, 8, 3, 6], 16),
    ],
)
def test_house_robber(nums, expected):
    solution = Solution()
    assert solution.rob(nums) == expected
