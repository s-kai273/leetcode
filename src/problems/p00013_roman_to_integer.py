class Solution:
    def __init__(self):
        self.romanDict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

    def romanToInt(self, s: str) -> int:
        def dfs(i: int):
            if i > len(s) - 1:
                return 0
            val = self.romanDict[s[i]]
            next_val = self.romanDict[s[i + 1]] if i < len(s) - 1 else 0
            if next_val > val:
                return next_val - val + dfs(i + 2)
            else:
                return val + dfs(i + 1)

        return dfs(0)
