import pytest

from problems.p00128_longest_consecutive_sequence import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999], 10),
    ],
)
def test_longest_consecutive_sequence(nums, expected):
    solution = Solution()
    assert solution.longestConsecutive(nums) == expected
