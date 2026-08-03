class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        # loop throught the array
        # 2 -> index 0.  val+x = target
        for i, val in enumerate(nums):
            needed = target-val
            if needed in d:
                return [d[needed],i]
            else:
                d[val]=i
