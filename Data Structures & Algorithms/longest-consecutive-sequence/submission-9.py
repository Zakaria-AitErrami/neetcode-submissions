class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxC = 1
        curMax = 1
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i]-1 == nums[i-1]:
                curMax+=1
                maxC = max(maxC, curMax)
            else:
                curMax = 1
        return maxC