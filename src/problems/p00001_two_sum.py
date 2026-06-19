class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            first = nums[i]
            second = target - first
            if second in nums_dict:
                return [nums_dict[second], i]
            nums_dict[first] = i
        return []
