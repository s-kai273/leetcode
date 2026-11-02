class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0
        for i in range(len(nums) - 1):
            prev1, prev2 = max(nums[i] + prev2, prev1), prev1
        max_rob = prev1

        prev1, prev2 = 0, 0
        for i in range(1, len(nums)):
            prev1, prev2 = max(nums[i] + prev2, prev1), prev1

        return max(max_rob, prev1)
