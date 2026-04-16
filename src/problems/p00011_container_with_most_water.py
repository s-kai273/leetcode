class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_amount = 0
        left = 0
        right = len(height) - 1
        while left != right:
            amount = (right - left) * min(height[right], height[left])
            max_amount = max(amount, max_amount)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_amount
