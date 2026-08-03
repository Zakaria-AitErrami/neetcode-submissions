class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index,total):
            # q1 - when do I have a valid answer
            if total == target:
                res.append(subset[:])
                return
            if total > target:
                return
            # q2 What choices do I have
            for i in range(index, len(nums)):
                # dfs(i)      # current number can be selected again
                # dfs(i + 1)  current number cannot be selected again
                subset.append(nums[i])
                dfs(i, total+nums[i]) # i and not i+1 to re-use nums[i]
                subset.pop()
        dfs(0,0)
        return res