import pytest

from problems.p00020_valid_parentheses import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("[", False),
        ("]", False),
    ],
)
def test_valid_parentheses(s, expected):
    solution = Solution()
    assert solution.isValid(s) == expected
