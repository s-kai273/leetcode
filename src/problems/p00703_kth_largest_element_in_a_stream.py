class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # min_heap length must be k
        self.min_heap = list()
        self.k = k
        # initialize heap
        for val in nums:
            self.min_sift_up(val)
            if len(self.min_heap) > k:
                self.min_sift_down()

    def min_sift_up(self, val: int):
        self.min_heap.append(val)
        i = len(self.min_heap) - 1
        pi = (i - 1) // 2
        while pi >= 0 and self.min_heap[i] < self.min_heap[pi]:
            self.min_heap[i], self.min_heap[pi] = self.min_heap[pi], self.min_heap[i]
            i = pi
            pi = (i - 1) // 2

    def min_sift_down(self) -> int:
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        min_val = self.min_heap.pop()
        i = 0
        li = 2 * i + 1 if 2 * i + 1 < len(self.min_heap) else None
        ri = 2 * i + 2 if 2 * i + 2 < len(self.min_heap) else None
        while li is not None or ri is not None:
            ci = None
            if li is None:
                ci = ri
            elif ri is None:
                ci = li
            else:
                ci = li if self.min_heap[li] < self.min_heap[ri] else ri
            if self.min_heap[i] > self.min_heap[ci]:
                self.min_heap[i], self.min_heap[ci] = (
                    self.min_heap[ci],
                    self.min_heap[i],
                )
                i = ci
                li = 2 * i + 1 if 2 * i + 1 < len(self.min_heap) else None
                ri = 2 * i + 2 if 2 * i + 2 < len(self.min_heap) else None
            else:
                break
        return min_val

    def add(self, val: int) -> int:
        self.min_sift_up(val)
        if len(self.min_heap) > self.k:
            self.min_sift_down()
        return self.min_heap[0]
