import pytest

from problems.p00016_3sum_closest import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
    ],
)
def test_3sum_closest(nums, target, expected):
    solution = Solution()
    assert solution.threeSumClosest(nums, target) == expected
