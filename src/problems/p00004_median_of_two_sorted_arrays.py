class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = sorted(nums1 + nums2)
        arr_len = len(arr)
        if arr_len % 2 == 1:
            return arr[arr_len // 2]
        return (arr[arr_len // 2 - 1] + arr[arr_len // 2]) / 2
