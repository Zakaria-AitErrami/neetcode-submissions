class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        numSet = set(nums)
        longest = 1
        for num in nums:
            currentMax = 1
            if not num-1 in numSet:
                exist = num+1
                while exist in numSet:
                    currentMax+=1
                    exist+=1
                longest = max(longest, currentMax)
            
        return longest