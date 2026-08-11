class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = list()

        def dfs(i: int, value_list: list[int]):
            nonlocal subsets
            subsets.append(value_list.copy())
            for j in range(i + 1, len(nums)):
                value_list.append(nums[j])
                dfs(j, value_list)
                value_list.pop()

        dfs(-1, [])
        return subsets
