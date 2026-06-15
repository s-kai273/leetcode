class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for val in num_set:
            if val - 1 not in num_set:
                current = val + 1
                length = 1
                while current in num_set:
                    current += 1
                    length += 1
                max_length = max(length, max_length)
        return max_length
