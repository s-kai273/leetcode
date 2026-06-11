class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_dict = dict()
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            key = tuple(count)
            group_dict.setdefault(key, []).append(s)
        return list(group_dict.values())
