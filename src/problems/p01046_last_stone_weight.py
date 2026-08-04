import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Heapify stones
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Do operation
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        return -1 * stones[0] if len(stones) > 0 else 0
