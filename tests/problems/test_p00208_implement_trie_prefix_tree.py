import pytest

from problems.p00208_implement_trie_prefix_tree import PrefixTree


@pytest.mark.parametrize(
    "methods, args, expected",
    [
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
        ),
    ],
)
def test_implement_trie(methods, args, expected):
    tree = PrefixTree()
    for i, op in enumerate(methods):
        if op == "Trie":
            assert expected[i] is None
        elif op == "insert":
            assert tree.insert(args[i][0]) == expected[i]
        elif op == "search":
            assert tree.search(args[i][0]) == expected[i]
        elif op == "startsWith":
            assert tree.startsWith(args[i][0]) == expected[i]
        else:
            raise RuntimeError
