import pytest

from problems.p00881_boats_to_save_people import Solution


@pytest.mark.parametrize(
    "people, limit, expected",
    [
        ([5, 1, 4, 2], 6, 2),
        ([1, 3, 2, 3, 2], 3, 4),
    ],
)
def test_boats_to_save_people(people, limit, expected):
    solution = Solution()
    assert solution.numRescueBoats(people, limit) == expected
