class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curSet = [], []
        def backtrack(i,curSet):
            res.append(curSet.copy())

            for index in range(i,len(nums)):
                curSet.append(nums[index])
                backtrack(index+1, curSet)
                curSet.pop()
        backtrack(0, [])
        return res
            