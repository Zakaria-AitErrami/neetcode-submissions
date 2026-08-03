class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxAmount = 0
        while l<r:
            width = r - l
            height = min(heights[r],heights[l])
            area = width * height
            maxAmount = max(maxAmount, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxAmount

