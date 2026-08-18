import pytest

from problems.p00081_search_in_rotated_sorted_array2 import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 5, 6, 0, 0, 1, 2], 0, True),
        ([2, 5, 6, 0, 0, 1, 2], 3, False),
    ],
)
def test_search_in_roted_sorted_array2(nums, target, expected):
    solution = Solution()
    assert solution.search(nums, target) == expected
