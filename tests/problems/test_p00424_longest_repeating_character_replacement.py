import pytest

from problems.p00424_longest_repeating_character_replacement import Solution


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ],
)
def test_valid_anagram(s, k, expected):
    solution = Solution()
    assert solution.characterReplacement(s, k) == expected
