from collections import deque


class Solution:
    def __init__(self):
        self.parenthesesMap = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

    def isValid(self, s: str) -> bool:
        queue = deque([])
        for ch in s:
            if ch in self.parenthesesMap.keys():
                queue.appendleft(ch)
                queue.append(self.parenthesesMap[ch])
            elif ch in self.parenthesesMap.values():
                if len(queue) < 2:
                    return False
                queue.popleft()
                close = queue.pop()
                if close != ch:
                    return False
        return len(queue) == 0
