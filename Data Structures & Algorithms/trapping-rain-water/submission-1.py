class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0,0
        res = 0
        while l < r:
            if height[l] <= height[r]:
                # check if we need to calculate (maxLeft > height[l]) move the min
                if maxLeft > height[l]:
                    res += maxLeft - height[l]
                else:
                    maxLeft = height[l]
                l+=1
            else:
                if height[r] < maxRight:
                    res+= maxRight - height[r]
                else:
                    maxRight = height[r]
                r-=1
        return res

