from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_window = list()
        queue = deque()
        for i, n in enumerate(nums):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= n:
                queue.pop()
            queue.append(i)
            if i - k >= -1:
                max_window.append(nums[queue[0]])
        return max_window
