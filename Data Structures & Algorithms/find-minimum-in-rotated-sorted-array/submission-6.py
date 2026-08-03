class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]
        if nums[r] > nums[l]:
            return nums[l]
        while l<=r:
            if nums[r] >= nums[l]:
                return min(res, nums[l])
            mid = (r+l) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid - 1
        return res