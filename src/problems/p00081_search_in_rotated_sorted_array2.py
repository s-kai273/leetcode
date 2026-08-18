class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == target or nums[right] == target:
                return True
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] < target:
                if nums[left] <= nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[right] > target:
                if target < nums[mid] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                break
        return False
