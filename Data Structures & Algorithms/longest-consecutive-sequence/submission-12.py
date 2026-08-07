class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        curr = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - nums[i-1] == 1:
                curr+=1
                res = max(curr, res)
            else:
                curr = 1
        return res