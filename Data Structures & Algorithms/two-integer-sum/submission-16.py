class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndexes = dict()
        for i, num in enumerate(nums):
            needed = target - num
            if needed in mapIndexes:
                return [mapIndexes[needed], i]
            mapIndexes[num] = i
            