class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(r,c):
            from collections import deque
            curArea = 1
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                R,C = queue.popleft()
                for dr, dc in directions:
                    nr, nc = R+dr, C+dc
                    if nr == rows or nc == cols or min(nr,nc) < 0 or (nr,nc) in visited or grid[nr][nc]==0:
                        continue
                    curArea+=1
                    queue.append((nr,nc))
                    visited.add((nr,nc))
            return curArea

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]==1:
                    area = max(area, bfs(r,c))
        return area