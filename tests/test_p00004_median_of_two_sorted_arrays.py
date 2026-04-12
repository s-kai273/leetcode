import pytest
from p00004_median_of_two_sorted_arrays import Solution


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        ([1, 3], [2], 2.00000),
        ([1, 2], [3, 4], 2.50000),
        ([2, 2, 4, 4], [2, 2, 2, 4, 4], 2.00000),
    ],
)
def test_median_of_two_sorted_arrays(num1, num2, expected):
    s = Solution()
    assert s.findMedianSortedArrays(num1, num2) == expected
