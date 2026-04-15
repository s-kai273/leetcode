import pytest

from problems.p00010_regular_expression_matching import Solution


@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
    ],
)
def test_regular_expression_matching(s, p, expected):
    solution = Solution()
    assert solution.isMatch(s, p) == expected
