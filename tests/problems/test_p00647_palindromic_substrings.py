import pytest

from problems.p00647_palindromic_substrings import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc", 3),
        ("aaa", 6),
    ],
)
def test_palindromic_substrings(s, expected):
    solution = Solution()
    assert solution.countSubstrings(s) == expected
