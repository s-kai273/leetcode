class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                li = j + 1
                ri = n - 1
                while li < ri:
                    total = nums[i] + nums[j] + nums[li] + nums[ri]
                    if total > target:
                        ri -= 1
                    elif total < target:
                        li += 1
                    else:
                        answer.append([nums[i], nums[j], nums[li], nums[ri]])
                        ri -= 1
                        li += 1
                        while li < ri:
                            if nums[ri] == nums[ri + 1]:
                                ri -= 1
                            else:
                                break
                        while li < ri:
                            if nums[li] == nums[li - 1]:
                                li += 1
                            else:
                                break
        return answer
