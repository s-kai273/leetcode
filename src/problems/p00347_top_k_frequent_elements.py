class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_val_dict = dict()
        val_count_dict = dict()
        for val in nums:
            val_count_dict[val] = val_count_dict.get(val, 0) + 1
            count_val_dict.setdefault(val_count_dict[val], set()).add(val)
            count_val_dict.setdefault(val_count_dict[val] - 1, set()).discard(val)
        count = 0
        top_k_val_list = list()
        for c in sorted(count_val_dict.keys(), reverse=True):
            top_k_val_list += count_val_dict[c]
            count += len(count_val_dict[c])
            if count == k:
                break
        return top_k_val_list
