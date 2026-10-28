class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1, prev2 = 1, 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev2 + prev1, prev2
        return prev2
