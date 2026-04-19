from itertools import product


class Solution:
    def __init__(self):
        self.letterMap = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> list[str]:
        letters_list = []
        for ch in digits:
            num = int(ch)
            letters_list.append(self.letterMap[num])
        return ["".join(p) for p in product(*letters_list)]
