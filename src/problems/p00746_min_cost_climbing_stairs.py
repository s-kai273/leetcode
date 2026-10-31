class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        total = [0, 0]

        # Calculate total cost to reach each steps until n + 1
        for i in range(2, n + 1):
            total.append(min(total[i - 2] + cost[i - 2], total[i - 1] + cost[i - 1]))
        total.append(total[n - 1] + cost[n - 1])

        return min(total[n], total[n + 1])
