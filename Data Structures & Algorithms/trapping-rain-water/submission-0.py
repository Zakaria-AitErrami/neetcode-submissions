class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i, n in enumerate(height):
            leftArray = height[:i]
            rightArray = height[i+1:]
            if len(leftArray) == 0:
                maxLeft = 0
            else:
                maxLeft = max(leftArray)
            if len(rightArray) == 0:
                maxRight = 0
            else:
                maxRight = max(rightArray)
            currentRes = min(maxLeft, maxRight) - n
            if currentRes > 0:
                res+= currentRes
        return res
            