import pytest

from p00006_zigzag_conversion import Solution


@pytest.mark.parametrize(
    "s, numRows, expected",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
    ],
)
def test_longest_palindromic_substring(s, numRows, expected):
    solution = Solution()
    assert solution.convert(s, numRows) == expected
