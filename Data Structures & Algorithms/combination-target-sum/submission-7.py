class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, ans = [], []

        def backtrack(i, ans):
            if sum(ans) == target:
                res.append(ans[:])
                return
            if sum(ans) > target:
                return
            
            for j in range(i, len(nums)):
                ans.append(nums[j])
                backtrack(j, ans)
                ans.pop()
        backtrack(0,[])
        return res

