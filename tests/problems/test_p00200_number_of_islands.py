import pytest

from problems.p00200_number_of_islands import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["0", "1", "1", "1", "0"],
                ["0", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "1"],
                ["1", "1", "0", "0", "1"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            4,
        ),
    ],
)
def test_number_of_islands(grid, expected):
    solution = Solution()
    assert solution.numIslands(grid) == expected
