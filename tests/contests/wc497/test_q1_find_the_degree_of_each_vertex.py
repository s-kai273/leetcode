import pytest

from contests.wc497.q1_find_the_degree_of_each_vertex import Solution


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], [2, 2, 2]),
        ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], [1, 1, 0]),
        ([[0]], [0]),
    ],
)
def test_find_the_degree_of_each_vertex(matrix, expected):
    s = Solution()
    assert s.findDegrees(matrix) == expected
