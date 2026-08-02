import pytest

from problems.p00703_kth_largest_element_in_a_stream import KthLargest


@pytest.mark.parametrize(
    "k, nums, add_args, expected",
    [
        (3, [1, 2, 3, 3], [3, 5, 6, 7, 8], [None, 3, 3, 3, 5, 6]),
    ],
)
def test_keth_largest_element_in_a_stream(k, nums, add_args, expected):
    kth_largest = KthLargest(k, nums)
    for i, arg in enumerate(add_args):
        assert kth_largest.add(arg) == expected[i + 1]
