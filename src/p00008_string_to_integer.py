class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s):
            if s[i] != " ":
                break
            i += 1
        if i > len(s) - 1:
            return 0
        sign = -1 if s[i] == "-" else 1
        if s[i] == "-" or s[i] == "+":
            i += 1
        while i < len(s):
            if s[i] != "0":
                break
            i += 1
        val = "0"
        while i < len(s):
            if s[i].isdigit():
                val += s[i]
                i += 1
            else:
                break
        val = sign * int(val)
        if val < -(2**31):
            return -(2**31)
        if val > 2**31 - 1:
            return 2**31 - 1
        return val
