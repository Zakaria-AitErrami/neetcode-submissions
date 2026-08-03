class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        L, R = 0,0
        SUM = 0
        while R < len(nums):
            SUM+=nums[R]
            while SUM >= target:
                SUM-=nums[L]
                res = min(res, R-L+1)
                L+=1
           
            R+=1
        return 0 if res == float("inf") else res
                