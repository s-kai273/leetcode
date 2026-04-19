import pytest

from problems.p00018_4sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([1, -2, -5, -4, -3, 3, 3, 5], -11, [[-5, -4, -3, 1]]),
    ],
)
def test_4sum(nums, target, expected):
    solution = Solution()
    assert solution.fourSum(nums, target) == expected
