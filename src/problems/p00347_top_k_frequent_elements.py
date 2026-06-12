class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        val_count_dict = dict()
        for val in nums:
            val_count_dict[val] = val_count_dict.get(val, 0) + 1
        count_val_list = [[] for _ in range(len(nums) + 1)]
        for val, count in val_count_dict.items():
            count_val_list[count].append(val)
        count = 0
        top_k_val_list = list()
        for c in range(len(nums), 0, -1):
            top_k_val_list.extend(count_val_list[c])
            count += len(count_val_list[c])
            if count == k:
                break
        return top_k_val_list
