class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index):
            # q1 - when do I have a valid answer
            total = sum(subset)
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
                dfs(i) # i and not i+1 to re-use nums[i]
                subset.pop() # # execution continues here after return
        dfs(0)
        return res