from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        max_minute, fresh_count = 0, 0
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1

        while queue:
            i, j, minute = queue.popleft()
            for x, y in [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    fresh_count -= 1
                    grid[x][y] = 2
                    queue.append((x, y, minute + 1))
            max_minute = max(max_minute, minute)
        return max_minute if fresh_count == 0 else -1
