class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 0
        right = max(piles)
        while right - left > 1:
            current_k = (left + right) // 2
            time = 0
            for banana_count in piles:
                time += (banana_count - 1) // current_k + 1
            if time > h:
                left = current_k
            else:
                right = current_k
        return left + 1
