class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, subSet = [], []

        def helper(i, nums, curSet, subSet):
            if i >= len(nums):
                subSet.append(curSet.copy())
                return
            
            # Choose
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subSet)
            curSet.pop()

            # do not choose
            helper(i+1, nums, curSet, subSet)
        
        helper(0,nums,curSet, subSet)
        return subSet