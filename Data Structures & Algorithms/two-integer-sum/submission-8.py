class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,n in enumerate(nums):
            d[n] = i
        for i, n in enumerate(nums):
            needed = target - n
            if needed in d and i!=d[needed]:
                return [i, d[needed]]
        