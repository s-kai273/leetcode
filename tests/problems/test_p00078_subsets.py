import pytest

from problems.p00078_subsets import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    ],
)
def test_subsets(nums, expected):
    solution = Solution()
    assert sorted(solution.subsets(nums)) == sorted(expected)
