class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            first = row[0]
            last = row[-1]
            if first <= target and last >= target:
                 L, R = 0, len(row)-1
                 while L<=R:
                    mid = (L+R) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        R = mid-1
                    else:
                        L = mid+1
        return False
