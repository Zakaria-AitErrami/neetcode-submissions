class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i,sol):
            if sum(sol) == target:
                res.append(sol[:])
            if sum(sol) > target:
                return
            
            for j in range(i, len(nums)):

                sol.append(nums[j])
                backtrack(j, sol)
                sol.pop()
        backtrack(0,[])
        return res
