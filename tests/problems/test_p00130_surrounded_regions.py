import pytest

from problems.p00130_surrounded_regions import Solution


@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
        ([["X"]], [["X"]]),
    ],
)
def test_surrounded_regions(board, expected):
    solution = Solution()
    solution.solve(board)
    assert board == expected
