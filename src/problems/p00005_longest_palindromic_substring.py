class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd_center_list = []
        even_center_list = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                even_center_list.append(i)
        for i in range(1, len(s) - 1):
            if s[i + 1] == s[i - 1]:
                odd_center_list.append(i)
        max_substring = ""
        for ci in even_center_list:
            dw = 0
            while True:
                if (
                    ci - 1 - dw < 0
                    or ci + dw > len(s) - 1
                    or s[ci - 1 - dw] != s[ci + dw]
                ):
                    break
                if len(max_substring) < 2 * (dw + 1):
                    max_substring = s[ci - 1 - dw : ci + dw + 1]
                dw += 1
        for ci in odd_center_list:
            dw = 0
            while True:
                if ci - dw < 0 or ci + dw > len(s) - 1 or s[ci - dw] != s[ci + dw]:
                    break
                if len(max_substring) < 2 * dw + 1:
                    max_substring = s[ci - dw : ci + dw + 1]
                dw += 1
        if max_substring == "":
            max_substring = s[0]
        return max_substring
