import pytest

from problems.p00005_longest_palindromic_substring import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("abcddcbaaa", "abcddcba"),
        ("a", "a"),
        ("ac", "a"),
        ("ccc", "ccc"),
    ],
)
def test_longest_palindromic_substring(s, expected):
    solution = Solution()
    assert solution.longestPalindrome(s) == expected
