class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        v = len(points)
        min_dist = [float("inf")] * v
        min_dist[0] = 0

        visited_set = set()
        total_cost = 0

        for _ in range(v):
            min_i = -1
            for i in range(v):
                if i in visited_set:
                    continue
                if min_i == -1 or min_dist[i] < min_dist[min_i]:
                    min_i = i
            total_cost += min_dist[min_i]
            visited_set.add(min_i)

            pt = points[min_i]
            for i in range(v):
                if i in visited_set:
                    continue
                pi = points[i]
                min_dist[i] = min(min_dist[i], abs(pt[0] - pi[0]) + abs(pt[1] - pi[1]))
        return int(total_cost)
