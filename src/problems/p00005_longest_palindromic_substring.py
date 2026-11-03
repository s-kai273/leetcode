class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        max_li, max_ri = 0, 0
        max_len = 0

        for l in range(1, n + 1):
            hl = l // 2
            for i in range(n):
                li = i - hl + 1 if l % 2 == 0 else i - hl
                ri = i + hl
                if li < 0 or ri > n - 1:
                    continue
                if s[li] == s[ri] and (ri - li <= 1 or dp[li + 1][ri - 1]):
                    dp[li][ri] = True
                    if max_len < l:
                        max_li = li
                        max_ri = ri
                        max_len = l
        return s[max_li : max_ri + 1]
