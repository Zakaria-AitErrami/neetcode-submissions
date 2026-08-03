class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, ans = [], []

        def dfs(index):
            if index == len(nums):
                res.append(ans[:])
                return
            
            ans.append(nums[index])
            dfs(index+1)
            ans.pop()

            dfs(index+1)
        dfs(0)
        return res
