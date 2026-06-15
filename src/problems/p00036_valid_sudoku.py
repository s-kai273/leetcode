class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            number_set = set()
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in number_set:
                    return False
                number_set.add(val)

        for i in range(9):
            number_set = set()
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                if val in number_set:
                    return False
                number_set.add(val)

        for o_i in [0, 3, 6]:
            for o_j in [0, 3, 6]:
                number_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[i + o_i][j + o_j]
                        if val == ".":
                            continue
                        if val in number_set:
                            return False
                        number_set.add(val)
        return True
