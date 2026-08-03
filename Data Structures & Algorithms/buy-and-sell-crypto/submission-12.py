class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxP = 0
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L=R
            else:
                profit = prices[R] - prices[L]
                maxP = max(profit, maxP)
        return maxP
            