class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curComb = [],[]
        
        def helper(i,combs, curComb, nums, target):
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return
            if sum(curComb) > target:
                return
            if i >= len(nums):
                return
                
            curComb.append(nums[i])
            helper(i,combs, curComb, nums, target)
            curComb.pop()

            helper(i+1,combs, curComb, nums, target)

        helper(0,combs, curComb, nums, target)
        return combs
