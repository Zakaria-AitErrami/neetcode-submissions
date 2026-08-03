class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numbersToFind in the hashmap
        ntfMap = dict()
        for i,n in enumerate(nums):
            # expression: n + ntf = target
            ntf = target - n
            if n not in ntfMap:
                ntfMap[ntf] = i
            else:
                return [ntfMap[n] , i ]