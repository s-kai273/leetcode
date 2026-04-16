import pytest

from problems.p00011_container_with_most_water import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([2, 3, 4, 5, 18, 17, 6], 17),
    ],
)
def test_regular_expression_matching(height, expected):
    solution = Solution()
    assert solution.maxArea(height) == expected
