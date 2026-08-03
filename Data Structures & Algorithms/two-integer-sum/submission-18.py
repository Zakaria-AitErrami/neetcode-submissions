class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for p1 in range(len(nums)-1):
            numberNeeded = target - nums[p1]
            for p2 in range(p1+1, len(nums)):
                if nums[p2] == numberNeeded:
                    return [p1, p2]