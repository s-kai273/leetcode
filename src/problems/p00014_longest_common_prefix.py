class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ""
        for i in range(200):
            ch = strs[0][i] if len(strs[0]) > i else ""
            for s in strs:
                if i > len(s) - 1:
                    return answer
                elif s[i] != ch:
                    return answer
            if ch is not None:
                answer += ch
        return answer
