class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_dict = dict()
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1
        for ch in s:
            count = t_dict.get(ch, 0)
            if count == 0:
                return False
            t_dict[ch] -= 1
        return True
