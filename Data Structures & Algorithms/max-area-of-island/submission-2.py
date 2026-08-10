class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        visited = set()
        def dfs(r,c):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    area = max(area, dfs(r,c))
        return area