import pytest

from problems.p00040_combination_sum2 import Solution


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([9, 2, 2, 4, 6, 1, 5], 8, [[1, 2, 5], [2, 2, 4], [2, 6]]),
        ([1, 2, 3, 4, 5], 7, [[1, 2, 4], [2, 5], [3, 4]]),
    ],
)
def test_combination_sum2(candidates, target, expected):
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    expected.sort()
    result.sort()
    for i in range(len(expected)):
        assert sorted(expected[i]) == sorted(result[i])
