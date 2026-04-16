class Solution:
    def __init__(self):
        self.symbolPairs = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

    def intToRoman(self, num: int) -> str:
        answer_list = []
        val = num
        for pair in self.symbolPairs:
            pnum = pair[0]
            pstr = pair[1]
            count = val // pnum
            answer_list.append(pstr * count)
            val = val - pnum * count
        return "".join(answer_list)
