class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [None] * len(nums)

        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            if memo[i] is not None:
                return memo[i]
            result = max(dfs(i + 1), nums[i] + dfs(i + 2))
            memo[i] = result
            return result

        return dfs(0)
