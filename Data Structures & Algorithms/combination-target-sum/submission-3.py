class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subSet, curSet = [], []

        def helper(i, nums, curSet, subSet):
            if sum(curSet) == target:
                subSet.append(curSet[:])
                return
            if sum(curSet) > target or i >= len(nums):
                return

            # decision to include nums[i]
            curSet.append(nums[i])

            helper(i,nums,curSet,subSet)
            curSet.pop()

            # decision to NOT include
            helper(i+1,nums,curSet,subSet)
        helper(0,nums,curSet,subSet)
        return subSet
