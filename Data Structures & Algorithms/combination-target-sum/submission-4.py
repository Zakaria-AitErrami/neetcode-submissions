class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curSet = []
        def helper(i, nums, res, curSet):
            if sum(curSet) == target:
                res.append(curSet.copy())
                return
            if i >= len(nums):
                return
            if sum(curSet) > target:
                return
            
            # choose
            curSet.append(nums[i])
            helper(i, nums, res, curSet) # i and not i+1 to allow to choose the same number multiple time
            curSet.pop()

            # Do not choose
            helper(i+1, nums, res, curSet)

        helper(0,nums,res,curSet)
        return res