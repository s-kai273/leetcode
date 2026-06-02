import pytest

from problems.p00875_koko_eating_bananas import Solution


@pytest.mark.parametrize(
    "piles, h, expected",
    [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ],
)
def test_valid_anagram(piles, h, expected):
    solution = Solution()
    assert solution.minEatingSpeed(piles, h) == expected
