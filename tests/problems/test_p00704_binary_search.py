import pytest

from problems.p00704_binary_search import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_valid_anagram(nums, target, expected):
    solution = Solution()
    assert solution.search(nums, target) == expected
