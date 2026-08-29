class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        combs = list()
        candidates.sort()

        def dfs(cur_comb: list[int], cur_sum: int, start_i: int):
            prev_candidate = -1
            for i in range(start_i, len(candidates)):
                if candidates[i] == prev_candidate:
                    continue
                cur_comb.append(candidates[i])
                sum_comb = cur_sum + candidates[i]
                if sum_comb == target:
                    combs.append(cur_comb.copy())
                elif sum_comb < target:
                    dfs(cur_comb, sum_comb, i + 1)
                cur_comb.pop()
                prev_candidate = candidates[i]
                if sum_comb > target:
                    break

        dfs([], 0, 0)
        return combs
