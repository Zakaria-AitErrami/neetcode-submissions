class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS,COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        maxArea = 0
        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c]==0 or (r,c) in visited:
                return 0
            count = 1
            visited.add((r,c))
            for dr,dc in directions:
                count +=dfs(r+dr,c+dc)
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    maxArea = max(maxArea,dfs(r,c))
        return maxArea