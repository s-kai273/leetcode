from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            current = queue.popleft()
            for x, y in [
                (current[0] + 1, current[1]),
                (current[0] - 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1),
            ]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == INF:
                    grid[x][y] = grid[current[0]][current[1]] + 1
                    queue.append((x, y))
