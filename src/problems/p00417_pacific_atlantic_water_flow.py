class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        cell_cond = [[""] * n for _ in range(m)]
        answer_cells = set()

        def dfs(r: int, c: int, cond: str):
            cur_cond = cell_cond[r][c]
            if (
                cur_cond == "b"
                or cur_cond == "p"
                and cond == "a"
                or cur_cond == "a"
                and cond == "p"
            ):
                cell_cond[r][c] = "b"
            else:
                cell_cond[r][c] = cond

            if cell_cond[r][c] == "b":
                answer_cells.add((r, c))

            for i, j in [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]:
                if (
                    0 <= r + i < m
                    and 0 <= c + j < n
                    and heights[r][c] <= heights[r + i][c + j]
                    and cell_cond[r + i][c + j] != "b"
                    and cell_cond[r + i][c + j] != cond
                ):
                    dfs(r + i, c + j, cond)

        dfs(0, 0, "p")
        dfs(0, n - 1, "b")
        dfs(m - 1, 0, "b")
        dfs(m - 1, n - 1, "a")

        for i in range(1, m - 1):
            dfs(i, 0, "p")
            dfs(i, n - 1, "a")

        for j in range(1, n - 1):
            dfs(0, j, "p")
            dfs(m - 1, j, "a")

        return list(map(list, answer_cells))
