class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int):
            if visited[x][y]:
                return

            visited[x][y] = True
            if board[x][y] == "X":
                return

            for dx, dy in [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    dfs(x + dx, y + dy)

        for i in range(1, m - 1):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(1, n - 1):
            dfs(0, i)
            dfs(m - 1, i)

        dfs(0, 0)
        dfs(0, n - 1)
        dfs(m - 1, 0)
        dfs(m - 1, n - 1)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == "O":
                    board[i][j] = "X"
                visited[i][j] = True
