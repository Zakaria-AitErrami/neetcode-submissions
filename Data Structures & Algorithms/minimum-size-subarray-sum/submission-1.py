class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0,0
        SUM = 0
        res = float("inf")
        while R < len(nums):
            # expand the window
            SUM+=nums[R]
            # shrink the window
            while SUM >= target:
                res = min(res, R-L+1)
                SUM-=nums[L]
                L+=1
            R+=1
        return 0 if res == float("inf") else res
