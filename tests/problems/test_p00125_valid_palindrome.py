import pytest

from problems.p00125_valid_palindrome import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
    ],
)
def test_valid_palindrome(s, expected):
    solution = Solution()
    assert solution.isPalindrome(s) == expected
