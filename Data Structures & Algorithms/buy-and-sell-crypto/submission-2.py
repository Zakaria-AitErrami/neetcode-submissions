class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for L in range(len(prices)):
            for R in range(L+1, len(prices)):
                profit = prices[R] - prices[L]
                maxP = max(maxP, profit)
        return maxP