class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices)-1):
            profit += max(0, prices[i+1]-prices[i])
        return profit