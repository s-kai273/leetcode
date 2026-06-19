class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_h_left = 0
        max_h_right = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                max_h_left = max(max_h_left, height[left])
                water += max_h_left - height[left]
                left += 1
            else:
                max_h_right = max(max_h_right, height[right])
                water += max_h_right - height[right]
                right -= 1
        return water
