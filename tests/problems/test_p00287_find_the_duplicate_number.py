import pytest

from problems.p00287_find_the_duplicate_number import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3), ([3, 3, 3, 3, 3], 3)],
)
def test_valid_anagram(nums, expected):
    solution = Solution()
    assert solution.findDuplicate(nums) == expected
