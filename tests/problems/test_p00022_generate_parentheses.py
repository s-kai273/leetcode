import pytest

from problems.p00022_generate_parentheses import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
    ],
)
def test_generate_parentheses(n, expected):
    solution = Solution()
    assert solution.generateParenthesis(n) == expected
