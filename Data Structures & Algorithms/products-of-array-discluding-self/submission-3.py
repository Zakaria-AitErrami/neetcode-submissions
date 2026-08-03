class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        suf = [1]*len(nums)
        res = [1]*len(nums)
        prod = 1
        for i in range(len(nums)):
            prod*=nums[i]
            pref[i] = prod
        
        postprod = 1
        for i in range(len(nums)-1,-1,-1):
            postprod*=nums[i]
            suf[i]=postprod
        
        for i in range(len(nums)):
            if i==0:
                res[i] = suf[i+1]
            elif i==len(nums)-1:
                res[i] = pref[i-1]
            else:
                res[i] = pref[i-1]*suf[i+1]
        return res


    


