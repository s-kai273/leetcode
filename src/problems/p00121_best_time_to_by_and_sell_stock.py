class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        answer = 0
        for p in prices[1:]:
            if min_price > p:
                min_price = p
            answer = max(answer, p - min_price)
        return answer
