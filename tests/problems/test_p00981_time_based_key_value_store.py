import pytest

from problems.p00981_time_based_key_value_store import TimeMap


@pytest.mark.parametrize(
    "methods, args, expected",
    [
        (
            ["TimeMap", "set", "get", "get", "set", "get", "get"],
            [
                [],
                ["foo", "bar", 1],
                ["foo", 1],
                ["foo", 3],
                ["foo", "bar2", 4],
                ["foo", 4],
                ["foo", 5],
            ],
            [None, None, "bar", "bar", None, "bar2", "bar2"],
        ),
    ],
)
def test_time_based_key_value_store(methods, args, expected):
    timemap = None
    for i in range(len(methods)):
        m = methods[i]
        if m == "TimeMap":
            timemap = TimeMap()
            assert expected[i] is None
        elif m == "set":
            a = args[i]
            if timemap is None:
                raise AssertionError
            assert timemap.set(a[0], a[1], a[2]) == expected[i]
        elif m == "get":
            a = args[i]
            if timemap is None:
                raise AssertionError
            assert timemap.get(a[0], a[1]) == expected[i]
        else:
            raise AssertionError
