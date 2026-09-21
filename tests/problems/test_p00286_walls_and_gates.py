import pytest

from problems.p00286_walls_and_gates import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [2147483647, -1, 0, 2147483647],
                [2147483647, 2147483647, 2147483647, -1],
                [2147483647, -1, 2147483647, -1],
                [0, -1, 2147483647, 2147483647],
            ],
            [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
        ),
        ([[0, -1], [2147483647, 2147483647]], [[0, -1], [1, 2]]),
    ],
)
def test_walls_and_gates(grid, expected):
    solution = Solution()
    solution.islandsAndTreasure(grid)
    assert grid == expected
