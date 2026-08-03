class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top+bot) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                break
            if target > matrix[mid][-1]:
                top = mid+1
            else:
                bot = mid - 1
        
        row = (top+bot) // 2
        L, R = 0, len(matrix[0]) - 1
        arr = matrix[row]
        while L <= R:
            mid = (L+R) // 2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                L = mid+1
            else:
                R = mid-1
        return False
