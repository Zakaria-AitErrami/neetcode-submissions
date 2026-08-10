class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            from collections import deque
            count = 1
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                R, C = queue.popleft()
                for dr, dc in directions:
                    nR, nC = R+dr, C+dc
                    if min(nR,nC) < 0 or nR >= rows or nC>=cols or grid[nR][nC]==0 or (nR,nC) in visited:
                        continue
                    count+=1
                    visited.add((nR,nC))
                    queue.append((nR,nC))
            return count
                





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area, bfs(r,c))

        return area
