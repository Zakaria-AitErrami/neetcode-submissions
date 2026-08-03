class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            row = matrix[r]
            if target > row[-1]:
                continue
            else:
                L, R = 0, cols-1
                while L <= R:
                    mid = (L+R) // 2
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        L = mid + 1
                    else:
                        R = mid - 1
        return False