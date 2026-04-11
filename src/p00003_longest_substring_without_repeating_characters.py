class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        current_len = 0
        ch_dict = dict()
        i = 0
        while i < len(s):
            ch = s[i]
            if ch_dict.get(ch) is None:
                ch_dict[ch] = i
                current_len += 1
            else:
                i = ch_dict[ch]
                answer = max(current_len, answer)
                current_len = 0
                ch_dict = dict()
            i += 1
        answer = max(current_len, answer)
        return answer
