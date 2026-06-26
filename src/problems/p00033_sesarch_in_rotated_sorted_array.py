class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (right + left) // 2
            if nums[left] > nums[right]:
                if nums[mid] > nums[left]:
                    if nums[right] < target < nums[mid]:
                        right = mid
                    else:
                        left = mid
                else:
                    if nums[mid] < target < nums[left]:
                        left = mid
                    else:
                        right = mid
            else:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
