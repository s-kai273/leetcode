import pytest

from problems.p01838_frequency_of_the_most_frequent_element import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 4], 5, 3),
        ([1, 4, 8, 13], 5, 2),
    ],
)
def test_frequency_of_the_most_frequent_element(nums, k, expected):
    solution = Solution()
    assert solution.maxFrequency(nums, k) == expected
