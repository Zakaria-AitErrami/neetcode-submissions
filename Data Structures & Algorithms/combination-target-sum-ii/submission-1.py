class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(index):
            # q1 - when do I have a complete answer
            if sum(subset) == target:
                res.append(subset[:])
                return
            if sum(subset) > target:
                return
            
            # q2 - what choices do I have
            for i in range(index,len(candidates)):
                if i != len(candidates) - 1:
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                subset.append(candidates[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return [list(x) for x in set(tuple(i) for i in res)]