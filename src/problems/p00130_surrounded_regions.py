from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        queue = deque()

        for x, y in (
            [(0, 0), (0, n - 1), (m - 1, 0), (m - 1, n - 1)]
            + [(i, j) for i in range(1, m) for j in (0, n - 1)]
            + [(i, j) for i in (0, m - 1) for j in range(1, n)]
        ):
            if board[x][y] == "X":
                continue
            queue.append((x, y))
            board[x][y] = "o"
            while queue:
                cur_x, cur_y = queue.popleft()
                for dx, dy in [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0),
                ]:
                    if (
                        0 <= cur_x + dx < m
                        and 0 <= cur_y + dy < n
                        and board[cur_x + dx][cur_y + dy] == "O"
                    ):
                        queue.append((cur_x + dx, cur_y + dy))
                        board[cur_x + dx][cur_y + dy] = "o"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "o":
                    board[i][j] = "O"
