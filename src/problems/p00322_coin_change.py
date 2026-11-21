class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for cur in range(1, amount + 1):
            for c in coins:
                if cur >= c:
                    dp[cur] = min(dp[cur], dp[cur - c] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
