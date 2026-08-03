class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, ans = [], []
        candidates.sort()
        def backtrack(i, ans):
            if sum(ans) == target:
                res.append(ans[:])
                return
            if sum(ans) > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                ans.append(candidates[j])
                backtrack(j+1, ans)
                ans.pop()
        backtrack(0,[])
        return res
                