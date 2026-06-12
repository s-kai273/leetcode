import pytest

from problems.p00347_top_k_frequent_elements import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
    ],
)
def test_valid_anagram(nums, k, expected):
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == sorted(expected)
