class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = float("-inf")

        for p1 in range(len(prices)):
            for p2 in range(p1+1, len(prices)):
                profit = prices[p2] - prices[p1]
                maxP = max(maxP, profit)
        return maxP if maxP > 0 else 0