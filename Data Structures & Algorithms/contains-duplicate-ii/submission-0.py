class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r = 0, 0
        window = set()
        while r < len(nums):
            # expand the window
            if r-l > k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
                r+=1
        return False
                
            