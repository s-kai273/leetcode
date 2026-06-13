class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        left_product_list = list()
        current = 1
        left_product_list.append(current)
        for i in range(len_nums - 1):
            current *= nums[i]
            left_product_list.append(current)
        right_product_list = list()
        current = 1
        right_product_list.append(current)
        for i in range(len_nums - 1, 0, -1):
            current *= nums[i]
            right_product_list.append(current)
        answer = list()
        for i in range(len_nums):
            answer.append(left_product_list[i] * right_product_list[len_nums - i - 1])
        return answer
