class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nbrToIndice = dict()

        for i in range(len(nums)):
            # nums[i] + needed = target
            needed = target - nums[i] 
            if needed in nbrToIndice:
                return [nbrToIndice[needed], i]
            nbrToIndice[nums[i]] = i
        return []