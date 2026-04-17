class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            li = i + 1
            ri = len(nums) - 1
            while li < ri:
                if nums[i] + nums[li] + nums[ri] > 0:
                    ri -= 1
                elif nums[i] + nums[li] + nums[ri] < 0:
                    li += 1
                else:
                    answer.append([nums[i], nums[li], nums[ri]])
                    ri -= 1
                    li += 1
                    while li < ri and nums[li] == nums[li - 1]:
                        li += 1
                    while li < ri and nums[ri] == nums[ri + 1]:
                        ri -= 1

        return answer
