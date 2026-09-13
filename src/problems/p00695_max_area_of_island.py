class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        def dfs(i: int, j: int) -> int:
            count = 1
            grid[i][j] = 0
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                count += dfs(i + 1, j)
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                count += dfs(i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                count += dfs(i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                count += dfs(i, j - 1)
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        return max_area
