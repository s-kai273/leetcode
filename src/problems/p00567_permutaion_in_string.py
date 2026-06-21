class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        s1_ch_count = dict()
        for ch in s1:
            s1_ch_count[ch] = s1_ch_count.get(ch, 0) + 1
        window_ch_count = dict()
        for ch in s2[:len_s1]:
            window_ch_count[ch] = window_ch_count.get(ch, 0) + 1

        if s1_ch_count == window_ch_count:
            return True

        for right in range(len_s1, len_s2):
            left = right - len_s1
            window_ch_count[s2[left]] -= 1
            window_ch_count[s2[right]] = window_ch_count.get(s2[right], 0) + 1
            if window_ch_count[s2[left]] == 0:
                del window_ch_count[s2[left]]
            if s1_ch_count == window_ch_count:
                return True
        return False
