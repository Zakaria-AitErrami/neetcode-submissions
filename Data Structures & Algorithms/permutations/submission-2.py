class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, ans = [],[]
        def backtrack(ans):
            if len(ans) == len(nums):
                res.append(ans[:])
                
                
            for j in range(len(nums)):
                if nums[j] not in ans:
                    ans.append(nums[j])
                    backtrack(ans)
                    ans.pop()
        backtrack([])

        return res