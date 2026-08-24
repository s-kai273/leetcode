import pytest

from problems.p00039_combination_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 5, 6, 9], 9, [[2, 2, 5], [9]]),
        ([3, 4, 5], 16, [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]),
        ([3], 5, []),
    ],
)
def test_combination_sum(nums, target, expected):
    solution = Solution()
    result = solution.combinationSum(nums, target)
    assert len(result) == len(expected)
    result.sort()
    expected.sort()
    for i in range(len(expected)):
        assert sorted(result[i]) == sorted(expected[i])
