import pytest

from problems.p00084_largest_rectangle_in_histogram import Solution


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
    ],
)
def test_largest_rectangle_in_histogram(heights, expected):
    solution = Solution()
    assert solution.largestRectangleArea(heights) == expected
