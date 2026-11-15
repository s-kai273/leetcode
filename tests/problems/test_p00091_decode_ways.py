import pytest

from problems.p00091_decode_ways import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("12", 2),
        ("01", 0),
    ],
)
def test_decode_ways(s, expected):
    solution = Solution()
    assert solution.numDecodings(s) == expected
