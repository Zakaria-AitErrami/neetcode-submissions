class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L, R = 0, 0

        window = set()
        while R < len(nums):
            if R-L > k:
                #L=R
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
            R+=1
        return False