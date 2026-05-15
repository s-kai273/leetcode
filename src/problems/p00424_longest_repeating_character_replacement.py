class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        left = 0
        max_freq = 0
        ch_count = dict()
        for right, ch in enumerate(s):
            ch_count[ch] = ch_count.get(ch, 0) + 1
            max_freq = max(max_freq, ch_count[ch])
            while right - left + 1 - max_freq > k:
                ch_count[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer
