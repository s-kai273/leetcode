import pytest

from problems.p00213_house_robber2 import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 3], 4),
        ([2, 9, 8, 3, 6], 15),
    ],
)
def test_house_robber2(nums, expected):
    solution = Solution()
    assert solution.rob(nums) == expected
