import pytest

from problems.p00239_sliding_window_maximum import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
    ],
)
def test_sliding_window_maximum(nums, k, expected):
    solution = Solution()
    assert solution.maxSlidingWindow(nums, k) == expected
