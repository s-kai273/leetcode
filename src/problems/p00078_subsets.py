class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = list()

        def dfs(i: int, value_list: list[int]):
            subsets.append(value_list.copy())
            for j in range(i, len(nums)):
                value_list.append(nums[j])
                dfs(j + 1, value_list)
                value_list.pop()

        dfs(0, [])
        return subsets
