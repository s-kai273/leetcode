import pytest

from problems.p00155_min_stack import MinStack


@pytest.mark.parametrize(
    "operation, input, expected",
    [
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2],
        ),
    ],
)
def test_min_stack(operation, input, expected):
    min_stack = None
    for i in range(len(operation)):
        op = operation[i]
        if op == "MinStack":
            min_stack = MinStack()
            assert expected[i] is None
        elif op == "push":
            if min_stack is None:
                raise AssertionError
            min_stack.push(input[i][0])
            assert expected[i] is None
        elif op == "pop":
            if min_stack is None:
                raise AssertionError
            min_stack.pop()
            assert expected[i] is None
        elif op == "top":
            if min_stack is None:
                raise AssertionError
            val = min_stack.top()
            assert expected[i] == val
        elif op == "top":
            if min_stack is None:
                raise AssertionError
            val = min_stack.getMin()
            assert expected[i] == val
