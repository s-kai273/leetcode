class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            li = i + 1
            ri = len(nums) - 1
            while li < ri:
                total = nums[i] + nums[li] + nums[ri]
                closest = (
                    total if abs(target - closest) > abs(target - total) else closest
                )
                if total > target:
                    ri -= 1
                elif total < target:
                    li += 1
                else:
                    return closest
        return closest
