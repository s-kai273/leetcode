class Solution:
    def numDecodings(self, s: str) -> int:
        prev1, prev2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            tmp = 0
            if s[i] != "0":
                tmp += prev1
            if s[i] != "0" and s[i : i + 2] <= "26":
                tmp += prev2
            prev1, prev2 = tmp, prev1

        return prev1
