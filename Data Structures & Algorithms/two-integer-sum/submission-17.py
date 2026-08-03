class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for p1 in range(len(nums)-1):
            for p2 in range(p1+1, len(nums)):
                if nums[p1] + nums[p2] == target:
                    return [p1, p2]