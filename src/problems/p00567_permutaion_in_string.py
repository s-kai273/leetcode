class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ch_count = dict()
        for ch in s1:
            s1_ch_count[ch] = s1_ch_count.get(ch, 0) + 1
        s2_ch_count = dict()
        start, end = 0, 0
        while start < len(s2):
            if s2[start] not in s1_ch_count:
                start += 1
                continue
            end = start
            while end < len(s2):
                ch = s2[end]
                if ch in s1_ch_count and s1_ch_count[ch] > s2_ch_count.setdefault(
                    ch, 0
                ):
                    s2_ch_count[ch] += 1
                    if s1_ch_count == s2_ch_count:
                        return True
                    end += 1
                else:
                    start += 1
                    break
            s2_ch_count = dict()
        return False
