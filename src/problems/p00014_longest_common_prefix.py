class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ""
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i > len(s) - 1 or s[i] != ch:
                    return answer
            answer += ch
        return answer
