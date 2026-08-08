import pytest

from problems.p00973_k_closest_points_to_origin import Solution


@pytest.mark.parametrize(
    "points, k, expected",
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
def test_k_closest_points_to_origin(points, k, expected):
    solution = Solution()
    result = solution.kClosest(points, k)
    assert sorted(expected) == sorted(result)
