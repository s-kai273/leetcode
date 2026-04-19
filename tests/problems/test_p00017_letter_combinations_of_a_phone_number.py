import pytest

from problems.p00017_letter_combinations_of_a_phone_number import Solution


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("7", ["p", "q", "r", "s"]),
    ],
)
def test_letter_combinations_of_a_phone_number(digits, expected):
    solution = Solution()
    assert solution.letterCombinations(digits) == expected
