class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
        return maxP