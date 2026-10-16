import pytest

from problems.p00743_network_delay_time import Solution


@pytest.mark.parametrize(
    "times, n, k, expected",
    [
        ([[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], 4, 1, 3),
        ([[1, 2, 1], [2, 3, 1]], 3, 2, -1),
    ],
)
def test_network_delay_time(times, n, k, expected):
    solution = Solution()
    assert solution.networkDelayTime(times, n, k) == expected
