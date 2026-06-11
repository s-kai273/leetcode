import pytest

from problems.p00049_group_anagrams import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(strs, expected):
    solution = Solution()
    actual = solution.groupAnagrams(strs)
    normalize = lambda groups: sorted([sorted(group) for group in groups])
    assert normalize(actual) == normalize(expected)
