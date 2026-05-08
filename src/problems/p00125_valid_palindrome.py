class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        sanitized_ch_list = []
        for ch in s:
            if "a" <= ch <= "z" or "0" <= ch <= "9":
                sanitized_ch_list.append(ch)
        s = "".join(sanitized_ch_list)
        s_len = len(s)
        for i in range(s_len // 2):
            if s[i] != s[s_len - 1 - i]:
                return False
        return True
