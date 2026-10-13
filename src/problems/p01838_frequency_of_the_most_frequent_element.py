class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        max_freq = 0
        op_count = 0
        j = 0
        for i in range(len(nums)):
            target = nums[i]
            if i != 0:
                op_count -= (j - 1 - i + 1) * (nums[i - 1] - target)
            while j < len(nums):
                # Calculate operation count for target value
                if op_count + (target - nums[j]) <= k:
                    op_count += target - nums[j]
                    j += 1
                else:
                    max_freq = max(max_freq, j - i)
                    break
            max_freq = max(max_freq, j - i)
        return max_freq
