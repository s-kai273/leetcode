import pytest

from problems.p00853_car_fleet import Solution


@pytest.mark.parametrize(
    "target, position, speed, expected",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (10, [3], [3], 1),
        (100, [0, 2, 4], [4, 2, 1], 1),
    ],
)
def test_car_fleet(target, position, speed, expected):
    solution = Solution()
    assert solution.carFleet(target, position, speed) == expected
