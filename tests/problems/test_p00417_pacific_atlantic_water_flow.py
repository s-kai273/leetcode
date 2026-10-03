import pytest

from problems.p00417_pacific_atlantic_water_flow import Solution


@pytest.mark.parametrize(
    "heights, expected",
    [
        (
            [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]],
            [[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]],
        ),
        ([[1], [1]], [[0, 0], [1, 0]]),
    ],
)
def test_pacific_atlantic_water_flow(heights, expected):
    solution = Solution()
    assert sorted(solution.pacificAtlantic(heights)) == sorted(expected)
