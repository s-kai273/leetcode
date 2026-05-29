import pytest

from problems.p00074_search_a_2d_matrix import Solution


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ],
)
def test_search_a_2d_matrix(matrix, target, expected):
    solution = Solution()
    assert solution.searchMatrix(matrix, target) == expected
