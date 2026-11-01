class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [None] * len(nums)

        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            if memo[i] is not None:
                return memo[i]
            result = nums[i] + max(dfs(i + 2), dfs(i + 3))
            memo[i] = result
            return result

        return max(dfs(0), dfs(1))
