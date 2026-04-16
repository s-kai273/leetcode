class Solution:
    def __init__(self):
        self.symbolMap = {
            0: {
                1: "I",
                4: "IV",
                5: "V",
                9: "IX",
            },
            1: {
                1: "X",
                4: "XL",
                5: "L",
                9: "XC",
            },
            2: {
                1: "C",
                4: "CD",
                5: "D",
                9: "CM",
            },
            3: {
                1: "M",
                4: "M" * 4,
                5: "M" * 5,
                9: "M" * 9,
            },
        }

    def intToRoman(self, num: int) -> str:
        answer = ""
        val = num
        for i in range(3, -1, -1):
            q = val // 10**i
            if q == 0:
                continue
            if q == 1 or q == 4 or q == 5 or q == 9:
                answer += self.symbolMap[i][q]
            elif q == 2 or q == 3:
                answer += self.symbolMap[i][1] * q
            elif q == 6 or q == 7 or q == 8:
                r = q % 5
                answer += self.symbolMap[i][5] + self.symbolMap[i][1] * r
            val = val - q * 10**i
        return answer
