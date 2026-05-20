class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = list()
        for ch in tokens:
            if ch in {"+", "-", "*", "/"}:
                second_val = stack.pop()
                first_val = stack.pop()
                if ch == "+":
                    stack.append(first_val + second_val)
                elif ch == "-":
                    stack.append(first_val - second_val)
                elif ch == "*":
                    stack.append(first_val * second_val)
                else:
                    stack.append(int(first_val / second_val))
            else:
                stack.append(int(ch))
        return stack.pop()
