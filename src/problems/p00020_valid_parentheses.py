class Solution:
    def __init__(self):
        self.closingMap = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in self.closingMap.keys():
                stack.append(self.closingMap[ch])
            elif ch in self.closingMap.values():
                if not stack or stack.pop() != ch:
                    return False
        return len(stack) == 0
