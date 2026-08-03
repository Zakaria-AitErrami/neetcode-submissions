class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        res = [1] * n
        preCal = 1
        for i in range(len(nums)):
            preCal *= nums[i]
            pref[i] = preCal
        sufCal = 1
        for j in range(n-1, -1, -1):
            sufCal *= nums[j]
            suff[j] = sufCal
        
        for i in range(n):
            left = pref[i - 1] if i > 0 else 1
            right = suff[i + 1] if i < n - 1 else 1
            res[i] = left * right
        return res
