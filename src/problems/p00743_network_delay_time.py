import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        relations = [list() for _ in range(n)]
        nodes = set()
        heap = list()

        # Convert times to relations
        for u, v, t in times:
            relations[u - 1].append((t, v - 1))

        # Store relations of k node in heap
        heapq.heappush(heap, (0, k - 1))

        # Update heap, nodes in loop
        while heap:
            t, i = heapq.heappop(heap)
            if i in nodes:
                continue
            nodes.add(i)
            for next_t, next_i in relations[i]:
                heapq.heappush(heap, (next_t + t, next_i))
            if len(nodes) == n:
                return t

        # The case it is impossible to send signal with all nodes
        return -1
