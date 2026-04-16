class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_amount = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i == j:
                    continue
                amount = abs(j - i) * min(height[i], height[j])
                max_amount = max(amount, max_amount)
        return max_amount
