class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet = []
        subSet = []

        def helper(i,nums, curSet, subSet):
            subSet.append(curSet.copy())
                
                

            for j in range(i,len(nums)):
                curSet.append(nums[j])
                helper(j+1, nums,curSet, subSet)
                curSet.pop()
        
        helper(0,nums,curSet, subSet)
        return subSet
            