class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        curSet = []

        def dfs(i, res, curSet, n,k):
            if len(curSet) == k:
                res.append(curSet.copy())
                return
            if i > n:
                return
            # choose
            curSet.append(i)
            dfs(i+1, res, curSet, n,k)
            curSet.pop()

            # Not choose
            dfs(i+1, res, curSet, n,k)

        dfs(1, res, curSet,n,k)
        return res