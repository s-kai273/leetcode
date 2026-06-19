class Solution:
    def trap(self, height: list[int]) -> int:
        trap = 0

        start = 0
        while start < len(height) and height[start] < 1:
            start += 1
        end = start + 1
        current_bar = 0
        while end < len(height):
            if height[end] < height[start]:
                current_bar += height[end]
            else:
                trap += height[start] * (end - start - 1) - current_bar
                current_bar = 0
                start = end
            end += 1
        last_start = start

        start = len(height) - 1
        while start > -1 and height[start] < 1:
            start -= 1
        end = start - 1
        current_bar = 0
        while end > last_start - 1:
            if height[end] < height[start]:
                current_bar += height[end]
            else:
                trap += height[start] * (start - end - 1) - current_bar
                current_bar = 0
                start = end
            end -= 1
        return trap
