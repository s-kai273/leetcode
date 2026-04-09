class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict: dict[int, list] = {}
        for i, n in enumerate(nums):
            if n in num_dict:
                num_dict[n].append(i)
            else:
                num_dict[n] = [i]
        num_keys = sorted(list(num_dict.keys()))
        for p1 in num_keys:
            p2 = target - p1
            if p1 == p2 and len(num_dict[p1]) > 1:
                return [num_dict[p1][0], num_dict[p1][1]]
            if p2 in num_keys:
                return [num_dict[p1][0], num_dict[p2][0]]
        return []
