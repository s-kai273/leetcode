import pytest

from problems.p00695_max_area_of_island import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]], 6),
    ],
)
def test_max_area_of_island(grid, expected):
    solution = Solution()
    assert solution.maxAreaOfIsland(grid) == expected
