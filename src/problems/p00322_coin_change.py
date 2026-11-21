class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for cur in range(1, amount + 1):
            if cur in coins:
                dp[cur] = 1
                continue
            min_coin_num = float("inf")
            for c in coins:
                if cur - c < 0 or dp[cur - c] == float("inf"):
                    continue
                min_coin_num = min(min_coin_num, dp[cur - c] + 1)
            dp[cur] = min_coin_num

        return dp[amount] if dp[amount] != float("inf") else -1
