class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset, curSet = [], []
        nums.sort()
        def dfs(i, nums, subset, curSet):
            if i == len(nums):
                subset.append(curSet[:])
                return
            
            # Choose
            curSet.append(nums[i])
            
            dfs(i+1,nums,subset,curSet)
            curSet.pop()
            # do not choose
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,nums,subset,curSet)
        
        dfs(0,nums,subset,curSet)
        return subset