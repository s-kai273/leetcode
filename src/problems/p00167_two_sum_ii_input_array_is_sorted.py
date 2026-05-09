class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            val = numbers[left] + numbers[right]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                return [left + 1, right + 1]
        raise ValueError("Not reachable")
