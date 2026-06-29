class Solution:
    def findKthSmallest(self, nums1: list[int], nums2: list[int], k: int):
        i_nums1, i_nums2 = 0, 0

        while True:
            if i_nums1 == len(nums1):
                return nums2[i_nums2 + k - 1]
            if i_nums2 == len(nums2):
                return nums1[i_nums1 + k - 1]

            if k == 1:
                return min(nums1[i_nums1], nums2[i_nums2])
            half = k // 2
            take1 = min(half, len(nums1) - i_nums1)
            take2 = min(half, len(nums2) - i_nums2)
            val1 = nums1[i_nums1 + take1 - 1]
            val2 = nums2[i_nums2 + take2 - 1]
            if val1 <= val2:
                i_nums1 += take1
                k -= take1
            else:
                i_nums2 += take2
                k -= take2

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return self.findKthSmallest(nums1, nums2, total_len // 2 + 1)
        return (
            self.findKthSmallest(nums1, nums2, total_len // 2)
            + self.findKthSmallest(nums1, nums2, total_len // 2 + 1)
        ) / 2.0
