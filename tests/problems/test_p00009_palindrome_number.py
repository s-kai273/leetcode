import pytest

from problems.p00009_palindrome_number import Solution


@pytest.mark.parametrize(
    "x, expected",
    [
        (121, True),
        (-121, False),
        (10, False),
    ],
)
def test_palindrome_number(x, expected):
    solution = Solution()
    assert solution.isPalindrome(x) == expected
