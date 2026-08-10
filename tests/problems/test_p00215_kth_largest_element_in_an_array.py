import pytest

from problems.p00215_kth_largest_element_in_an_array import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ],
)
def test_kth_largest_element_in_an_array(nums, k, expected):
    solution = Solution()
    assert solution.findKthLargest(nums, k) == expected
