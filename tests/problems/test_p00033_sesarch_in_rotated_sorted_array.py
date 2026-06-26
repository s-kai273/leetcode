import pytest

from problems.p00033_sesarch_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    ],
)
def test_search_in_rotated_sorted_array(nums, target, expected):
    solution = Solution()
    assert solution.search(nums, target) == expected
