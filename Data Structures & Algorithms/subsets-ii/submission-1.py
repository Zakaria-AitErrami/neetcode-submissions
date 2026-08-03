class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subSet, curSet = [], []
        nums.sort()
        def helper(i,nums,curSet,subSet):
            if i >= len(nums):
                subSet.append(curSet.copy())
                return
            
            

            # choose
            curSet.append(nums[i])
            helper(i+1,nums,curSet,subSet)
            curSet.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1,nums,curSet,subSet)
        
        helper(0,nums,curSet,subSet)
        return subSet