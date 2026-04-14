import pytest

from p00008_string_to_integer import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("42", 42),
        (" -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("", 0),
    ],
)
def test_string_to_integer(s, expected):
    solution = Solution()
    assert solution.myAtoi(s) == expected
