class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def dfs(path, open_count, close_count):
            pcount = len(path)
            if pcount == 2 * n:
                result.append("".join(path))
                return

            for s in ["(", ")"]:
                if s == "(" and open_count < n:
                    path.append(s)
                    open_count += 1
                elif s == ")" and close_count < open_count:
                    path.append(s)
                    close_count += 1
                if len(path) > pcount:
                    dfs(path, open_count, close_count)
                    s = path.pop()
                    if s == "(":
                        open_count -= 1
                    elif s == ")":
                        close_count -= 1

        dfs([], 0, 0)
        return result
