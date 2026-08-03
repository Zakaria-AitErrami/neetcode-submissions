class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for L in range(len(nums)):
            for R in range(L+1, min(L+k+1,len(nums))):
                if nums[L] == nums[R]:
                    return True
        return False
