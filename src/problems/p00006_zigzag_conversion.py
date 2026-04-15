class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        parts = [[] for _ in range(numRows)]
        for i in range(len(s)):
            m = 2 * (numRows - 1)
            d = i % m
            dist = min(d, m - d)
            parts[dist].append(s[i])
        return "".join("".join(p) for p in parts)
