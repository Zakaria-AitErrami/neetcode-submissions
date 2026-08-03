class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        def backtrack(sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                 
            for j in range(len(nums)):
                if nums[j] not in sol:
                    sol.append(nums[j])
                    backtrack(sol)
                    sol.pop()
        
        backtrack([])
        return res