class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSet, curSet = [], []

        def helper(i, nums, curSet, subSet):
            if i >= len(nums):
                subSet.append(curSet[:])
                return
            
            # choose to include
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subSet)
            curSet.pop()
            # choose to not include
            helper(i+1, nums, curSet, subSet)
        
        helper(0,nums,curSet,subSet)
        return subSet
