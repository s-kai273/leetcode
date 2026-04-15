import pytest

from problems.p00001_two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3, 3, 2, 9], 12, [0, 3]),
    ],
)
def test_two_sum(nums, target, expected):
    s = Solution()
    assert s.twoSum(nums, target) == expected
