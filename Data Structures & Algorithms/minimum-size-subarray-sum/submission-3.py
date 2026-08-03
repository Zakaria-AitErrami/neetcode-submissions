class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        SUM=0
        res = float("inf")
        for i in range(len(nums)):
            SUM=0
            for j in range(i, len(nums)):
                SUM+=nums[j]
                if SUM >= target:
                    res = min(res, j-i+1)
                    break
        return 0 if res == float("inf") else res