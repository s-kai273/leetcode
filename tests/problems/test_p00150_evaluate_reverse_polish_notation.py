import pytest

from problems.p00150_evaluate_reverse_polish_notation import Solution


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_evaluate_reverse_polish_notation(tokens, expected):
    solution = Solution()
    assert solution.evalRPN(tokens) == expected
