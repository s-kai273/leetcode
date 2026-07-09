import pytest

from problems.p00146_lru_cache import LRUCache


@pytest.mark.parametrize(
    "methods, args, expected",
    [
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
    ],
)
def test_lru_cache(methods, args, expected):
    lru_cache = None
    for i, m in enumerate(methods):
        a = args[i]
        if m == "LRUCache":
            lru_cache = LRUCache(a[0])
            assert expected[i] is None
        elif m == "get":
            assert lru_cache is not None
            assert lru_cache.get(a[0]) == expected[i]
        elif m == "put":
            assert lru_cache is not None
            lru_cache.put(a[0], a[1])
            assert expected[i] is None
        else:
            raise AssertionError
