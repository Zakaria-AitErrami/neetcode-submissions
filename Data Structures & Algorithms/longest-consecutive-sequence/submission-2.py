class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 1
        currentMax = 1
        arr = sorted(nums)
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if arr[i] == arr[i-1]:
                continue
            if arr[i] - arr[i-1] == 1:
                currentMax+=1
                maxi = max(currentMax, maxi)
            else:
                currentMax = 1
        return maxi
