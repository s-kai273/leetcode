class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        code_dict = dict()
        for s in strs:
            ch_dict = dict()
            for ch in s:
                ch_dict[ch] = ch_dict.get(ch, 0) + 1
            code = ""
            for ch in sorted(ch_dict.keys()):
                code += f"{ch_dict[ch]}{ch}"
            d = code_dict.get(code, [])
            d.append(s)
            code_dict[code] = d
        group = list()
        for code in code_dict.keys():
            group.append(code_dict[code])
        return group
