class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        comb_list = list()
        nums.sort()

        def dfs(start_i: int, arr: list[int], arr_sum):
            for i in range(start_i, len(nums)):
                n = nums[i]
                if arr_sum + n > target:
                    break
                arr.append(n)
                if arr_sum + n == target:
                    comb_list.append(arr.copy())
                elif arr_sum + n < target:
                    dfs(i, arr, arr_sum + n)
                arr.pop()

        dfs(0, [], 0)
        return comb_list
