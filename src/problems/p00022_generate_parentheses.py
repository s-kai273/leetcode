class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        target_len = 2 * n

        def dfs(path: list[str], open_count: int, close_count: int):
            if len(path) == target_len:
                result.append("".join(path))
                return

            for s in ["(", ")"]:
                if s == "(" and open_count < n:
                    path.append(s)
                    dfs(path, open_count + 1, close_count)
                    path.pop()
                elif s == ")" and close_count < open_count:
                    path.append(s)
                    dfs(path, open_count, close_count + 1)
                    path.pop()

        dfs([], 0, 0)
        return result
