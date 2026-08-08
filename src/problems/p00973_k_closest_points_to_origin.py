import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = list()
        for p in points:
            # Calculate dist and store in min_heap and dist_dict
            dist = math.sqrt(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(max_heap, (-dist, p))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [p for _, p in max_heap]
