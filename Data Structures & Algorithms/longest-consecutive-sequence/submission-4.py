class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        longest = 1
        current = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1] +1 == nums[i]:
                current+=1
                longest = max(longest,current)
            else:
                current = 1
        return longest
            
