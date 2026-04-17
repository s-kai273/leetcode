import pytest

from problems.p00013_roman_to_integer import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_integer_to_roman(s, expected):
    solution = Solution()
    assert solution.romanToInt(s) == expected
