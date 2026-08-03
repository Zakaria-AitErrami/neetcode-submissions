class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        def dfs(indice):
            # Q1 when do I have a complete answer
            res.append(subset[:])
            # Q2 what choices do I have
            for i in range(indice,len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return res


        