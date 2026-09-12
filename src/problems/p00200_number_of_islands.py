class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        island_count = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(i: int, j: int):
            visited[i][j] = True
            if i + 1 < len(grid) and not visited[i + 1][j] and grid[i + 1][j] == "1":
                dfs(i + 1, j)
            if i - 1 >= 0 and not visited[i - 1][j] and grid[i - 1][j] == "1":
                dfs(i - 1, j)
            if j + 1 < len(grid[0]) and not visited[i][j + 1] and grid[i][j + 1] == "1":
                dfs(i, j + 1)
            if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j - 1] == "1":
                dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                if grid[i][j] == "0":
                    visited[i][j] = True
                else:
                    island_count += 1
                    dfs(i, j)
        return island_count
