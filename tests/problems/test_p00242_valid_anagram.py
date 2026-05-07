import pytest

from problems.p00242_valid_anagram import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [("anagram", "nagaram", True), ("rat", "car", False)],
)
def test_valid_anagram(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
