class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        total_prev1, total_prev2 = 0, 0

        # Calculate total cost to reach each steps until n + 1
        for i in range(2, n + 1):
            total = min(total_prev1 + cost[i - 1], total_prev2 + cost[i - 2])
            total_prev1, total_prev2 = total, total_prev1
        total_prev1, total_prev2 = total_prev2 + cost[n - 1], total_prev1

        return min(total_prev1, total_prev2)
