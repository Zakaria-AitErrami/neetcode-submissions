class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l<=r:
            rate = (l+r) // 2
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p/rate)
            if totalHours <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        return res 
        # minRate = 1
        # while True:
        #    totalHours = 0
        #    for p in piles:
        #        totalHours += math.ceil(p/minRate)
        #    if totalHours > h:
        #        minRate+=1
        #    else:
        #        break
        #return minRate