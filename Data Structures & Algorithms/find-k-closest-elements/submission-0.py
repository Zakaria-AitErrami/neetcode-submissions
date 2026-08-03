class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        bestScore = float("inf")
        window = []
        for L in range(len(arr)-k+1):
            subArr = arr[L:L+k]
            curScore = 0
            for a in subArr:
                curScore+=abs(a-x)
            if curScore < bestScore:
                bestScore = curScore
                window = subArr
        return window