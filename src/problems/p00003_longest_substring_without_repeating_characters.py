class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        start_i = 0
        ch_dict = dict()
        for i in range(len(s)):
            if s[i] not in ch_dict or ch_dict[s[i]] < start_i:
                ch_dict[s[i]] = i
                answer = max(answer, i - start_i + 1)
            else:
                start_i = ch_dict[s[i]] + 1
                ch_dict[s[i]] = i
        return answer
