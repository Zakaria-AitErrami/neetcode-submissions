class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        candidates.sort()
        def backtrack(i,sol):
            if sum(sol) == target:
                res.append(sol[:])
            if sum(sol) > target:
                return
            

            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                sol.append(candidates[j])
                backtrack(j+1,sol)
                sol.pop()
        backtrack(0, sol)
        return res
                