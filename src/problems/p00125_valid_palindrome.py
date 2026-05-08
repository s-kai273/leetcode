class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        sanitized_s = ""
        for ch in s:
            if "a" <= ch <= "z" or "0" <= ch <= "9":
                sanitized_s += ch
        s_len = len(sanitized_s)
        for i in range(s_len // 2):
            if sanitized_s[i] != sanitized_s[s_len - 1 - i]:
                return False
        return True
