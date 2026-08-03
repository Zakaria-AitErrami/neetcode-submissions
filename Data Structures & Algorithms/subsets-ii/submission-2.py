class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        def dfs(i, sol):
            res.append(sol[:])
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                sol.append(nums[j])
                dfs(j+1, sol)
                sol.pop()
        dfs(0, sol)
        return res