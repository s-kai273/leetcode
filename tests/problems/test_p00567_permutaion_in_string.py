import pytest

from problems.p00567_permutaion_in_string import Solution


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
    ],
)
def test_permutation_in_string(s1, s2, expected):
    solution = Solution()
    assert solution.checkInclusion(s1, s2) == expected
