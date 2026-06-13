class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        answer = [1]
        current = answer[0]
        for i in range(len_nums - 1):
            current *= nums[i]
            answer.append(current)
        current = 1
        for i in range(len_nums):
            answer[len_nums - i - 1] *= current
            current *= nums[len_nums - i - 1]
        return answer
