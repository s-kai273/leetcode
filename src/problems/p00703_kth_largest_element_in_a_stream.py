import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # min_heap length must be k
        self.min_heap = nums
        self.k = k
        # initialize heap
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
