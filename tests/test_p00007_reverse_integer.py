import pytest

from p00007_reverse_integer import Solution


@pytest.mark.parametrize(
    "x, expected",
    [(123, 321), (-123, -321), (120, 21), (1534236469, 0)],
)
def test_reverse_integer(x, expected):
    solution = Solution()
    assert solution.reverse(x) == expected
