class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curComb = []
        res = []
        candidates.sort()
        
        def helper(i, candidates, res, curComb, target):
            if sum(curComb) == target:
                res.append(curComb.copy())
                return
            
            if sum(curComb) > target:
                return
            if i >= len(candidates):
                return
            
            curComb.append(candidates[i])
            helper(i+1, candidates, res, curComb, target)
            curComb.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            
            helper(i+1, candidates, res, curComb, target)

        helper(0, candidates, res, curComb, target)
        return res    

