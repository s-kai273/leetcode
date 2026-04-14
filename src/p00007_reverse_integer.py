class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        rev_val = int(str(x)[::-1]) if not negative else -1 * int(str(x * -1)[::-1])
        if rev_val < -(2**31) or rev_val > 2**31 - 1:
            return 0
        return rev_val
