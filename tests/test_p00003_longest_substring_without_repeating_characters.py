import pytest

from p00003_longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
    ],
)
def test_add_two_numbers(s, expected):
    solution = Solution()
    answer = solution.lengthOfLongestSubstring(s)
    assert answer == expected
