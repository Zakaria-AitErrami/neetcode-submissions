class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curSet = []
        candidates.sort()

        def helper(i, nums, res, curSet):
            if sum(curSet) == target:
                res.append(curSet.copy())
                return
            if sum(curSet) > target or i >= len(nums):
                return
            
            curSet.append(nums[i])
            helper(i+1, nums, res, curSet)
            curSet.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, nums, res, curSet)
        
        helper(0,candidates,res,curSet)
        return res