import pytest

from problems.p00014_longest_common_prefix import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        ([""], ""),
    ],
)
def test_integer_to_roman(strs, expected):
    solution = Solution()
    assert solution.longestCommonPrefix(strs) == expected
