import pytest

from problems.p00211_design_add_and_search_words_data_structure import WordDictionary


@pytest.mark.parametrize(
    "methods, args, expected",
    [
        (
            [
                "WordDictionary",
                "addWord",
                "addWord",
                "addWord",
                "search",
                "search",
                "search",
                "search",
            ],
            [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, None, False, True, True, True],
        ),
    ],
)
def test_design_add_and_search_words_data_structure(methods, args, expected):
    wd = None
    for i, m in enumerate(methods):
        if m == "WordDictionary":
            wd = WordDictionary()
            assert expected[i] is None
        elif m == "addWord":
            assert wd is not None
            assert wd.addWord(args[i][0]) == expected[i]
        elif m == "search":
            assert wd is not None
            assert wd.search(args[i][0]) == expected[i]
