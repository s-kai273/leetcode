class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        ch_dict = dict()
        min_i = -1
        for i in range(len(s)):
            ch = s[i]
            if ch_dict.get(ch) is None:
                ch_dict[ch] = i
            else:
                answer = max(i - min_i - 1, answer)
                min_i = max(min_i, ch_dict[ch])
                ch_dict[ch] = i
        answer = max(len(s) - 1 - min_i, answer)
        return answer
