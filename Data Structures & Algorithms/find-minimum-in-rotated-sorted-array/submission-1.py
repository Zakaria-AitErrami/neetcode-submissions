class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mini = nums[0]
        while l <=r:
            if nums[r] > nums[l]:
                mini = min(mini, nums[l])
                break
            else:
                mid = (l+r) // 2
                mini = min(mini, nums[mid])
                if nums[mid] >= nums[l]:
                    l = mid+1
                else:
                    r = mid - 1
        return mini
