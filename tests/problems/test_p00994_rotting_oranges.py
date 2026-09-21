import pytest

from problems.p00994_rotting_oranges import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 1, 0], [0, 1, 1], [0, 1, 2]], 4),
        ([[1, 0, 1], [0, 2, 0], [1, 0, 1]], -1),
    ],
)
def test_rotting_fruit(grid, expected):
    solution = Solution()
    assert solution.orangesRotting(grid) == expected
