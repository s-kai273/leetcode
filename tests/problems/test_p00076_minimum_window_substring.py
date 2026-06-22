import pytest

from problems.p00076_minimum_window_substring import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("a", "b", ""),
        ("ab", "a", "a"),
        ("bdab", "ab", "ab"),
        ("bba", "ab", "ba"),
    ],
)
def test_minimum_window_substring(s, t, expected):
    solution = Solution()
    assert solution.minWindow(s, t) == expected
