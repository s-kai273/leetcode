class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        parts = [""] * numRows
        for i in range(len(s)):
            m = 2 * (numRows - 1)
            x = i // m
            dist = min(abs(i - m * x), abs(i - m * (x + 1)))
            parts[dist] += s[i]
        return "".join(parts)
