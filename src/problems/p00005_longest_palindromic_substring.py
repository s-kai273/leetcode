class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        max_li, max_ri = 0, 0
        max_len = 0

        for l in range(1, n + 1):
            for li in range(n - l + 1):
                ri = li + l - 1
                if s[li] == s[ri] and (ri - li <= 1 or dp[li + 1][ri - 1]):
                    dp[li][ri] = True
                    if max_len < l:
                        max_li = li
                        max_ri = ri
                        max_len = l
        return s[max_li : max_ri + 1]
