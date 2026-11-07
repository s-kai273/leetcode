class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # Iterate length
        for l in range(1, n + 1):
            # Iterate start point
            for si in range(n - l + 1):
                # Utilize dp charasteristic to count up
                if l <= 2:
                    dp[si][si + l - 1] = s[si] == s[si + l - 1]
                else:
                    dp[si][si + l - 1] = (
                        s[si] == s[si + l - 1] and dp[si + 1][si + l - 2]
                    )
                if dp[si][si + l - 1]:
                    count += 1

        return count
