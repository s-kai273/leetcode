import pytest

from problems.p00012_integer_to_roman import Solution


@pytest.mark.parametrize(
    "num, expected",
    [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ],
)
def test_integer_to_roman(num, expected):
    solution = Solution()
    assert solution.intToRoman(num) == expected
