class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i,v in enumerate(nums):
            for j,val in enumerate(nums):
                if i!=j:
                    res[i] *= nums[j]
        return res
        